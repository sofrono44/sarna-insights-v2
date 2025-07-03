import common_pb2 as _common_pb2
import orders_pb2 as _orders_pb2
import orders_enums_pb2 as _orders_enums_pb2
import execution_acceptor_enums_pb2 as _execution_acceptor_enums_pb2
import execution_api_hub_enums_pb2 as _execution_api_hub_enums_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExecutionAcceptorRequest(_message.Message):
    __slots__ = ("ExecutionAcceptorRequestType", "ExecutionUpdateInfo")
    EXECUTIONACCEPTORREQUESTTYPE_FIELD_NUMBER: _ClassVar[int]
    EXECUTIONUPDATEINFO_FIELD_NUMBER: _ClassVar[int]
    ExecutionAcceptorRequestType: _execution_api_hub_enums_pb2.ExecutionAcceptorRequestType
    ExecutionUpdateInfo: ExecutionUpdateInfo
    def __init__(self, ExecutionAcceptorRequestType: _Optional[_Union[_execution_api_hub_enums_pb2.ExecutionAcceptorRequestType, str]] = ..., ExecutionUpdateInfo: _Optional[_Union[ExecutionUpdateInfo, _Mapping]] = ...) -> None: ...

class ExecutionUpdateInfo(_message.Message):
    __slots__ = ("ClOrderId", "OrigClOrderId", "ExternalOrderId", "LegNumber", "OrderStatus", "OrderQuantity", "CumFillQuantity", "LastFillQuantity", "TransactionTime", "PriceType", "LimitPrice", "StopPrice", "MessageFromExchange", "FillPrice", "ExecutionUpdateType", "ExecId", "OrderAction", "PositionEffect", "SecurityType", "Symbol", "TransactionValue", "Commission", "ExecRefID", "ExecTransType", "AccountNumber", "IsSpread", "IsTradeAwayExecution", "OrderDuration", "Cusip")
    CLORDERID_FIELD_NUMBER: _ClassVar[int]
    ORIGCLORDERID_FIELD_NUMBER: _ClassVar[int]
    EXTERNALORDERID_FIELD_NUMBER: _ClassVar[int]
    LEGNUMBER_FIELD_NUMBER: _ClassVar[int]
    ORDERSTATUS_FIELD_NUMBER: _ClassVar[int]
    ORDERQUANTITY_FIELD_NUMBER: _ClassVar[int]
    CUMFILLQUANTITY_FIELD_NUMBER: _ClassVar[int]
    LASTFILLQUANTITY_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONTIME_FIELD_NUMBER: _ClassVar[int]
    PRICETYPE_FIELD_NUMBER: _ClassVar[int]
    LIMITPRICE_FIELD_NUMBER: _ClassVar[int]
    STOPPRICE_FIELD_NUMBER: _ClassVar[int]
    MESSAGEFROMEXCHANGE_FIELD_NUMBER: _ClassVar[int]
    FILLPRICE_FIELD_NUMBER: _ClassVar[int]
    EXECUTIONUPDATETYPE_FIELD_NUMBER: _ClassVar[int]
    EXECID_FIELD_NUMBER: _ClassVar[int]
    ORDERACTION_FIELD_NUMBER: _ClassVar[int]
    POSITIONEFFECT_FIELD_NUMBER: _ClassVar[int]
    SECURITYTYPE_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONVALUE_FIELD_NUMBER: _ClassVar[int]
    COMMISSION_FIELD_NUMBER: _ClassVar[int]
    EXECREFID_FIELD_NUMBER: _ClassVar[int]
    EXECTRANSTYPE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTNUMBER_FIELD_NUMBER: _ClassVar[int]
    ISSPREAD_FIELD_NUMBER: _ClassVar[int]
    ISTRADEAWAYEXECUTION_FIELD_NUMBER: _ClassVar[int]
    ORDERDURATION_FIELD_NUMBER: _ClassVar[int]
    CUSIP_FIELD_NUMBER: _ClassVar[int]
    ClOrderId: str
    OrigClOrderId: str
    ExternalOrderId: str
    LegNumber: int
    OrderStatus: _orders_enums_pb2.EnumOrderStatus
    OrderQuantity: float
    CumFillQuantity: float
    LastFillQuantity: float
    TransactionTime: _timestamp_pb2.Timestamp
    PriceType: _orders_enums_pb2.EnumPriceType
    LimitPrice: float
    StopPrice: float
    MessageFromExchange: str
    FillPrice: float
    ExecutionUpdateType: _execution_acceptor_enums_pb2.EnumExecutionUpdateType
    ExecId: str
    OrderAction: _orders_enums_pb2.EnumOrderAction
    PositionEffect: _orders_enums_pb2.EnumPositionEffect
    SecurityType: _orders_enums_pb2.EnumSecurityType
    Symbol: str
    TransactionValue: float
    Commission: float
    ExecRefID: str
    ExecTransType: _execution_api_hub_enums_pb2.EnumExecTransType
    AccountNumber: str
    IsSpread: bool
    IsTradeAwayExecution: bool
    OrderDuration: _orders_enums_pb2.EnumOrderDuration
    Cusip: str
    def __init__(self, ClOrderId: _Optional[str] = ..., OrigClOrderId: _Optional[str] = ..., ExternalOrderId: _Optional[str] = ..., LegNumber: _Optional[int] = ..., OrderStatus: _Optional[_Union[_orders_enums_pb2.EnumOrderStatus, str]] = ..., OrderQuantity: _Optional[float] = ..., CumFillQuantity: _Optional[float] = ..., LastFillQuantity: _Optional[float] = ..., TransactionTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., PriceType: _Optional[_Union[_orders_enums_pb2.EnumPriceType, str]] = ..., LimitPrice: _Optional[float] = ..., StopPrice: _Optional[float] = ..., MessageFromExchange: _Optional[str] = ..., FillPrice: _Optional[float] = ..., ExecutionUpdateType: _Optional[_Union[_execution_acceptor_enums_pb2.EnumExecutionUpdateType, str]] = ..., ExecId: _Optional[str] = ..., OrderAction: _Optional[_Union[_orders_enums_pb2.EnumOrderAction, str]] = ..., PositionEffect: _Optional[_Union[_orders_enums_pb2.EnumPositionEffect, str]] = ..., SecurityType: _Optional[_Union[_orders_enums_pb2.EnumSecurityType, str]] = ..., Symbol: _Optional[str] = ..., TransactionValue: _Optional[float] = ..., Commission: _Optional[float] = ..., ExecRefID: _Optional[str] = ..., ExecTransType: _Optional[_Union[_execution_api_hub_enums_pb2.EnumExecTransType, str]] = ..., AccountNumber: _Optional[str] = ..., IsSpread: bool = ..., IsTradeAwayExecution: bool = ..., OrderDuration: _Optional[_Union[_orders_enums_pb2.EnumOrderDuration, str]] = ..., Cusip: _Optional[str] = ...) -> None: ...

class ExecutionAcceptorResponse(_message.Message):
    __slots__ = ("ACK", "ExecutionAcceptorResponseInfo", "Warnings", "Errors")
    ACK_FIELD_NUMBER: _ClassVar[int]
    EXECUTIONACCEPTORRESPONSEINFO_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    ACK: bool
    ExecutionAcceptorResponseInfo: ExecutionAcceptorResponseInfo
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, ACK: bool = ..., ExecutionAcceptorResponseInfo: _Optional[_Union[ExecutionAcceptorResponseInfo, _Mapping]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class ExecutionAcceptorResponseInfo(_message.Message):
    __slots__ = ("OrderId",)
    ORDERID_FIELD_NUMBER: _ClassVar[int]
    OrderId: int
    def __init__(self, OrderId: _Optional[int] = ...) -> None: ...

class ExecutionInitiatorRequest(_message.Message):
    __slots__ = ("ExecutionInitiatorRequestType", "Order")
    EXECUTIONINITIATORREQUESTTYPE_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    ExecutionInitiatorRequestType: _execution_api_hub_enums_pb2.ExecutionInitiatorRequestType
    Order: _orders_pb2.Order
    def __init__(self, ExecutionInitiatorRequestType: _Optional[_Union[_execution_api_hub_enums_pb2.ExecutionInitiatorRequestType, str]] = ..., Order: _Optional[_Union[_orders_pb2.Order, _Mapping]] = ...) -> None: ...

class ExecutionInitiatorResponse(_message.Message):
    __slots__ = ("ACK", "ExecutionInitiatorOrderInitiationResponse", "Warnings", "Errors")
    ACK_FIELD_NUMBER: _ClassVar[int]
    EXECUTIONINITIATORORDERINITIATIONRESPONSE_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    ACK: bool
    ExecutionInitiatorOrderInitiationResponse: ExecutionInitiatorOrderInitiationResponse
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, ACK: bool = ..., ExecutionInitiatorOrderInitiationResponse: _Optional[_Union[ExecutionInitiatorOrderInitiationResponse, _Mapping]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class ExecutionInitiatorOrderInitiationResponse(_message.Message):
    __slots__ = ("OrderId",)
    ORDERID_FIELD_NUMBER: _ClassVar[int]
    OrderId: int
    def __init__(self, OrderId: _Optional[int] = ...) -> None: ...

class ExecutionFixDropRequest(_message.Message):
    __slots__ = ("FixDropMessages",)
    FIXDROPMESSAGES_FIELD_NUMBER: _ClassVar[int]
    FixDropMessages: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, FixDropMessages: _Optional[_Iterable[str]] = ...) -> None: ...

class ExecutionFixDropResponse(_message.Message):
    __slots__ = ("ExecutionAcceptorResponses",)
    EXECUTIONACCEPTORRESPONSES_FIELD_NUMBER: _ClassVar[int]
    ExecutionAcceptorResponses: _containers.RepeatedCompositeFieldContainer[ExecutionAcceptorResponse]
    def __init__(self, ExecutionAcceptorResponses: _Optional[_Iterable[_Union[ExecutionAcceptorResponse, _Mapping]]] = ...) -> None: ...
