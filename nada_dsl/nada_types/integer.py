# This file is automatically generated. Do not edit!

from . import NadaType
from dataclasses import dataclass
from nada_dsl.circuit_io import Literal
from nada_dsl.nada_types.boolean import Boolean, PublicBoolean, SecretBoolean
from nada_dsl.operations import Addition, Division, Equals, GreaterOrEqualThan, GreaterThan, LeftShift, LessOrEqualThan, LessThan, Modulo, Multiplication, Power, RightShift, Subtraction
from nada_dsl.source_ref import SourceRef
from typing import Union

@dataclass
class Integer(NadaType):
    value: int

    def __init__(self, value: int):
        super().__init__(inner=Literal(value=value, source_ref=SourceRef.back_frame()))
        if isinstance(value, int):
            self.value = value
        else:
            raise ValueError(f"Expected int, got {type(value).__name__}")

    def __add__(
        self, other: Union["Integer", "PublicInteger", "SecretInteger"]
    ) -> Union["Integer", "PublicInteger", "SecretInteger"]:
        if isinstance(other, Integer):
            return Integer(value=int(self.value + other.value))
        elif isinstance(other, PublicInteger):
            operation = Addition(left=self, right=other, source_ref=SourceRef.back_frame())
            return PublicInteger(inner=operation)
        elif isinstance(other, SecretInteger):
            operation = Addition(left=self, right=other, source_ref=SourceRef.back_frame())
            return SecretInteger(inner=operation)
        else:
            raise TypeError(f"Invalid operation: {self} + {other}")

    def __sub__(
        self, other: Union["Integer", "PublicInteger", "SecretInteger"]
    ) -> Union["Integer", "PublicInteger", "SecretInteger"]:
        if isinstance(other, Integer):
            return Integer(value=int(self.value - other.value))
        elif isinstance(other, PublicInteger):
            operation = Subtraction(left=self, right=other, source_ref=SourceRef.back_frame())
            return PublicInteger(inner=operation)
        elif isinstance(other, SecretInteger):
            operation = Subtraction(left=self, right=other, source_ref=SourceRef.back_frame())
            return SecretInteger(inner=operation)
        else:
            raise TypeError(f"Invalid operation: {self} - {other}")

    def __mul__(
        self, other: Union["Integer", "PublicInteger", "SecretInteger"]
    ) -> Union["Integer", "PublicInteger", "SecretInteger"]:
        if isinstance(other, Integer):
            return Integer(value=int(self.value * other.value))
        elif isinstance(other, PublicInteger):
            operation = Multiplication(left=self, right=other, source_ref=SourceRef.back_frame())
            return PublicInteger(inner=operation)
        elif isinstance(other, SecretInteger):
            operation = Multiplication(left=self, right=other, source_ref=SourceRef.back_frame())
            return SecretInteger(inner=operation)
        else:
            raise TypeError(f"Invalid operation: {self} * {other}")

    def __truediv__(
        self, other: Union["Integer", "PublicInteger"]
    ) -> Union["Integer", "PublicInteger"]:
        if isinstance(other, Integer):
            return Integer(value=int(self.value / other.value))
        elif isinstance(other, PublicInteger):
            operation = Division(left=self, right=other, source_ref=SourceRef.back_frame())
            return PublicInteger(inner=operation)
        else:
            raise TypeError(f"Invalid operation: {self} / {other}")

    def __mod__(
        self, other: Union["Integer", "PublicInteger"]
    ) -> Union["Integer", "PublicInteger"]:
        if isinstance(other, Integer):
            return Integer(value=int(self.value % other.value))
        elif isinstance(other, PublicInteger):
            operation = Modulo(left=self, right=other, source_ref=SourceRef.back_frame())
            return PublicInteger(inner=operation)
        else:
            raise TypeError(f"Invalid operation: {self} % {other}")

    def __pow__(
        self, other: Union["Integer", "PublicInteger"]
    ) -> Union["Integer", "PublicInteger"]:
        if isinstance(other, Integer):
            return Integer(value=int(self.value ** other.value))
        elif isinstance(other, PublicInteger):
            operation = Power(left=self, right=other, source_ref=SourceRef.back_frame())
            return PublicInteger(inner=operation)
        else:
            raise TypeError(f"Invalid operation: {self} ** {other}")

    def __lshift__(
        self, other: Union["Integer", "PublicInteger"]
    ) -> Union["Integer", "PublicInteger"]:
        if isinstance(other, Integer):
            return Integer(value=int(self.value << other.value))
        elif isinstance(other, PublicInteger):
            operation = LeftShift(left=self, right=other, source_ref=SourceRef.back_frame())
            return PublicInteger(inner=operation)
        else:
            raise TypeError(f"Invalid operation: {self} << {other}")

    def __rshift__(
        self, other: Union["Integer", "PublicInteger"]
    ) -> Union["Integer", "PublicInteger"]:
        if isinstance(other, Integer):
            return Integer(value=int(self.value >> other.value))
        elif isinstance(other, PublicInteger):
            operation = RightShift(left=self, right=other, source_ref=SourceRef.back_frame())
            return PublicInteger(inner=operation)
        else:
            raise TypeError(f"Invalid operation: {self} >> {other}")

    def __lt__(
        self, other: Union["Integer", "PublicInteger", "SecretInteger"]
    ) -> Union["Boolean", "PublicBoolean", "SecretBoolean"]:
        if isinstance(other, Integer):
            return Boolean(value=bool(self.value < other.value))
        elif isinstance(other, PublicInteger):
            operation = LessThan(left=self, right=other, source_ref=SourceRef.back_frame())
            return PublicBoolean(inner=operation)
        elif isinstance(other, SecretInteger):
            operation = LessThan(left=self, right=other, source_ref=SourceRef.back_frame())
            return SecretBoolean(inner=operation)
        else:
            raise TypeError(f"Invalid operation: {self} < {other}")

    def __gt__(
        self, other: Union["Integer", "PublicInteger", "SecretInteger"]
    ) -> Union["Boolean", "PublicBoolean", "SecretBoolean"]:
        if isinstance(other, Integer):
            return Boolean(value=bool(self.value > other.value))
        elif isinstance(other, PublicInteger):
            operation = GreaterThan(left=self, right=other, source_ref=SourceRef.back_frame())
            return PublicBoolean(inner=operation)
        elif isinstance(other, SecretInteger):
            operation = GreaterThan(left=self, right=other, source_ref=SourceRef.back_frame())
            return SecretBoolean(inner=operation)
        else:
            raise TypeError(f"Invalid operation: {self} > {other}")

    def __le__(
        self, other: Union["Integer", "PublicInteger", "SecretInteger"]
    ) -> Union["Boolean", "PublicBoolean", "SecretBoolean"]:
        if isinstance(other, Integer):
            return Boolean(value=bool(self.value <= other.value))
        elif isinstance(other, PublicInteger):
            operation = LessOrEqualThan(left=self, right=other, source_ref=SourceRef.back_frame())
            return PublicBoolean(inner=operation)
        elif isinstance(other, SecretInteger):
            operation = LessOrEqualThan(left=self, right=other, source_ref=SourceRef.back_frame())
            return SecretBoolean(inner=operation)
        else:
            raise TypeError(f"Invalid operation: {self} <= {other}")

    def __ge__(
        self, other: Union["Integer", "PublicInteger", "SecretInteger"]
    ) -> Union["Boolean", "PublicBoolean", "SecretBoolean"]:
        if isinstance(other, Integer):
            return Boolean(value=bool(self.value >= other.value))
        elif isinstance(other, PublicInteger):
            operation = GreaterOrEqualThan(left=self, right=other, source_ref=SourceRef.back_frame())
            return PublicBoolean(inner=operation)
        elif isinstance(other, SecretInteger):
            operation = GreaterOrEqualThan(left=self, right=other, source_ref=SourceRef.back_frame())
            return SecretBoolean(inner=operation)
        else:
            raise TypeError(f"Invalid operation: {self} >= {other}")

    def __eq__(
        self, other: Union["Integer", "PublicInteger", "SecretInteger"]
    ) -> Union["Boolean", "PublicBoolean", "SecretBoolean"]:
        if isinstance(other, Integer):
            return Boolean(value=bool(self.value == other.value))
        elif isinstance(other, PublicInteger):
            operation = Equals(left=self, right=other, source_ref=SourceRef.back_frame())
            return PublicBoolean(inner=operation)
        elif isinstance(other, SecretInteger):
            operation = Equals(left=self, right=other, source_ref=SourceRef.back_frame())
            return SecretBoolean(inner=operation)
        else:
            raise TypeError(f"Invalid operation: {self} == {other}")

@dataclass
class PublicInteger(NadaType):
    def __add__(
        self, other: Union["Integer", "PublicInteger", "SecretInteger"]
    ) -> Union["PublicInteger", "SecretInteger"]:
        if isinstance(other, Integer):
            operation = Addition(left=self, right=other, source_ref=SourceRef.back_frame())
            return PublicInteger(inner=operation)
        elif isinstance(other, PublicInteger):
            operation = Addition(left=self, right=other, source_ref=SourceRef.back_frame())
            return PublicInteger(inner=operation)
        elif isinstance(other, SecretInteger):
            operation = Addition(left=self, right=other, source_ref=SourceRef.back_frame())
            return SecretInteger(inner=operation)
        else:
            raise TypeError(f"Invalid operation: {self} + {other}")

    def __sub__(
        self, other: Union["Integer", "PublicInteger", "SecretInteger"]
    ) -> Union["PublicInteger", "SecretInteger"]:
        if isinstance(other, Integer):
            operation = Subtraction(left=self, right=other, source_ref=SourceRef.back_frame())
            return PublicInteger(inner=operation)
        elif isinstance(other, PublicInteger):
            operation = Subtraction(left=self, right=other, source_ref=SourceRef.back_frame())
            return PublicInteger(inner=operation)
        elif isinstance(other, SecretInteger):
            operation = Subtraction(left=self, right=other, source_ref=SourceRef.back_frame())
            return SecretInteger(inner=operation)
        else:
            raise TypeError(f"Invalid operation: {self} - {other}")

    def __mul__(
        self, other: Union["Integer", "PublicInteger", "SecretInteger"]
    ) -> Union["PublicInteger", "SecretInteger"]:
        if isinstance(other, Integer):
            operation = Multiplication(left=self, right=other, source_ref=SourceRef.back_frame())
            return PublicInteger(inner=operation)
        elif isinstance(other, PublicInteger):
            operation = Multiplication(left=self, right=other, source_ref=SourceRef.back_frame())
            return PublicInteger(inner=operation)
        elif isinstance(other, SecretInteger):
            operation = Multiplication(left=self, right=other, source_ref=SourceRef.back_frame())
            return SecretInteger(inner=operation)
        else:
            raise TypeError(f"Invalid operation: {self} * {other}")

    def __truediv__(
        self, other: Union["Integer", "PublicInteger"]
    ) -> "PublicInteger":
        if isinstance(other, Integer):
            operation = Division(left=self, right=other, source_ref=SourceRef.back_frame())
            return PublicInteger(inner=operation)
        elif isinstance(other, PublicInteger):
            operation = Division(left=self, right=other, source_ref=SourceRef.back_frame())
            return PublicInteger(inner=operation)
        else:
            raise TypeError(f"Invalid operation: {self} / {other}")

    def __mod__(
        self, other: Union["Integer", "PublicInteger"]
    ) -> "PublicInteger":
        if isinstance(other, Integer):
            operation = Modulo(left=self, right=other, source_ref=SourceRef.back_frame())
            return PublicInteger(inner=operation)
        elif isinstance(other, PublicInteger):
            operation = Modulo(left=self, right=other, source_ref=SourceRef.back_frame())
            return PublicInteger(inner=operation)
        else:
            raise TypeError(f"Invalid operation: {self} % {other}")

    def __pow__(
        self, other: Union["Integer", "PublicInteger"]
    ) -> "PublicInteger":
        if isinstance(other, Integer):
            operation = Power(left=self, right=other, source_ref=SourceRef.back_frame())
            return PublicInteger(inner=operation)
        elif isinstance(other, PublicInteger):
            operation = Power(left=self, right=other, source_ref=SourceRef.back_frame())
            return PublicInteger(inner=operation)
        else:
            raise TypeError(f"Invalid operation: {self} ** {other}")

    def __lshift__(
        self, other: Union["Integer", "PublicInteger"]
    ) -> "PublicInteger":
        if isinstance(other, Integer):
            operation = LeftShift(left=self, right=other, source_ref=SourceRef.back_frame())
            return PublicInteger(inner=operation)
        elif isinstance(other, PublicInteger):
            operation = LeftShift(left=self, right=other, source_ref=SourceRef.back_frame())
            return PublicInteger(inner=operation)
        else:
            raise TypeError(f"Invalid operation: {self} << {other}")

    def __rshift__(
        self, other: Union["Integer", "PublicInteger"]
    ) -> "PublicInteger":
        if isinstance(other, Integer):
            operation = RightShift(left=self, right=other, source_ref=SourceRef.back_frame())
            return PublicInteger(inner=operation)
        elif isinstance(other, PublicInteger):
            operation = RightShift(left=self, right=other, source_ref=SourceRef.back_frame())
            return PublicInteger(inner=operation)
        else:
            raise TypeError(f"Invalid operation: {self} >> {other}")

    def __lt__(
        self, other: Union["Integer", "PublicInteger", "SecretInteger"]
    ) -> Union["PublicBoolean", "SecretBoolean"]:
        if isinstance(other, Integer):
            operation = LessThan(left=self, right=other, source_ref=SourceRef.back_frame())
            return PublicBoolean(inner=operation)
        elif isinstance(other, PublicInteger):
            operation = LessThan(left=self, right=other, source_ref=SourceRef.back_frame())
            return PublicBoolean(inner=operation)
        elif isinstance(other, SecretInteger):
            operation = LessThan(left=self, right=other, source_ref=SourceRef.back_frame())
            return SecretBoolean(inner=operation)
        else:
            raise TypeError(f"Invalid operation: {self} < {other}")

    def __gt__(
        self, other: Union["Integer", "PublicInteger", "SecretInteger"]
    ) -> Union["PublicBoolean", "SecretBoolean"]:
        if isinstance(other, Integer):
            operation = GreaterThan(left=self, right=other, source_ref=SourceRef.back_frame())
            return PublicBoolean(inner=operation)
        elif isinstance(other, PublicInteger):
            operation = GreaterThan(left=self, right=other, source_ref=SourceRef.back_frame())
            return PublicBoolean(inner=operation)
        elif isinstance(other, SecretInteger):
            operation = GreaterThan(left=self, right=other, source_ref=SourceRef.back_frame())
            return SecretBoolean(inner=operation)
        else:
            raise TypeError(f"Invalid operation: {self} > {other}")

    def __le__(
        self, other: Union["Integer", "PublicInteger", "SecretInteger"]
    ) -> Union["PublicBoolean", "SecretBoolean"]:
        if isinstance(other, Integer):
            operation = LessOrEqualThan(left=self, right=other, source_ref=SourceRef.back_frame())
            return PublicBoolean(inner=operation)
        elif isinstance(other, PublicInteger):
            operation = LessOrEqualThan(left=self, right=other, source_ref=SourceRef.back_frame())
            return PublicBoolean(inner=operation)
        elif isinstance(other, SecretInteger):
            operation = LessOrEqualThan(left=self, right=other, source_ref=SourceRef.back_frame())
            return SecretBoolean(inner=operation)
        else:
            raise TypeError(f"Invalid operation: {self} <= {other}")

    def __ge__(
        self, other: Union["Integer", "PublicInteger", "SecretInteger"]
    ) -> Union["PublicBoolean", "SecretBoolean"]:
        if isinstance(other, Integer):
            operation = GreaterOrEqualThan(left=self, right=other, source_ref=SourceRef.back_frame())
            return PublicBoolean(inner=operation)
        elif isinstance(other, PublicInteger):
            operation = GreaterOrEqualThan(left=self, right=other, source_ref=SourceRef.back_frame())
            return PublicBoolean(inner=operation)
        elif isinstance(other, SecretInteger):
            operation = GreaterOrEqualThan(left=self, right=other, source_ref=SourceRef.back_frame())
            return SecretBoolean(inner=operation)
        else:
            raise TypeError(f"Invalid operation: {self} >= {other}")

    def __eq__(
        self, other: Union["Integer", "PublicInteger"]
    ) -> "PublicBoolean":
        if isinstance(other, Integer):
            operation = Equals(left=self, right=other, source_ref=SourceRef.back_frame())
            return PublicBoolean(inner=operation)
        elif isinstance(other, PublicInteger):
            operation = Equals(left=self, right=other, source_ref=SourceRef.back_frame())
            return PublicBoolean(inner=operation)
        else:
            raise TypeError(f"Invalid operation: {self} == {other}")

@dataclass
class SecretInteger(NadaType):
    def __add__(
        self, other: Union["Integer", "PublicInteger", "SecretInteger"]
    ) -> "SecretInteger":
        if isinstance(other, Integer):
            operation = Addition(left=self, right=other, source_ref=SourceRef.back_frame())
            return SecretInteger(inner=operation)
        elif isinstance(other, PublicInteger):
            operation = Addition(left=self, right=other, source_ref=SourceRef.back_frame())
            return SecretInteger(inner=operation)
        elif isinstance(other, SecretInteger):
            operation = Addition(left=self, right=other, source_ref=SourceRef.back_frame())
            return SecretInteger(inner=operation)
        else:
            raise TypeError(f"Invalid operation: {self} + {other}")

    def __sub__(
        self, other: Union["Integer", "PublicInteger", "SecretInteger"]
    ) -> "SecretInteger":
        if isinstance(other, Integer):
            operation = Subtraction(left=self, right=other, source_ref=SourceRef.back_frame())
            return SecretInteger(inner=operation)
        elif isinstance(other, PublicInteger):
            operation = Subtraction(left=self, right=other, source_ref=SourceRef.back_frame())
            return SecretInteger(inner=operation)
        elif isinstance(other, SecretInteger):
            operation = Subtraction(left=self, right=other, source_ref=SourceRef.back_frame())
            return SecretInteger(inner=operation)
        else:
            raise TypeError(f"Invalid operation: {self} - {other}")

    def __mul__(
        self, other: Union["Integer", "PublicInteger", "SecretInteger"]
    ) -> "SecretInteger":
        if isinstance(other, Integer):
            operation = Multiplication(left=self, right=other, source_ref=SourceRef.back_frame())
            return SecretInteger(inner=operation)
        elif isinstance(other, PublicInteger):
            operation = Multiplication(left=self, right=other, source_ref=SourceRef.back_frame())
            return SecretInteger(inner=operation)
        elif isinstance(other, SecretInteger):
            operation = Multiplication(left=self, right=other, source_ref=SourceRef.back_frame())
            return SecretInteger(inner=operation)
        else:
            raise TypeError(f"Invalid operation: {self} * {other}")

    def __truediv__(
        self, other: Union["Integer", "PublicInteger"]
    ) -> "SecretInteger":
        if isinstance(other, Integer):
            operation = Division(left=self, right=other, source_ref=SourceRef.back_frame())
            return SecretInteger(inner=operation)
        elif isinstance(other, PublicInteger):
            operation = Division(left=self, right=other, source_ref=SourceRef.back_frame())
            return SecretInteger(inner=operation)
        else:
            raise TypeError(f"Invalid operation: {self} / {other}")

    def __mod__(
        self, other: Union["Integer", "PublicInteger"]
    ) -> "SecretInteger":
        if isinstance(other, Integer):
            operation = Modulo(left=self, right=other, source_ref=SourceRef.back_frame())
            return SecretInteger(inner=operation)
        elif isinstance(other, PublicInteger):
            operation = Modulo(left=self, right=other, source_ref=SourceRef.back_frame())
            return SecretInteger(inner=operation)
        else:
            raise TypeError(f"Invalid operation: {self} % {other}")

    def __pow__(
        self, other: Union["Integer", "PublicInteger"]
    ) -> "SecretInteger":
        if isinstance(other, Integer):
            operation = Power(left=self, right=other, source_ref=SourceRef.back_frame())
            return SecretInteger(inner=operation)
        elif isinstance(other, PublicInteger):
            operation = Power(left=self, right=other, source_ref=SourceRef.back_frame())
            return SecretInteger(inner=operation)
        else:
            raise TypeError(f"Invalid operation: {self} ** {other}")

    def __lshift__(
        self, other: Union["Integer", "PublicInteger"]
    ) -> "SecretInteger":
        if isinstance(other, Integer):
            operation = LeftShift(left=self, right=other, source_ref=SourceRef.back_frame())
            return SecretInteger(inner=operation)
        elif isinstance(other, PublicInteger):
            operation = LeftShift(left=self, right=other, source_ref=SourceRef.back_frame())
            return SecretInteger(inner=operation)
        else:
            raise TypeError(f"Invalid operation: {self} << {other}")

    def __rshift__(
        self, other: Union["Integer", "PublicInteger"]
    ) -> "SecretInteger":
        if isinstance(other, Integer):
            operation = RightShift(left=self, right=other, source_ref=SourceRef.back_frame())
            return SecretInteger(inner=operation)
        elif isinstance(other, PublicInteger):
            operation = RightShift(left=self, right=other, source_ref=SourceRef.back_frame())
            return SecretInteger(inner=operation)
        else:
            raise TypeError(f"Invalid operation: {self} >> {other}")

    def __lt__(
        self, other: Union["Integer", "PublicInteger", "SecretInteger"]
    ) -> "SecretBoolean":
        if isinstance(other, Integer):
            operation = LessThan(left=self, right=other, source_ref=SourceRef.back_frame())
            return SecretBoolean(inner=operation)
        elif isinstance(other, PublicInteger):
            operation = LessThan(left=self, right=other, source_ref=SourceRef.back_frame())
            return SecretBoolean(inner=operation)
        elif isinstance(other, SecretInteger):
            operation = LessThan(left=self, right=other, source_ref=SourceRef.back_frame())
            return SecretBoolean(inner=operation)
        else:
            raise TypeError(f"Invalid operation: {self} < {other}")

    def __gt__(
        self, other: Union["Integer", "PublicInteger", "SecretInteger"]
    ) -> "SecretBoolean":
        if isinstance(other, Integer):
            operation = GreaterThan(left=self, right=other, source_ref=SourceRef.back_frame())
            return SecretBoolean(inner=operation)
        elif isinstance(other, PublicInteger):
            operation = GreaterThan(left=self, right=other, source_ref=SourceRef.back_frame())
            return SecretBoolean(inner=operation)
        elif isinstance(other, SecretInteger):
            operation = GreaterThan(left=self, right=other, source_ref=SourceRef.back_frame())
            return SecretBoolean(inner=operation)
        else:
            raise TypeError(f"Invalid operation: {self} > {other}")

    def __le__(
        self, other: Union["Integer", "PublicInteger", "SecretInteger"]
    ) -> "SecretBoolean":
        if isinstance(other, Integer):
            operation = LessOrEqualThan(left=self, right=other, source_ref=SourceRef.back_frame())
            return SecretBoolean(inner=operation)
        elif isinstance(other, PublicInteger):
            operation = LessOrEqualThan(left=self, right=other, source_ref=SourceRef.back_frame())
            return SecretBoolean(inner=operation)
        elif isinstance(other, SecretInteger):
            operation = LessOrEqualThan(left=self, right=other, source_ref=SourceRef.back_frame())
            return SecretBoolean(inner=operation)
        else:
            raise TypeError(f"Invalid operation: {self} <= {other}")

    def __ge__(
        self, other: Union["Integer", "PublicInteger", "SecretInteger"]
    ) -> "SecretBoolean":
        if isinstance(other, Integer):
            operation = GreaterOrEqualThan(left=self, right=other, source_ref=SourceRef.back_frame())
            return SecretBoolean(inner=operation)
        elif isinstance(other, PublicInteger):
            operation = GreaterOrEqualThan(left=self, right=other, source_ref=SourceRef.back_frame())
            return SecretBoolean(inner=operation)
        elif isinstance(other, SecretInteger):
            operation = GreaterOrEqualThan(left=self, right=other, source_ref=SourceRef.back_frame())
            return SecretBoolean(inner=operation)
        else:
            raise TypeError(f"Invalid operation: {self} >= {other}")

    def __eq__(
        self, other: Union["Integer", "SecretInteger"]
    ) -> "SecretBoolean":
        if isinstance(other, Integer):
            operation = Equals(left=self, right=other, source_ref=SourceRef.back_frame())
            return SecretBoolean(inner=operation)
        elif isinstance(other, SecretInteger):
            operation = Equals(left=self, right=other, source_ref=SourceRef.back_frame())
            return SecretBoolean(inner=operation)
        else:
            raise TypeError(f"Invalid operation: {self} == {other}")

