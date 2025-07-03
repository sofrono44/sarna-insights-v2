from google.protobuf import timestamp_pb2 as _timestamp_pb2
import account_maintenance_fee_enums_pb2 as _account_maintenance_fee_enums_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AccountMaintenanceFeeInfo(_message.Message):
    __slots__ = ("AccountId", "AccountMaintenanceFee")
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTMAINTENANCEFEE_FIELD_NUMBER: _ClassVar[int]
    AccountId: int
    AccountMaintenanceFee: AccountMaintenanceFee
    def __init__(self, AccountId: _Optional[int] = ..., AccountMaintenanceFee: _Optional[_Union[AccountMaintenanceFee, _Mapping]] = ...) -> None: ...

class AccountMaintenanceFee(_message.Message):
    __slots__ = ("AccountMaintenanceFeeId", "AccountMaintenanceFeeSchedule", "FeeAmount", "FeePeriodInDays", "MinNumberOfTrades", "MinNumberOfTradesPeriodInDays", "MinLevelOfAccountAssets", "MinLevelOfAccountAssetsPeriodInDays", "Description", "CreatedTime", "LastModifiedTime", "LastModifiedUserId", "IsSoftDeleted")
    ACCOUNTMAINTENANCEFEEID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTMAINTENANCEFEESCHEDULE_FIELD_NUMBER: _ClassVar[int]
    FEEAMOUNT_FIELD_NUMBER: _ClassVar[int]
    FEEPERIODINDAYS_FIELD_NUMBER: _ClassVar[int]
    MINNUMBEROFTRADES_FIELD_NUMBER: _ClassVar[int]
    MINNUMBEROFTRADESPERIODINDAYS_FIELD_NUMBER: _ClassVar[int]
    MINLEVELOFACCOUNTASSETS_FIELD_NUMBER: _ClassVar[int]
    MINLEVELOFACCOUNTASSETSPERIODINDAYS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATEDTIME_FIELD_NUMBER: _ClassVar[int]
    LASTMODIFIEDTIME_FIELD_NUMBER: _ClassVar[int]
    LASTMODIFIEDUSERID_FIELD_NUMBER: _ClassVar[int]
    ISSOFTDELETED_FIELD_NUMBER: _ClassVar[int]
    AccountMaintenanceFeeId: int
    AccountMaintenanceFeeSchedule: _account_maintenance_fee_enums_pb2.EnumAccountMaintenanceFeeSchedule
    FeeAmount: float
    FeePeriodInDays: int
    MinNumberOfTrades: int
    MinNumberOfTradesPeriodInDays: int
    MinLevelOfAccountAssets: float
    MinLevelOfAccountAssetsPeriodInDays: int
    Description: str
    CreatedTime: _timestamp_pb2.Timestamp
    LastModifiedTime: _timestamp_pb2.Timestamp
    LastModifiedUserId: int
    IsSoftDeleted: bool
    def __init__(self, AccountMaintenanceFeeId: _Optional[int] = ..., AccountMaintenanceFeeSchedule: _Optional[_Union[_account_maintenance_fee_enums_pb2.EnumAccountMaintenanceFeeSchedule, str]] = ..., FeeAmount: _Optional[float] = ..., FeePeriodInDays: _Optional[int] = ..., MinNumberOfTrades: _Optional[int] = ..., MinNumberOfTradesPeriodInDays: _Optional[int] = ..., MinLevelOfAccountAssets: _Optional[float] = ..., MinLevelOfAccountAssetsPeriodInDays: _Optional[int] = ..., Description: _Optional[str] = ..., CreatedTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., LastModifiedTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., LastModifiedUserId: _Optional[int] = ..., IsSoftDeleted: bool = ...) -> None: ...
