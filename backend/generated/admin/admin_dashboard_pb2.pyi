from google.protobuf import timestamp_pb2 as _timestamp_pb2
import accounts_pb2 as _accounts_pb2
import common_pb2 as _common_pb2
import sessions_enums_pb2 as _sessions_enums_pb2
from admin import admin_trading_level_change_pb2 as _admin_trading_level_change_pb2
import common_pb2 as _common_pb2_1
from admin import admin_mde_pb2 as _admin_mde_pb2
from admin import admin_dashboard_enums_pb2 as _admin_dashboard_enums_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AdminDashboardRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AdminDashboardResponse(_message.Message):
    __slots__ = ("items", "Warnings", "Errors")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[AdminDashboardItem]
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2_1.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2_1.ResponseError]
    def __init__(self, items: _Optional[_Iterable[_Union[AdminDashboardItem, _Mapping]]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2_1.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2_1.ResponseError, _Mapping]]] = ...) -> None: ...

class VerificationDecision(_message.Message):
    __slots__ = ("VerificationDecisionId", "VerificationSessionId", "Status", "DecisionTime")
    VERIFICATIONDECISIONID_FIELD_NUMBER: _ClassVar[int]
    VERIFICATIONSESSIONID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DECISIONTIME_FIELD_NUMBER: _ClassVar[int]
    VerificationDecisionId: int
    VerificationSessionId: str
    Status: _sessions_enums_pb2.EnumVerificationStatus
    DecisionTime: _timestamp_pb2.Timestamp
    def __init__(self, VerificationDecisionId: _Optional[int] = ..., VerificationSessionId: _Optional[str] = ..., Status: _Optional[_Union[_sessions_enums_pb2.EnumVerificationStatus, str]] = ..., DecisionTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AdminDashboardItem(_message.Message):
    __slots__ = ("type", "verificationDecision", "account", "tradingLevelChange", "marketDataEntitlement")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VERIFICATIONDECISION_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    TRADINGLEVELCHANGE_FIELD_NUMBER: _ClassVar[int]
    MARKETDATAENTITLEMENT_FIELD_NUMBER: _ClassVar[int]
    type: _admin_dashboard_enums_pb2.EnumAdminDashboardItemType
    verificationDecision: VerificationDecision
    account: _accounts_pb2.Account
    tradingLevelChange: _admin_trading_level_change_pb2.AdminSearchTradingLevelChange
    marketDataEntitlement: _admin_mde_pb2.MdeRequest
    def __init__(self, type: _Optional[_Union[_admin_dashboard_enums_pb2.EnumAdminDashboardItemType, str]] = ..., verificationDecision: _Optional[_Union[VerificationDecision, _Mapping]] = ..., account: _Optional[_Union[_accounts_pb2.Account, _Mapping]] = ..., tradingLevelChange: _Optional[_Union[_admin_trading_level_change_pb2.AdminSearchTradingLevelChange, _Mapping]] = ..., marketDataEntitlement: _Optional[_Union[_admin_mde_pb2.MdeRequest, _Mapping]] = ...) -> None: ...
