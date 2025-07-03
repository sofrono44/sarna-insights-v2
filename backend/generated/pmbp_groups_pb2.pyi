import bp_enums_pb2 as _bp_enums_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BasketGroup(_message.Message):
    __slots__ = ("BasketId", "ClassGroupId", "Products", "NAV", "Minimum", "GainsAndLosses", "AppliedOffsetPercent", "ScenariosPercentages", "MorningNAV", "DayPnL", "DayPnL_Utilization")
    BASKETID_FIELD_NUMBER: _ClassVar[int]
    CLASSGROUPID_FIELD_NUMBER: _ClassVar[int]
    PRODUCTS_FIELD_NUMBER: _ClassVar[int]
    NAV_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_FIELD_NUMBER: _ClassVar[int]
    GAINSANDLOSSES_FIELD_NUMBER: _ClassVar[int]
    APPLIEDOFFSETPERCENT_FIELD_NUMBER: _ClassVar[int]
    SCENARIOSPERCENTAGES_FIELD_NUMBER: _ClassVar[int]
    MORNINGNAV_FIELD_NUMBER: _ClassVar[int]
    DAYPNL_FIELD_NUMBER: _ClassVar[int]
    DAYPNL_UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    BasketId: str
    ClassGroupId: str
    Products: _containers.RepeatedCompositeFieldContainer[Product]
    NAV: float
    Minimum: float
    GainsAndLosses: _containers.RepeatedScalarFieldContainer[float]
    AppliedOffsetPercent: float
    ScenariosPercentages: _containers.RepeatedScalarFieldContainer[float]
    MorningNAV: float
    DayPnL: float
    DayPnL_Utilization: float
    def __init__(self, BasketId: _Optional[str] = ..., ClassGroupId: _Optional[str] = ..., Products: _Optional[_Iterable[_Union[Product, _Mapping]]] = ..., NAV: _Optional[float] = ..., Minimum: _Optional[float] = ..., GainsAndLosses: _Optional[_Iterable[float]] = ..., AppliedOffsetPercent: _Optional[float] = ..., ScenariosPercentages: _Optional[_Iterable[float]] = ..., MorningNAV: _Optional[float] = ..., DayPnL: _Optional[float] = ..., DayPnL_Utilization: _Optional[float] = ...) -> None: ...

class ClassGroup(_message.Message):
    __slots__ = ("ClassGroupId", "ProductGroupId", "Products", "BasketGroups", "NAV", "Minimum", "RiskCharge", "GainsAndLosses", "ConcentrationPercentage", "ConcentrationToNetLiq", "ScenariosPercentages", "AppliedIVShockDirection", "AppliedIVShockValues", "MorningNAV", "PositionAggregations", "DayPnL", "DayPnL_Utilization", "Requirement", "AdvShockLabel", "AppliedAddOns")
    CLASSGROUPID_FIELD_NUMBER: _ClassVar[int]
    PRODUCTGROUPID_FIELD_NUMBER: _ClassVar[int]
    PRODUCTS_FIELD_NUMBER: _ClassVar[int]
    BASKETGROUPS_FIELD_NUMBER: _ClassVar[int]
    NAV_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_FIELD_NUMBER: _ClassVar[int]
    RISKCHARGE_FIELD_NUMBER: _ClassVar[int]
    GAINSANDLOSSES_FIELD_NUMBER: _ClassVar[int]
    CONCENTRATIONPERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    CONCENTRATIONTONETLIQ_FIELD_NUMBER: _ClassVar[int]
    SCENARIOSPERCENTAGES_FIELD_NUMBER: _ClassVar[int]
    APPLIEDIVSHOCKDIRECTION_FIELD_NUMBER: _ClassVar[int]
    APPLIEDIVSHOCKVALUES_FIELD_NUMBER: _ClassVar[int]
    MORNINGNAV_FIELD_NUMBER: _ClassVar[int]
    POSITIONAGGREGATIONS_FIELD_NUMBER: _ClassVar[int]
    DAYPNL_FIELD_NUMBER: _ClassVar[int]
    DAYPNL_UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    REQUIREMENT_FIELD_NUMBER: _ClassVar[int]
    ADVSHOCKLABEL_FIELD_NUMBER: _ClassVar[int]
    APPLIEDADDONS_FIELD_NUMBER: _ClassVar[int]
    ClassGroupId: str
    ProductGroupId: str
    Products: _containers.RepeatedCompositeFieldContainer[Product]
    BasketGroups: _containers.RepeatedCompositeFieldContainer[BasketGroup]
    NAV: float
    Minimum: float
    RiskCharge: float
    GainsAndLosses: _containers.RepeatedScalarFieldContainer[float]
    ConcentrationPercentage: float
    ConcentrationToNetLiq: float
    ScenariosPercentages: _containers.RepeatedScalarFieldContainer[float]
    AppliedIVShockDirection: int
    AppliedIVShockValues: _containers.RepeatedScalarFieldContainer[float]
    MorningNAV: float
    PositionAggregations: AdvancedAggregations
    DayPnL: float
    DayPnL_Utilization: float
    Requirement: float
    AdvShockLabel: _containers.RepeatedScalarFieldContainer[str]
    AppliedAddOns: AppliedAddOns
    def __init__(self, ClassGroupId: _Optional[str] = ..., ProductGroupId: _Optional[str] = ..., Products: _Optional[_Iterable[_Union[Product, _Mapping]]] = ..., BasketGroups: _Optional[_Iterable[_Union[BasketGroup, _Mapping]]] = ..., NAV: _Optional[float] = ..., Minimum: _Optional[float] = ..., RiskCharge: _Optional[float] = ..., GainsAndLosses: _Optional[_Iterable[float]] = ..., ConcentrationPercentage: _Optional[float] = ..., ConcentrationToNetLiq: _Optional[float] = ..., ScenariosPercentages: _Optional[_Iterable[float]] = ..., AppliedIVShockDirection: _Optional[int] = ..., AppliedIVShockValues: _Optional[_Iterable[float]] = ..., MorningNAV: _Optional[float] = ..., PositionAggregations: _Optional[_Union[AdvancedAggregations, _Mapping]] = ..., DayPnL: _Optional[float] = ..., DayPnL_Utilization: _Optional[float] = ..., Requirement: _Optional[float] = ..., AdvShockLabel: _Optional[_Iterable[str]] = ..., AppliedAddOns: _Optional[_Union[AppliedAddOns, _Mapping]] = ...) -> None: ...

class Groupings(_message.Message):
    __slots__ = ("PortfolioAggregations", "PortfolioGroups", "ProductGroups")
    PORTFOLIOAGGREGATIONS_FIELD_NUMBER: _ClassVar[int]
    PORTFOLIOGROUPS_FIELD_NUMBER: _ClassVar[int]
    PRODUCTGROUPS_FIELD_NUMBER: _ClassVar[int]
    PortfolioAggregations: _containers.RepeatedCompositeFieldContainer[PortfolioAggregation]
    PortfolioGroups: _containers.RepeatedCompositeFieldContainer[PortfolioGroup]
    ProductGroups: _containers.RepeatedCompositeFieldContainer[ProductGroup]
    def __init__(self, PortfolioAggregations: _Optional[_Iterable[_Union[PortfolioAggregation, _Mapping]]] = ..., PortfolioGroups: _Optional[_Iterable[_Union[PortfolioGroup, _Mapping]]] = ..., ProductGroups: _Optional[_Iterable[_Union[ProductGroup, _Mapping]]] = ...) -> None: ...

class PortfolioAggregation(_message.Message):
    __slots__ = ("PortfolioGroups", "NAV", "Minimum", "RiskCharge", "GainsAndLosses", "ConcentrationPercentage", "ConcentrationToNetLiq", "AppliedIVShockValues", "MorningNAV", "DayPnL", "DayPnL_Utilization")
    PORTFOLIOGROUPS_FIELD_NUMBER: _ClassVar[int]
    NAV_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_FIELD_NUMBER: _ClassVar[int]
    RISKCHARGE_FIELD_NUMBER: _ClassVar[int]
    GAINSANDLOSSES_FIELD_NUMBER: _ClassVar[int]
    CONCENTRATIONPERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    CONCENTRATIONTONETLIQ_FIELD_NUMBER: _ClassVar[int]
    APPLIEDIVSHOCKVALUES_FIELD_NUMBER: _ClassVar[int]
    MORNINGNAV_FIELD_NUMBER: _ClassVar[int]
    DAYPNL_FIELD_NUMBER: _ClassVar[int]
    DAYPNL_UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    PortfolioGroups: _containers.RepeatedCompositeFieldContainer[PortfolioGroup]
    NAV: float
    Minimum: float
    RiskCharge: float
    GainsAndLosses: _containers.RepeatedScalarFieldContainer[float]
    ConcentrationPercentage: float
    ConcentrationToNetLiq: float
    AppliedIVShockValues: _containers.RepeatedScalarFieldContainer[float]
    MorningNAV: float
    DayPnL: float
    DayPnL_Utilization: float
    def __init__(self, PortfolioGroups: _Optional[_Iterable[_Union[PortfolioGroup, _Mapping]]] = ..., NAV: _Optional[float] = ..., Minimum: _Optional[float] = ..., RiskCharge: _Optional[float] = ..., GainsAndLosses: _Optional[_Iterable[float]] = ..., ConcentrationPercentage: _Optional[float] = ..., ConcentrationToNetLiq: _Optional[float] = ..., AppliedIVShockValues: _Optional[_Iterable[float]] = ..., MorningNAV: _Optional[float] = ..., DayPnL: _Optional[float] = ..., DayPnL_Utilization: _Optional[float] = ...) -> None: ...

class PortfolioGroup(_message.Message):
    __slots__ = ("PortfolioGroupId", "ProductGroups", "NAV", "Minimum", "RiskCharge", "GainsAndLosses", "AppliedOffsetPercent", "ConcentrationPercentage", "ConcentrationToNetLiq", "AppliedIVShockValues", "MorningNAV", "PositionAggregations", "DayPnL", "DayPnL_Utilization", "Requirement")
    PORTFOLIOGROUPID_FIELD_NUMBER: _ClassVar[int]
    PRODUCTGROUPS_FIELD_NUMBER: _ClassVar[int]
    NAV_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_FIELD_NUMBER: _ClassVar[int]
    RISKCHARGE_FIELD_NUMBER: _ClassVar[int]
    GAINSANDLOSSES_FIELD_NUMBER: _ClassVar[int]
    APPLIEDOFFSETPERCENT_FIELD_NUMBER: _ClassVar[int]
    CONCENTRATIONPERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    CONCENTRATIONTONETLIQ_FIELD_NUMBER: _ClassVar[int]
    APPLIEDIVSHOCKVALUES_FIELD_NUMBER: _ClassVar[int]
    MORNINGNAV_FIELD_NUMBER: _ClassVar[int]
    POSITIONAGGREGATIONS_FIELD_NUMBER: _ClassVar[int]
    DAYPNL_FIELD_NUMBER: _ClassVar[int]
    DAYPNL_UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    REQUIREMENT_FIELD_NUMBER: _ClassVar[int]
    PortfolioGroupId: str
    ProductGroups: _containers.RepeatedCompositeFieldContainer[ProductGroup]
    NAV: float
    Minimum: float
    RiskCharge: float
    GainsAndLosses: _containers.RepeatedScalarFieldContainer[float]
    AppliedOffsetPercent: float
    ConcentrationPercentage: float
    ConcentrationToNetLiq: float
    AppliedIVShockValues: _containers.RepeatedScalarFieldContainer[float]
    MorningNAV: float
    PositionAggregations: AdvancedAggregations
    DayPnL: float
    DayPnL_Utilization: float
    Requirement: float
    def __init__(self, PortfolioGroupId: _Optional[str] = ..., ProductGroups: _Optional[_Iterable[_Union[ProductGroup, _Mapping]]] = ..., NAV: _Optional[float] = ..., Minimum: _Optional[float] = ..., RiskCharge: _Optional[float] = ..., GainsAndLosses: _Optional[_Iterable[float]] = ..., AppliedOffsetPercent: _Optional[float] = ..., ConcentrationPercentage: _Optional[float] = ..., ConcentrationToNetLiq: _Optional[float] = ..., AppliedIVShockValues: _Optional[_Iterable[float]] = ..., MorningNAV: _Optional[float] = ..., PositionAggregations: _Optional[_Union[AdvancedAggregations, _Mapping]] = ..., DayPnL: _Optional[float] = ..., DayPnL_Utilization: _Optional[float] = ..., Requirement: _Optional[float] = ...) -> None: ...

class Product(_message.Message):
    __slots__ = ("ProductType", "ClassGroupId", "ProductGroupId", "BasketId", "GainsAndLossesScenarios", "PriceMovementValues", "UnderlyingSymbol", "Quantity", "Symbol", "Multiplier", "NAV", "Minimum", "CallPut", "Strike", "UnderlyingPrice", "InputStrategyComponentType", "OrderId", "PendingTransaction", "ConcentrationPercentage", "ConcentrationToNetLiq", "VolatilityDownShock", "VolatilityUpShock", "ScenariosPercentages", "IsETF", "MarketMoveAdjustmentFactor", "IsUserUploaded", "UnderlyingPriceMovementValues", "MorningNAV", "ExternalDataSourceName", "Greeks", "DayPnL", "DayPnL_Utilization", "QuantityOpenedToday", "QuantityClosedToday", "ProductId", "WhatIfAdjustment", "Requirement", "Expiration", "IsPMEligible", "IsShockEligible", "Price", "AdvShockLabel", "AppliedAddOns")
    PRODUCTTYPE_FIELD_NUMBER: _ClassVar[int]
    CLASSGROUPID_FIELD_NUMBER: _ClassVar[int]
    PRODUCTGROUPID_FIELD_NUMBER: _ClassVar[int]
    BASKETID_FIELD_NUMBER: _ClassVar[int]
    GAINSANDLOSSESSCENARIOS_FIELD_NUMBER: _ClassVar[int]
    PRICEMOVEMENTVALUES_FIELD_NUMBER: _ClassVar[int]
    UNDERLYINGSYMBOL_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
    NAV_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_FIELD_NUMBER: _ClassVar[int]
    CALLPUT_FIELD_NUMBER: _ClassVar[int]
    STRIKE_FIELD_NUMBER: _ClassVar[int]
    UNDERLYINGPRICE_FIELD_NUMBER: _ClassVar[int]
    INPUTSTRATEGYCOMPONENTTYPE_FIELD_NUMBER: _ClassVar[int]
    ORDERID_FIELD_NUMBER: _ClassVar[int]
    PENDINGTRANSACTION_FIELD_NUMBER: _ClassVar[int]
    CONCENTRATIONPERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    CONCENTRATIONTONETLIQ_FIELD_NUMBER: _ClassVar[int]
    VOLATILITYDOWNSHOCK_FIELD_NUMBER: _ClassVar[int]
    VOLATILITYUPSHOCK_FIELD_NUMBER: _ClassVar[int]
    SCENARIOSPERCENTAGES_FIELD_NUMBER: _ClassVar[int]
    ISETF_FIELD_NUMBER: _ClassVar[int]
    MARKETMOVEADJUSTMENTFACTOR_FIELD_NUMBER: _ClassVar[int]
    ISUSERUPLOADED_FIELD_NUMBER: _ClassVar[int]
    UNDERLYINGPRICEMOVEMENTVALUES_FIELD_NUMBER: _ClassVar[int]
    MORNINGNAV_FIELD_NUMBER: _ClassVar[int]
    EXTERNALDATASOURCENAME_FIELD_NUMBER: _ClassVar[int]
    GREEKS_FIELD_NUMBER: _ClassVar[int]
    DAYPNL_FIELD_NUMBER: _ClassVar[int]
    DAYPNL_UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    QUANTITYOPENEDTODAY_FIELD_NUMBER: _ClassVar[int]
    QUANTITYCLOSEDTODAY_FIELD_NUMBER: _ClassVar[int]
    PRODUCTID_FIELD_NUMBER: _ClassVar[int]
    WHATIFADJUSTMENT_FIELD_NUMBER: _ClassVar[int]
    REQUIREMENT_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    ISPMELIGIBLE_FIELD_NUMBER: _ClassVar[int]
    ISSHOCKELIGIBLE_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    ADVSHOCKLABEL_FIELD_NUMBER: _ClassVar[int]
    APPLIEDADDONS_FIELD_NUMBER: _ClassVar[int]
    ProductType: str
    ClassGroupId: str
    ProductGroupId: str
    BasketId: str
    GainsAndLossesScenarios: _containers.RepeatedScalarFieldContainer[float]
    PriceMovementValues: _containers.RepeatedScalarFieldContainer[float]
    UnderlyingSymbol: str
    Quantity: float
    Symbol: str
    Multiplier: float
    NAV: float
    Minimum: float
    CallPut: str
    Strike: float
    UnderlyingPrice: float
    InputStrategyComponentType: _bp_enums_pb2.EnumInputStrategyComponentType
    OrderId: str
    PendingTransaction: float
    ConcentrationPercentage: float
    ConcentrationToNetLiq: float
    VolatilityDownShock: VolatilityShockResult
    VolatilityUpShock: VolatilityShockResult
    ScenariosPercentages: _containers.RepeatedScalarFieldContainer[float]
    IsETF: bool
    MarketMoveAdjustmentFactor: float
    IsUserUploaded: bool
    UnderlyingPriceMovementValues: _containers.RepeatedScalarFieldContainer[float]
    MorningNAV: float
    ExternalDataSourceName: str
    Greeks: ProductGreeks
    DayPnL: float
    DayPnL_Utilization: float
    QuantityOpenedToday: float
    QuantityClosedToday: float
    ProductId: str
    WhatIfAdjustment: ProductWhatIfAdjustment
    Requirement: float
    Expiration: str
    IsPMEligible: bool
    IsShockEligible: bool
    Price: float
    AdvShockLabel: _containers.RepeatedScalarFieldContainer[str]
    AppliedAddOns: AppliedAddOns
    def __init__(self, ProductType: _Optional[str] = ..., ClassGroupId: _Optional[str] = ..., ProductGroupId: _Optional[str] = ..., BasketId: _Optional[str] = ..., GainsAndLossesScenarios: _Optional[_Iterable[float]] = ..., PriceMovementValues: _Optional[_Iterable[float]] = ..., UnderlyingSymbol: _Optional[str] = ..., Quantity: _Optional[float] = ..., Symbol: _Optional[str] = ..., Multiplier: _Optional[float] = ..., NAV: _Optional[float] = ..., Minimum: _Optional[float] = ..., CallPut: _Optional[str] = ..., Strike: _Optional[float] = ..., UnderlyingPrice: _Optional[float] = ..., InputStrategyComponentType: _Optional[_Union[_bp_enums_pb2.EnumInputStrategyComponentType, str]] = ..., OrderId: _Optional[str] = ..., PendingTransaction: _Optional[float] = ..., ConcentrationPercentage: _Optional[float] = ..., ConcentrationToNetLiq: _Optional[float] = ..., VolatilityDownShock: _Optional[_Union[VolatilityShockResult, _Mapping]] = ..., VolatilityUpShock: _Optional[_Union[VolatilityShockResult, _Mapping]] = ..., ScenariosPercentages: _Optional[_Iterable[float]] = ..., IsETF: bool = ..., MarketMoveAdjustmentFactor: _Optional[float] = ..., IsUserUploaded: bool = ..., UnderlyingPriceMovementValues: _Optional[_Iterable[float]] = ..., MorningNAV: _Optional[float] = ..., ExternalDataSourceName: _Optional[str] = ..., Greeks: _Optional[_Union[ProductGreeks, _Mapping]] = ..., DayPnL: _Optional[float] = ..., DayPnL_Utilization: _Optional[float] = ..., QuantityOpenedToday: _Optional[float] = ..., QuantityClosedToday: _Optional[float] = ..., ProductId: _Optional[str] = ..., WhatIfAdjustment: _Optional[_Union[ProductWhatIfAdjustment, _Mapping]] = ..., Requirement: _Optional[float] = ..., Expiration: _Optional[str] = ..., IsPMEligible: bool = ..., IsShockEligible: bool = ..., Price: _Optional[float] = ..., AdvShockLabel: _Optional[_Iterable[str]] = ..., AppliedAddOns: _Optional[_Union[AppliedAddOns, _Mapping]] = ...) -> None: ...

class AppliedAddOns(_message.Message):
    __slots__ = ("LowPricedStocksAddOn", "ConcentrationAddOn", "LiquidityAddOn")
    LOWPRICEDSTOCKSADDON_FIELD_NUMBER: _ClassVar[int]
    CONCENTRATIONADDON_FIELD_NUMBER: _ClassVar[int]
    LIQUIDITYADDON_FIELD_NUMBER: _ClassVar[int]
    LowPricedStocksAddOn: float
    ConcentrationAddOn: float
    LiquidityAddOn: float
    def __init__(self, LowPricedStocksAddOn: _Optional[float] = ..., ConcentrationAddOn: _Optional[float] = ..., LiquidityAddOn: _Optional[float] = ...) -> None: ...

class ProductGroup(_message.Message):
    __slots__ = ("ProductGroupId", "ClassGroups", "NAV", "Minimum", "RiskCharge", "GainsAndLosses", "AppliedOffsetPercent", "Requirement", "ConcentrationPercentage", "ConcentrationToNetLiq", "ScenariosPercentages", "AppliedIVShockValues", "MorningNAV", "PositionAggregations", "DayPnL", "DayPnL_Utilization")
    PRODUCTGROUPID_FIELD_NUMBER: _ClassVar[int]
    CLASSGROUPS_FIELD_NUMBER: _ClassVar[int]
    NAV_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_FIELD_NUMBER: _ClassVar[int]
    RISKCHARGE_FIELD_NUMBER: _ClassVar[int]
    GAINSANDLOSSES_FIELD_NUMBER: _ClassVar[int]
    APPLIEDOFFSETPERCENT_FIELD_NUMBER: _ClassVar[int]
    REQUIREMENT_FIELD_NUMBER: _ClassVar[int]
    CONCENTRATIONPERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    CONCENTRATIONTONETLIQ_FIELD_NUMBER: _ClassVar[int]
    SCENARIOSPERCENTAGES_FIELD_NUMBER: _ClassVar[int]
    APPLIEDIVSHOCKVALUES_FIELD_NUMBER: _ClassVar[int]
    MORNINGNAV_FIELD_NUMBER: _ClassVar[int]
    POSITIONAGGREGATIONS_FIELD_NUMBER: _ClassVar[int]
    DAYPNL_FIELD_NUMBER: _ClassVar[int]
    DAYPNL_UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    ProductGroupId: str
    ClassGroups: _containers.RepeatedCompositeFieldContainer[ClassGroup]
    NAV: float
    Minimum: float
    RiskCharge: float
    GainsAndLosses: _containers.RepeatedScalarFieldContainer[float]
    AppliedOffsetPercent: float
    Requirement: float
    ConcentrationPercentage: float
    ConcentrationToNetLiq: float
    ScenariosPercentages: _containers.RepeatedScalarFieldContainer[float]
    AppliedIVShockValues: _containers.RepeatedScalarFieldContainer[float]
    MorningNAV: float
    PositionAggregations: AdvancedAggregations
    DayPnL: float
    DayPnL_Utilization: float
    def __init__(self, ProductGroupId: _Optional[str] = ..., ClassGroups: _Optional[_Iterable[_Union[ClassGroup, _Mapping]]] = ..., NAV: _Optional[float] = ..., Minimum: _Optional[float] = ..., RiskCharge: _Optional[float] = ..., GainsAndLosses: _Optional[_Iterable[float]] = ..., AppliedOffsetPercent: _Optional[float] = ..., Requirement: _Optional[float] = ..., ConcentrationPercentage: _Optional[float] = ..., ConcentrationToNetLiq: _Optional[float] = ..., ScenariosPercentages: _Optional[_Iterable[float]] = ..., AppliedIVShockValues: _Optional[_Iterable[float]] = ..., MorningNAV: _Optional[float] = ..., PositionAggregations: _Optional[_Union[AdvancedAggregations, _Mapping]] = ..., DayPnL: _Optional[float] = ..., DayPnL_Utilization: _Optional[float] = ...) -> None: ...

class VolatilityShockResult(_message.Message):
    __slots__ = ("GainsAndLossesScenarios", "ShockPercentages", "TimeToExpirationFactors", "ImpliedVolatility", "Vega", "ShockValues", "Prices")
    GAINSANDLOSSESSCENARIOS_FIELD_NUMBER: _ClassVar[int]
    SHOCKPERCENTAGES_FIELD_NUMBER: _ClassVar[int]
    TIMETOEXPIRATIONFACTORS_FIELD_NUMBER: _ClassVar[int]
    IMPLIEDVOLATILITY_FIELD_NUMBER: _ClassVar[int]
    VEGA_FIELD_NUMBER: _ClassVar[int]
    SHOCKVALUES_FIELD_NUMBER: _ClassVar[int]
    PRICES_FIELD_NUMBER: _ClassVar[int]
    GainsAndLossesScenarios: _containers.RepeatedScalarFieldContainer[float]
    ShockPercentages: _containers.RepeatedScalarFieldContainer[float]
    TimeToExpirationFactors: _containers.RepeatedScalarFieldContainer[float]
    ImpliedVolatility: float
    Vega: float
    ShockValues: _containers.RepeatedScalarFieldContainer[float]
    Prices: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, GainsAndLossesScenarios: _Optional[_Iterable[float]] = ..., ShockPercentages: _Optional[_Iterable[float]] = ..., TimeToExpirationFactors: _Optional[_Iterable[float]] = ..., ImpliedVolatility: _Optional[float] = ..., Vega: _Optional[float] = ..., ShockValues: _Optional[_Iterable[float]] = ..., Prices: _Optional[_Iterable[float]] = ...) -> None: ...

class ProductGreeks(_message.Message):
    __slots__ = ("Delta", "Vega", "ImpliedVolatility", "Theta", "Gamma")
    DELTA_FIELD_NUMBER: _ClassVar[int]
    VEGA_FIELD_NUMBER: _ClassVar[int]
    IMPLIEDVOLATILITY_FIELD_NUMBER: _ClassVar[int]
    THETA_FIELD_NUMBER: _ClassVar[int]
    GAMMA_FIELD_NUMBER: _ClassVar[int]
    Delta: float
    Vega: float
    ImpliedVolatility: float
    Theta: float
    Gamma: float
    def __init__(self, Delta: _Optional[float] = ..., Vega: _Optional[float] = ..., ImpliedVolatility: _Optional[float] = ..., Theta: _Optional[float] = ..., Gamma: _Optional[float] = ...) -> None: ...

class AdvancedAggregations(_message.Message):
    __slots__ = ("LongMarketValue", "ShortMarketValue", "DeltaLongExposure", "DeltaShortExposure", "DeltaLongCount", "DeltaShortCount", "VegaExposure", "ThetaExposure", "GammaExposure")
    LONGMARKETVALUE_FIELD_NUMBER: _ClassVar[int]
    SHORTMARKETVALUE_FIELD_NUMBER: _ClassVar[int]
    DELTALONGEXPOSURE_FIELD_NUMBER: _ClassVar[int]
    DELTASHORTEXPOSURE_FIELD_NUMBER: _ClassVar[int]
    DELTALONGCOUNT_FIELD_NUMBER: _ClassVar[int]
    DELTASHORTCOUNT_FIELD_NUMBER: _ClassVar[int]
    VEGAEXPOSURE_FIELD_NUMBER: _ClassVar[int]
    THETAEXPOSURE_FIELD_NUMBER: _ClassVar[int]
    GAMMAEXPOSURE_FIELD_NUMBER: _ClassVar[int]
    LongMarketValue: float
    ShortMarketValue: float
    DeltaLongExposure: float
    DeltaShortExposure: float
    DeltaLongCount: float
    DeltaShortCount: float
    VegaExposure: float
    ThetaExposure: float
    GammaExposure: float
    def __init__(self, LongMarketValue: _Optional[float] = ..., ShortMarketValue: _Optional[float] = ..., DeltaLongExposure: _Optional[float] = ..., DeltaShortExposure: _Optional[float] = ..., DeltaLongCount: _Optional[float] = ..., DeltaShortCount: _Optional[float] = ..., VegaExposure: _Optional[float] = ..., ThetaExposure: _Optional[float] = ..., GammaExposure: _Optional[float] = ...) -> None: ...

class ProductWhatIfAdjustment(_message.Message):
    __slots__ = ("ChangeInCash", "ChangeInQuantity")
    CHANGEINCASH_FIELD_NUMBER: _ClassVar[int]
    CHANGEINQUANTITY_FIELD_NUMBER: _ClassVar[int]
    ChangeInCash: float
    ChangeInQuantity: float
    def __init__(self, ChangeInCash: _Optional[float] = ..., ChangeInQuantity: _Optional[float] = ...) -> None: ...
