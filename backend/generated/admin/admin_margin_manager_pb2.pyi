import common_pb2 as _common_pb2
import accounts_pb2 as _accounts_pb2
import common_pb2 as _common_pb2_1
import bp_pb2 as _bp_pb2
import pmbp_pb2 as _pmbp_pb2
import bp_enums_pb2 as _bp_enums_pb2
import search_pb2 as _search_pb2
import common_enums_pb2 as _common_enums_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MarginManagerRequest(_message.Message):
    __slots__ = ("MarginManagerStrategyRequest", "MarginManagerPortfolioRequest")
    MARGINMANAGERSTRATEGYREQUEST_FIELD_NUMBER: _ClassVar[int]
    MARGINMANAGERPORTFOLIOREQUEST_FIELD_NUMBER: _ClassVar[int]
    MarginManagerStrategyRequest: MarginManagerStrategyRequest
    MarginManagerPortfolioRequest: MarginManagerPortfolioRequest
    def __init__(self, MarginManagerStrategyRequest: _Optional[_Union[MarginManagerStrategyRequest, _Mapping]] = ..., MarginManagerPortfolioRequest: _Optional[_Union[MarginManagerPortfolioRequest, _Mapping]] = ...) -> None: ...

class MarginManagerStrategyRequest(_message.Message):
    __slots__ = ("AccountIDs", "AccountNumbers", "ExtraPositionsInOCCStyleCSVs", "StressTestInput", "NumberOfScenarios", "UnderlyingPriceShockPercentDown", "UnderlyingPriceShockPercentUp", "VolatilityShockPercentage", "VolatilityShockDirection", "ApplyTimeToExpirationFactor", "IncludeOrders", "StressTestCalculationsOptimizationLevel", "AppliedRiskProfileIds", "LotsAggregatorAlgo", "BpAccountWhatIfAdjustments", "AccountGroupIds", "FetchAllAccounts", "SearchCriteria")
    ACCOUNTIDS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTNUMBERS_FIELD_NUMBER: _ClassVar[int]
    EXTRAPOSITIONSINOCCSTYLECSVS_FIELD_NUMBER: _ClassVar[int]
    STRESSTESTINPUT_FIELD_NUMBER: _ClassVar[int]
    NUMBEROFSCENARIOS_FIELD_NUMBER: _ClassVar[int]
    UNDERLYINGPRICESHOCKPERCENTDOWN_FIELD_NUMBER: _ClassVar[int]
    UNDERLYINGPRICESHOCKPERCENTUP_FIELD_NUMBER: _ClassVar[int]
    VOLATILITYSHOCKPERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    VOLATILITYSHOCKDIRECTION_FIELD_NUMBER: _ClassVar[int]
    APPLYTIMETOEXPIRATIONFACTOR_FIELD_NUMBER: _ClassVar[int]
    INCLUDEORDERS_FIELD_NUMBER: _ClassVar[int]
    STRESSTESTCALCULATIONSOPTIMIZATIONLEVEL_FIELD_NUMBER: _ClassVar[int]
    APPLIEDRISKPROFILEIDS_FIELD_NUMBER: _ClassVar[int]
    LOTSAGGREGATORALGO_FIELD_NUMBER: _ClassVar[int]
    BPACCOUNTWHATIFADJUSTMENTS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTGROUPIDS_FIELD_NUMBER: _ClassVar[int]
    FETCHALLACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    SEARCHCRITERIA_FIELD_NUMBER: _ClassVar[int]
    AccountIDs: _containers.RepeatedScalarFieldContainer[int]
    AccountNumbers: _containers.RepeatedScalarFieldContainer[str]
    ExtraPositionsInOCCStyleCSVs: _containers.RepeatedCompositeFieldContainer[ExtraPositionsInOCCStyleCSV]
    StressTestInput: _bp_pb2.BpStressTestInput
    NumberOfScenarios: int
    UnderlyingPriceShockPercentDown: float
    UnderlyingPriceShockPercentUp: float
    VolatilityShockPercentage: float
    VolatilityShockDirection: int
    ApplyTimeToExpirationFactor: int
    IncludeOrders: bool
    StressTestCalculationsOptimizationLevel: _bp_enums_pb2.EnumStressTestCalculationsOptimizationLevel
    AppliedRiskProfileIds: _containers.RepeatedScalarFieldContainer[int]
    LotsAggregatorAlgo: int
    BpAccountWhatIfAdjustments: _containers.RepeatedCompositeFieldContainer[_bp_pb2.BpAccountWhatIfAdjustment]
    AccountGroupIds: _containers.RepeatedScalarFieldContainer[int]
    FetchAllAccounts: bool
    SearchCriteria: _search_pb2.SearchCriteria
    def __init__(self, AccountIDs: _Optional[_Iterable[int]] = ..., AccountNumbers: _Optional[_Iterable[str]] = ..., ExtraPositionsInOCCStyleCSVs: _Optional[_Iterable[_Union[ExtraPositionsInOCCStyleCSV, _Mapping]]] = ..., StressTestInput: _Optional[_Union[_bp_pb2.BpStressTestInput, _Mapping]] = ..., NumberOfScenarios: _Optional[int] = ..., UnderlyingPriceShockPercentDown: _Optional[float] = ..., UnderlyingPriceShockPercentUp: _Optional[float] = ..., VolatilityShockPercentage: _Optional[float] = ..., VolatilityShockDirection: _Optional[int] = ..., ApplyTimeToExpirationFactor: _Optional[int] = ..., IncludeOrders: bool = ..., StressTestCalculationsOptimizationLevel: _Optional[_Union[_bp_enums_pb2.EnumStressTestCalculationsOptimizationLevel, str]] = ..., AppliedRiskProfileIds: _Optional[_Iterable[int]] = ..., LotsAggregatorAlgo: _Optional[int] = ..., BpAccountWhatIfAdjustments: _Optional[_Iterable[_Union[_bp_pb2.BpAccountWhatIfAdjustment, _Mapping]]] = ..., AccountGroupIds: _Optional[_Iterable[int]] = ..., FetchAllAccounts: bool = ..., SearchCriteria: _Optional[_Union[_search_pb2.SearchCriteria, _Mapping]] = ...) -> None: ...

class MarginManagerPortfolioRequest(_message.Message):
    __slots__ = ("AccountIDs", "AccountNumbers", "NumberOfScenarios", "UnderlyingPriceShockPercentDown", "UnderlyingPriceShockPercentUp", "VolatilityShockPercentage", "VolatilityShockDirection", "ApplyTimeToExpirationFactor", "ReturnOccStyleReportForPM", "ReturnOccStyleInputForPM", "ExtraPositionsInOCCStyleCSVs", "StressTestInput", "FetchAllAccounts", "IncludeOrders", "OptionPricingModel", "AppliedRiskProfileIds", "LotsAggregatorAlgo", "PMAccountWhatIfAdjustments", "AccountGroupIds", "RequirementAddOns", "SearchCriteria")
    ACCOUNTIDS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTNUMBERS_FIELD_NUMBER: _ClassVar[int]
    NUMBEROFSCENARIOS_FIELD_NUMBER: _ClassVar[int]
    UNDERLYINGPRICESHOCKPERCENTDOWN_FIELD_NUMBER: _ClassVar[int]
    UNDERLYINGPRICESHOCKPERCENTUP_FIELD_NUMBER: _ClassVar[int]
    VOLATILITYSHOCKPERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    VOLATILITYSHOCKDIRECTION_FIELD_NUMBER: _ClassVar[int]
    APPLYTIMETOEXPIRATIONFACTOR_FIELD_NUMBER: _ClassVar[int]
    RETURNOCCSTYLEREPORTFORPM_FIELD_NUMBER: _ClassVar[int]
    RETURNOCCSTYLEINPUTFORPM_FIELD_NUMBER: _ClassVar[int]
    EXTRAPOSITIONSINOCCSTYLECSVS_FIELD_NUMBER: _ClassVar[int]
    STRESSTESTINPUT_FIELD_NUMBER: _ClassVar[int]
    FETCHALLACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    INCLUDEORDERS_FIELD_NUMBER: _ClassVar[int]
    OPTIONPRICINGMODEL_FIELD_NUMBER: _ClassVar[int]
    APPLIEDRISKPROFILEIDS_FIELD_NUMBER: _ClassVar[int]
    LOTSAGGREGATORALGO_FIELD_NUMBER: _ClassVar[int]
    PMACCOUNTWHATIFADJUSTMENTS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTGROUPIDS_FIELD_NUMBER: _ClassVar[int]
    REQUIREMENTADDONS_FIELD_NUMBER: _ClassVar[int]
    SEARCHCRITERIA_FIELD_NUMBER: _ClassVar[int]
    AccountIDs: _containers.RepeatedScalarFieldContainer[int]
    AccountNumbers: _containers.RepeatedScalarFieldContainer[str]
    NumberOfScenarios: int
    UnderlyingPriceShockPercentDown: float
    UnderlyingPriceShockPercentUp: float
    VolatilityShockPercentage: float
    VolatilityShockDirection: int
    ApplyTimeToExpirationFactor: int
    ReturnOccStyleReportForPM: bool
    ReturnOccStyleInputForPM: bool
    ExtraPositionsInOCCStyleCSVs: _containers.RepeatedCompositeFieldContainer[ExtraPositionsInOCCStyleCSV]
    StressTestInput: _pmbp_pb2.PmBpStressTestInput
    FetchAllAccounts: bool
    IncludeOrders: bool
    OptionPricingModel: int
    AppliedRiskProfileIds: _containers.RepeatedScalarFieldContainer[int]
    LotsAggregatorAlgo: int
    PMAccountWhatIfAdjustments: _containers.RepeatedCompositeFieldContainer[_pmbp_pb2.PMAccountWhatIfAdjustment]
    AccountGroupIds: _containers.RepeatedScalarFieldContainer[int]
    RequirementAddOns: RequirementAddOns
    SearchCriteria: _search_pb2.SearchCriteria
    def __init__(self, AccountIDs: _Optional[_Iterable[int]] = ..., AccountNumbers: _Optional[_Iterable[str]] = ..., NumberOfScenarios: _Optional[int] = ..., UnderlyingPriceShockPercentDown: _Optional[float] = ..., UnderlyingPriceShockPercentUp: _Optional[float] = ..., VolatilityShockPercentage: _Optional[float] = ..., VolatilityShockDirection: _Optional[int] = ..., ApplyTimeToExpirationFactor: _Optional[int] = ..., ReturnOccStyleReportForPM: bool = ..., ReturnOccStyleInputForPM: bool = ..., ExtraPositionsInOCCStyleCSVs: _Optional[_Iterable[_Union[ExtraPositionsInOCCStyleCSV, _Mapping]]] = ..., StressTestInput: _Optional[_Union[_pmbp_pb2.PmBpStressTestInput, _Mapping]] = ..., FetchAllAccounts: bool = ..., IncludeOrders: bool = ..., OptionPricingModel: _Optional[int] = ..., AppliedRiskProfileIds: _Optional[_Iterable[int]] = ..., LotsAggregatorAlgo: _Optional[int] = ..., PMAccountWhatIfAdjustments: _Optional[_Iterable[_Union[_pmbp_pb2.PMAccountWhatIfAdjustment, _Mapping]]] = ..., AccountGroupIds: _Optional[_Iterable[int]] = ..., RequirementAddOns: _Optional[_Union[RequirementAddOns, _Mapping]] = ..., SearchCriteria: _Optional[_Union[_search_pb2.SearchCriteria, _Mapping]] = ...) -> None: ...

class RequirementAddOns(_message.Message):
    __slots__ = ("ApplyLowPricedStocksAddOn", "ApplyConcentrationAddOn", "ApplyLiquidityAddOn")
    APPLYLOWPRICEDSTOCKSADDON_FIELD_NUMBER: _ClassVar[int]
    APPLYCONCENTRATIONADDON_FIELD_NUMBER: _ClassVar[int]
    APPLYLIQUIDITYADDON_FIELD_NUMBER: _ClassVar[int]
    ApplyLowPricedStocksAddOn: bool
    ApplyConcentrationAddOn: bool
    ApplyLiquidityAddOn: bool
    def __init__(self, ApplyLowPricedStocksAddOn: bool = ..., ApplyConcentrationAddOn: bool = ..., ApplyLiquidityAddOn: bool = ...) -> None: ...

class PmAttributeUpdateRequest(_message.Message):
    __slots__ = ("PmAttributeUpdates",)
    PMATTRIBUTEUPDATES_FIELD_NUMBER: _ClassVar[int]
    PmAttributeUpdates: _containers.RepeatedCompositeFieldContainer[PmAttributeUpdate]
    def __init__(self, PmAttributeUpdates: _Optional[_Iterable[_Union[PmAttributeUpdate, _Mapping]]] = ...) -> None: ...

class PmAttributeUpdate(_message.Message):
    __slots__ = ("AccountId", "AccountNumber", "CreditLimit", "PMBPLeverageFactor", "Details")
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTNUMBER_FIELD_NUMBER: _ClassVar[int]
    CREDITLIMIT_FIELD_NUMBER: _ClassVar[int]
    PMBPLEVERAGEFACTOR_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    AccountId: int
    AccountNumber: str
    CreditLimit: PmAttributeDecimalValue
    PMBPLeverageFactor: PmAttributeDecimalValue
    Details: str
    def __init__(self, AccountId: _Optional[int] = ..., AccountNumber: _Optional[str] = ..., CreditLimit: _Optional[_Union[PmAttributeDecimalValue, _Mapping]] = ..., PMBPLeverageFactor: _Optional[_Union[PmAttributeDecimalValue, _Mapping]] = ..., Details: _Optional[str] = ...) -> None: ...

class PmAttributeDecimalValue(_message.Message):
    __slots__ = ("Value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    Value: float
    def __init__(self, Value: _Optional[float] = ...) -> None: ...

class PmAttributeUpdateResponse(_message.Message):
    __slots__ = ("PmAttributeUpdateStatuses", "Warnings", "Errors")
    PMATTRIBUTEUPDATESTATUSES_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    PmAttributeUpdateStatuses: _containers.RepeatedCompositeFieldContainer[PmAttributeUpdateStatus]
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2_1.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2_1.ResponseError]
    def __init__(self, PmAttributeUpdateStatuses: _Optional[_Iterable[_Union[PmAttributeUpdateStatus, _Mapping]]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2_1.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2_1.ResponseError, _Mapping]]] = ...) -> None: ...

class PmAttributeUpdateStatus(_message.Message):
    __slots__ = ("AccountId", "AccountNumber", "IsSuccess")
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTNUMBER_FIELD_NUMBER: _ClassVar[int]
    ISSUCCESS_FIELD_NUMBER: _ClassVar[int]
    AccountId: int
    AccountNumber: str
    IsSuccess: bool
    def __init__(self, AccountId: _Optional[int] = ..., AccountNumber: _Optional[str] = ..., IsSuccess: bool = ...) -> None: ...

class MarginManagerResponse(_message.Message):
    __slots__ = ("MarginManagerInfo", "PmBpAggregatedGreeksSummary", "Warnings", "Errors", "SearchCriteria", "Page")
    class MarginManagerInfoEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: MarginManagerInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[MarginManagerInfo, _Mapping]] = ...) -> None: ...
    MARGINMANAGERINFO_FIELD_NUMBER: _ClassVar[int]
    PMBPAGGREGATEDGREEKSSUMMARY_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    SEARCHCRITERIA_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    MarginManagerInfo: _containers.MessageMap[int, MarginManagerInfo]
    PmBpAggregatedGreeksSummary: _containers.RepeatedScalarFieldContainer[str]
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2_1.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2_1.ResponseError]
    SearchCriteria: _search_pb2.SearchCriteria
    Page: _search_pb2.PageResponse
    def __init__(self, MarginManagerInfo: _Optional[_Mapping[int, MarginManagerInfo]] = ..., PmBpAggregatedGreeksSummary: _Optional[_Iterable[str]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2_1.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2_1.ResponseError, _Mapping]]] = ..., SearchCriteria: _Optional[_Union[_search_pb2.SearchCriteria, _Mapping]] = ..., Page: _Optional[_Union[_search_pb2.PageResponse, _Mapping]] = ...) -> None: ...

class MarginManagerInfo(_message.Message):
    __slots__ = ("AccountId", "AccountNumber", "BpValuesResponse", "PmBpValuesResponse", "YesterdayLiquidationValue", "Cash", "OccStyleReportForPM", "OccStyleInputForPM", "IsPMAccount", "AccountRiskType", "Alerts", "AlertLevel")
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTNUMBER_FIELD_NUMBER: _ClassVar[int]
    BPVALUESRESPONSE_FIELD_NUMBER: _ClassVar[int]
    PMBPVALUESRESPONSE_FIELD_NUMBER: _ClassVar[int]
    YESTERDAYLIQUIDATIONVALUE_FIELD_NUMBER: _ClassVar[int]
    CASH_FIELD_NUMBER: _ClassVar[int]
    OCCSTYLEREPORTFORPM_FIELD_NUMBER: _ClassVar[int]
    OCCSTYLEINPUTFORPM_FIELD_NUMBER: _ClassVar[int]
    ISPMACCOUNT_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTRISKTYPE_FIELD_NUMBER: _ClassVar[int]
    ALERTS_FIELD_NUMBER: _ClassVar[int]
    ALERTLEVEL_FIELD_NUMBER: _ClassVar[int]
    AccountId: int
    AccountNumber: str
    BpValuesResponse: _bp_pb2.BpValuesResponse
    PmBpValuesResponse: _pmbp_pb2.PmBpValuesResponse
    YesterdayLiquidationValue: float
    Cash: float
    OccStyleReportForPM: str
    OccStyleInputForPM: str
    IsPMAccount: bool
    AccountRiskType: _common_enums_pb2.EnumAccountRiskType
    Alerts: _containers.RepeatedCompositeFieldContainer[_common_pb2_1.ResponseWarning]
    AlertLevel: int
    def __init__(self, AccountId: _Optional[int] = ..., AccountNumber: _Optional[str] = ..., BpValuesResponse: _Optional[_Union[_bp_pb2.BpValuesResponse, _Mapping]] = ..., PmBpValuesResponse: _Optional[_Union[_pmbp_pb2.PmBpValuesResponse, _Mapping]] = ..., YesterdayLiquidationValue: _Optional[float] = ..., Cash: _Optional[float] = ..., OccStyleReportForPM: _Optional[str] = ..., OccStyleInputForPM: _Optional[str] = ..., IsPMAccount: bool = ..., AccountRiskType: _Optional[_Union[_common_enums_pb2.EnumAccountRiskType, str]] = ..., Alerts: _Optional[_Iterable[_Union[_common_pb2_1.ResponseWarning, _Mapping]]] = ..., AlertLevel: _Optional[int] = ...) -> None: ...

class ExtraPositionsInOCCStyleCSV(_message.Message):
    __slots__ = ("AccountId", "AccountNumber", "UploadName", "FileContent")
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTNUMBER_FIELD_NUMBER: _ClassVar[int]
    UPLOADNAME_FIELD_NUMBER: _ClassVar[int]
    FILECONTENT_FIELD_NUMBER: _ClassVar[int]
    AccountId: int
    AccountNumber: str
    UploadName: str
    FileContent: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, AccountId: _Optional[int] = ..., AccountNumber: _Optional[str] = ..., UploadName: _Optional[str] = ..., FileContent: _Optional[_Iterable[str]] = ...) -> None: ...
