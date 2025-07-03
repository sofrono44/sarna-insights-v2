import common_pb2 as _common_pb2
import orders_enums_pb2 as _orders_enums_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OrdersInfoRequest(_message.Message):
    __slots__ = ("OrdersInfoRequestTypes", "OrdersInfoRequestSearchCriteria")
    ORDERSINFOREQUESTTYPES_FIELD_NUMBER: _ClassVar[int]
    ORDERSINFOREQUESTSEARCHCRITERIA_FIELD_NUMBER: _ClassVar[int]
    OrdersInfoRequestTypes: _containers.RepeatedScalarFieldContainer[_orders_enums_pb2.EnumOrdersInfoRequestType]
    OrdersInfoRequestSearchCriteria: OrdersInfoRequestSearchCriteria
    def __init__(self, OrdersInfoRequestTypes: _Optional[_Iterable[_Union[_orders_enums_pb2.EnumOrdersInfoRequestType, str]]] = ..., OrdersInfoRequestSearchCriteria: _Optional[_Union[OrdersInfoRequestSearchCriteria, _Mapping]] = ...) -> None: ...

class OrdersInfoRequestSearchCriteria(_message.Message):
    __slots__ = ("AccountIDs", "AccountNumbers", "OrderIDs", "ExternalOrderIDs", "IncludeGTAllocations", "SkipFetchingCurrentPrices")
    ACCOUNTIDS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTNUMBERS_FIELD_NUMBER: _ClassVar[int]
    ORDERIDS_FIELD_NUMBER: _ClassVar[int]
    EXTERNALORDERIDS_FIELD_NUMBER: _ClassVar[int]
    INCLUDEGTALLOCATIONS_FIELD_NUMBER: _ClassVar[int]
    SKIPFETCHINGCURRENTPRICES_FIELD_NUMBER: _ClassVar[int]
    AccountIDs: _containers.RepeatedScalarFieldContainer[int]
    AccountNumbers: _containers.RepeatedScalarFieldContainer[str]
    OrderIDs: _containers.RepeatedScalarFieldContainer[int]
    ExternalOrderIDs: _containers.RepeatedScalarFieldContainer[str]
    IncludeGTAllocations: bool
    SkipFetchingCurrentPrices: bool
    def __init__(self, AccountIDs: _Optional[_Iterable[int]] = ..., AccountNumbers: _Optional[_Iterable[str]] = ..., OrderIDs: _Optional[_Iterable[int]] = ..., ExternalOrderIDs: _Optional[_Iterable[str]] = ..., IncludeGTAllocations: bool = ..., SkipFetchingCurrentPrices: bool = ...) -> None: ...

class OrdersInfoResponse(_message.Message):
    __slots__ = ("HasData", "ResetUiRepository", "CurrentOrdersInfo", "HistoricalOrdersInfo", "Warnings", "Errors")
    HASDATA_FIELD_NUMBER: _ClassVar[int]
    RESETUIREPOSITORY_FIELD_NUMBER: _ClassVar[int]
    CURRENTORDERSINFO_FIELD_NUMBER: _ClassVar[int]
    HISTORICALORDERSINFO_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    HasData: bool
    ResetUiRepository: bool
    CurrentOrdersInfo: CurrentOrdersInfo
    HistoricalOrdersInfo: HistoricalOrdersInfo
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, HasData: bool = ..., ResetUiRepository: bool = ..., CurrentOrdersInfo: _Optional[_Union[CurrentOrdersInfo, _Mapping]] = ..., HistoricalOrdersInfo: _Optional[_Union[HistoricalOrdersInfo, _Mapping]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class CurrentOrdersInfo(_message.Message):
    __slots__ = ("OrderInfos", "CurrentOrderValueByOrderId")
    class CurrentOrderValueByOrderIdEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: float
        def __init__(self, key: _Optional[int] = ..., value: _Optional[float] = ...) -> None: ...
    ORDERINFOS_FIELD_NUMBER: _ClassVar[int]
    CURRENTORDERVALUEBYORDERID_FIELD_NUMBER: _ClassVar[int]
    OrderInfos: _containers.RepeatedCompositeFieldContainer[OrderInfo]
    CurrentOrderValueByOrderId: _containers.ScalarMap[int, float]
    def __init__(self, OrderInfos: _Optional[_Iterable[_Union[OrderInfo, _Mapping]]] = ..., CurrentOrderValueByOrderId: _Optional[_Mapping[int, float]] = ...) -> None: ...

class HistoricalOrdersInfo(_message.Message):
    __slots__ = ("OrderInfos",)
    ORDERINFOS_FIELD_NUMBER: _ClassVar[int]
    OrderInfos: _containers.RepeatedCompositeFieldContainer[OrderInfo]
    def __init__(self, OrderInfos: _Optional[_Iterable[_Union[OrderInfo, _Mapping]]] = ...) -> None: ...

class OrderInfo(_message.Message):
    __slots__ = ("Order", "CurrentPricePerShare", "Timestamp", "GroupingKey", "AllowedActions", "SpreadPositionEffect", "SpreadOrderAction", "IsAnyLegExpired")
    ORDER_FIELD_NUMBER: _ClassVar[int]
    CURRENTPRICEPERSHARE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    GROUPINGKEY_FIELD_NUMBER: _ClassVar[int]
    ALLOWEDACTIONS_FIELD_NUMBER: _ClassVar[int]
    SPREADPOSITIONEFFECT_FIELD_NUMBER: _ClassVar[int]
    SPREADORDERACTION_FIELD_NUMBER: _ClassVar[int]
    ISANYLEGEXPIRED_FIELD_NUMBER: _ClassVar[int]
    Order: Order
    CurrentPricePerShare: float
    Timestamp: int
    GroupingKey: str
    AllowedActions: _containers.RepeatedScalarFieldContainer[bool]
    SpreadPositionEffect: _orders_enums_pb2.EnumSpreadPositionEffect
    SpreadOrderAction: _orders_enums_pb2.EnumOrderAction
    IsAnyLegExpired: bool
    def __init__(self, Order: _Optional[_Union[Order, _Mapping]] = ..., CurrentPricePerShare: _Optional[float] = ..., Timestamp: _Optional[int] = ..., GroupingKey: _Optional[str] = ..., AllowedActions: _Optional[_Iterable[bool]] = ..., SpreadPositionEffect: _Optional[_Union[_orders_enums_pb2.EnumSpreadPositionEffect, str]] = ..., SpreadOrderAction: _Optional[_Union[_orders_enums_pb2.EnumOrderAction, str]] = ..., IsAnyLegExpired: bool = ...) -> None: ...

class Order(_message.Message):
    __slots__ = ("Header", "Legs", "RequestLifecycleAttributes")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    LEGS_FIELD_NUMBER: _ClassVar[int]
    REQUESTLIFECYCLEATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    Header: OrderHeader
    Legs: _containers.RepeatedCompositeFieldContainer[OrderLeg]
    RequestLifecycleAttributes: RequestLifecycleAttributes
    def __init__(self, Header: _Optional[_Union[OrderHeader, _Mapping]] = ..., Legs: _Optional[_Iterable[_Union[OrderLeg, _Mapping]]] = ..., RequestLifecycleAttributes: _Optional[_Union[RequestLifecycleAttributes, _Mapping]] = ...) -> None: ...

class OrderHeader(_message.Message):
    __slots__ = ("OrderId", "UnderlyingSymbol", "AccountNumber", "AccountId", "Quantity", "PriceType", "LimitPrice", "StopPrice", "StrategyType", "AllOrNone", "Duration", "ClOrderId", "OrigClOrderId", "ExternalOrderId", "OrderStatus", "ExecutionRoute", "IsOffMarketHourOrder", "OrderAllocationType", "FilledQuantity", "FilledPrice", "SubaccountId", "CreatedTime", "CreatedUserId", "LastModifiedTime", "LastModifiedUserId", "Description", "CommissionEstimated", "CommissionCharged", "PendingTransaction", "ReplacedQuantity", "ReplacedPriceType", "ReplacedLimitPrice", "ReplacedStopPrice", "ReplacedClOrderId", "IsManualTrade", "ExecutedAs", "PlacedAs", "IsLive", "ParentOrderId", "IsConstructedFromExecReport")
    ORDERID_FIELD_NUMBER: _ClassVar[int]
    UNDERLYINGSYMBOL_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTNUMBER_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    PRICETYPE_FIELD_NUMBER: _ClassVar[int]
    LIMITPRICE_FIELD_NUMBER: _ClassVar[int]
    STOPPRICE_FIELD_NUMBER: _ClassVar[int]
    STRATEGYTYPE_FIELD_NUMBER: _ClassVar[int]
    ALLORNONE_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    CLORDERID_FIELD_NUMBER: _ClassVar[int]
    ORIGCLORDERID_FIELD_NUMBER: _ClassVar[int]
    EXTERNALORDERID_FIELD_NUMBER: _ClassVar[int]
    ORDERSTATUS_FIELD_NUMBER: _ClassVar[int]
    EXECUTIONROUTE_FIELD_NUMBER: _ClassVar[int]
    ISOFFMARKETHOURORDER_FIELD_NUMBER: _ClassVar[int]
    ORDERALLOCATIONTYPE_FIELD_NUMBER: _ClassVar[int]
    FILLEDQUANTITY_FIELD_NUMBER: _ClassVar[int]
    FILLEDPRICE_FIELD_NUMBER: _ClassVar[int]
    SUBACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    CREATEDTIME_FIELD_NUMBER: _ClassVar[int]
    CREATEDUSERID_FIELD_NUMBER: _ClassVar[int]
    LASTMODIFIEDTIME_FIELD_NUMBER: _ClassVar[int]
    LASTMODIFIEDUSERID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    COMMISSIONESTIMATED_FIELD_NUMBER: _ClassVar[int]
    COMMISSIONCHARGED_FIELD_NUMBER: _ClassVar[int]
    PENDINGTRANSACTION_FIELD_NUMBER: _ClassVar[int]
    REPLACEDQUANTITY_FIELD_NUMBER: _ClassVar[int]
    REPLACEDPRICETYPE_FIELD_NUMBER: _ClassVar[int]
    REPLACEDLIMITPRICE_FIELD_NUMBER: _ClassVar[int]
    REPLACEDSTOPPRICE_FIELD_NUMBER: _ClassVar[int]
    REPLACEDCLORDERID_FIELD_NUMBER: _ClassVar[int]
    ISMANUALTRADE_FIELD_NUMBER: _ClassVar[int]
    EXECUTEDAS_FIELD_NUMBER: _ClassVar[int]
    PLACEDAS_FIELD_NUMBER: _ClassVar[int]
    ISLIVE_FIELD_NUMBER: _ClassVar[int]
    PARENTORDERID_FIELD_NUMBER: _ClassVar[int]
    ISCONSTRUCTEDFROMEXECREPORT_FIELD_NUMBER: _ClassVar[int]
    OrderId: int
    UnderlyingSymbol: str
    AccountNumber: str
    AccountId: int
    Quantity: float
    PriceType: _orders_enums_pb2.EnumPriceType
    LimitPrice: float
    StopPrice: float
    StrategyType: _orders_enums_pb2.EnumStrategyType
    AllOrNone: bool
    Duration: _orders_enums_pb2.EnumOrderDuration
    ClOrderId: str
    OrigClOrderId: str
    ExternalOrderId: str
    OrderStatus: _orders_enums_pb2.EnumOrderStatus
    ExecutionRoute: _orders_enums_pb2.EnumExecutionRoute
    IsOffMarketHourOrder: bool
    OrderAllocationType: _orders_enums_pb2.EnumOrderAllocationType
    FilledQuantity: float
    FilledPrice: float
    SubaccountId: int
    CreatedTime: _timestamp_pb2.Timestamp
    CreatedUserId: int
    LastModifiedTime: _timestamp_pb2.Timestamp
    LastModifiedUserId: int
    Description: str
    CommissionEstimated: float
    CommissionCharged: float
    PendingTransaction: float
    ReplacedQuantity: float
    ReplacedPriceType: _orders_enums_pb2.EnumPriceType
    ReplacedLimitPrice: float
    ReplacedStopPrice: float
    ReplacedClOrderId: str
    IsManualTrade: bool
    ExecutedAs: _orders_enums_pb2.EnumExecutedAs
    PlacedAs: _orders_enums_pb2.EnumPlacedAs
    IsLive: bool
    ParentOrderId: int
    IsConstructedFromExecReport: bool
    def __init__(self, OrderId: _Optional[int] = ..., UnderlyingSymbol: _Optional[str] = ..., AccountNumber: _Optional[str] = ..., AccountId: _Optional[int] = ..., Quantity: _Optional[float] = ..., PriceType: _Optional[_Union[_orders_enums_pb2.EnumPriceType, str]] = ..., LimitPrice: _Optional[float] = ..., StopPrice: _Optional[float] = ..., StrategyType: _Optional[_Union[_orders_enums_pb2.EnumStrategyType, str]] = ..., AllOrNone: bool = ..., Duration: _Optional[_Union[_orders_enums_pb2.EnumOrderDuration, str]] = ..., ClOrderId: _Optional[str] = ..., OrigClOrderId: _Optional[str] = ..., ExternalOrderId: _Optional[str] = ..., OrderStatus: _Optional[_Union[_orders_enums_pb2.EnumOrderStatus, str]] = ..., ExecutionRoute: _Optional[_Union[_orders_enums_pb2.EnumExecutionRoute, str]] = ..., IsOffMarketHourOrder: bool = ..., OrderAllocationType: _Optional[_Union[_orders_enums_pb2.EnumOrderAllocationType, str]] = ..., FilledQuantity: _Optional[float] = ..., FilledPrice: _Optional[float] = ..., SubaccountId: _Optional[int] = ..., CreatedTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., CreatedUserId: _Optional[int] = ..., LastModifiedTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., LastModifiedUserId: _Optional[int] = ..., Description: _Optional[str] = ..., CommissionEstimated: _Optional[float] = ..., CommissionCharged: _Optional[float] = ..., PendingTransaction: _Optional[float] = ..., ReplacedQuantity: _Optional[float] = ..., ReplacedPriceType: _Optional[_Union[_orders_enums_pb2.EnumPriceType, str]] = ..., ReplacedLimitPrice: _Optional[float] = ..., ReplacedStopPrice: _Optional[float] = ..., ReplacedClOrderId: _Optional[str] = ..., IsManualTrade: bool = ..., ExecutedAs: _Optional[_Union[_orders_enums_pb2.EnumExecutedAs, str]] = ..., PlacedAs: _Optional[_Union[_orders_enums_pb2.EnumPlacedAs, str]] = ..., IsLive: bool = ..., ParentOrderId: _Optional[int] = ..., IsConstructedFromExecReport: bool = ...) -> None: ...

class RequestLifecycleAttributes(_message.Message):
    __slots__ = ("OrderInitiationType", "OverrideValidationWarnings", "GTOrderAllocations", "OrderAllocationHeader", "BypassInputValidation", "BypassBPCheck", "ExternalAccountNumber")
    ORDERINITIATIONTYPE_FIELD_NUMBER: _ClassVar[int]
    OVERRIDEVALIDATIONWARNINGS_FIELD_NUMBER: _ClassVar[int]
    GTORDERALLOCATIONS_FIELD_NUMBER: _ClassVar[int]
    ORDERALLOCATIONHEADER_FIELD_NUMBER: _ClassVar[int]
    BYPASSINPUTVALIDATION_FIELD_NUMBER: _ClassVar[int]
    BYPASSBPCHECK_FIELD_NUMBER: _ClassVar[int]
    EXTERNALACCOUNTNUMBER_FIELD_NUMBER: _ClassVar[int]
    OrderInitiationType: _orders_enums_pb2.EnumOrderInitiationType
    OverrideValidationWarnings: bool
    GTOrderAllocations: _containers.RepeatedCompositeFieldContainer[GTOrderAllocation]
    OrderAllocationHeader: OrderAllocationHeader
    BypassInputValidation: bool
    BypassBPCheck: bool
    ExternalAccountNumber: str
    def __init__(self, OrderInitiationType: _Optional[_Union[_orders_enums_pb2.EnumOrderInitiationType, str]] = ..., OverrideValidationWarnings: bool = ..., GTOrderAllocations: _Optional[_Iterable[_Union[GTOrderAllocation, _Mapping]]] = ..., OrderAllocationHeader: _Optional[_Union[OrderAllocationHeader, _Mapping]] = ..., BypassInputValidation: bool = ..., BypassBPCheck: bool = ..., ExternalAccountNumber: _Optional[str] = ...) -> None: ...

class GTOrderAllocation(_message.Message):
    __slots__ = ("AccountId", "SubaccountId", "OrderId", "ClOrderId", "Quantity", "PendingTransaction", "CommissionId", "ExternalOrderId", "AccountNumber")
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    SUBACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    ORDERID_FIELD_NUMBER: _ClassVar[int]
    CLORDERID_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    PENDINGTRANSACTION_FIELD_NUMBER: _ClassVar[int]
    COMMISSIONID_FIELD_NUMBER: _ClassVar[int]
    EXTERNALORDERID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTNUMBER_FIELD_NUMBER: _ClassVar[int]
    AccountId: int
    SubaccountId: int
    OrderId: int
    ClOrderId: str
    Quantity: float
    PendingTransaction: float
    CommissionId: int
    ExternalOrderId: str
    AccountNumber: str
    def __init__(self, AccountId: _Optional[int] = ..., SubaccountId: _Optional[int] = ..., OrderId: _Optional[int] = ..., ClOrderId: _Optional[str] = ..., Quantity: _Optional[float] = ..., PendingTransaction: _Optional[float] = ..., CommissionId: _Optional[int] = ..., ExternalOrderId: _Optional[str] = ..., AccountNumber: _Optional[str] = ...) -> None: ...

class OrderLeg(_message.Message):
    __slots__ = ("LegNumber", "Quantity", "FilledQuantity", "Symbol", "SymbolDescription", "OrderId", "OrderAction", "PositionEffect", "LegSecType", "FilledPrice", "Multiplier", "ContractSize", "StockOrderLeg", "OptionOrderLeg", "MutualFundOrderLeg", "FixedIncomeOrderLeg", "LegUniqueKey")
    LEGNUMBER_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    FILLEDQUANTITY_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    SYMBOLDESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ORDERID_FIELD_NUMBER: _ClassVar[int]
    ORDERACTION_FIELD_NUMBER: _ClassVar[int]
    POSITIONEFFECT_FIELD_NUMBER: _ClassVar[int]
    LEGSECTYPE_FIELD_NUMBER: _ClassVar[int]
    FILLEDPRICE_FIELD_NUMBER: _ClassVar[int]
    MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
    CONTRACTSIZE_FIELD_NUMBER: _ClassVar[int]
    STOCKORDERLEG_FIELD_NUMBER: _ClassVar[int]
    OPTIONORDERLEG_FIELD_NUMBER: _ClassVar[int]
    MUTUALFUNDORDERLEG_FIELD_NUMBER: _ClassVar[int]
    FIXEDINCOMEORDERLEG_FIELD_NUMBER: _ClassVar[int]
    LEGUNIQUEKEY_FIELD_NUMBER: _ClassVar[int]
    LegNumber: int
    Quantity: float
    FilledQuantity: float
    Symbol: str
    SymbolDescription: str
    OrderId: int
    OrderAction: _orders_enums_pb2.EnumOrderAction
    PositionEffect: _orders_enums_pb2.EnumPositionEffect
    LegSecType: _orders_enums_pb2.EnumLegSecType
    FilledPrice: float
    Multiplier: float
    ContractSize: float
    StockOrderLeg: StockOrderLeg
    OptionOrderLeg: OptionOrderLeg
    MutualFundOrderLeg: MutualFundOrderLeg
    FixedIncomeOrderLeg: FixedIncomeOrderLeg
    LegUniqueKey: str
    def __init__(self, LegNumber: _Optional[int] = ..., Quantity: _Optional[float] = ..., FilledQuantity: _Optional[float] = ..., Symbol: _Optional[str] = ..., SymbolDescription: _Optional[str] = ..., OrderId: _Optional[int] = ..., OrderAction: _Optional[_Union[_orders_enums_pb2.EnumOrderAction, str]] = ..., PositionEffect: _Optional[_Union[_orders_enums_pb2.EnumPositionEffect, str]] = ..., LegSecType: _Optional[_Union[_orders_enums_pb2.EnumLegSecType, str]] = ..., FilledPrice: _Optional[float] = ..., Multiplier: _Optional[float] = ..., ContractSize: _Optional[float] = ..., StockOrderLeg: _Optional[_Union[StockOrderLeg, _Mapping]] = ..., OptionOrderLeg: _Optional[_Union[OptionOrderLeg, _Mapping]] = ..., MutualFundOrderLeg: _Optional[_Union[MutualFundOrderLeg, _Mapping]] = ..., FixedIncomeOrderLeg: _Optional[_Union[FixedIncomeOrderLeg, _Mapping]] = ..., LegUniqueKey: _Optional[str] = ...) -> None: ...

class OptionOrderLeg(_message.Message):
    __slots__ = ("CallOrPut", "Expiration", "StrikePrice", "OrdersOptionLegId")
    CALLORPUT_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    STRIKEPRICE_FIELD_NUMBER: _ClassVar[int]
    ORDERSOPTIONLEGID_FIELD_NUMBER: _ClassVar[int]
    CallOrPut: _orders_enums_pb2.EnumCallOrPut
    Expiration: _timestamp_pb2.Timestamp
    StrikePrice: float
    OrdersOptionLegId: int
    def __init__(self, CallOrPut: _Optional[_Union[_orders_enums_pb2.EnumCallOrPut, str]] = ..., Expiration: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., StrikePrice: _Optional[float] = ..., OrdersOptionLegId: _Optional[int] = ...) -> None: ...

class StockOrderLeg(_message.Message):
    __slots__ = ("OrdersStockLegId", "Cusip")
    ORDERSSTOCKLEGID_FIELD_NUMBER: _ClassVar[int]
    CUSIP_FIELD_NUMBER: _ClassVar[int]
    OrdersStockLegId: int
    Cusip: str
    def __init__(self, OrdersStockLegId: _Optional[int] = ..., Cusip: _Optional[str] = ...) -> None: ...

class FixedIncomeOrderLeg(_message.Message):
    __slots__ = ("OrdersFixedIncomeLegId", "Cusip")
    ORDERSFIXEDINCOMELEGID_FIELD_NUMBER: _ClassVar[int]
    CUSIP_FIELD_NUMBER: _ClassVar[int]
    OrdersFixedIncomeLegId: int
    Cusip: str
    def __init__(self, OrdersFixedIncomeLegId: _Optional[int] = ..., Cusip: _Optional[str] = ...) -> None: ...

class MutualFundOrderLeg(_message.Message):
    __slots__ = ("OrdersMutualFundLegId", "Cusip")
    ORDERSMUTUALFUNDLEGID_FIELD_NUMBER: _ClassVar[int]
    CUSIP_FIELD_NUMBER: _ClassVar[int]
    OrdersMutualFundLegId: int
    Cusip: str
    def __init__(self, OrdersMutualFundLegId: _Optional[int] = ..., Cusip: _Optional[str] = ...) -> None: ...

class OrderAllocationHeader(_message.Message):
    __slots__ = ("OrderAllocationHeaderId", "InventoryOrderId", "GTGroupId", "BypassInventoryBPCheck")
    ORDERALLOCATIONHEADERID_FIELD_NUMBER: _ClassVar[int]
    INVENTORYORDERID_FIELD_NUMBER: _ClassVar[int]
    GTGROUPID_FIELD_NUMBER: _ClassVar[int]
    BYPASSINVENTORYBPCHECK_FIELD_NUMBER: _ClassVar[int]
    OrderAllocationHeaderId: int
    InventoryOrderId: int
    GTGroupId: int
    BypassInventoryBPCheck: bool
    def __init__(self, OrderAllocationHeaderId: _Optional[int] = ..., InventoryOrderId: _Optional[int] = ..., GTGroupId: _Optional[int] = ..., BypassInventoryBPCheck: bool = ...) -> None: ...
