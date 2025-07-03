from google.protobuf import timestamp_pb2 as _timestamp_pb2
from admin import account_pb2 as _account_pb2
import common_bp_enums_pb2 as _common_bp_enums_pb2
import user_pb2 as _user_pb2
from admin import admin_trading_level_change_enums_pb2 as _admin_trading_level_change_enums_pb2
import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
from common_pb2 import ResponseError as ResponseError
from common_pb2 import ResponseWarning as ResponseWarning
from common_pb2 import ResponseMessage as ResponseMessage
from common_pb2 import MOVEShockInput as MOVEShockInput
from common_pb2 import MOVECreditSpreadShockInput as MOVECreditSpreadShockInput
from common_pb2 import YieldShockInput as YieldShockInput

DESCRIPTOR: _descriptor.FileDescriptor

class AdminTradingLevelChange(_message.Message):
    __slots__ = ("Id", "Status", "CreatedTime", "ExpectedTradingLevel", "Reason", "RecommendedTradingLevel")
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATEDTIME_FIELD_NUMBER: _ClassVar[int]
    EXPECTEDTRADINGLEVEL_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDEDTRADINGLEVEL_FIELD_NUMBER: _ClassVar[int]
    Id: int
    Status: _admin_trading_level_change_enums_pb2.EnumAccountApprovalStatus
    CreatedTime: _timestamp_pb2.Timestamp
    ExpectedTradingLevel: _common_bp_enums_pb2.EnumBpOptionTradingLevel
    Reason: str
    RecommendedTradingLevel: _common_bp_enums_pb2.EnumBpOptionTradingLevel
    def __init__(self, Id: _Optional[int] = ..., Status: _Optional[_Union[_admin_trading_level_change_enums_pb2.EnumAccountApprovalStatus, str]] = ..., CreatedTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ExpectedTradingLevel: _Optional[_Union[_common_bp_enums_pb2.EnumBpOptionTradingLevel, str]] = ..., Reason: _Optional[str] = ..., RecommendedTradingLevel: _Optional[_Union[_common_bp_enums_pb2.EnumBpOptionTradingLevel, str]] = ...) -> None: ...

class AdminSearchTradingLevelChange(_message.Message):
    __slots__ = ("Approval", "User", "Account")
    APPROVAL_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    Approval: AdminTradingLevelChange
    User: _user_pb2.User
    Account: _account_pb2.AdminSearchAccount
    def __init__(self, Approval: _Optional[_Union[AdminTradingLevelChange, _Mapping]] = ..., User: _Optional[_Union[_user_pb2.User, _Mapping]] = ..., Account: _Optional[_Union[_account_pb2.AdminSearchAccount, _Mapping]] = ...) -> None: ...

class AdminSearchTradingLevelChangeRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AdminSearchTradingLevelChangeResponse(_message.Message):
    __slots__ = ("Items", "Warnings", "Errors")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    Items: _containers.RepeatedCompositeFieldContainer[AdminSearchTradingLevelChange]
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, Items: _Optional[_Iterable[_Union[AdminSearchTradingLevelChange, _Mapping]]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class ResolveTradingLevelChangeRequest(_message.Message):
    __slots__ = ("ApprovalId", "Approve", "Reject")
    class ApproveTradingLevelChange(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class RejectTradingLevelChange(_message.Message):
        __slots__ = ("Reason",)
        REASON_FIELD_NUMBER: _ClassVar[int]
        Reason: str
        def __init__(self, Reason: _Optional[str] = ...) -> None: ...
    APPROVALID_FIELD_NUMBER: _ClassVar[int]
    APPROVE_FIELD_NUMBER: _ClassVar[int]
    REJECT_FIELD_NUMBER: _ClassVar[int]
    ApprovalId: int
    Approve: ResolveTradingLevelChangeRequest.ApproveTradingLevelChange
    Reject: ResolveTradingLevelChangeRequest.RejectTradingLevelChange
    def __init__(self, ApprovalId: _Optional[int] = ..., Approve: _Optional[_Union[ResolveTradingLevelChangeRequest.ApproveTradingLevelChange, _Mapping]] = ..., Reject: _Optional[_Union[ResolveTradingLevelChangeRequest.RejectTradingLevelChange, _Mapping]] = ...) -> None: ...
