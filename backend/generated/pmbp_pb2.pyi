import common_pb2 as _common_pb2
import pmbp_groups_pb2 as _pmbp_groups_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PmBpResponse(_message.Message):
    __slots__ = ("Status", "PmBpValuesResponses", "PmBpForProposedOrderResponses", "Version")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PMBPVALUESRESPONSES_FIELD_NUMBER: _ClassVar[int]
    PMBPFORPROPOSEDORDERRESPONSES_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    Status: str
    PmBpValuesResponses: _containers.RepeatedCompositeFieldContainer[PmBpValuesResponse]
    PmBpForProposedOrderResponses: _containers.RepeatedCompositeFieldContainer[PmBpForProposedOrderResponse]
    Version: str
    def __init__(self, Status: _Optional[str] = ..., PmBpValuesResponses: _Optional[_Iterable[_Union[PmBpValuesResponse, _Mapping]]] = ..., PmBpForProposedOrderResponses: _Optional[_Iterable[_Union[PmBpForProposedOrderResponse, _Mapping]]] = ..., Version: _Optional[str] = ...) -> None: ...

class PmBpForProposedOrderResponse(_message.Message):
    __slots__ = ("PmBpValuesWithoutProposedLots", "PmBpValuesWithProposedLots", "AccountId", "AccountNumber", "AccountName", "SubaccountsPmBpForProposedOrderResponses", "MetaInfo", "Errors", "Warnings")
    class SubaccountsPmBpForProposedOrderResponsesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: PmBpForProposedOrderResponse
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[PmBpForProposedOrderResponse, _Mapping]] = ...) -> None: ...
    PMBPVALUESWITHOUTPROPOSEDLOTS_FIELD_NUMBER: _ClassVar[int]
    PMBPVALUESWITHPROPOSEDLOTS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTNUMBER_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTNAME_FIELD_NUMBER: _ClassVar[int]
    SUBACCOUNTSPMBPFORPROPOSEDORDERRESPONSES_FIELD_NUMBER: _ClassVar[int]
    METAINFO_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    PmBpValuesWithoutProposedLots: PmBpValues
    PmBpValuesWithProposedLots: PmBpValues
    AccountId: str
    AccountNumber: str
    AccountName: str
    SubaccountsPmBpForProposedOrderResponses: _containers.MessageMap[int, PmBpForProposedOrderResponse]
    MetaInfo: PmBpMetaInfo
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    def __init__(self, PmBpValuesWithoutProposedLots: _Optional[_Union[PmBpValues, _Mapping]] = ..., PmBpValuesWithProposedLots: _Optional[_Union[PmBpValues, _Mapping]] = ..., AccountId: _Optional[str] = ..., AccountNumber: _Optional[str] = ..., AccountName: _Optional[str] = ..., SubaccountsPmBpForProposedOrderResponses: _Optional[_Mapping[int, PmBpForProposedOrderResponse]] = ..., MetaInfo: _Optional[_Union[PmBpMetaInfo, _Mapping]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ...) -> None: ...

class PmBpValuesResponse(_message.Message):
    __slots__ = ("PmBpValues", "AccountId", "AccountNumber", "AccountName", "SubaccountsPmBpValuesResponses", "MetaInfo", "Errors", "Warnings")
    class SubaccountsPmBpValuesResponsesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: PmBpValuesResponse
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[PmBpValuesResponse, _Mapping]] = ...) -> None: ...
    PMBPVALUES_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTNUMBER_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTNAME_FIELD_NUMBER: _ClassVar[int]
    SUBACCOUNTSPMBPVALUESRESPONSES_FIELD_NUMBER: _ClassVar[int]
    METAINFO_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    PmBpValues: PmBpValues
    AccountId: str
    AccountNumber: str
    AccountName: str
    SubaccountsPmBpValuesResponses: _containers.MessageMap[int, PmBpValuesResponse]
    MetaInfo: PmBpMetaInfo
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    def __init__(self, PmBpValues: _Optional[_Union[PmBpValues, _Mapping]] = ..., AccountId: _Optional[str] = ..., AccountNumber: _Optional[str] = ..., AccountName: _Optional[str] = ..., SubaccountsPmBpValuesResponses: _Optional[_Mapping[int, PmBpValuesResponse]] = ..., MetaInfo: _Optional[_Union[PmBpMetaInfo, _Mapping]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ...) -> None: ...

class PmBpValues(_message.Message):
    __slots__ = ("Groupings", "NAV", "Requirement", "Cash", "CreditLimit", "AdvancedValues", "BuyingPower", "PendingTransaction", "PendingDebitTransaction", "NetLiquidity", "ValueAtRiskResult", "GainsAndLosses", "MorningNAV", "CreditUtilization", "DayPnL", "DayPnL_Utilization", "ScenarioOutputs", "ExcessLiquidity", "PositionAggregations")
    GROUPINGS_FIELD_NUMBER: _ClassVar[int]
    NAV_FIELD_NUMBER: _ClassVar[int]
    REQUIREMENT_FIELD_NUMBER: _ClassVar[int]
    CASH_FIELD_NUMBER: _ClassVar[int]
    CREDITLIMIT_FIELD_NUMBER: _ClassVar[int]
    ADVANCEDVALUES_FIELD_NUMBER: _ClassVar[int]
    BUYINGPOWER_FIELD_NUMBER: _ClassVar[int]
    PENDINGTRANSACTION_FIELD_NUMBER: _ClassVar[int]
    PENDINGDEBITTRANSACTION_FIELD_NUMBER: _ClassVar[int]
    NETLIQUIDITY_FIELD_NUMBER: _ClassVar[int]
    VALUEATRISKRESULT_FIELD_NUMBER: _ClassVar[int]
    GAINSANDLOSSES_FIELD_NUMBER: _ClassVar[int]
    MORNINGNAV_FIELD_NUMBER: _ClassVar[int]
    CREDITUTILIZATION_FIELD_NUMBER: _ClassVar[int]
    DAYPNL_FIELD_NUMBER: _ClassVar[int]
    DAYPNL_UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    SCENARIOOUTPUTS_FIELD_NUMBER: _ClassVar[int]
    EXCESSLIQUIDITY_FIELD_NUMBER: _ClassVar[int]
    POSITIONAGGREGATIONS_FIELD_NUMBER: _ClassVar[int]
    Groupings: _pmbp_groups_pb2.Groupings
    NAV: float
    Requirement: float
    Cash: float
    CreditLimit: float
    AdvancedValues: AdvancedValues
    BuyingPower: float
    PendingTransaction: float
    PendingDebitTransaction: float
    NetLiquidity: float
    ValueAtRiskResult: ValueAtRiskResult
    GainsAndLosses: _containers.RepeatedScalarFieldContainer[float]
    MorningNAV: float
    CreditUtilization: float
    DayPnL: float
    DayPnL_Utilization: float
    ScenarioOutputs: _containers.RepeatedCompositeFieldContainer[PmBpScenarioOutput]
    ExcessLiquidity: float
    PositionAggregations: _pmbp_groups_pb2.AdvancedAggregations
    def __init__(self, Groupings: _Optional[_Union[_pmbp_groups_pb2.Groupings, _Mapping]] = ..., NAV: _Optional[float] = ..., Requirement: _Optional[float] = ..., Cash: _Optional[float] = ..., CreditLimit: _Optional[float] = ..., AdvancedValues: _Optional[_Union[AdvancedValues, _Mapping]] = ..., BuyingPower: _Optional[float] = ..., PendingTransaction: _Optional[float] = ..., PendingDebitTransaction: _Optional[float] = ..., NetLiquidity: _Optional[float] = ..., ValueAtRiskResult: _Optional[_Union[ValueAtRiskResult, _Mapping]] = ..., GainsAndLosses: _Optional[_Iterable[float]] = ..., MorningNAV: _Optional[float] = ..., CreditUtilization: _Optional[float] = ..., DayPnL: _Optional[float] = ..., DayPnL_Utilization: _Optional[float] = ..., ScenarioOutputs: _Optional[_Iterable[_Union[PmBpScenarioOutput, _Mapping]]] = ..., ExcessLiquidity: _Optional[float] = ..., PositionAggregations: _Optional[_Union[_pmbp_groups_pb2.AdvancedAggregations, _Mapping]] = ...) -> None: ...

class PmBpScenarioOutput(_message.Message):
    __slots__ = ("ScenarioIndex", "ScenarioDescription", "RiskProfileId")
    SCENARIOINDEX_FIELD_NUMBER: _ClassVar[int]
    SCENARIODESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    RISKPROFILEID_FIELD_NUMBER: _ClassVar[int]
    ScenarioIndex: int
    ScenarioDescription: str
    RiskProfileId: int
    def __init__(self, ScenarioIndex: _Optional[int] = ..., ScenarioDescription: _Optional[str] = ..., RiskProfileId: _Optional[int] = ...) -> None: ...

class AdvancedValues(_message.Message):
    __slots__ = ("ClassGroupsPortfolios", "ValueAtRiskResults", "EngineConfigValues", "AppliedIVShockValues")
    CLASSGROUPSPORTFOLIOS_FIELD_NUMBER: _ClassVar[int]
    VALUEATRISKRESULTS_FIELD_NUMBER: _ClassVar[int]
    ENGINECONFIGVALUES_FIELD_NUMBER: _ClassVar[int]
    APPLIEDIVSHOCKVALUES_FIELD_NUMBER: _ClassVar[int]
    ClassGroupsPortfolios: _containers.RepeatedCompositeFieldContainer[_pmbp_groups_pb2.ClassGroup]
    ValueAtRiskResults: _containers.RepeatedCompositeFieldContainer[ValueAtRiskResult]
    EngineConfigValues: _containers.RepeatedScalarFieldContainer[str]
    AppliedIVShockValues: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, ClassGroupsPortfolios: _Optional[_Iterable[_Union[_pmbp_groups_pb2.ClassGroup, _Mapping]]] = ..., ValueAtRiskResults: _Optional[_Iterable[_Union[ValueAtRiskResult, _Mapping]]] = ..., EngineConfigValues: _Optional[_Iterable[str]] = ..., AppliedIVShockValues: _Optional[_Iterable[float]] = ...) -> None: ...

class ValueAtRiskResult(_message.Message):
    __slots__ = ("ValueAtRisk", "InputDate")
    VALUEATRISK_FIELD_NUMBER: _ClassVar[int]
    INPUTDATE_FIELD_NUMBER: _ClassVar[int]
    ValueAtRisk: float
    InputDate: str
    def __init__(self, ValueAtRisk: _Optional[float] = ..., InputDate: _Optional[str] = ...) -> None: ...

class PmBpStressTestInput(_message.Message):
    __slots__ = ("UnderlyingPriceShockInputs", "VolatilityShockInputs", "MOVEShockInputs", "MOVECreditSpreadShockInputs", "YieldShockInputs", "PmBpRiskProfiles")
    UNDERLYINGPRICESHOCKINPUTS_FIELD_NUMBER: _ClassVar[int]
    VOLATILITYSHOCKINPUTS_FIELD_NUMBER: _ClassVar[int]
    MOVESHOCKINPUTS_FIELD_NUMBER: _ClassVar[int]
    MOVECREDITSPREADSHOCKINPUTS_FIELD_NUMBER: _ClassVar[int]
    YIELDSHOCKINPUTS_FIELD_NUMBER: _ClassVar[int]
    PMBPRISKPROFILES_FIELD_NUMBER: _ClassVar[int]
    UnderlyingPriceShockInputs: _containers.RepeatedCompositeFieldContainer[PmBpUnderlyingPriceShockInput]
    VolatilityShockInputs: _containers.RepeatedCompositeFieldContainer[PmBpVolatilityShockInput]
    MOVEShockInputs: _containers.RepeatedCompositeFieldContainer[_common_pb2.MOVEShockInput]
    MOVECreditSpreadShockInputs: _containers.RepeatedCompositeFieldContainer[_common_pb2.MOVECreditSpreadShockInput]
    YieldShockInputs: _containers.RepeatedCompositeFieldContainer[_common_pb2.YieldShockInput]
    PmBpRiskProfiles: _containers.RepeatedCompositeFieldContainer[PmBpRiskProfile]
    def __init__(self, UnderlyingPriceShockInputs: _Optional[_Iterable[_Union[PmBpUnderlyingPriceShockInput, _Mapping]]] = ..., VolatilityShockInputs: _Optional[_Iterable[_Union[PmBpVolatilityShockInput, _Mapping]]] = ..., MOVEShockInputs: _Optional[_Iterable[_Union[_common_pb2.MOVEShockInput, _Mapping]]] = ..., MOVECreditSpreadShockInputs: _Optional[_Iterable[_Union[_common_pb2.MOVECreditSpreadShockInput, _Mapping]]] = ..., YieldShockInputs: _Optional[_Iterable[_Union[_common_pb2.YieldShockInput, _Mapping]]] = ..., PmBpRiskProfiles: _Optional[_Iterable[_Union[PmBpRiskProfile, _Mapping]]] = ...) -> None: ...

class PmBpRiskProfile(_message.Message):
    __slots__ = ("RiskProfileId", "Name", "Scenarios", "IncludeOpenOrders")
    RISKPROFILEID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SCENARIOS_FIELD_NUMBER: _ClassVar[int]
    INCLUDEOPENORDERS_FIELD_NUMBER: _ClassVar[int]
    RiskProfileId: int
    Name: str
    Scenarios: _containers.RepeatedCompositeFieldContainer[PmBpScenario]
    IncludeOpenOrders: bool
    def __init__(self, RiskProfileId: _Optional[int] = ..., Name: _Optional[str] = ..., Scenarios: _Optional[_Iterable[_Union[PmBpScenario, _Mapping]]] = ..., IncludeOpenOrders: bool = ...) -> None: ...

class PmBpScenario(_message.Message):
    __slots__ = ("UnderlyingPriceShockInputs", "VolatilityShockInputs", "MOVEShockInputs", "MOVECreditSpreadShockInputs", "YieldShockInputs")
    UNDERLYINGPRICESHOCKINPUTS_FIELD_NUMBER: _ClassVar[int]
    VOLATILITYSHOCKINPUTS_FIELD_NUMBER: _ClassVar[int]
    MOVESHOCKINPUTS_FIELD_NUMBER: _ClassVar[int]
    MOVECREDITSPREADSHOCKINPUTS_FIELD_NUMBER: _ClassVar[int]
    YIELDSHOCKINPUTS_FIELD_NUMBER: _ClassVar[int]
    UnderlyingPriceShockInputs: _containers.RepeatedCompositeFieldContainer[PmBpUnderlyingPriceShockInput]
    VolatilityShockInputs: _containers.RepeatedCompositeFieldContainer[PmBpVolatilityShockInput]
    MOVEShockInputs: _containers.RepeatedCompositeFieldContainer[_common_pb2.MOVEShockInput]
    MOVECreditSpreadShockInputs: _containers.RepeatedCompositeFieldContainer[_common_pb2.MOVECreditSpreadShockInput]
    YieldShockInputs: _containers.RepeatedCompositeFieldContainer[_common_pb2.YieldShockInput]
    def __init__(self, UnderlyingPriceShockInputs: _Optional[_Iterable[_Union[PmBpUnderlyingPriceShockInput, _Mapping]]] = ..., VolatilityShockInputs: _Optional[_Iterable[_Union[PmBpVolatilityShockInput, _Mapping]]] = ..., MOVEShockInputs: _Optional[_Iterable[_Union[_common_pb2.MOVEShockInput, _Mapping]]] = ..., MOVECreditSpreadShockInputs: _Optional[_Iterable[_Union[_common_pb2.MOVECreditSpreadShockInput, _Mapping]]] = ..., YieldShockInputs: _Optional[_Iterable[_Union[_common_pb2.YieldShockInput, _Mapping]]] = ...) -> None: ...

class PmBpUnderlyingPriceShockInput(_message.Message):
    __slots__ = ("ApplyAcrossPortfolio", "ProductGroupId", "ClassGroupId", "UnderlyingSymbol", "BasketId", "PercentDown", "PercentUp")
    APPLYACROSSPORTFOLIO_FIELD_NUMBER: _ClassVar[int]
    PRODUCTGROUPID_FIELD_NUMBER: _ClassVar[int]
    CLASSGROUPID_FIELD_NUMBER: _ClassVar[int]
    UNDERLYINGSYMBOL_FIELD_NUMBER: _ClassVar[int]
    BASKETID_FIELD_NUMBER: _ClassVar[int]
    PERCENTDOWN_FIELD_NUMBER: _ClassVar[int]
    PERCENTUP_FIELD_NUMBER: _ClassVar[int]
    ApplyAcrossPortfolio: bool
    ProductGroupId: str
    ClassGroupId: str
    UnderlyingSymbol: str
    BasketId: str
    PercentDown: float
    PercentUp: float
    def __init__(self, ApplyAcrossPortfolio: bool = ..., ProductGroupId: _Optional[str] = ..., ClassGroupId: _Optional[str] = ..., UnderlyingSymbol: _Optional[str] = ..., BasketId: _Optional[str] = ..., PercentDown: _Optional[float] = ..., PercentUp: _Optional[float] = ...) -> None: ...

class PmBpVolatilityShockInput(_message.Message):
    __slots__ = ("ApplyAcrossPortfolio", "ProductGroupId", "UnderlyingSymbol", "ApplyTimeToExpirationFactor", "PercentDown", "PercentUp")
    APPLYACROSSPORTFOLIO_FIELD_NUMBER: _ClassVar[int]
    PRODUCTGROUPID_FIELD_NUMBER: _ClassVar[int]
    UNDERLYINGSYMBOL_FIELD_NUMBER: _ClassVar[int]
    APPLYTIMETOEXPIRATIONFACTOR_FIELD_NUMBER: _ClassVar[int]
    PERCENTDOWN_FIELD_NUMBER: _ClassVar[int]
    PERCENTUP_FIELD_NUMBER: _ClassVar[int]
    ApplyAcrossPortfolio: bool
    ProductGroupId: str
    UnderlyingSymbol: str
    ApplyTimeToExpirationFactor: int
    PercentDown: float
    PercentUp: float
    def __init__(self, ApplyAcrossPortfolio: bool = ..., ProductGroupId: _Optional[str] = ..., UnderlyingSymbol: _Optional[str] = ..., ApplyTimeToExpirationFactor: _Optional[int] = ..., PercentDown: _Optional[float] = ..., PercentUp: _Optional[float] = ...) -> None: ...

class PmBpMetaInfo(_message.Message):
    __slots__ = ("OCCTPBizDate", "ElapsedTimeInMs")
    OCCTPBIZDATE_FIELD_NUMBER: _ClassVar[int]
    ELAPSEDTIMEINMS_FIELD_NUMBER: _ClassVar[int]
    OCCTPBizDate: str
    ElapsedTimeInMs: float
    def __init__(self, OCCTPBizDate: _Optional[str] = ..., ElapsedTimeInMs: _Optional[float] = ...) -> None: ...

class PMAccountWhatIfAdjustment(_message.Message):
    __slots__ = ("AccountNumber", "PMWhatIfAdjustedProducts")
    ACCOUNTNUMBER_FIELD_NUMBER: _ClassVar[int]
    PMWHATIFADJUSTEDPRODUCTS_FIELD_NUMBER: _ClassVar[int]
    AccountNumber: str
    PMWhatIfAdjustedProducts: _containers.RepeatedCompositeFieldContainer[PMWhatIfAdjustedProduct]
    def __init__(self, AccountNumber: _Optional[str] = ..., PMWhatIfAdjustedProducts: _Optional[_Iterable[_Union[PMWhatIfAdjustedProduct, _Mapping]]] = ...) -> None: ...

class PMWhatIfAdjustedProduct(_message.Message):
    __slots__ = ("ProductId", "Symbol", "NoCashImpact", "Quantity", "Price", "UnderlyingPrice")
    PRODUCTID_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    NOCASHIMPACT_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    UNDERLYINGPRICE_FIELD_NUMBER: _ClassVar[int]
    ProductId: str
    Symbol: str
    NoCashImpact: bool
    Quantity: float
    Price: float
    UnderlyingPrice: float
    def __init__(self, ProductId: _Optional[str] = ..., Symbol: _Optional[str] = ..., NoCashImpact: bool = ..., Quantity: _Optional[float] = ..., Price: _Optional[float] = ..., UnderlyingPrice: _Optional[float] = ...) -> None: ...
