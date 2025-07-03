from google.protobuf import timestamp_pb2 as _timestamp_pb2
import orders_enums_pb2 as _orders_enums_pb2
import common_pb2 as _common_pb2
import quotes_enums_pb2 as _quotes_enums_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QuoteRequest(_message.Message):
    __slots__ = ("GetQuoteRequestInfos", "GetNetQuoteRequestInfos")
    GETQUOTEREQUESTINFOS_FIELD_NUMBER: _ClassVar[int]
    GETNETQUOTEREQUESTINFOS_FIELD_NUMBER: _ClassVar[int]
    GetQuoteRequestInfos: _containers.RepeatedCompositeFieldContainer[GetQuoteRequestInfo]
    GetNetQuoteRequestInfos: _containers.RepeatedCompositeFieldContainer[GetNetQuoteRequestInfo]
    def __init__(self, GetQuoteRequestInfos: _Optional[_Iterable[_Union[GetQuoteRequestInfo, _Mapping]]] = ..., GetNetQuoteRequestInfos: _Optional[_Iterable[_Union[GetNetQuoteRequestInfo, _Mapping]]] = ...) -> None: ...

class ChainQuoteRequest(_message.Message):
    __slots__ = ("GetChainQuotesRequestInfo",)
    GETCHAINQUOTESREQUESTINFO_FIELD_NUMBER: _ClassVar[int]
    GetChainQuotesRequestInfo: GetChainQuotesRequestInfo
    def __init__(self, GetChainQuotesRequestInfo: _Optional[_Union[GetChainQuotesRequestInfo, _Mapping]] = ...) -> None: ...

class GetExpirationsRequest(_message.Message):
    __slots__ = ("UnderlyingSymbol",)
    UNDERLYINGSYMBOL_FIELD_NUMBER: _ClassVar[int]
    UnderlyingSymbol: str
    def __init__(self, UnderlyingSymbol: _Optional[str] = ...) -> None: ...

class ChainQuoteResponse(_message.Message):
    __slots__ = ("GetChainQuotesResponseInfo", "Warnings", "Errors")
    GETCHAINQUOTESRESPONSEINFO_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    GetChainQuotesResponseInfo: GetChainQuotesResponseInfo
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, GetChainQuotesResponseInfo: _Optional[_Union[GetChainQuotesResponseInfo, _Mapping]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class GetExpirationsResponse(_message.Message):
    __slots__ = ("ExpirationInfos", "Warnings", "Errors")
    EXPIRATIONINFOS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    ExpirationInfos: _containers.RepeatedCompositeFieldContainer[ExpirationInfo]
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, ExpirationInfos: _Optional[_Iterable[_Union[ExpirationInfo, _Mapping]]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class ExpirationInfo(_message.Message):
    __slots__ = ("ExpirationDate",)
    EXPIRATIONDATE_FIELD_NUMBER: _ClassVar[int]
    ExpirationDate: _timestamp_pb2.Timestamp
    def __init__(self, ExpirationDate: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetChainQuotesRequestInfo(_message.Message):
    __slots__ = ("UnderlyingSymbol", "ExpirationDates")
    UNDERLYINGSYMBOL_FIELD_NUMBER: _ClassVar[int]
    EXPIRATIONDATES_FIELD_NUMBER: _ClassVar[int]
    UnderlyingSymbol: str
    ExpirationDates: _containers.RepeatedCompositeFieldContainer[_timestamp_pb2.Timestamp]
    def __init__(self, UnderlyingSymbol: _Optional[str] = ..., ExpirationDates: _Optional[_Iterable[_Union[_timestamp_pb2.Timestamp, _Mapping]]] = ...) -> None: ...

class GetQuoteRequestInfo(_message.Message):
    __slots__ = ("Symbol", "GetSyntheticQuote")
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    GETSYNTHETICQUOTE_FIELD_NUMBER: _ClassVar[int]
    Symbol: str
    GetSyntheticQuote: bool
    def __init__(self, Symbol: _Optional[str] = ..., GetSyntheticQuote: bool = ...) -> None: ...

class GetQuotesRequestInfo(_message.Message):
    __slots__ = ("Symbols", "GetSyntheticQuote")
    SYMBOLS_FIELD_NUMBER: _ClassVar[int]
    GETSYNTHETICQUOTE_FIELD_NUMBER: _ClassVar[int]
    Symbols: _containers.RepeatedScalarFieldContainer[str]
    GetSyntheticQuote: bool
    def __init__(self, Symbols: _Optional[_Iterable[str]] = ..., GetSyntheticQuote: bool = ...) -> None: ...

class GetNetQuoteRequestInfos(_message.Message):
    __slots__ = ("GetNetQuoteRequestInfo",)
    GETNETQUOTEREQUESTINFO_FIELD_NUMBER: _ClassVar[int]
    GetNetQuoteRequestInfo: _containers.RepeatedCompositeFieldContainer[GetNetQuoteRequestInfo]
    def __init__(self, GetNetQuoteRequestInfo: _Optional[_Iterable[_Union[GetNetQuoteRequestInfo, _Mapping]]] = ...) -> None: ...

class GetNetQuoteRequestInfo(_message.Message):
    __slots__ = ("LegSymbols", "LegOrderActions", "LegQuantities", "OrderQuantity", "OrderMultiplier", "UniqueKey")
    LEGSYMBOLS_FIELD_NUMBER: _ClassVar[int]
    LEGORDERACTIONS_FIELD_NUMBER: _ClassVar[int]
    LEGQUANTITIES_FIELD_NUMBER: _ClassVar[int]
    ORDERQUANTITY_FIELD_NUMBER: _ClassVar[int]
    ORDERMULTIPLIER_FIELD_NUMBER: _ClassVar[int]
    UNIQUEKEY_FIELD_NUMBER: _ClassVar[int]
    LegSymbols: _containers.RepeatedScalarFieldContainer[str]
    LegOrderActions: _containers.RepeatedScalarFieldContainer[_orders_enums_pb2.EnumOrderAction]
    LegQuantities: _containers.RepeatedScalarFieldContainer[float]
    OrderQuantity: float
    OrderMultiplier: float
    UniqueKey: int
    def __init__(self, LegSymbols: _Optional[_Iterable[str]] = ..., LegOrderActions: _Optional[_Iterable[_Union[_orders_enums_pb2.EnumOrderAction, str]]] = ..., LegQuantities: _Optional[_Iterable[float]] = ..., OrderQuantity: _Optional[float] = ..., OrderMultiplier: _Optional[float] = ..., UniqueKey: _Optional[int] = ...) -> None: ...

class QuoteResponse(_message.Message):
    __slots__ = ("HasData", "QuoteDatas", "NetQuoteInfos", "Warnings", "Errors")
    HASDATA_FIELD_NUMBER: _ClassVar[int]
    QUOTEDATAS_FIELD_NUMBER: _ClassVar[int]
    NETQUOTEINFOS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    HasData: bool
    QuoteDatas: _containers.RepeatedCompositeFieldContainer[QuoteData]
    NetQuoteInfos: _containers.RepeatedCompositeFieldContainer[NetQuoteInfo]
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, HasData: bool = ..., QuoteDatas: _Optional[_Iterable[_Union[QuoteData, _Mapping]]] = ..., NetQuoteInfos: _Optional[_Iterable[_Union[NetQuoteInfo, _Mapping]]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class NetQuoteInfo(_message.Message):
    __slots__ = ("NetQuote", "UniqueKey")
    NETQUOTE_FIELD_NUMBER: _ClassVar[int]
    UNIQUEKEY_FIELD_NUMBER: _ClassVar[int]
    NetQuote: NetQuote
    UniqueKey: int
    def __init__(self, NetQuote: _Optional[_Union[NetQuote, _Mapping]] = ..., UniqueKey: _Optional[int] = ...) -> None: ...

class NetQuote(_message.Message):
    __slots__ = ("Summary", "LegQuotes")
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    LEGQUOTES_FIELD_NUMBER: _ClassVar[int]
    Summary: NetQuoteSummary
    LegQuotes: _containers.RepeatedCompositeFieldContainer[Quote]
    def __init__(self, Summary: _Optional[_Union[NetQuoteSummary, _Mapping]] = ..., LegQuotes: _Optional[_Iterable[_Union[Quote, _Mapping]]] = ...) -> None: ...

class NetQuoteSummary(_message.Message):
    __slots__ = ("Quote", "QuoteTime", "IsCredit")
    QUOTE_FIELD_NUMBER: _ClassVar[int]
    QUOTETIME_FIELD_NUMBER: _ClassVar[int]
    ISCREDIT_FIELD_NUMBER: _ClassVar[int]
    Quote: Quote
    QuoteTime: _timestamp_pb2.Timestamp
    IsCredit: bool
    def __init__(self, Quote: _Optional[_Union[Quote, _Mapping]] = ..., QuoteTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., IsCredit: bool = ...) -> None: ...

class QuoteProxyResponse(_message.Message):
    __slots__ = ("ACK", "GetQuoteResponseInfos", "GetChainQuotesResponseInfo", "SubscriptionTopicResponseInfo", "Warnings", "Errors")
    ACK_FIELD_NUMBER: _ClassVar[int]
    GETQUOTERESPONSEINFOS_FIELD_NUMBER: _ClassVar[int]
    GETCHAINQUOTESRESPONSEINFO_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTIONTOPICRESPONSEINFO_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    ACK: bool
    GetQuoteResponseInfos: _containers.RepeatedCompositeFieldContainer[GetQuoteResponseInfo]
    GetChainQuotesResponseInfo: GetChainQuotesResponseInfo
    SubscriptionTopicResponseInfo: SubscriptionTopicResponseInfo
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, ACK: bool = ..., GetQuoteResponseInfos: _Optional[_Iterable[_Union[GetQuoteResponseInfo, _Mapping]]] = ..., GetChainQuotesResponseInfo: _Optional[_Union[GetChainQuotesResponseInfo, _Mapping]] = ..., SubscriptionTopicResponseInfo: _Optional[_Union[SubscriptionTopicResponseInfo, _Mapping]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class GetChainQuotesResponseInfo(_message.Message):
    __slots__ = ("QuoteData",)
    QUOTEDATA_FIELD_NUMBER: _ClassVar[int]
    QuoteData: QuoteData
    def __init__(self, QuoteData: _Optional[_Union[QuoteData, _Mapping]] = ...) -> None: ...

class GetQuoteResponseInfo(_message.Message):
    __slots__ = ("QuoteData",)
    QUOTEDATA_FIELD_NUMBER: _ClassVar[int]
    QuoteData: QuoteData
    def __init__(self, QuoteData: _Optional[_Union[QuoteData, _Mapping]] = ...) -> None: ...

class Quote(_message.Message):
    __slots__ = ("Last", "Bid", "Ask", "Symbol", "Multiplier", "ContractSize", "Midpoint", "LastSize", "AskSize", "BidSize", "AskExchangeParticipantId", "BidExchangeParticipantId", "LastExchangeParticipantId", "AskExchangeName", "BidExchangeName", "LastExchangeName", "Volume", "PriceChange", "PriceChangePercent", "OpenPrice", "ClosePrice", "PreviousClosePrice", "DayLowPrice", "DayHighPrice", "IsRealTime", "StockQuote", "OptionQuote", "FixedIncomeQuote")
    LAST_FIELD_NUMBER: _ClassVar[int]
    BID_FIELD_NUMBER: _ClassVar[int]
    ASK_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
    CONTRACTSIZE_FIELD_NUMBER: _ClassVar[int]
    MIDPOINT_FIELD_NUMBER: _ClassVar[int]
    LASTSIZE_FIELD_NUMBER: _ClassVar[int]
    ASKSIZE_FIELD_NUMBER: _ClassVar[int]
    BIDSIZE_FIELD_NUMBER: _ClassVar[int]
    ASKEXCHANGEPARTICIPANTID_FIELD_NUMBER: _ClassVar[int]
    BIDEXCHANGEPARTICIPANTID_FIELD_NUMBER: _ClassVar[int]
    LASTEXCHANGEPARTICIPANTID_FIELD_NUMBER: _ClassVar[int]
    ASKEXCHANGENAME_FIELD_NUMBER: _ClassVar[int]
    BIDEXCHANGENAME_FIELD_NUMBER: _ClassVar[int]
    LASTEXCHANGENAME_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    PRICECHANGE_FIELD_NUMBER: _ClassVar[int]
    PRICECHANGEPERCENT_FIELD_NUMBER: _ClassVar[int]
    OPENPRICE_FIELD_NUMBER: _ClassVar[int]
    CLOSEPRICE_FIELD_NUMBER: _ClassVar[int]
    PREVIOUSCLOSEPRICE_FIELD_NUMBER: _ClassVar[int]
    DAYLOWPRICE_FIELD_NUMBER: _ClassVar[int]
    DAYHIGHPRICE_FIELD_NUMBER: _ClassVar[int]
    ISREALTIME_FIELD_NUMBER: _ClassVar[int]
    STOCKQUOTE_FIELD_NUMBER: _ClassVar[int]
    OPTIONQUOTE_FIELD_NUMBER: _ClassVar[int]
    FIXEDINCOMEQUOTE_FIELD_NUMBER: _ClassVar[int]
    Last: float
    Bid: float
    Ask: float
    Symbol: str
    Multiplier: float
    ContractSize: float
    Midpoint: float
    LastSize: int
    AskSize: int
    BidSize: int
    AskExchangeParticipantId: str
    BidExchangeParticipantId: str
    LastExchangeParticipantId: str
    AskExchangeName: str
    BidExchangeName: str
    LastExchangeName: str
    Volume: float
    PriceChange: float
    PriceChangePercent: float
    OpenPrice: float
    ClosePrice: float
    PreviousClosePrice: float
    DayLowPrice: float
    DayHighPrice: float
    IsRealTime: bool
    StockQuote: StockQuote
    OptionQuote: OptionQuote
    FixedIncomeQuote: FixedIncomeQuote
    def __init__(self, Last: _Optional[float] = ..., Bid: _Optional[float] = ..., Ask: _Optional[float] = ..., Symbol: _Optional[str] = ..., Multiplier: _Optional[float] = ..., ContractSize: _Optional[float] = ..., Midpoint: _Optional[float] = ..., LastSize: _Optional[int] = ..., AskSize: _Optional[int] = ..., BidSize: _Optional[int] = ..., AskExchangeParticipantId: _Optional[str] = ..., BidExchangeParticipantId: _Optional[str] = ..., LastExchangeParticipantId: _Optional[str] = ..., AskExchangeName: _Optional[str] = ..., BidExchangeName: _Optional[str] = ..., LastExchangeName: _Optional[str] = ..., Volume: _Optional[float] = ..., PriceChange: _Optional[float] = ..., PriceChangePercent: _Optional[float] = ..., OpenPrice: _Optional[float] = ..., ClosePrice: _Optional[float] = ..., PreviousClosePrice: _Optional[float] = ..., DayLowPrice: _Optional[float] = ..., DayHighPrice: _Optional[float] = ..., IsRealTime: bool = ..., StockQuote: _Optional[_Union[StockQuote, _Mapping]] = ..., OptionQuote: _Optional[_Union[OptionQuote, _Mapping]] = ..., FixedIncomeQuote: _Optional[_Union[FixedIncomeQuote, _Mapping]] = ...) -> None: ...

class StockQuote(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SubscriptionTopicResponseInfo(_message.Message):
    __slots__ = ("TopicsAvailableForStreaming",)
    TOPICSAVAILABLEFORSTREAMING_FIELD_NUMBER: _ClassVar[int]
    TopicsAvailableForStreaming: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, TopicsAvailableForStreaming: _Optional[_Iterable[str]] = ...) -> None: ...

class OptionQuote(_message.Message):
    __slots__ = ("ExpirationYear", "ExpirationMonth", "ExpirationDay", "Strike", "IsCall", "OptionGreeks", "BreakEvenPrice", "ImpliedVolatility", "OpenInterest")
    EXPIRATIONYEAR_FIELD_NUMBER: _ClassVar[int]
    EXPIRATIONMONTH_FIELD_NUMBER: _ClassVar[int]
    EXPIRATIONDAY_FIELD_NUMBER: _ClassVar[int]
    STRIKE_FIELD_NUMBER: _ClassVar[int]
    ISCALL_FIELD_NUMBER: _ClassVar[int]
    OPTIONGREEKS_FIELD_NUMBER: _ClassVar[int]
    BREAKEVENPRICE_FIELD_NUMBER: _ClassVar[int]
    IMPLIEDVOLATILITY_FIELD_NUMBER: _ClassVar[int]
    OPENINTEREST_FIELD_NUMBER: _ClassVar[int]
    ExpirationYear: int
    ExpirationMonth: int
    ExpirationDay: int
    Strike: float
    IsCall: bool
    OptionGreeks: OptionGreeks
    BreakEvenPrice: float
    ImpliedVolatility: float
    OpenInterest: float
    def __init__(self, ExpirationYear: _Optional[int] = ..., ExpirationMonth: _Optional[int] = ..., ExpirationDay: _Optional[int] = ..., Strike: _Optional[float] = ..., IsCall: bool = ..., OptionGreeks: _Optional[_Union[OptionGreeks, _Mapping]] = ..., BreakEvenPrice: _Optional[float] = ..., ImpliedVolatility: _Optional[float] = ..., OpenInterest: _Optional[float] = ...) -> None: ...

class OptionGreeks(_message.Message):
    __slots__ = ("Delta", "Gamma", "Theta", "Vega")
    DELTA_FIELD_NUMBER: _ClassVar[int]
    GAMMA_FIELD_NUMBER: _ClassVar[int]
    THETA_FIELD_NUMBER: _ClassVar[int]
    VEGA_FIELD_NUMBER: _ClassVar[int]
    Delta: float
    Gamma: float
    Theta: float
    Vega: float
    def __init__(self, Delta: _Optional[float] = ..., Gamma: _Optional[float] = ..., Theta: _Optional[float] = ..., Vega: _Optional[float] = ...) -> None: ...

class ChainQuotes(_message.Message):
    __slots__ = ("UnderlyingStockQuote", "OptionQuotes")
    UNDERLYINGSTOCKQUOTE_FIELD_NUMBER: _ClassVar[int]
    OPTIONQUOTES_FIELD_NUMBER: _ClassVar[int]
    UnderlyingStockQuote: StockQuote
    OptionQuotes: _containers.RepeatedCompositeFieldContainer[Quote]
    def __init__(self, UnderlyingStockQuote: _Optional[_Union[StockQuote, _Mapping]] = ..., OptionQuotes: _Optional[_Iterable[_Union[Quote, _Mapping]]] = ...) -> None: ...

class FixedIncomeQuote(_message.Message):
    __slots__ = ("Cusip", "BondTypeCode", "UnitQuantity", "Factor", "IsMarginable")
    CUSIP_FIELD_NUMBER: _ClassVar[int]
    BONDTYPECODE_FIELD_NUMBER: _ClassVar[int]
    UNITQUANTITY_FIELD_NUMBER: _ClassVar[int]
    FACTOR_FIELD_NUMBER: _ClassVar[int]
    ISMARGINABLE_FIELD_NUMBER: _ClassVar[int]
    Cusip: str
    BondTypeCode: str
    UnitQuantity: float
    Factor: float
    IsMarginable: bool
    def __init__(self, Cusip: _Optional[str] = ..., BondTypeCode: _Optional[str] = ..., UnitQuantity: _Optional[float] = ..., Factor: _Optional[float] = ..., IsMarginable: bool = ...) -> None: ...

class QuoteData(_message.Message):
    __slots__ = ("QuoteDataType", "QuoteTime", "ChainQuotes", "Quote", "QuoteProvider")
    QUOTEDATATYPE_FIELD_NUMBER: _ClassVar[int]
    QUOTETIME_FIELD_NUMBER: _ClassVar[int]
    CHAINQUOTES_FIELD_NUMBER: _ClassVar[int]
    QUOTE_FIELD_NUMBER: _ClassVar[int]
    QUOTEPROVIDER_FIELD_NUMBER: _ClassVar[int]
    QuoteDataType: _quotes_enums_pb2.EnumQuoteDataType
    QuoteTime: _timestamp_pb2.Timestamp
    ChainQuotes: ChainQuotes
    Quote: Quote
    QuoteProvider: str
    def __init__(self, QuoteDataType: _Optional[_Union[_quotes_enums_pb2.EnumQuoteDataType, str]] = ..., QuoteTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ChainQuotes: _Optional[_Union[ChainQuotes, _Mapping]] = ..., Quote: _Optional[_Union[Quote, _Mapping]] = ..., QuoteProvider: _Optional[str] = ...) -> None: ...
