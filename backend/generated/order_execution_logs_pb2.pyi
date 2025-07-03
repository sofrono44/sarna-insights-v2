import common_pb2 as _common_pb2
import orders_enums_pb2 as _orders_enums_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EnumOrderExecutionLogsRequestType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumOrderExecutionLogsRequestType_Undefined: _ClassVar[EnumOrderExecutionLogsRequestType]
    EnumOrderExecutionLogsRequestType_BrowseAllByOrderId: _ClassVar[EnumOrderExecutionLogsRequestType]
    EnumOrderExecutionLogsRequestType_FillEventsByAccountIdToday: _ClassVar[EnumOrderExecutionLogsRequestType]
    EnumOrderExecutionLogsRequestType_FillEventsByAccountIdHistorical: _ClassVar[EnumOrderExecutionLogsRequestType]
EnumOrderExecutionLogsRequestType_Undefined: EnumOrderExecutionLogsRequestType
EnumOrderExecutionLogsRequestType_BrowseAllByOrderId: EnumOrderExecutionLogsRequestType
EnumOrderExecutionLogsRequestType_FillEventsByAccountIdToday: EnumOrderExecutionLogsRequestType
EnumOrderExecutionLogsRequestType_FillEventsByAccountIdHistorical: EnumOrderExecutionLogsRequestType

class OrderExecutionLogsRequest(_message.Message):
    __slots__ = ("OrderExecutionLogsRequestTypes", "OrderExecutionLogsSearchCriteria")
    ORDEREXECUTIONLOGSREQUESTTYPES_FIELD_NUMBER: _ClassVar[int]
    ORDEREXECUTIONLOGSSEARCHCRITERIA_FIELD_NUMBER: _ClassVar[int]
    OrderExecutionLogsRequestTypes: _containers.RepeatedScalarFieldContainer[EnumOrderExecutionLogsRequestType]
    OrderExecutionLogsSearchCriteria: OrderExecutionLogsSearchCriteria
    def __init__(self, OrderExecutionLogsRequestTypes: _Optional[_Iterable[_Union[EnumOrderExecutionLogsRequestType, str]]] = ..., OrderExecutionLogsSearchCriteria: _Optional[_Union[OrderExecutionLogsSearchCriteria, _Mapping]] = ...) -> None: ...

class OrderExecutionLogsSearchCriteria(_message.Message):
    __slots__ = ("AccountIDs", "AccountNumbers", "OrderId")
    ACCOUNTIDS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTNUMBERS_FIELD_NUMBER: _ClassVar[int]
    ORDERID_FIELD_NUMBER: _ClassVar[int]
    AccountIDs: _containers.RepeatedScalarFieldContainer[int]
    AccountNumbers: _containers.RepeatedScalarFieldContainer[str]
    OrderId: int
    def __init__(self, AccountIDs: _Optional[_Iterable[int]] = ..., AccountNumbers: _Optional[_Iterable[str]] = ..., OrderId: _Optional[int] = ...) -> None: ...

class OrderExecutionLogsResponse(_message.Message):
    __slots__ = ("HasData", "OrderExecutionLogInfos", "ResetUiRepository", "Warnings", "Errors")
    HASDATA_FIELD_NUMBER: _ClassVar[int]
    ORDEREXECUTIONLOGINFOS_FIELD_NUMBER: _ClassVar[int]
    RESETUIREPOSITORY_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    HasData: bool
    OrderExecutionLogInfos: _containers.RepeatedCompositeFieldContainer[OrderExecutionLogInfo]
    ResetUiRepository: bool
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, HasData: bool = ..., OrderExecutionLogInfos: _Optional[_Iterable[_Union[OrderExecutionLogInfo, _Mapping]]] = ..., ResetUiRepository: bool = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class OrderExecutionLogInfo(_message.Message):
    __slots__ = ("OrderExecutionLog", "IsUtcToday")
    ORDEREXECUTIONLOG_FIELD_NUMBER: _ClassVar[int]
    ISUTCTODAY_FIELD_NUMBER: _ClassVar[int]
    OrderExecutionLog: OrderExecutionLog
    IsUtcToday: bool
    def __init__(self, OrderExecutionLog: _Optional[_Union[OrderExecutionLog, _Mapping]] = ..., IsUtcToday: bool = ...) -> None: ...

class OrderExecutionLog(_message.Message):
    __slots__ = ("OrderExecutionLogId", "OrderId", "LastModifiedTime", "TransactTime", "FilledValue", "CreatedTime", "OrigClOrderId", "CommissionCharged", "ExecId", "ClOrderId", "SecurityType", "LegNumber", "PositionEffect", "OrderAction", "OrderStatus", "FilledQuantity", "FilledPrice", "Symbol", "CommissionCreditAmount", "Quantity", "Description", "PriceType", "CreatedUserId", "AccountId", "SubaccountId", "OrderPriceType", "LimitPrice", "StopPrice")
    ORDEREXECUTIONLOGID_FIELD_NUMBER: _ClassVar[int]
    ORDERID_FIELD_NUMBER: _ClassVar[int]
    LASTMODIFIEDTIME_FIELD_NUMBER: _ClassVar[int]
    TRANSACTTIME_FIELD_NUMBER: _ClassVar[int]
    FILLEDVALUE_FIELD_NUMBER: _ClassVar[int]
    CREATEDTIME_FIELD_NUMBER: _ClassVar[int]
    ORIGCLORDERID_FIELD_NUMBER: _ClassVar[int]
    COMMISSIONCHARGED_FIELD_NUMBER: _ClassVar[int]
    EXECID_FIELD_NUMBER: _ClassVar[int]
    CLORDERID_FIELD_NUMBER: _ClassVar[int]
    SECURITYTYPE_FIELD_NUMBER: _ClassVar[int]
    LEGNUMBER_FIELD_NUMBER: _ClassVar[int]
    POSITIONEFFECT_FIELD_NUMBER: _ClassVar[int]
    ORDERACTION_FIELD_NUMBER: _ClassVar[int]
    ORDERSTATUS_FIELD_NUMBER: _ClassVar[int]
    FILLEDQUANTITY_FIELD_NUMBER: _ClassVar[int]
    FILLEDPRICE_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    COMMISSIONCREDITAMOUNT_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PRICETYPE_FIELD_NUMBER: _ClassVar[int]
    CREATEDUSERID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    SUBACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    ORDERPRICETYPE_FIELD_NUMBER: _ClassVar[int]
    LIMITPRICE_FIELD_NUMBER: _ClassVar[int]
    STOPPRICE_FIELD_NUMBER: _ClassVar[int]
    OrderExecutionLogId: int
    OrderId: int
    LastModifiedTime: _timestamp_pb2.Timestamp
    TransactTime: _timestamp_pb2.Timestamp
    FilledValue: float
    CreatedTime: _timestamp_pb2.Timestamp
    OrigClOrderId: str
    CommissionCharged: float
    ExecId: str
    ClOrderId: str
    SecurityType: _orders_enums_pb2.EnumSecurityType
    LegNumber: int
    PositionEffect: _orders_enums_pb2.EnumPositionEffect
    OrderAction: _orders_enums_pb2.EnumOrderAction
    OrderStatus: _orders_enums_pb2.EnumOrderStatus
    FilledQuantity: float
    FilledPrice: float
    Symbol: str
    CommissionCreditAmount: float
    Quantity: float
    Description: str
    PriceType: str
    CreatedUserId: int
    AccountId: int
    SubaccountId: int
    OrderPriceType: _orders_enums_pb2.EnumPriceType
    LimitPrice: float
    StopPrice: float
    def __init__(self, OrderExecutionLogId: _Optional[int] = ..., OrderId: _Optional[int] = ..., LastModifiedTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., TransactTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., FilledValue: _Optional[float] = ..., CreatedTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., OrigClOrderId: _Optional[str] = ..., CommissionCharged: _Optional[float] = ..., ExecId: _Optional[str] = ..., ClOrderId: _Optional[str] = ..., SecurityType: _Optional[_Union[_orders_enums_pb2.EnumSecurityType, str]] = ..., LegNumber: _Optional[int] = ..., PositionEffect: _Optional[_Union[_orders_enums_pb2.EnumPositionEffect, str]] = ..., OrderAction: _Optional[_Union[_orders_enums_pb2.EnumOrderAction, str]] = ..., OrderStatus: _Optional[_Union[_orders_enums_pb2.EnumOrderStatus, str]] = ..., FilledQuantity: _Optional[float] = ..., FilledPrice: _Optional[float] = ..., Symbol: _Optional[str] = ..., CommissionCreditAmount: _Optional[float] = ..., Quantity: _Optional[float] = ..., Description: _Optional[str] = ..., PriceType: _Optional[str] = ..., CreatedUserId: _Optional[int] = ..., AccountId: _Optional[int] = ..., SubaccountId: _Optional[int] = ..., OrderPriceType: _Optional[_Union[_orders_enums_pb2.EnumPriceType, str]] = ..., LimitPrice: _Optional[float] = ..., StopPrice: _Optional[float] = ...) -> None: ...
