from google.protobuf import timestamp_pb2 as _timestamp_pb2
from admin import admin_mde_enums_pb2 as _admin_mde_enums_pb2
import account_application_pb2 as _account_application_pb2
import common_pb2 as _common_pb2
import market_data_entitlement_pb2 as _market_data_entitlement_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AdminSearchMdeRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AdminSearchMdeResponse(_message.Message):
    __slots__ = ("Items", "Warnings", "Errors")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    Items: _containers.RepeatedCompositeFieldContainer[MdeRequest]
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, Items: _Optional[_Iterable[_Union[MdeRequest, _Mapping]]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class MdeRequest(_message.Message):
    __slots__ = ("Id", "Mde", "CreatedTime", "Employment")
    ID_FIELD_NUMBER: _ClassVar[int]
    MDE_FIELD_NUMBER: _ClassVar[int]
    CREATEDTIME_FIELD_NUMBER: _ClassVar[int]
    EMPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    Id: int
    Mde: _market_data_entitlement_pb2.MarketDataEntitlementFormResponses
    CreatedTime: _timestamp_pb2.Timestamp
    Employment: _account_application_pb2.Employment
    def __init__(self, Id: _Optional[int] = ..., Mde: _Optional[_Union[_market_data_entitlement_pb2.MarketDataEntitlementFormResponses, _Mapping]] = ..., CreatedTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., Employment: _Optional[_Union[_account_application_pb2.Employment, _Mapping]] = ...) -> None: ...

class ResolveMdeRequest(_message.Message):
    __slots__ = ("MarketDataEntitlementId", "Action", "Reason")
    MARKETDATAENTITLEMENTID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    MarketDataEntitlementId: int
    Action: _admin_mde_enums_pb2.EnumAdminMdeAction
    Reason: str
    def __init__(self, MarketDataEntitlementId: _Optional[int] = ..., Action: _Optional[_Union[_admin_mde_enums_pb2.EnumAdminMdeAction, str]] = ..., Reason: _Optional[str] = ...) -> None: ...
