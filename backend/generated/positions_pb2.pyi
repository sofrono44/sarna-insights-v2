import common_pb2 as _common_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
import orders_enums_pb2 as _orders_enums_pb2
import positions_enums_pb2 as _positions_enums_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PositionsInfoRequest(_message.Message):
    __slots__ = ("RequestedPositionsLots", "PositionsInfoRequestSearchCriteria", "PairLotsInfo", "UnpairLotsInfo")
    REQUESTEDPOSITIONSLOTS_FIELD_NUMBER: _ClassVar[int]
    POSITIONSINFOREQUESTSEARCHCRITERIA_FIELD_NUMBER: _ClassVar[int]
    PAIRLOTSINFO_FIELD_NUMBER: _ClassVar[int]
    UNPAIRLOTSINFO_FIELD_NUMBER: _ClassVar[int]
    RequestedPositionsLots: _containers.RepeatedScalarFieldContainer[_positions_enums_pb2.EnumRequestedPositionsLots]
    PositionsInfoRequestSearchCriteria: PositionsInfoRequestSearchCriteria
    PairLotsInfo: _containers.RepeatedCompositeFieldContainer[PairLotsInfo]
    UnpairLotsInfo: _containers.RepeatedCompositeFieldContainer[UnpairLotsInfo]
    def __init__(self, RequestedPositionsLots: _Optional[_Iterable[_Union[_positions_enums_pb2.EnumRequestedPositionsLots, str]]] = ..., PositionsInfoRequestSearchCriteria: _Optional[_Union[PositionsInfoRequestSearchCriteria, _Mapping]] = ..., PairLotsInfo: _Optional[_Iterable[_Union[PairLotsInfo, _Mapping]]] = ..., UnpairLotsInfo: _Optional[_Iterable[_Union[UnpairLotsInfo, _Mapping]]] = ...) -> None: ...

class PairLotsInfo(_message.Message):
    __slots__ = ("AccountIds", "SubaccountIds", "GroupingKeys", "MaxPairedSpreadQty", "LegQuantityRatios", "ForceUnpairExistingSpread", "PairToFractionalQuantity")
    class LegQuantityRatiosEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: float
        def __init__(self, key: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...
    ACCOUNTIDS_FIELD_NUMBER: _ClassVar[int]
    SUBACCOUNTIDS_FIELD_NUMBER: _ClassVar[int]
    GROUPINGKEYS_FIELD_NUMBER: _ClassVar[int]
    MAXPAIREDSPREADQTY_FIELD_NUMBER: _ClassVar[int]
    LEGQUANTITYRATIOS_FIELD_NUMBER: _ClassVar[int]
    FORCEUNPAIREXISTINGSPREAD_FIELD_NUMBER: _ClassVar[int]
    PAIRTOFRACTIONALQUANTITY_FIELD_NUMBER: _ClassVar[int]
    AccountIds: _containers.RepeatedScalarFieldContainer[int]
    SubaccountIds: _containers.RepeatedScalarFieldContainer[int]
    GroupingKeys: _containers.RepeatedScalarFieldContainer[str]
    MaxPairedSpreadQty: _containers.RepeatedScalarFieldContainer[float]
    LegQuantityRatios: _containers.ScalarMap[str, float]
    ForceUnpairExistingSpread: bool
    PairToFractionalQuantity: bool
    def __init__(self, AccountIds: _Optional[_Iterable[int]] = ..., SubaccountIds: _Optional[_Iterable[int]] = ..., GroupingKeys: _Optional[_Iterable[str]] = ..., MaxPairedSpreadQty: _Optional[_Iterable[float]] = ..., LegQuantityRatios: _Optional[_Mapping[str, float]] = ..., ForceUnpairExistingSpread: bool = ..., PairToFractionalQuantity: bool = ...) -> None: ...

class UnpairLotsInfo(_message.Message):
    __slots__ = ("AccountIds", "SubaccountIds", "GroupingKeys")
    ACCOUNTIDS_FIELD_NUMBER: _ClassVar[int]
    SUBACCOUNTIDS_FIELD_NUMBER: _ClassVar[int]
    GROUPINGKEYS_FIELD_NUMBER: _ClassVar[int]
    AccountIds: _containers.RepeatedScalarFieldContainer[int]
    SubaccountIds: _containers.RepeatedScalarFieldContainer[int]
    GroupingKeys: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, AccountIds: _Optional[_Iterable[int]] = ..., SubaccountIds: _Optional[_Iterable[int]] = ..., GroupingKeys: _Optional[_Iterable[str]] = ...) -> None: ...

class PositionsInfoRequestSearchCriteria(_message.Message):
    __slots__ = ("AccountIDs", "AccountNumbers", "IgnoreSpreadPairings")
    ACCOUNTIDS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTNUMBERS_FIELD_NUMBER: _ClassVar[int]
    IGNORESPREADPAIRINGS_FIELD_NUMBER: _ClassVar[int]
    AccountIDs: _containers.RepeatedScalarFieldContainer[int]
    AccountNumbers: _containers.RepeatedScalarFieldContainer[str]
    IgnoreSpreadPairings: bool
    def __init__(self, AccountIDs: _Optional[_Iterable[int]] = ..., AccountNumbers: _Optional[_Iterable[str]] = ..., IgnoreSpreadPairings: bool = ...) -> None: ...

class PositionsInfoResponse(_message.Message):
    __slots__ = ("HasData", "resetUiRepository", "OpenPositionsInfo", "ClosedPositionsInfo", "UnpairLotsResponse", "PairLotsResponse", "Warnings", "Errors")
    HASDATA_FIELD_NUMBER: _ClassVar[int]
    RESETUIREPOSITORY_FIELD_NUMBER: _ClassVar[int]
    OPENPOSITIONSINFO_FIELD_NUMBER: _ClassVar[int]
    CLOSEDPOSITIONSINFO_FIELD_NUMBER: _ClassVar[int]
    UNPAIRLOTSRESPONSE_FIELD_NUMBER: _ClassVar[int]
    PAIRLOTSRESPONSE_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    HasData: bool
    resetUiRepository: bool
    OpenPositionsInfo: OpenPositionsInfo
    ClosedPositionsInfo: ClosedPositionsInfo
    UnpairLotsResponse: _containers.RepeatedCompositeFieldContainer[UnpairLotsResponse]
    PairLotsResponse: _containers.RepeatedCompositeFieldContainer[PairLotsResponse]
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, HasData: bool = ..., resetUiRepository: bool = ..., OpenPositionsInfo: _Optional[_Union[OpenPositionsInfo, _Mapping]] = ..., ClosedPositionsInfo: _Optional[_Union[ClosedPositionsInfo, _Mapping]] = ..., UnpairLotsResponse: _Optional[_Iterable[_Union[UnpairLotsResponse, _Mapping]]] = ..., PairLotsResponse: _Optional[_Iterable[_Union[PairLotsResponse, _Mapping]]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class UnpairLotsResponse(_message.Message):
    __slots__ = ("AffectedAccountsCount", "AffectedSubaccountsCount", "ResponseMessages")
    AFFECTEDACCOUNTSCOUNT_FIELD_NUMBER: _ClassVar[int]
    AFFECTEDSUBACCOUNTSCOUNT_FIELD_NUMBER: _ClassVar[int]
    RESPONSEMESSAGES_FIELD_NUMBER: _ClassVar[int]
    AffectedAccountsCount: int
    AffectedSubaccountsCount: int
    ResponseMessages: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseMessage]
    def __init__(self, AffectedAccountsCount: _Optional[int] = ..., AffectedSubaccountsCount: _Optional[int] = ..., ResponseMessages: _Optional[_Iterable[_Union[_common_pb2.ResponseMessage, _Mapping]]] = ...) -> None: ...

class PairLotsResponse(_message.Message):
    __slots__ = ("AffectedAccountsCount", "AffectedSubaccountsCount", "ResponseMessages")
    AFFECTEDACCOUNTSCOUNT_FIELD_NUMBER: _ClassVar[int]
    AFFECTEDSUBACCOUNTSCOUNT_FIELD_NUMBER: _ClassVar[int]
    RESPONSEMESSAGES_FIELD_NUMBER: _ClassVar[int]
    AffectedAccountsCount: int
    AffectedSubaccountsCount: int
    ResponseMessages: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseMessage]
    def __init__(self, AffectedAccountsCount: _Optional[int] = ..., AffectedSubaccountsCount: _Optional[int] = ..., ResponseMessages: _Optional[_Iterable[_Union[_common_pb2.ResponseMessage, _Mapping]]] = ...) -> None: ...

class OpenPositionsInfo(_message.Message):
    __slots__ = ("OpenPositionLotsInfo", "LotsUsedForAggregation", "CurrentPositionValueBySymbol")
    class OpenPositionLotsInfoEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: OpenPositionLotsInfoList
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[OpenPositionLotsInfoList, _Mapping]] = ...) -> None: ...
    class LotsUsedForAggregationEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: OpenPositionLotsInfoList
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[OpenPositionLotsInfoList, _Mapping]] = ...) -> None: ...
    class CurrentPositionValueBySymbolEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: float
        def __init__(self, key: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...
    OPENPOSITIONLOTSINFO_FIELD_NUMBER: _ClassVar[int]
    LOTSUSEDFORAGGREGATION_FIELD_NUMBER: _ClassVar[int]
    CURRENTPOSITIONVALUEBYSYMBOL_FIELD_NUMBER: _ClassVar[int]
    OpenPositionLotsInfo: _containers.MessageMap[str, OpenPositionLotsInfoList]
    LotsUsedForAggregation: _containers.MessageMap[int, OpenPositionLotsInfoList]
    CurrentPositionValueBySymbol: _containers.ScalarMap[str, float]
    def __init__(self, OpenPositionLotsInfo: _Optional[_Mapping[str, OpenPositionLotsInfoList]] = ..., LotsUsedForAggregation: _Optional[_Mapping[int, OpenPositionLotsInfoList]] = ..., CurrentPositionValueBySymbol: _Optional[_Mapping[str, float]] = ...) -> None: ...

class OpenPositionLotsInfoList(_message.Message):
    __slots__ = ("OpenPositionLotsInfo",)
    OPENPOSITIONLOTSINFO_FIELD_NUMBER: _ClassVar[int]
    OpenPositionLotsInfo: _containers.RepeatedCompositeFieldContainer[OpenPositionLotInfo]
    def __init__(self, OpenPositionLotsInfo: _Optional[_Iterable[_Union[OpenPositionLotInfo, _Mapping]]] = ...) -> None: ...

class OpenPositionLotInfo(_message.Message):
    __slots__ = ("OpenPositionLot", "CurrentPricePerShare", "Timestamp", "IsLongTerm", "GroupingKey", "AllowedActions", "PairedPositionInfo")
    OPENPOSITIONLOT_FIELD_NUMBER: _ClassVar[int]
    CURRENTPRICEPERSHARE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ISLONGTERM_FIELD_NUMBER: _ClassVar[int]
    GROUPINGKEY_FIELD_NUMBER: _ClassVar[int]
    ALLOWEDACTIONS_FIELD_NUMBER: _ClassVar[int]
    PAIREDPOSITIONINFO_FIELD_NUMBER: _ClassVar[int]
    OpenPositionLot: OpenPositionLot
    CurrentPricePerShare: float
    Timestamp: int
    IsLongTerm: bool
    GroupingKey: str
    AllowedActions: _containers.RepeatedScalarFieldContainer[bool]
    PairedPositionInfo: PairedPositionInfo
    def __init__(self, OpenPositionLot: _Optional[_Union[OpenPositionLot, _Mapping]] = ..., CurrentPricePerShare: _Optional[float] = ..., Timestamp: _Optional[int] = ..., IsLongTerm: bool = ..., GroupingKey: _Optional[str] = ..., AllowedActions: _Optional[_Iterable[bool]] = ..., PairedPositionInfo: _Optional[_Union[PairedPositionInfo, _Mapping]] = ...) -> None: ...

class OpenPositionLot(_message.Message):
    __slots__ = ("OpenPositionLotId", "OrderId", "Multiplier", "LastModifiedTime", "Description", "Expiration", "SubaccountId", "Commission", "CreatedTime", "AccountId", "SecurityType", "CallOrPut", "CostBasisPerShare", "OpenQuantity", "PreviousDayClosePrice", "OpenPrice", "StrikePrice", "ClosedQuantity", "Symbol", "UnderlyingSymbol", "ContractSize", "AcquisitionDate", "Cusip", "SpreadPairingKey", "ExternalSecurityId", "AccountNumber")
    OPENPOSITIONLOTID_FIELD_NUMBER: _ClassVar[int]
    ORDERID_FIELD_NUMBER: _ClassVar[int]
    MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
    LASTMODIFIEDTIME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    SUBACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    COMMISSION_FIELD_NUMBER: _ClassVar[int]
    CREATEDTIME_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    SECURITYTYPE_FIELD_NUMBER: _ClassVar[int]
    CALLORPUT_FIELD_NUMBER: _ClassVar[int]
    COSTBASISPERSHARE_FIELD_NUMBER: _ClassVar[int]
    OPENQUANTITY_FIELD_NUMBER: _ClassVar[int]
    PREVIOUSDAYCLOSEPRICE_FIELD_NUMBER: _ClassVar[int]
    OPENPRICE_FIELD_NUMBER: _ClassVar[int]
    STRIKEPRICE_FIELD_NUMBER: _ClassVar[int]
    CLOSEDQUANTITY_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    UNDERLYINGSYMBOL_FIELD_NUMBER: _ClassVar[int]
    CONTRACTSIZE_FIELD_NUMBER: _ClassVar[int]
    ACQUISITIONDATE_FIELD_NUMBER: _ClassVar[int]
    CUSIP_FIELD_NUMBER: _ClassVar[int]
    SPREADPAIRINGKEY_FIELD_NUMBER: _ClassVar[int]
    EXTERNALSECURITYID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTNUMBER_FIELD_NUMBER: _ClassVar[int]
    OpenPositionLotId: int
    OrderId: int
    Multiplier: float
    LastModifiedTime: _timestamp_pb2.Timestamp
    Description: str
    Expiration: _timestamp_pb2.Timestamp
    SubaccountId: int
    Commission: float
    CreatedTime: _timestamp_pb2.Timestamp
    AccountId: int
    SecurityType: _orders_enums_pb2.EnumSecurityType
    CallOrPut: _orders_enums_pb2.EnumCallOrPut
    CostBasisPerShare: float
    OpenQuantity: float
    PreviousDayClosePrice: float
    OpenPrice: float
    StrikePrice: float
    ClosedQuantity: float
    Symbol: str
    UnderlyingSymbol: str
    ContractSize: float
    AcquisitionDate: _timestamp_pb2.Timestamp
    Cusip: str
    SpreadPairingKey: int
    ExternalSecurityId: str
    AccountNumber: str
    def __init__(self, OpenPositionLotId: _Optional[int] = ..., OrderId: _Optional[int] = ..., Multiplier: _Optional[float] = ..., LastModifiedTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., Description: _Optional[str] = ..., Expiration: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., SubaccountId: _Optional[int] = ..., Commission: _Optional[float] = ..., CreatedTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., AccountId: _Optional[int] = ..., SecurityType: _Optional[_Union[_orders_enums_pb2.EnumSecurityType, str]] = ..., CallOrPut: _Optional[_Union[_orders_enums_pb2.EnumCallOrPut, str]] = ..., CostBasisPerShare: _Optional[float] = ..., OpenQuantity: _Optional[float] = ..., PreviousDayClosePrice: _Optional[float] = ..., OpenPrice: _Optional[float] = ..., StrikePrice: _Optional[float] = ..., ClosedQuantity: _Optional[float] = ..., Symbol: _Optional[str] = ..., UnderlyingSymbol: _Optional[str] = ..., ContractSize: _Optional[float] = ..., AcquisitionDate: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., Cusip: _Optional[str] = ..., SpreadPairingKey: _Optional[int] = ..., ExternalSecurityId: _Optional[str] = ..., AccountNumber: _Optional[str] = ...) -> None: ...

class PairedPositionInfo(_message.Message):
    __slots__ = ("SpreadQuantity", "StrategyType", "LegQuantityRatios", "CostBasisPerShare")
    class LegQuantityRatiosEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: float
        def __init__(self, key: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...
    SPREADQUANTITY_FIELD_NUMBER: _ClassVar[int]
    STRATEGYTYPE_FIELD_NUMBER: _ClassVar[int]
    LEGQUANTITYRATIOS_FIELD_NUMBER: _ClassVar[int]
    COSTBASISPERSHARE_FIELD_NUMBER: _ClassVar[int]
    SpreadQuantity: float
    StrategyType: _orders_enums_pb2.EnumStrategyType
    LegQuantityRatios: _containers.ScalarMap[str, float]
    CostBasisPerShare: float
    def __init__(self, SpreadQuantity: _Optional[float] = ..., StrategyType: _Optional[_Union[_orders_enums_pb2.EnumStrategyType, str]] = ..., LegQuantityRatios: _Optional[_Mapping[str, float]] = ..., CostBasisPerShare: _Optional[float] = ...) -> None: ...

class ClosedPositionsInfo(_message.Message):
    __slots__ = ("ClosedPositionLotsInfo",)
    CLOSEDPOSITIONLOTSINFO_FIELD_NUMBER: _ClassVar[int]
    ClosedPositionLotsInfo: _containers.RepeatedCompositeFieldContainer[ClosedPositionLotInfo]
    def __init__(self, ClosedPositionLotsInfo: _Optional[_Iterable[_Union[ClosedPositionLotInfo, _Mapping]]] = ...) -> None: ...

class ClosedPositionLotInfo(_message.Message):
    __slots__ = ("ClosedPositionLot", "AllowedActions")
    CLOSEDPOSITIONLOT_FIELD_NUMBER: _ClassVar[int]
    ALLOWEDACTIONS_FIELD_NUMBER: _ClassVar[int]
    ClosedPositionLot: ClosedPositionLot
    AllowedActions: _containers.RepeatedScalarFieldContainer[bool]
    def __init__(self, ClosedPositionLot: _Optional[_Union[ClosedPositionLot, _Mapping]] = ..., AllowedActions: _Optional[_Iterable[bool]] = ...) -> None: ...

class ClosedPositionLot(_message.Message):
    __slots__ = ("ClosedPositionLotId", "OpenOrderId", "AccountId", "SubaccountId", "Symbol", "UnderlyingSymbol", "Description", "OpenQuantity", "ClosedQuantity", "OpenPrice", "ClosedPrice", "OpenCostBasisPerShare", "ClosedCostBasisPerShare", "OpenCommission", "ClosedCommission", "SecurityType", "CallOrPut", "Expiration", "StrikePrice", "Multiplier", "OpenPositionLotCreatedTime", "CreatedTime", "LastModifiedTime", "AccountNumber")
    CLOSEDPOSITIONLOTID_FIELD_NUMBER: _ClassVar[int]
    OPENORDERID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    SUBACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    UNDERLYINGSYMBOL_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    OPENQUANTITY_FIELD_NUMBER: _ClassVar[int]
    CLOSEDQUANTITY_FIELD_NUMBER: _ClassVar[int]
    OPENPRICE_FIELD_NUMBER: _ClassVar[int]
    CLOSEDPRICE_FIELD_NUMBER: _ClassVar[int]
    OPENCOSTBASISPERSHARE_FIELD_NUMBER: _ClassVar[int]
    CLOSEDCOSTBASISPERSHARE_FIELD_NUMBER: _ClassVar[int]
    OPENCOMMISSION_FIELD_NUMBER: _ClassVar[int]
    CLOSEDCOMMISSION_FIELD_NUMBER: _ClassVar[int]
    SECURITYTYPE_FIELD_NUMBER: _ClassVar[int]
    CALLORPUT_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    STRIKEPRICE_FIELD_NUMBER: _ClassVar[int]
    MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
    OPENPOSITIONLOTCREATEDTIME_FIELD_NUMBER: _ClassVar[int]
    CREATEDTIME_FIELD_NUMBER: _ClassVar[int]
    LASTMODIFIEDTIME_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTNUMBER_FIELD_NUMBER: _ClassVar[int]
    ClosedPositionLotId: int
    OpenOrderId: int
    AccountId: int
    SubaccountId: int
    Symbol: str
    UnderlyingSymbol: str
    Description: str
    OpenQuantity: float
    ClosedQuantity: float
    OpenPrice: float
    ClosedPrice: float
    OpenCostBasisPerShare: float
    ClosedCostBasisPerShare: float
    OpenCommission: float
    ClosedCommission: float
    SecurityType: _orders_enums_pb2.EnumSecurityType
    CallOrPut: _orders_enums_pb2.EnumCallOrPut
    Expiration: _timestamp_pb2.Timestamp
    StrikePrice: float
    Multiplier: float
    OpenPositionLotCreatedTime: _timestamp_pb2.Timestamp
    CreatedTime: _timestamp_pb2.Timestamp
    LastModifiedTime: _timestamp_pb2.Timestamp
    AccountNumber: str
    def __init__(self, ClosedPositionLotId: _Optional[int] = ..., OpenOrderId: _Optional[int] = ..., AccountId: _Optional[int] = ..., SubaccountId: _Optional[int] = ..., Symbol: _Optional[str] = ..., UnderlyingSymbol: _Optional[str] = ..., Description: _Optional[str] = ..., OpenQuantity: _Optional[float] = ..., ClosedQuantity: _Optional[float] = ..., OpenPrice: _Optional[float] = ..., ClosedPrice: _Optional[float] = ..., OpenCostBasisPerShare: _Optional[float] = ..., ClosedCostBasisPerShare: _Optional[float] = ..., OpenCommission: _Optional[float] = ..., ClosedCommission: _Optional[float] = ..., SecurityType: _Optional[_Union[_orders_enums_pb2.EnumSecurityType, str]] = ..., CallOrPut: _Optional[_Union[_orders_enums_pb2.EnumCallOrPut, str]] = ..., Expiration: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., StrikePrice: _Optional[float] = ..., Multiplier: _Optional[float] = ..., OpenPositionLotCreatedTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., CreatedTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., LastModifiedTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., AccountNumber: _Optional[str] = ...) -> None: ...
