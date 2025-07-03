from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EnumTradeRequestType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumTradeRequestType_Undefined: _ClassVar[EnumTradeRequestType]
    EnumTradeRequestType_ReviewOrder: _ClassVar[EnumTradeRequestType]
    EnumTradeRequestType_InitiateOrderExecution: _ClassVar[EnumTradeRequestType]
EnumTradeRequestType_Undefined: EnumTradeRequestType
EnumTradeRequestType_ReviewOrder: EnumTradeRequestType
EnumTradeRequestType_InitiateOrderExecution: EnumTradeRequestType
