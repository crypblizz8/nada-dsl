from . import NadaType, Mode, BaseType
from nada_dsl.circuit_io import Literal
from typing import Union
from nada_dsl.operations import *
from .. import SourceRef


def new_constant(base_type: BaseType, value):
    if base_type == BaseType.BOOLEAN:
        return Boolean(value=bool(value))
    elif base_type == BaseType.INTEGER:
        return Integer(value=int(value))
    else:
        return UnsignedInteger(value=int(value))


def new_public(base_type: BaseType, operation):
    if base_type == BaseType.BOOLEAN:
        return PublicBoolean(inner=operation)
    elif base_type == BaseType.INTEGER:
        return PublicInteger(inner=operation)
    else:
        return PublicUnsignedInteger(inner=operation)


def new_secret(base_type: BaseType, operation):
    if base_type == BaseType.BOOLEAN:
        return SecretBoolean(inner=operation)
    elif base_type == BaseType.INTEGER:
        return SecretInteger(inner=operation)
    else:
        return SecretUnsignedInteger(inner=operation)


class ScalarType(NadaType):

    def __eq__(self, other):
        return equals_operation("Equals", "==", self, other, lambda lhs, rhs: lhs == rhs)

    def __ne__(self, other):
        return equals_operation("NotEquals", "!=", self, other, lambda lhs, rhs: lhs != rhs)


class NumericType(ScalarType):

    def __add__(self, other):
        return binary_arithmetic_operation("Addition", "+", self, other, lambda lhs, rhs: lhs + rhs)

    def __sub__(self, other):
        return binary_arithmetic_operation("Subtraction", "-", self, other, lambda lhs, rhs: lhs - rhs)

    def __mul__(self, other):
        return binary_arithmetic_operation("Multiplication", "*", self, other, lambda lhs, rhs: lhs * rhs)

    def __truediv__(self, other):
        return binary_arithmetic_operation("Division", "/", self, other, lambda lhs, rhs: lhs / rhs)

    def __mod__(self, other):
        return binary_arithmetic_operation("Modulo", "%", self, other, lambda lhs, rhs: lhs % rhs)

    def __pow__(self, other):
        base_type = self.to_base_type()
        if (base_type != other.to_base_type() or
                not (base_type == BaseType.INTEGER or base_type == BaseType.UNSIGNED_INTEGER)):
            raise TypeError(f"Invalid operation: {self} ** {other}")
        mode = Mode(max([self.to_mode().value, other.to_mode().value]))
        if mode == Mode.CONSTANT:
            return new_constant(base_type, self.value ** other.value)
        elif mode == Mode.PUBLIC:
            operation = Power(left=self, right=other, source_ref=SourceRef.back_frame())
            return new_public(base_type, operation)
        else:
            raise TypeError(f"Invalid operation: {self} ** {other}")

    def __lshift__(self, other):
        return shift_operation("LeftShift", "<<", self, other, lambda lhs, rhs: lhs << rhs)

    def __rshift__(self, other):
        return shift_operation("RightShift", ">>", self, other, lambda lhs, rhs: lhs >> rhs)

    def __lt__(self, other):
        return binary_relational_operation("LessThan", "<", self, other, lambda lhs, rhs: lhs < rhs)

    def __gt__(self, other):
        return binary_relational_operation("GreaterThan", ">", self, other, lambda lhs, rhs: lhs > rhs)

    def __le__(self, other):
        return binary_relational_operation("LessOrEqualThan", "<=", self, other, lambda lhs, rhs: lhs <= rhs)

    def __ge__(self, other):
        return binary_relational_operation("GreaterOrEqualThan", ">=", self, other, lambda lhs, rhs: lhs >= rhs)


class BooleanType(ScalarType):

    def __and__(self, other):
        return binary_logical_operation("BooleanAnd", "&", self, other, lambda lhs, rhs: lhs & rhs)

    def __or__(self, other):
        return binary_logical_operation("BooleanOr", "|", self, other, lambda lhs, rhs: lhs | rhs)

    def __xor__(self, other):
        return binary_logical_operation("BooleanXor", "^", self, other, lambda lhs, rhs: lhs ^ rhs)

    def if_else(self, arg_0: ScalarType, arg_1: ScalarType) -> ScalarType:
        base_type = arg_0.to_base_type()
        if base_type != arg_1.to_base_type() or base_type == BaseType.BOOLEAN or self.to_mode() == Mode.CONSTANT:
            raise TypeError(f"Invalid operation: {self}.IfElse({arg_0}, {arg_1})")
        mode = Mode(max([self.to_mode().value, arg_0.to_mode().value, arg_1.to_mode().value]))
        operation = IfElse(this=self, arg_0=arg_0, arg_1=arg_1, source_ref=SourceRef.back_frame())
        if mode == Mode.CONSTANT or mode == Mode.PUBLIC:
            return new_public(base_type, operation)
        else:
            return new_secret(base_type, operation)


@dataclass
class Integer(NumericType):
    value: int

    def __init__(self, value: int):
        super().__init__(inner=Literal(value=value, source_ref=SourceRef.back_frame()))
        if isinstance(value, int):
            self.value = value
        else:
            raise ValueError(f"Expected int, got {type(value).__name__}")

    def to_base_type(self) -> BaseType:
        return BaseType.INTEGER

    def to_mode(self) -> Mode:
        return Mode.CONSTANT

    def __eq__(self, other):
        return ScalarType.__eq__(self, other)


@dataclass
class UnsignedInteger(NumericType):
    value: int

    def __init__(self, value: int):
        super().__init__(inner=Literal(value=value, source_ref=SourceRef.back_frame()))
        if isinstance(value, int):
            self.value = value
        else:
            raise ValueError(f"Expected int, got {type(value).__name__}")

    def to_base_type(self) -> BaseType:
        return BaseType.UNSIGNED_INTEGER

    def to_mode(self) -> Mode:
        return Mode.CONSTANT

    def __eq__(self, other):
        return ScalarType.__eq__(self, other)


@dataclass
class Boolean(BooleanType):
    value: bool

    def __init__(self, value: bool):
        super().__init__(inner=Literal(value=value, source_ref=SourceRef.back_frame()))
        if isinstance(value, bool):
            self.value = value
        else:
            raise ValueError(f"Expected bool, got {type(value).__name__}")

    def __bool__(self) -> bool:
        return self.value

    def to_base_type(self) -> BaseType:
        return BaseType.BOOLEAN

    def to_mode(self) -> Mode:
        return Mode.CONSTANT

    def __eq__(self, other):
        return ScalarType.__eq__(self, other)

    def __invert__(self: "Boolean") -> "Boolean":
        return Boolean(value=bool(not self.value))


@dataclass
class PublicInteger(NumericType):

    def __init__(self, inner: NadaType):
        super().__init__(inner)

    def to_base_type(self) -> BaseType:
        return BaseType.INTEGER

    def to_mode(self) -> Mode:
        return Mode.PUBLIC

    def __eq__(self, other):
        return ScalarType.__eq__(self, other)

    def public_equals(self, other: Union["PublicInteger", "SecretInteger"]) -> "PublicBoolean":
        return public_equals_operation(self, other)


@dataclass
class PublicUnsignedInteger(NumericType):

    def __init__(self, inner: NadaType):
        super().__init__(inner)

    def to_base_type(self) -> BaseType:
        return BaseType.UNSIGNED_INTEGER

    def to_mode(self) -> Mode:
        return Mode.PUBLIC

    def __eq__(self, other):
        return ScalarType.__eq__(self, other)

    def public_equals(self, other: Union["PublicUnsignedInteger", "SecretUnsignedInteger"]) -> "PublicBoolean":
        return public_equals_operation(self, other)


@dataclass
class PublicBoolean(BooleanType):

    def __init__(self, inner: NadaType):
        super().__init__(inner)

    def to_base_type(self) -> BaseType:
        return BaseType.BOOLEAN

    def to_mode(self) -> Mode:
        return Mode.PUBLIC

    def __eq__(self, other):
        return ScalarType.__eq__(self, other)

    def __invert__(self: "PublicBoolean") -> "PublicBoolean":
        operation = Not(this=self, source_ref=SourceRef.back_frame())
        return PublicBoolean(inner=operation)


@dataclass
class SecretInteger(NumericType):

    def __init__(self, inner: NadaType):
        super().__init__(inner)

    def to_base_type(self) -> BaseType:
        return BaseType.INTEGER

    def to_mode(self) -> Mode:
        return Mode.SECRET

    def __eq__(self, other):
        return ScalarType.__eq__(self, other)

    def public_equals(self, other: Union["PublicInteger", "SecretInteger"]) -> "PublicBoolean":
        return public_equals_operation(self, other)

    def trunc_pr(self, other: Union["PublicUnsignedInteger", "UnsignedInteger"]) -> "SecretInteger":
        if isinstance(other, UnsignedInteger):
            operation = TruncPr(left=self, right=other, source_ref=SourceRef.back_frame())
            return SecretInteger(inner=operation)
        elif isinstance(other, PublicUnsignedInteger):
            operation = TruncPr(left=self, right=other, source_ref=SourceRef.back_frame())
            return SecretInteger(inner=operation)
        else:
            raise TypeError(f"Invalid operation: {self}.trunc_pr({other})")

    @classmethod
    def random(cls) -> "SecretInteger":
        return SecretInteger(inner=Random(source_ref=SourceRef.back_frame()))

    def to_public(self: "SecretInteger") -> "PublicInteger":
        operation = Reveal(this=self, source_ref=SourceRef.back_frame())
        return PublicInteger(inner=operation)


@dataclass
class SecretUnsignedInteger(NumericType):
    def __init__(self, inner: NadaType):
        super().__init__(inner)

    def to_base_type(self) -> BaseType:
        return BaseType.UNSIGNED_INTEGER

    def to_mode(self) -> Mode:
        return Mode.SECRET

    def __eq__(self, other):
        return ScalarType.__eq__(self, other)

    def public_equals(self, other: Union["PublicUnsignedInteger", "SecretUnsignedInteger"]) -> "PublicBoolean":
        return public_equals_operation(self, other)

    def trunc_pr(self, other: Union["PublicUnsignedInteger", "UnsignedInteger"]) -> "SecretUnsignedInteger":
        if isinstance(other, UnsignedInteger):
            operation = TruncPr(left=self, right=other, source_ref=SourceRef.back_frame())
            return SecretUnsignedInteger(inner=operation)
        elif isinstance(other, PublicUnsignedInteger):
            operation = TruncPr(left=self, right=other, source_ref=SourceRef.back_frame())
            return SecretUnsignedInteger(inner=operation)
        else:
            raise TypeError(f"Invalid operation: {self}.trunc_pr({other})")

    @classmethod
    def random(cls) -> "SecretUnsignedInteger":
        return SecretUnsignedInteger(inner=Random(source_ref=SourceRef.back_frame()))

    def to_public(self: "SecretUnsignedInteger",) -> "PublicUnsignedInteger":
        operation = Reveal(this=self, source_ref=SourceRef.back_frame())
        return PublicUnsignedInteger(inner=operation)


@dataclass
class SecretBoolean(BooleanType):
    def __init__(self, inner: NadaType):
        super().__init__(inner)

    def to_base_type(self) -> BaseType:
        return BaseType.BOOLEAN

    def to_mode(self) -> Mode:
        return Mode.SECRET

    def __eq__(self, other):
        return ScalarType.__eq__(self, other)

    def __invert__(self: "SecretBoolean") -> "SecretBoolean":
        operation = Not(this=self, source_ref=SourceRef.back_frame())
        return SecretBoolean(inner=operation)

    def to_public(self: "SecretBoolean") -> "PublicBoolean":
        operation = Reveal(this=self, source_ref=SourceRef.back_frame())
        return PublicBoolean(inner=operation)


def binary_arithmetic_operation(operation, operator, left: ScalarType, right: ScalarType, f) -> ScalarType:
    base_type = left.to_base_type()
    if (base_type != right.to_base_type() or
            not (base_type == BaseType.INTEGER or base_type == BaseType.UNSIGNED_INTEGER)):
        raise TypeError(f"Invalid operation: {left} {operator} {right}")
    mode = Mode(max([left.to_mode().value, right.to_mode().value]))
    if mode == Mode.CONSTANT:
        return new_constant(base_type, f(left.value, right.value))
    elif mode == Mode.PUBLIC:
        operation = globals()[operation](left=left, right=right, source_ref=SourceRef.back_frame())
        return new_public(base_type, operation)
    else:
        operation = globals()[operation](left=left, right=right, source_ref=SourceRef.back_frame())
        return new_secret(base_type, operation)


def shift_operation(operation, operator, left: ScalarType, right: ScalarType, f) -> ScalarType:
    base_type = left.to_base_type()
    right_base_type = right.to_base_type()
    if (not (base_type == BaseType.INTEGER or base_type == BaseType.UNSIGNED_INTEGER)
            or not right_base_type == BaseType.UNSIGNED_INTEGER):
        raise TypeError(f"Invalid operation: {left} {operator} {right}")
    right_mode = right.to_mode()
    if not (right_mode == Mode.CONSTANT or right_mode == Mode.PUBLIC):
        raise TypeError(f"Invalid operation: {left} {operator} {right}")
    mode = Mode(max([left.to_mode().value, right_mode.value]))
    if mode == Mode.CONSTANT:
        return new_constant(base_type, f(left.value, right.value))
    elif mode == Mode.PUBLIC:
        operation = globals()[operation](left=left, right=right, source_ref=SourceRef.back_frame())
        return new_public(base_type, operation)
    else:
        operation = globals()[operation](left=left, right=right, source_ref=SourceRef.back_frame())
        return new_secret(base_type, operation)


def binary_relational_operation(operation, operator, left: ScalarType, right: ScalarType, f) -> ScalarType:
    base_type = left.to_base_type()
    if (base_type != right.to_base_type() or
            not (base_type == BaseType.INTEGER or base_type == BaseType.UNSIGNED_INTEGER)):
        raise TypeError(f"Invalid operation: {left} {operator} {right}")
    mode = Mode(max([left.to_mode().value, right.to_mode().value]))
    if mode == Mode.CONSTANT:
        return Boolean(value=bool(f(left.value, right.value)))
    elif mode == Mode.PUBLIC:
        operation = globals()[operation](left=left, right=right, source_ref=SourceRef.back_frame())
        return PublicBoolean(inner=operation)
    else:
        operation = globals()[operation](left=left, right=right, source_ref=SourceRef.back_frame())
        return SecretBoolean(inner=operation)


def equals_operation(operation, operator, left: ScalarType, right: ScalarType, f) -> ScalarType:
    base_type = left.to_base_type()
    if base_type != right.to_base_type():
        raise TypeError(f"Invalid operation: {left} {operator} {right}")
    mode = Mode(max([left.to_mode().value, right.to_mode().value]))
    if mode == Mode.CONSTANT:
        return Boolean(value=bool(f(left.value, right.value)))
    elif mode == Mode.PUBLIC:
        operation = globals()[operation](left=left, right=right, source_ref=SourceRef.back_frame())
        return PublicBoolean(inner=operation)
    else:
        operation = globals()[operation](left=left, right=right, source_ref=SourceRef.back_frame())
        return SecretBoolean(inner=operation)


def public_equals_operation(left: ScalarType, right: ScalarType) -> ScalarType:
    base_type = left.to_base_type()
    if (base_type != right.to_base_type() or
            not (base_type == BaseType.INTEGER or base_type == BaseType.UNSIGNED_INTEGER)):
        raise TypeError(f"Invalid operation: {left}.public_equals({right})")
    if left.to_mode() == Mode.CONSTANT or right.to_mode() == Mode.CONSTANT:
        raise TypeError(f"Invalid operation: {left}.public_equals({right})")
    else:
        operation = PublicOutputEquality(left=left, right=right, source_ref=SourceRef.back_frame())
        return PublicBoolean(inner=operation)


def binary_logical_operation(operation, operator, left: ScalarType, right: ScalarType, f) -> ScalarType:
    base_type = left.to_base_type()
    if base_type != right.to_base_type() or not base_type == BaseType.BOOLEAN:
        raise TypeError(f"Invalid operation: {left} {operator} {right}")
    mode = Mode(max([left.to_mode().value, right.to_mode().value]))
    if mode == Mode.CONSTANT:
        return Boolean(value=bool(f(left.value, right.value)))
    elif mode == Mode.PUBLIC:
        operation = globals()[operation](left=left, right=right, source_ref=SourceRef.back_frame())
        return PublicBoolean(inner=operation)
    else:
        operation = globals()[operation](left=left, right=right, source_ref=SourceRef.back_frame())
        return SecretBoolean(inner=operation)