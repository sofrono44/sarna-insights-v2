import common_pb2 as _common_pb2
import common_bp_enums_pb2 as _common_bp_enums_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AskForTradingLevelChangeRequest(_message.Message):
    __slots__ = ("AccountId", "AccountNumber", "ExpectedTradingLevel")
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTNUMBER_FIELD_NUMBER: _ClassVar[int]
    EXPECTEDTRADINGLEVEL_FIELD_NUMBER: _ClassVar[int]
    AccountId: int
    AccountNumber: str
    ExpectedTradingLevel: _common_bp_enums_pb2.EnumBpOptionTradingLevel
    def __init__(self, AccountId: _Optional[int] = ..., AccountNumber: _Optional[str] = ..., ExpectedTradingLevel: _Optional[_Union[_common_bp_enums_pb2.EnumBpOptionTradingLevel, str]] = ...) -> None: ...

class AskForTradingLevelChangeResponse(_message.Message):
    __slots__ = ("Warnings", "Errors")
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...
