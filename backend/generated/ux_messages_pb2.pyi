import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetUxMessagesRequest(_message.Message):
    __slots__ = ("LanguageCode",)
    LANGUAGECODE_FIELD_NUMBER: _ClassVar[int]
    LanguageCode: str
    def __init__(self, LanguageCode: _Optional[str] = ...) -> None: ...

class GetUxMessagesResponse(_message.Message):
    __slots__ = ("UxMessages", "Warnings", "Errors")
    UXMESSAGES_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    UxMessages: _containers.RepeatedCompositeFieldContainer[UxMessage]
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, UxMessages: _Optional[_Iterable[_Union[UxMessage, _Mapping]]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class UxMessage(_message.Message):
    __slots__ = ("Code", "Message")
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    Code: str
    Message: str
    def __init__(self, Code: _Optional[str] = ..., Message: _Optional[str] = ...) -> None: ...
