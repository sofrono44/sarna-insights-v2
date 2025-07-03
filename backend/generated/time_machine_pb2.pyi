from google.protobuf import timestamp_pb2 as _timestamp_pb2
import common_pb2 as _common_pb2
import bp_pb2 as _bp_pb2
import pmbp_pb2 as _pmbp_pb2
import time_machine_enums_pb2 as _time_machine_enums_pb2
import accounts_pb2 as _accounts_pb2
import common_pb2 as _common_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TimeMachineBrowseRequest(_message.Message):
    __slots__ = ("AccountId", "AccountNumber", "From", "To", "RequestOrigin")
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTNUMBER_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    REQUESTORIGIN_FIELD_NUMBER: _ClassVar[int]
    AccountId: int
    AccountNumber: str
    From: _timestamp_pb2.Timestamp
    To: _timestamp_pb2.Timestamp
    RequestOrigin: _time_machine_enums_pb2.EnumTimeMachineRequestOrigin
    def __init__(self, AccountId: _Optional[int] = ..., AccountNumber: _Optional[str] = ..., From: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., To: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., RequestOrigin: _Optional[_Union[_time_machine_enums_pb2.EnumTimeMachineRequestOrigin, str]] = ...) -> None: ...

class TimeMachineDownloadRequest(_message.Message):
    __slots__ = ("FileName",)
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    FileName: str
    def __init__(self, FileName: _Optional[str] = ...) -> None: ...

class TimeMachineBrowseResponse(_message.Message):
    __slots__ = ("Files", "AccountGroups", "Warnings", "Errors")
    FILES_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTGROUPS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    Files: _containers.RepeatedCompositeFieldContainer[TimeMachineFileInfo]
    AccountGroups: _containers.RepeatedCompositeFieldContainer[_accounts_pb2.AccountGroupLight]
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2_1.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2_1.ResponseError]
    def __init__(self, Files: _Optional[_Iterable[_Union[TimeMachineFileInfo, _Mapping]]] = ..., AccountGroups: _Optional[_Iterable[_Union[_accounts_pb2.AccountGroupLight, _Mapping]]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2_1.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2_1.ResponseError, _Mapping]]] = ...) -> None: ...

class TimeMachineFileInfo(_message.Message):
    __slots__ = ("FileName", "IsArchived", "CreatedTime", "RequestOrigin", "Type", "Requirement", "NetLiquidity", "DayPnL", "DayPnLUtilization", "CreditUtilization", "ExcessLiquidity", "AccountGroupIds", "WarningCount", "ErrorCount")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    ISARCHIVED_FIELD_NUMBER: _ClassVar[int]
    CREATEDTIME_FIELD_NUMBER: _ClassVar[int]
    REQUESTORIGIN_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    REQUIREMENT_FIELD_NUMBER: _ClassVar[int]
    NETLIQUIDITY_FIELD_NUMBER: _ClassVar[int]
    DAYPNL_FIELD_NUMBER: _ClassVar[int]
    DAYPNLUTILIZATION_FIELD_NUMBER: _ClassVar[int]
    CREDITUTILIZATION_FIELD_NUMBER: _ClassVar[int]
    EXCESSLIQUIDITY_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTGROUPIDS_FIELD_NUMBER: _ClassVar[int]
    WARNINGCOUNT_FIELD_NUMBER: _ClassVar[int]
    ERRORCOUNT_FIELD_NUMBER: _ClassVar[int]
    FileName: str
    IsArchived: bool
    CreatedTime: _timestamp_pb2.Timestamp
    RequestOrigin: _time_machine_enums_pb2.EnumTimeMachineRequestOrigin
    Type: _time_machine_enums_pb2.EnumBpType
    Requirement: int
    NetLiquidity: int
    DayPnL: int
    DayPnLUtilization: float
    CreditUtilization: float
    ExcessLiquidity: int
    AccountGroupIds: _containers.RepeatedScalarFieldContainer[int]
    WarningCount: int
    ErrorCount: int
    def __init__(self, FileName: _Optional[str] = ..., IsArchived: bool = ..., CreatedTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., RequestOrigin: _Optional[_Union[_time_machine_enums_pb2.EnumTimeMachineRequestOrigin, str]] = ..., Type: _Optional[_Union[_time_machine_enums_pb2.EnumBpType, str]] = ..., Requirement: _Optional[int] = ..., NetLiquidity: _Optional[int] = ..., DayPnL: _Optional[int] = ..., DayPnLUtilization: _Optional[float] = ..., CreditUtilization: _Optional[float] = ..., ExcessLiquidity: _Optional[int] = ..., AccountGroupIds: _Optional[_Iterable[int]] = ..., WarningCount: _Optional[int] = ..., ErrorCount: _Optional[int] = ...) -> None: ...

class TimeMachineDownloadResponse(_message.Message):
    __slots__ = ("FileName", "Request", "Response", "PmBpValuesResponse", "PmBpForProposedOrderResponse", "BpValuesResponse", "RegTBpForProposedOrderResponseInfo", "PortfolioReport", "Warnings", "Errors")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    PMBPVALUESRESPONSE_FIELD_NUMBER: _ClassVar[int]
    PMBPFORPROPOSEDORDERRESPONSE_FIELD_NUMBER: _ClassVar[int]
    BPVALUESRESPONSE_FIELD_NUMBER: _ClassVar[int]
    REGTBPFORPROPOSEDORDERRESPONSEINFO_FIELD_NUMBER: _ClassVar[int]
    PORTFOLIOREPORT_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    FileName: str
    Request: str
    Response: str
    PmBpValuesResponse: _pmbp_pb2.PmBpValuesResponse
    PmBpForProposedOrderResponse: _pmbp_pb2.PmBpForProposedOrderResponse
    BpValuesResponse: _bp_pb2.BpValuesResponse
    RegTBpForProposedOrderResponseInfo: _bp_pb2.RegTBpForProposedOrderResponseInfo
    PortfolioReport: str
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2_1.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2_1.ResponseError]
    def __init__(self, FileName: _Optional[str] = ..., Request: _Optional[str] = ..., Response: _Optional[str] = ..., PmBpValuesResponse: _Optional[_Union[_pmbp_pb2.PmBpValuesResponse, _Mapping]] = ..., PmBpForProposedOrderResponse: _Optional[_Union[_pmbp_pb2.PmBpForProposedOrderResponse, _Mapping]] = ..., BpValuesResponse: _Optional[_Union[_bp_pb2.BpValuesResponse, _Mapping]] = ..., RegTBpForProposedOrderResponseInfo: _Optional[_Union[_bp_pb2.RegTBpForProposedOrderResponseInfo, _Mapping]] = ..., PortfolioReport: _Optional[str] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2_1.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2_1.ResponseError, _Mapping]]] = ...) -> None: ...
