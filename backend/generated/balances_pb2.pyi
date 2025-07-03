import common_pb2 as _common_pb2
import bp_pb2 as _bp_pb2
import pmbp_pb2 as _pmbp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BalancesInfoRequest(_message.Message):
    __slots__ = ("AccountIDs", "AccountNumbers", "ReturnOccStyleReportForPM")
    ACCOUNTIDS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTNUMBERS_FIELD_NUMBER: _ClassVar[int]
    RETURNOCCSTYLEREPORTFORPM_FIELD_NUMBER: _ClassVar[int]
    AccountIDs: _containers.RepeatedScalarFieldContainer[int]
    AccountNumbers: _containers.RepeatedScalarFieldContainer[str]
    ReturnOccStyleReportForPM: bool
    def __init__(self, AccountIDs: _Optional[_Iterable[int]] = ..., AccountNumbers: _Optional[_Iterable[str]] = ..., ReturnOccStyleReportForPM: bool = ...) -> None: ...

class BalancesInfoResponse(_message.Message):
    __slots__ = ("HasData", "AccountBalances", "Warnings", "Errors")
    class AccountBalancesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: AccountBalanceInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[AccountBalanceInfo, _Mapping]] = ...) -> None: ...
    HASDATA_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTBALANCES_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    HasData: bool
    AccountBalances: _containers.MessageMap[int, AccountBalanceInfo]
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, HasData: bool = ..., AccountBalances: _Optional[_Mapping[int, AccountBalanceInfo]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class AccountBalanceInfo(_message.Message):
    __slots__ = ("AccountId", "BpValuesResponse", "SubaccountBalancesInfos", "YesterdayLiquidationValue", "Cash", "PmBpValuesResponse", "OccStyleReportForPM", "IsPMAccount")
    class SubaccountBalancesInfosEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: SubaccountBalanceInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[SubaccountBalanceInfo, _Mapping]] = ...) -> None: ...
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    BPVALUESRESPONSE_FIELD_NUMBER: _ClassVar[int]
    SUBACCOUNTBALANCESINFOS_FIELD_NUMBER: _ClassVar[int]
    YESTERDAYLIQUIDATIONVALUE_FIELD_NUMBER: _ClassVar[int]
    CASH_FIELD_NUMBER: _ClassVar[int]
    PMBPVALUESRESPONSE_FIELD_NUMBER: _ClassVar[int]
    OCCSTYLEREPORTFORPM_FIELD_NUMBER: _ClassVar[int]
    ISPMACCOUNT_FIELD_NUMBER: _ClassVar[int]
    AccountId: int
    BpValuesResponse: _bp_pb2.BpValuesResponse
    SubaccountBalancesInfos: _containers.MessageMap[int, SubaccountBalanceInfo]
    YesterdayLiquidationValue: float
    Cash: float
    PmBpValuesResponse: _pmbp_pb2.PmBpValuesResponse
    OccStyleReportForPM: str
    IsPMAccount: bool
    def __init__(self, AccountId: _Optional[int] = ..., BpValuesResponse: _Optional[_Union[_bp_pb2.BpValuesResponse, _Mapping]] = ..., SubaccountBalancesInfos: _Optional[_Mapping[int, SubaccountBalanceInfo]] = ..., YesterdayLiquidationValue: _Optional[float] = ..., Cash: _Optional[float] = ..., PmBpValuesResponse: _Optional[_Union[_pmbp_pb2.PmBpValuesResponse, _Mapping]] = ..., OccStyleReportForPM: _Optional[str] = ..., IsPMAccount: bool = ...) -> None: ...

class SubaccountBalanceInfo(_message.Message):
    __slots__ = ("SubaccountId", "YesterdayLiquidationValue", "Cash")
    SUBACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    YESTERDAYLIQUIDATIONVALUE_FIELD_NUMBER: _ClassVar[int]
    CASH_FIELD_NUMBER: _ClassVar[int]
    SubaccountId: int
    YesterdayLiquidationValue: float
    Cash: float
    def __init__(self, SubaccountId: _Optional[int] = ..., YesterdayLiquidationValue: _Optional[float] = ..., Cash: _Optional[float] = ...) -> None: ...

class BalanceAdjustmentRequest(_message.Message):
    __slots__ = ("BalanceAdjustments",)
    BALANCEADJUSTMENTS_FIELD_NUMBER: _ClassVar[int]
    BalanceAdjustments: _containers.RepeatedCompositeFieldContainer[BalanceAdjustment]
    def __init__(self, BalanceAdjustments: _Optional[_Iterable[_Union[BalanceAdjustment, _Mapping]]] = ...) -> None: ...

class BalanceCashInfoRequest(_message.Message):
    __slots__ = ("AccountId", "AccountNumber")
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTNUMBER_FIELD_NUMBER: _ClassVar[int]
    AccountId: int
    AccountNumber: str
    def __init__(self, AccountId: _Optional[int] = ..., AccountNumber: _Optional[str] = ...) -> None: ...

class BalanceCashInfoResponse(_message.Message):
    __slots__ = ("Cash", "Sma", "Warnings", "Errors")
    CASH_FIELD_NUMBER: _ClassVar[int]
    SMA_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    Cash: float
    Sma: float
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, Cash: _Optional[float] = ..., Sma: _Optional[float] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class BalanceAdjustment(_message.Message):
    __slots__ = ("AccountId", "AccountNumber", "CashAdjustment", "SMAAdjustment", "Details")
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTNUMBER_FIELD_NUMBER: _ClassVar[int]
    CASHADJUSTMENT_FIELD_NUMBER: _ClassVar[int]
    SMAADJUSTMENT_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    AccountId: int
    AccountNumber: str
    CashAdjustment: float
    SMAAdjustment: float
    Details: str
    def __init__(self, AccountId: _Optional[int] = ..., AccountNumber: _Optional[str] = ..., CashAdjustment: _Optional[float] = ..., SMAAdjustment: _Optional[float] = ..., Details: _Optional[str] = ...) -> None: ...

class BalanceAdjustmentResponse(_message.Message):
    __slots__ = ("BalanceAdjustmentStatuses", "Warnings", "Errors")
    BALANCEADJUSTMENTSTATUSES_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    BalanceAdjustmentStatuses: _containers.RepeatedCompositeFieldContainer[BalanceAdjustmentStatus]
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, BalanceAdjustmentStatuses: _Optional[_Iterable[_Union[BalanceAdjustmentStatus, _Mapping]]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class BalanceAdjustmentStatus(_message.Message):
    __slots__ = ("AccountId", "AccountNumber", "IsSuccess")
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTNUMBER_FIELD_NUMBER: _ClassVar[int]
    ISSUCCESS_FIELD_NUMBER: _ClassVar[int]
    AccountId: int
    AccountNumber: str
    IsSuccess: bool
    def __init__(self, AccountId: _Optional[int] = ..., AccountNumber: _Optional[str] = ..., IsSuccess: bool = ...) -> None: ...
