import common_pb2 as _common_pb2
import sessions_enums_pb2 as _sessions_enums_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateSessionRequest(_message.Message):
    __slots__ = ("LanguageCode", "RegionCode", "AzureAdAccessToken")
    LANGUAGECODE_FIELD_NUMBER: _ClassVar[int]
    REGIONCODE_FIELD_NUMBER: _ClassVar[int]
    AZUREADACCESSTOKEN_FIELD_NUMBER: _ClassVar[int]
    LanguageCode: str
    RegionCode: str
    AzureAdAccessToken: str
    def __init__(self, LanguageCode: _Optional[str] = ..., RegionCode: _Optional[str] = ..., AzureAdAccessToken: _Optional[str] = ...) -> None: ...

class SessionInfoResponse(_message.Message):
    __slots__ = ("HasData", "MustReLogin", "SessionId", "UserType", "RequestId", "UserLabel", "Warnings", "Errors")
    HASDATA_FIELD_NUMBER: _ClassVar[int]
    MUSTRELOGIN_FIELD_NUMBER: _ClassVar[int]
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    USERTYPE_FIELD_NUMBER: _ClassVar[int]
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    USERLABEL_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    HasData: bool
    MustReLogin: bool
    SessionId: str
    UserType: _sessions_enums_pb2.EnumUserType
    RequestId: str
    UserLabel: str
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, HasData: bool = ..., MustReLogin: bool = ..., SessionId: _Optional[str] = ..., UserType: _Optional[_Union[_sessions_enums_pb2.EnumUserType, str]] = ..., RequestId: _Optional[str] = ..., UserLabel: _Optional[str] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...
