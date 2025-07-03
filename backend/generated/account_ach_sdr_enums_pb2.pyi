from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EnumAbaAccountType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumAbaAccountType_Undefined: _ClassVar[EnumAbaAccountType]
    EnumAbaAccountType_Checking: _ClassVar[EnumAbaAccountType]
    EnumAbaAccountType_Savings: _ClassVar[EnumAbaAccountType]

class EnumAbaAccountOwnerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumAbaAccountOwnerType_Undefined: _ClassVar[EnumAbaAccountOwnerType]
    EnumAbaAccountOwnerType_Individual: _ClassVar[EnumAbaAccountOwnerType]
    EnumAbaAccountOwnerType_Business: _ClassVar[EnumAbaAccountOwnerType]
EnumAbaAccountType_Undefined: EnumAbaAccountType
EnumAbaAccountType_Checking: EnumAbaAccountType
EnumAbaAccountType_Savings: EnumAbaAccountType
EnumAbaAccountOwnerType_Undefined: EnumAbaAccountOwnerType
EnumAbaAccountOwnerType_Individual: EnumAbaAccountOwnerType
EnumAbaAccountOwnerType_Business: EnumAbaAccountOwnerType
