import user_pb2 as _user_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from admin import audit_trail_enums_pb2 as _audit_trail_enums_pb2
import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AuditTrail(_message.Message):
    __slots__ = ("Id", "Data", "Metadata", "CreatedTime", "Type", "AffectedUser", "ExecutingUser")
    ID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CREATEDTIME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    AFFECTEDUSER_FIELD_NUMBER: _ClassVar[int]
    EXECUTINGUSER_FIELD_NUMBER: _ClassVar[int]
    Id: int
    Data: str
    Metadata: str
    CreatedTime: _timestamp_pb2.Timestamp
    Type: _audit_trail_enums_pb2.EnumRegulatoryAuditTrailType
    AffectedUser: _user_pb2.User
    ExecutingUser: _user_pb2.User
    def __init__(self, Id: _Optional[int] = ..., Data: _Optional[str] = ..., Metadata: _Optional[str] = ..., CreatedTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., Type: _Optional[_Union[_audit_trail_enums_pb2.EnumRegulatoryAuditTrailType, str]] = ..., AffectedUser: _Optional[_Union[_user_pb2.User, _Mapping]] = ..., ExecutingUser: _Optional[_Union[_user_pb2.User, _Mapping]] = ...) -> None: ...

class AdminRegulatoryAuditTrailResponse(_message.Message):
    __slots__ = ("Items", "Warnings", "Errors")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    Items: _containers.RepeatedCompositeFieldContainer[AuditTrail]
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, Items: _Optional[_Iterable[_Union[AuditTrail, _Mapping]]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class AdminRegulatoryAuditTrailRequest(_message.Message):
    __slots__ = ("AffectedUserId", "AffectedAccountId")
    AFFECTEDUSERID_FIELD_NUMBER: _ClassVar[int]
    AFFECTEDACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    AffectedUserId: int
    AffectedAccountId: int
    def __init__(self, AffectedUserId: _Optional[int] = ..., AffectedAccountId: _Optional[int] = ...) -> None: ...
