from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ExecutionAcceptorRequestType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ExecutionAcceptorRequestType_Undefined: _ClassVar[ExecutionAcceptorRequestType]
    ExecutionAcceptorRequestType_ExecutionUpdateInfo: _ClassVar[ExecutionAcceptorRequestType]

class EnumExecTransType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumExecTransType_Undefined: _ClassVar[EnumExecTransType]
    EnumExecTransType_Cancel: _ClassVar[EnumExecTransType]
    EnumExecTransType_Correct: _ClassVar[EnumExecTransType]
    EnumExecTransType_Status: _ClassVar[EnumExecTransType]
    EnumExecTransType_New: _ClassVar[EnumExecTransType]

class ExecutionInitiatorRequestType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ExecutionInitiatorRequestType_Undefined: _ClassVar[ExecutionInitiatorRequestType]
    ExecutionInitiatorRequestType_OrderInitiation: _ClassVar[ExecutionInitiatorRequestType]
ExecutionAcceptorRequestType_Undefined: ExecutionAcceptorRequestType
ExecutionAcceptorRequestType_ExecutionUpdateInfo: ExecutionAcceptorRequestType
EnumExecTransType_Undefined: EnumExecTransType
EnumExecTransType_Cancel: EnumExecTransType
EnumExecTransType_Correct: EnumExecTransType
EnumExecTransType_Status: EnumExecTransType
EnumExecTransType_New: EnumExecTransType
ExecutionInitiatorRequestType_Undefined: ExecutionInitiatorRequestType
ExecutionInitiatorRequestType_OrderInitiation: ExecutionInitiatorRequestType
