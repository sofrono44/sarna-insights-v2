import orders_enums_pb2 as _orders_enums_pb2
import orders_pb2 as _orders_pb2
import bp_pb2 as _bp_pb2
import pmbp_pb2 as _pmbp_pb2
import common_pb2 as _common_pb2
import trading_enums_pb2 as _trading_enums_pb2
import quotes_pb2 as _quotes_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TradeRequest(_message.Message):
    __slots__ = ("TradeRequestType", "TradeRequestOrderInfos", "ReturnBPDetails")
    TRADEREQUESTTYPE_FIELD_NUMBER: _ClassVar[int]
    TRADEREQUESTORDERINFOS_FIELD_NUMBER: _ClassVar[int]
    RETURNBPDETAILS_FIELD_NUMBER: _ClassVar[int]
    TradeRequestType: _trading_enums_pb2.EnumTradeRequestType
    TradeRequestOrderInfos: _containers.RepeatedCompositeFieldContainer[TradeRequestOrderInfo]
    ReturnBPDetails: bool
    def __init__(self, TradeRequestType: _Optional[_Union[_trading_enums_pb2.EnumTradeRequestType, str]] = ..., TradeRequestOrderInfos: _Optional[_Iterable[_Union[TradeRequestOrderInfo, _Mapping]]] = ..., ReturnBPDetails: bool = ...) -> None: ...

class TradeRequestOrderInfo(_message.Message):
    __slots__ = ("Order",)
    ORDER_FIELD_NUMBER: _ClassVar[int]
    Order: _orders_pb2.Order
    def __init__(self, Order: _Optional[_Union[_orders_pb2.Order, _Mapping]] = ...) -> None: ...

class TradeResponse(_message.Message):
    __slots__ = ("HasData", "TradeResponseOrderInfos", "Warnings", "Errors")
    HASDATA_FIELD_NUMBER: _ClassVar[int]
    TRADERESPONSEORDERINFOS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    HasData: bool
    TradeResponseOrderInfos: _containers.RepeatedCompositeFieldContainer[TradeResponseOrderInfo]
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, HasData: bool = ..., TradeResponseOrderInfos: _Optional[_Iterable[_Union[TradeResponseOrderInfo, _Mapping]]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class TradeResponseOrderInfo(_message.Message):
    __slots__ = ("AccountId", "AccountNumber", "SubaccountId", "ChildAllocationOrderInfos", "SpreadPositionEffect", "OrderPrice", "PendingTransaction", "CommissionEstimated", "FeesEstimated", "ProposedOrderResponseBpEngine", "ExecutionInitiatorResponseInfo", "QuoteData", "ProposedOrderResponsePmBpEngine", "IsPMAccount", "Warnings", "Errors")
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTNUMBER_FIELD_NUMBER: _ClassVar[int]
    SUBACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    CHILDALLOCATIONORDERINFOS_FIELD_NUMBER: _ClassVar[int]
    SPREADPOSITIONEFFECT_FIELD_NUMBER: _ClassVar[int]
    ORDERPRICE_FIELD_NUMBER: _ClassVar[int]
    PENDINGTRANSACTION_FIELD_NUMBER: _ClassVar[int]
    COMMISSIONESTIMATED_FIELD_NUMBER: _ClassVar[int]
    FEESESTIMATED_FIELD_NUMBER: _ClassVar[int]
    PROPOSEDORDERRESPONSEBPENGINE_FIELD_NUMBER: _ClassVar[int]
    EXECUTIONINITIATORRESPONSEINFO_FIELD_NUMBER: _ClassVar[int]
    QUOTEDATA_FIELD_NUMBER: _ClassVar[int]
    PROPOSEDORDERRESPONSEPMBPENGINE_FIELD_NUMBER: _ClassVar[int]
    ISPMACCOUNT_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    AccountId: int
    AccountNumber: str
    SubaccountId: int
    ChildAllocationOrderInfos: _containers.RepeatedCompositeFieldContainer[TradeResponseOrderInfo]
    SpreadPositionEffect: _orders_enums_pb2.EnumSpreadPositionEffect
    OrderPrice: float
    PendingTransaction: float
    CommissionEstimated: float
    FeesEstimated: float
    ProposedOrderResponseBpEngine: _bp_pb2.RegTBpForProposedOrderResponseInfo
    ExecutionInitiatorResponseInfo: ExecutionInitiatorResponseInfo
    QuoteData: _quotes_pb2.QuoteData
    ProposedOrderResponsePmBpEngine: _pmbp_pb2.PmBpForProposedOrderResponse
    IsPMAccount: bool
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, AccountId: _Optional[int] = ..., AccountNumber: _Optional[str] = ..., SubaccountId: _Optional[int] = ..., ChildAllocationOrderInfos: _Optional[_Iterable[_Union[TradeResponseOrderInfo, _Mapping]]] = ..., SpreadPositionEffect: _Optional[_Union[_orders_enums_pb2.EnumSpreadPositionEffect, str]] = ..., OrderPrice: _Optional[float] = ..., PendingTransaction: _Optional[float] = ..., CommissionEstimated: _Optional[float] = ..., FeesEstimated: _Optional[float] = ..., ProposedOrderResponseBpEngine: _Optional[_Union[_bp_pb2.RegTBpForProposedOrderResponseInfo, _Mapping]] = ..., ExecutionInitiatorResponseInfo: _Optional[_Union[ExecutionInitiatorResponseInfo, _Mapping]] = ..., QuoteData: _Optional[_Union[_quotes_pb2.QuoteData, _Mapping]] = ..., ProposedOrderResponsePmBpEngine: _Optional[_Union[_pmbp_pb2.PmBpForProposedOrderResponse, _Mapping]] = ..., IsPMAccount: bool = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class ExecutionInitiatorResponseInfo(_message.Message):
    __slots__ = ("OrderId", "Warnings", "Errors")
    ORDERID_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    OrderId: int
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, OrderId: _Optional[int] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...
