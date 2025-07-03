import common_pb2 as _common_pb2
import bp_enums_pb2 as _bp_enums_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BuyingPowerRequest(_message.Message):
    __slots__ = ("BpValuesRequest", "BpForProposedOrderRequest")
    BPVALUESREQUEST_FIELD_NUMBER: _ClassVar[int]
    BPFORPROPOSEDORDERREQUEST_FIELD_NUMBER: _ClassVar[int]
    BpValuesRequest: BpValuesRequest
    BpForProposedOrderRequest: BpForProposedOrderRequest
    def __init__(self, BpValuesRequest: _Optional[_Union[BpValuesRequest, _Mapping]] = ..., BpForProposedOrderRequest: _Optional[_Union[BpForProposedOrderRequest, _Mapping]] = ...) -> None: ...

class BpValuesRequest(_message.Message):
    __slots__ = ("AccountsInfos",)
    ACCOUNTSINFOS_FIELD_NUMBER: _ClassVar[int]
    AccountsInfos: _containers.RepeatedCompositeFieldContainer[BpValuesRequestAccountInfo]
    def __init__(self, AccountsInfos: _Optional[_Iterable[_Union[BpValuesRequestAccountInfo, _Mapping]]] = ...) -> None: ...

class BpForProposedOrderRequest(_message.Message):
    __slots__ = ("ProposedOrderInfo", "AccountsInfos")
    PROPOSEDORDERINFO_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTSINFOS_FIELD_NUMBER: _ClassVar[int]
    ProposedOrderInfo: BpForProposedOrderRequestOrderInfo
    AccountsInfos: _containers.RepeatedCompositeFieldContainer[BpForProposedOrderRequestAccountInfo]
    def __init__(self, ProposedOrderInfo: _Optional[_Union[BpForProposedOrderRequestOrderInfo, _Mapping]] = ..., AccountsInfos: _Optional[_Iterable[_Union[BpForProposedOrderRequestAccountInfo, _Mapping]]] = ...) -> None: ...

class BpValuesRequestAccountInfo(_message.Message):
    __slots__ = ("accountId", "subaccountIDs")
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    SUBACCOUNTIDS_FIELD_NUMBER: _ClassVar[int]
    accountId: int
    subaccountIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, accountId: _Optional[int] = ..., subaccountIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class BpForProposedOrderRequestAccountInfo(_message.Message):
    __slots__ = ("accountId", "subaccountIDs")
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    SUBACCOUNTIDS_FIELD_NUMBER: _ClassVar[int]
    accountId: int
    subaccountIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, accountId: _Optional[int] = ..., subaccountIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class BpForProposedOrderRequestOrderInfo(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BuyingPowerResponse(_message.Message):
    __slots__ = ("hasData", "BpEngineBpValuesResponseInfos", "BpEngineProposedOrderResponseInfos", "Warnings", "Errors")
    HASDATA_FIELD_NUMBER: _ClassVar[int]
    BPENGINEBPVALUESRESPONSEINFOS_FIELD_NUMBER: _ClassVar[int]
    BPENGINEPROPOSEDORDERRESPONSEINFOS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    hasData: bool
    BpEngineBpValuesResponseInfos: _containers.RepeatedCompositeFieldContainer[BpValuesResponse]
    BpEngineProposedOrderResponseInfos: _containers.RepeatedCompositeFieldContainer[RegTBpForProposedOrderResponseInfo]
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, hasData: bool = ..., BpEngineBpValuesResponseInfos: _Optional[_Iterable[_Union[BpValuesResponse, _Mapping]]] = ..., BpEngineProposedOrderResponseInfos: _Optional[_Iterable[_Union[RegTBpForProposedOrderResponseInfo, _Mapping]]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class BpValuesResponse(_message.Message):
    __slots__ = ("OutputGroupings", "BpValues", "SubaccountsBpValuesResponses", "AccountId", "AccountNumber", "AccountName", "StressTestOutput", "Warnings", "Errors")
    class SubaccountsBpValuesResponsesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: BpValuesResponse
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[BpValuesResponse, _Mapping]] = ...) -> None: ...
    OUTPUTGROUPINGS_FIELD_NUMBER: _ClassVar[int]
    BPVALUES_FIELD_NUMBER: _ClassVar[int]
    SUBACCOUNTSBPVALUESRESPONSES_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTNUMBER_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTNAME_FIELD_NUMBER: _ClassVar[int]
    STRESSTESTOUTPUT_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    OutputGroupings: _containers.RepeatedCompositeFieldContainer[OutputGrouping]
    BpValues: OutputSummaryBpValues
    SubaccountsBpValuesResponses: _containers.MessageMap[int, BpValuesResponse]
    AccountId: int
    AccountNumber: str
    AccountName: str
    StressTestOutput: StressTestOutput
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, OutputGroupings: _Optional[_Iterable[_Union[OutputGrouping, _Mapping]]] = ..., BpValues: _Optional[_Union[OutputSummaryBpValues, _Mapping]] = ..., SubaccountsBpValuesResponses: _Optional[_Mapping[int, BpValuesResponse]] = ..., AccountId: _Optional[int] = ..., AccountNumber: _Optional[str] = ..., AccountName: _Optional[str] = ..., StressTestOutput: _Optional[_Union[StressTestOutput, _Mapping]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class RegTBpForProposedOrderResponseInfo(_message.Message):
    __slots__ = ("BpValuesWithoutProposedLots", "BpValuesWithProposedLots", "SubaccountsRegTBpForProposedOrderResponseInfo", "AccountId", "AccountNumber", "AccountName", "Warnings", "Errors")
    class SubaccountsRegTBpForProposedOrderResponseInfoEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: RegTBpForProposedOrderResponseInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[RegTBpForProposedOrderResponseInfo, _Mapping]] = ...) -> None: ...
    BPVALUESWITHOUTPROPOSEDLOTS_FIELD_NUMBER: _ClassVar[int]
    BPVALUESWITHPROPOSEDLOTS_FIELD_NUMBER: _ClassVar[int]
    SUBACCOUNTSREGTBPFORPROPOSEDORDERRESPONSEINFO_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTNUMBER_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTNAME_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    BpValuesWithoutProposedLots: BpValuesResponse
    BpValuesWithProposedLots: BpValuesResponse
    SubaccountsRegTBpForProposedOrderResponseInfo: _containers.MessageMap[int, RegTBpForProposedOrderResponseInfo]
    AccountId: int
    AccountNumber: str
    AccountName: str
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, BpValuesWithoutProposedLots: _Optional[_Union[BpValuesResponse, _Mapping]] = ..., BpValuesWithProposedLots: _Optional[_Union[BpValuesResponse, _Mapping]] = ..., SubaccountsRegTBpForProposedOrderResponseInfo: _Optional[_Mapping[int, RegTBpForProposedOrderResponseInfo]] = ..., AccountId: _Optional[int] = ..., AccountNumber: _Optional[str] = ..., AccountName: _Optional[str] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class OutputGrouping(_message.Message):
    __slots__ = ("UnderlyingSymbol", "Strategies", "BpValues", "GroupingId", "OutputGroupingStressTest")
    UNDERLYINGSYMBOL_FIELD_NUMBER: _ClassVar[int]
    STRATEGIES_FIELD_NUMBER: _ClassVar[int]
    BPVALUES_FIELD_NUMBER: _ClassVar[int]
    GROUPINGID_FIELD_NUMBER: _ClassVar[int]
    OUTPUTGROUPINGSTRESSTEST_FIELD_NUMBER: _ClassVar[int]
    UnderlyingSymbol: str
    Strategies: _containers.RepeatedCompositeFieldContainer[OutputStrategy]
    BpValues: OutputGroupingBpValues
    GroupingId: str
    OutputGroupingStressTest: OutputGroupingStressTest
    def __init__(self, UnderlyingSymbol: _Optional[str] = ..., Strategies: _Optional[_Iterable[_Union[OutputStrategy, _Mapping]]] = ..., BpValues: _Optional[_Union[OutputGroupingBpValues, _Mapping]] = ..., GroupingId: _Optional[str] = ..., OutputGroupingStressTest: _Optional[_Union[OutputGroupingStressTest, _Mapping]] = ...) -> None: ...

class OutputGroupingBpValues(_message.Message):
    __slots__ = ("HighestRequirement", "HighestRequirementOption", "HighestRequirementStock", "HighestRequirementEtf", "HighestRequirementFixedIncome", "HighestRequirementFuture", "HighestRequirementFutureOption", "HighestRequirementInitial", "HighestRequirementMaintenance", "HighestRequirementMutualFund", "HighestRequirementCrypto", "HighestMarginOrCapitalRequirementOption", "HighestMarginOrCapitalRequirementStock", "HighestMarginOrCapitalRequirementEtf", "HighestMarginOrCapitalRequirementFixedIncome", "HighestMarginOrCapitalRequirementFuture", "HighestMarginOrCapitalRequirementFutureOption", "HighestMarginOrCapitalRequirementInitial", "HighestMarginOrCapitalRequirementMaintenance", "HighestMarginOrCapitalRequirementMutualFund", "HighestMarginOrCapitalRequirementCrypto", "OpenPositionsMarginOrCapitalRequirement", "OpenPositionsMarginOrCapitalRequirementStock", "OpenPositionsMarginOrCapitalRequirementSingleOption", "OpenPositionsMarginOrCapitalRequirementOptionSpread", "OpenPositionsMarginOrCapitalRequirementOptionSpreadWithStockComponent", "OpenPositionsMarginOrCapitalRequirementEtf", "OpenPositionsMarginOrCapitalRequirementFixedIncome", "OpenPositionsMarginOrCapitalRequirementFuture", "OpenPositionsMarginOrCapitalRequirementFutureOption", "OpenPositionsMarginOrCapitalRequirementMutualFund", "OpenPositionsMarginOrCapitalRequirementCrypto", "OpenPositionsMarketValue", "OpenPositionsMarketValueLongStock", "OpenPositionsMarketValueShortStock", "OpenPositionsMarketValueLongOption", "OpenPositionsMarketValueShortOption", "OpenPositionsMarketValueLongFixedIncome", "OpenPositionsMarketValueShortFixedIncome", "OpenPositionsMarketValueLongEtf", "OpenPositionsMarketValueShortEtf", "OpenPositionsMarketValueLongFuture", "OpenPositionsMarketValueShortFuture", "OpenPositionsMarketValueLongFututreOption", "OpenPositionsMarketValueShortFututreOption", "OpenPositionsMarketValueLongMutualFund", "OpenPositionsMarketValueShortMutualFund", "OpenPositionsMarketValueLongCrypto", "OpenPositionsMarketValueShortCrypto", "SpecialMemorandumAccountDebit", "OpenPositionsMarginExcess", "PendingTransaction", "LowestAvailableFundsPendingTransaction", "LowestAvailableFundsPendingMarginExcess", "LowestAvailableFundsPendingMarginOrCapitalRequirement", "HighestRequirementRegT", "CoveredOptionLoss", "LowestAvailableFundsPendingRequirementMaint", "NAV", "MorningNAV", "DayPnL", "DayPnL_Utilization")
    HIGHESTREQUIREMENT_FIELD_NUMBER: _ClassVar[int]
    HIGHESTREQUIREMENTOPTION_FIELD_NUMBER: _ClassVar[int]
    HIGHESTREQUIREMENTSTOCK_FIELD_NUMBER: _ClassVar[int]
    HIGHESTREQUIREMENTETF_FIELD_NUMBER: _ClassVar[int]
    HIGHESTREQUIREMENTFIXEDINCOME_FIELD_NUMBER: _ClassVar[int]
    HIGHESTREQUIREMENTFUTURE_FIELD_NUMBER: _ClassVar[int]
    HIGHESTREQUIREMENTFUTUREOPTION_FIELD_NUMBER: _ClassVar[int]
    HIGHESTREQUIREMENTINITIAL_FIELD_NUMBER: _ClassVar[int]
    HIGHESTREQUIREMENTMAINTENANCE_FIELD_NUMBER: _ClassVar[int]
    HIGHESTREQUIREMENTMUTUALFUND_FIELD_NUMBER: _ClassVar[int]
    HIGHESTREQUIREMENTCRYPTO_FIELD_NUMBER: _ClassVar[int]
    HIGHESTMARGINORCAPITALREQUIREMENTOPTION_FIELD_NUMBER: _ClassVar[int]
    HIGHESTMARGINORCAPITALREQUIREMENTSTOCK_FIELD_NUMBER: _ClassVar[int]
    HIGHESTMARGINORCAPITALREQUIREMENTETF_FIELD_NUMBER: _ClassVar[int]
    HIGHESTMARGINORCAPITALREQUIREMENTFIXEDINCOME_FIELD_NUMBER: _ClassVar[int]
    HIGHESTMARGINORCAPITALREQUIREMENTFUTURE_FIELD_NUMBER: _ClassVar[int]
    HIGHESTMARGINORCAPITALREQUIREMENTFUTUREOPTION_FIELD_NUMBER: _ClassVar[int]
    HIGHESTMARGINORCAPITALREQUIREMENTINITIAL_FIELD_NUMBER: _ClassVar[int]
    HIGHESTMARGINORCAPITALREQUIREMENTMAINTENANCE_FIELD_NUMBER: _ClassVar[int]
    HIGHESTMARGINORCAPITALREQUIREMENTMUTUALFUND_FIELD_NUMBER: _ClassVar[int]
    HIGHESTMARGINORCAPITALREQUIREMENTCRYPTO_FIELD_NUMBER: _ClassVar[int]
    OPENPOSITIONSMARGINORCAPITALREQUIREMENT_FIELD_NUMBER: _ClassVar[int]
    OPENPOSITIONSMARGINORCAPITALREQUIREMENTSTOCK_FIELD_NUMBER: _ClassVar[int]
    OPENPOSITIONSMARGINORCAPITALREQUIREMENTSINGLEOPTION_FIELD_NUMBER: _ClassVar[int]
    OPENPOSITIONSMARGINORCAPITALREQUIREMENTOPTIONSPREAD_FIELD_NUMBER: _ClassVar[int]
    OPENPOSITIONSMARGINORCAPITALREQUIREMENTOPTIONSPREADWITHSTOCKCOMPONENT_FIELD_NUMBER: _ClassVar[int]
    OPENPOSITIONSMARGINORCAPITALREQUIREMENTETF_FIELD_NUMBER: _ClassVar[int]
    OPENPOSITIONSMARGINORCAPITALREQUIREMENTFIXEDINCOME_FIELD_NUMBER: _ClassVar[int]
    OPENPOSITIONSMARGINORCAPITALREQUIREMENTFUTURE_FIELD_NUMBER: _ClassVar[int]
    OPENPOSITIONSMARGINORCAPITALREQUIREMENTFUTUREOPTION_FIELD_NUMBER: _ClassVar[int]
    OPENPOSITIONSMARGINORCAPITALREQUIREMENTMUTUALFUND_FIELD_NUMBER: _ClassVar[int]
    OPENPOSITIONSMARGINORCAPITALREQUIREMENTCRYPTO_FIELD_NUMBER: _ClassVar[int]
    OPENPOSITIONSMARKETVALUE_FIELD_NUMBER: _ClassVar[int]
    OPENPOSITIONSMARKETVALUELONGSTOCK_FIELD_NUMBER: _ClassVar[int]
    OPENPOSITIONSMARKETVALUESHORTSTOCK_FIELD_NUMBER: _ClassVar[int]
    OPENPOSITIONSMARKETVALUELONGOPTION_FIELD_NUMBER: _ClassVar[int]
    OPENPOSITIONSMARKETVALUESHORTOPTION_FIELD_NUMBER: _ClassVar[int]
    OPENPOSITIONSMARKETVALUELONGFIXEDINCOME_FIELD_NUMBER: _ClassVar[int]
    OPENPOSITIONSMARKETVALUESHORTFIXEDINCOME_FIELD_NUMBER: _ClassVar[int]
    OPENPOSITIONSMARKETVALUELONGETF_FIELD_NUMBER: _ClassVar[int]
    OPENPOSITIONSMARKETVALUESHORTETF_FIELD_NUMBER: _ClassVar[int]
    OPENPOSITIONSMARKETVALUELONGFUTURE_FIELD_NUMBER: _ClassVar[int]
    OPENPOSITIONSMARKETVALUESHORTFUTURE_FIELD_NUMBER: _ClassVar[int]
    OPENPOSITIONSMARKETVALUELONGFUTUTREOPTION_FIELD_NUMBER: _ClassVar[int]
    OPENPOSITIONSMARKETVALUESHORTFUTUTREOPTION_FIELD_NUMBER: _ClassVar[int]
    OPENPOSITIONSMARKETVALUELONGMUTUALFUND_FIELD_NUMBER: _ClassVar[int]
    OPENPOSITIONSMARKETVALUESHORTMUTUALFUND_FIELD_NUMBER: _ClassVar[int]
    OPENPOSITIONSMARKETVALUELONGCRYPTO_FIELD_NUMBER: _ClassVar[int]
    OPENPOSITIONSMARKETVALUESHORTCRYPTO_FIELD_NUMBER: _ClassVar[int]
    SPECIALMEMORANDUMACCOUNTDEBIT_FIELD_NUMBER: _ClassVar[int]
    OPENPOSITIONSMARGINEXCESS_FIELD_NUMBER: _ClassVar[int]
    PENDINGTRANSACTION_FIELD_NUMBER: _ClassVar[int]
    LOWESTAVAILABLEFUNDSPENDINGTRANSACTION_FIELD_NUMBER: _ClassVar[int]
    LOWESTAVAILABLEFUNDSPENDINGMARGINEXCESS_FIELD_NUMBER: _ClassVar[int]
    LOWESTAVAILABLEFUNDSPENDINGMARGINORCAPITALREQUIREMENT_FIELD_NUMBER: _ClassVar[int]
    HIGHESTREQUIREMENTREGT_FIELD_NUMBER: _ClassVar[int]
    COVEREDOPTIONLOSS_FIELD_NUMBER: _ClassVar[int]
    LOWESTAVAILABLEFUNDSPENDINGREQUIREMENTMAINT_FIELD_NUMBER: _ClassVar[int]
    NAV_FIELD_NUMBER: _ClassVar[int]
    MORNINGNAV_FIELD_NUMBER: _ClassVar[int]
    DAYPNL_FIELD_NUMBER: _ClassVar[int]
    DAYPNL_UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    HighestRequirement: float
    HighestRequirementOption: float
    HighestRequirementStock: float
    HighestRequirementEtf: float
    HighestRequirementFixedIncome: float
    HighestRequirementFuture: float
    HighestRequirementFutureOption: float
    HighestRequirementInitial: float
    HighestRequirementMaintenance: float
    HighestRequirementMutualFund: float
    HighestRequirementCrypto: float
    HighestMarginOrCapitalRequirementOption: float
    HighestMarginOrCapitalRequirementStock: float
    HighestMarginOrCapitalRequirementEtf: float
    HighestMarginOrCapitalRequirementFixedIncome: float
    HighestMarginOrCapitalRequirementFuture: float
    HighestMarginOrCapitalRequirementFutureOption: float
    HighestMarginOrCapitalRequirementInitial: float
    HighestMarginOrCapitalRequirementMaintenance: float
    HighestMarginOrCapitalRequirementMutualFund: float
    HighestMarginOrCapitalRequirementCrypto: float
    OpenPositionsMarginOrCapitalRequirement: float
    OpenPositionsMarginOrCapitalRequirementStock: float
    OpenPositionsMarginOrCapitalRequirementSingleOption: float
    OpenPositionsMarginOrCapitalRequirementOptionSpread: float
    OpenPositionsMarginOrCapitalRequirementOptionSpreadWithStockComponent: float
    OpenPositionsMarginOrCapitalRequirementEtf: float
    OpenPositionsMarginOrCapitalRequirementFixedIncome: float
    OpenPositionsMarginOrCapitalRequirementFuture: float
    OpenPositionsMarginOrCapitalRequirementFutureOption: float
    OpenPositionsMarginOrCapitalRequirementMutualFund: float
    OpenPositionsMarginOrCapitalRequirementCrypto: float
    OpenPositionsMarketValue: float
    OpenPositionsMarketValueLongStock: float
    OpenPositionsMarketValueShortStock: float
    OpenPositionsMarketValueLongOption: float
    OpenPositionsMarketValueShortOption: float
    OpenPositionsMarketValueLongFixedIncome: float
    OpenPositionsMarketValueShortFixedIncome: float
    OpenPositionsMarketValueLongEtf: float
    OpenPositionsMarketValueShortEtf: float
    OpenPositionsMarketValueLongFuture: float
    OpenPositionsMarketValueShortFuture: float
    OpenPositionsMarketValueLongFututreOption: float
    OpenPositionsMarketValueShortFututreOption: float
    OpenPositionsMarketValueLongMutualFund: float
    OpenPositionsMarketValueShortMutualFund: float
    OpenPositionsMarketValueLongCrypto: float
    OpenPositionsMarketValueShortCrypto: float
    SpecialMemorandumAccountDebit: float
    OpenPositionsMarginExcess: float
    PendingTransaction: float
    LowestAvailableFundsPendingTransaction: float
    LowestAvailableFundsPendingMarginExcess: float
    LowestAvailableFundsPendingMarginOrCapitalRequirement: float
    HighestRequirementRegT: float
    CoveredOptionLoss: float
    LowestAvailableFundsPendingRequirementMaint: float
    NAV: float
    MorningNAV: float
    DayPnL: float
    DayPnL_Utilization: float
    def __init__(self, HighestRequirement: _Optional[float] = ..., HighestRequirementOption: _Optional[float] = ..., HighestRequirementStock: _Optional[float] = ..., HighestRequirementEtf: _Optional[float] = ..., HighestRequirementFixedIncome: _Optional[float] = ..., HighestRequirementFuture: _Optional[float] = ..., HighestRequirementFutureOption: _Optional[float] = ..., HighestRequirementInitial: _Optional[float] = ..., HighestRequirementMaintenance: _Optional[float] = ..., HighestRequirementMutualFund: _Optional[float] = ..., HighestRequirementCrypto: _Optional[float] = ..., HighestMarginOrCapitalRequirementOption: _Optional[float] = ..., HighestMarginOrCapitalRequirementStock: _Optional[float] = ..., HighestMarginOrCapitalRequirementEtf: _Optional[float] = ..., HighestMarginOrCapitalRequirementFixedIncome: _Optional[float] = ..., HighestMarginOrCapitalRequirementFuture: _Optional[float] = ..., HighestMarginOrCapitalRequirementFutureOption: _Optional[float] = ..., HighestMarginOrCapitalRequirementInitial: _Optional[float] = ..., HighestMarginOrCapitalRequirementMaintenance: _Optional[float] = ..., HighestMarginOrCapitalRequirementMutualFund: _Optional[float] = ..., HighestMarginOrCapitalRequirementCrypto: _Optional[float] = ..., OpenPositionsMarginOrCapitalRequirement: _Optional[float] = ..., OpenPositionsMarginOrCapitalRequirementStock: _Optional[float] = ..., OpenPositionsMarginOrCapitalRequirementSingleOption: _Optional[float] = ..., OpenPositionsMarginOrCapitalRequirementOptionSpread: _Optional[float] = ..., OpenPositionsMarginOrCapitalRequirementOptionSpreadWithStockComponent: _Optional[float] = ..., OpenPositionsMarginOrCapitalRequirementEtf: _Optional[float] = ..., OpenPositionsMarginOrCapitalRequirementFixedIncome: _Optional[float] = ..., OpenPositionsMarginOrCapitalRequirementFuture: _Optional[float] = ..., OpenPositionsMarginOrCapitalRequirementFutureOption: _Optional[float] = ..., OpenPositionsMarginOrCapitalRequirementMutualFund: _Optional[float] = ..., OpenPositionsMarginOrCapitalRequirementCrypto: _Optional[float] = ..., OpenPositionsMarketValue: _Optional[float] = ..., OpenPositionsMarketValueLongStock: _Optional[float] = ..., OpenPositionsMarketValueShortStock: _Optional[float] = ..., OpenPositionsMarketValueLongOption: _Optional[float] = ..., OpenPositionsMarketValueShortOption: _Optional[float] = ..., OpenPositionsMarketValueLongFixedIncome: _Optional[float] = ..., OpenPositionsMarketValueShortFixedIncome: _Optional[float] = ..., OpenPositionsMarketValueLongEtf: _Optional[float] = ..., OpenPositionsMarketValueShortEtf: _Optional[float] = ..., OpenPositionsMarketValueLongFuture: _Optional[float] = ..., OpenPositionsMarketValueShortFuture: _Optional[float] = ..., OpenPositionsMarketValueLongFututreOption: _Optional[float] = ..., OpenPositionsMarketValueShortFututreOption: _Optional[float] = ..., OpenPositionsMarketValueLongMutualFund: _Optional[float] = ..., OpenPositionsMarketValueShortMutualFund: _Optional[float] = ..., OpenPositionsMarketValueLongCrypto: _Optional[float] = ..., OpenPositionsMarketValueShortCrypto: _Optional[float] = ..., SpecialMemorandumAccountDebit: _Optional[float] = ..., OpenPositionsMarginExcess: _Optional[float] = ..., PendingTransaction: _Optional[float] = ..., LowestAvailableFundsPendingTransaction: _Optional[float] = ..., LowestAvailableFundsPendingMarginExcess: _Optional[float] = ..., LowestAvailableFundsPendingMarginOrCapitalRequirement: _Optional[float] = ..., HighestRequirementRegT: _Optional[float] = ..., CoveredOptionLoss: _Optional[float] = ..., LowestAvailableFundsPendingRequirementMaint: _Optional[float] = ..., NAV: _Optional[float] = ..., MorningNAV: _Optional[float] = ..., DayPnL: _Optional[float] = ..., DayPnL_Utilization: _Optional[float] = ...) -> None: ...

class OutputSummaryBpValues(_message.Message):
    __slots__ = ("AggregatedGroupingBpValues", "AvailableFundsForTrading", "LiquidationValue", "OpenPositionsHsxBP", "OptionsBuyingPower", "StockBuyingPower", "Cash", "EquityValueForRequiredLevelCheck", "UnsettledCash", "IntradayBpCappedBySMA", "SMA", "StockBuyingPowerHSX", "StockBuyingPowerSMA", "AvailableFundsForTradingHSX", "AvailableFundsForTradingSMA", "CreditUtilization", "DayPnL", "DayPnL_Utilization", "ExcessLiquidity")
    AGGREGATEDGROUPINGBPVALUES_FIELD_NUMBER: _ClassVar[int]
    AVAILABLEFUNDSFORTRADING_FIELD_NUMBER: _ClassVar[int]
    LIQUIDATIONVALUE_FIELD_NUMBER: _ClassVar[int]
    OPENPOSITIONSHSXBP_FIELD_NUMBER: _ClassVar[int]
    OPTIONSBUYINGPOWER_FIELD_NUMBER: _ClassVar[int]
    STOCKBUYINGPOWER_FIELD_NUMBER: _ClassVar[int]
    CASH_FIELD_NUMBER: _ClassVar[int]
    EQUITYVALUEFORREQUIREDLEVELCHECK_FIELD_NUMBER: _ClassVar[int]
    UNSETTLEDCASH_FIELD_NUMBER: _ClassVar[int]
    INTRADAYBPCAPPEDBYSMA_FIELD_NUMBER: _ClassVar[int]
    SMA_FIELD_NUMBER: _ClassVar[int]
    STOCKBUYINGPOWERHSX_FIELD_NUMBER: _ClassVar[int]
    STOCKBUYINGPOWERSMA_FIELD_NUMBER: _ClassVar[int]
    AVAILABLEFUNDSFORTRADINGHSX_FIELD_NUMBER: _ClassVar[int]
    AVAILABLEFUNDSFORTRADINGSMA_FIELD_NUMBER: _ClassVar[int]
    CREDITUTILIZATION_FIELD_NUMBER: _ClassVar[int]
    DAYPNL_FIELD_NUMBER: _ClassVar[int]
    DAYPNL_UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    EXCESSLIQUIDITY_FIELD_NUMBER: _ClassVar[int]
    AggregatedGroupingBpValues: OutputGroupingBpValues
    AvailableFundsForTrading: float
    LiquidationValue: float
    OpenPositionsHsxBP: float
    OptionsBuyingPower: float
    StockBuyingPower: float
    Cash: float
    EquityValueForRequiredLevelCheck: float
    UnsettledCash: float
    IntradayBpCappedBySMA: bool
    SMA: float
    StockBuyingPowerHSX: float
    StockBuyingPowerSMA: float
    AvailableFundsForTradingHSX: float
    AvailableFundsForTradingSMA: float
    CreditUtilization: float
    DayPnL: float
    DayPnL_Utilization: float
    ExcessLiquidity: float
    def __init__(self, AggregatedGroupingBpValues: _Optional[_Union[OutputGroupingBpValues, _Mapping]] = ..., AvailableFundsForTrading: _Optional[float] = ..., LiquidationValue: _Optional[float] = ..., OpenPositionsHsxBP: _Optional[float] = ..., OptionsBuyingPower: _Optional[float] = ..., StockBuyingPower: _Optional[float] = ..., Cash: _Optional[float] = ..., EquityValueForRequiredLevelCheck: _Optional[float] = ..., UnsettledCash: _Optional[float] = ..., IntradayBpCappedBySMA: bool = ..., SMA: _Optional[float] = ..., StockBuyingPowerHSX: _Optional[float] = ..., StockBuyingPowerSMA: _Optional[float] = ..., AvailableFundsForTradingHSX: _Optional[float] = ..., AvailableFundsForTradingSMA: _Optional[float] = ..., CreditUtilization: _Optional[float] = ..., DayPnL: _Optional[float] = ..., DayPnL_Utilization: _Optional[float] = ..., ExcessLiquidity: _Optional[float] = ...) -> None: ...

class OutputStrategy(_message.Message):
    __slots__ = ("StrategyType", "Quantity", "RequirementPerUnit", "SmaDebitPerUnit", "Legs", "Multiplier", "ContractSize", "Description", "NAV", "MorningNAV", "DayPnL", "DayPnL_Utilization")
    STRATEGYTYPE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    REQUIREMENTPERUNIT_FIELD_NUMBER: _ClassVar[int]
    SMADEBITPERUNIT_FIELD_NUMBER: _ClassVar[int]
    LEGS_FIELD_NUMBER: _ClassVar[int]
    MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
    CONTRACTSIZE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    NAV_FIELD_NUMBER: _ClassVar[int]
    MORNINGNAV_FIELD_NUMBER: _ClassVar[int]
    DAYPNL_FIELD_NUMBER: _ClassVar[int]
    DAYPNL_UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    StrategyType: _bp_enums_pb2.EnumBpStrategy
    Quantity: float
    RequirementPerUnit: float
    SmaDebitPerUnit: float
    Legs: _containers.RepeatedCompositeFieldContainer[OutputStrategyLeg]
    Multiplier: float
    ContractSize: float
    Description: str
    NAV: float
    MorningNAV: float
    DayPnL: float
    DayPnL_Utilization: float
    def __init__(self, StrategyType: _Optional[_Union[_bp_enums_pb2.EnumBpStrategy, str]] = ..., Quantity: _Optional[float] = ..., RequirementPerUnit: _Optional[float] = ..., SmaDebitPerUnit: _Optional[float] = ..., Legs: _Optional[_Iterable[_Union[OutputStrategyLeg, _Mapping]]] = ..., Multiplier: _Optional[float] = ..., ContractSize: _Optional[float] = ..., Description: _Optional[str] = ..., NAV: _Optional[float] = ..., MorningNAV: _Optional[float] = ..., DayPnL: _Optional[float] = ..., DayPnL_Utilization: _Optional[float] = ...) -> None: ...

class OutputStrategyLeg(_message.Message):
    __slots__ = ("Symbol", "Quantity", "StrategyType", "Id", "Description", "InputStrategyComponentType", "Price", "Greeks", "NAV", "MorningNAV", "DayPnL", "DayPnL_Utilization", "QuantityOpenedToday", "QuantityClosedToday")
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    STRATEGYTYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    INPUTSTRATEGYCOMPONENTTYPE_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    GREEKS_FIELD_NUMBER: _ClassVar[int]
    NAV_FIELD_NUMBER: _ClassVar[int]
    MORNINGNAV_FIELD_NUMBER: _ClassVar[int]
    DAYPNL_FIELD_NUMBER: _ClassVar[int]
    DAYPNL_UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    QUANTITYOPENEDTODAY_FIELD_NUMBER: _ClassVar[int]
    QUANTITYCLOSEDTODAY_FIELD_NUMBER: _ClassVar[int]
    Symbol: str
    Quantity: float
    StrategyType: _bp_enums_pb2.EnumBpStrategy
    Id: str
    Description: str
    InputStrategyComponentType: _bp_enums_pb2.EnumInputStrategyComponentType
    Price: float
    Greeks: OutputStrategyLegGreeks
    NAV: float
    MorningNAV: float
    DayPnL: float
    DayPnL_Utilization: float
    QuantityOpenedToday: float
    QuantityClosedToday: float
    def __init__(self, Symbol: _Optional[str] = ..., Quantity: _Optional[float] = ..., StrategyType: _Optional[_Union[_bp_enums_pb2.EnumBpStrategy, str]] = ..., Id: _Optional[str] = ..., Description: _Optional[str] = ..., InputStrategyComponentType: _Optional[_Union[_bp_enums_pb2.EnumInputStrategyComponentType, str]] = ..., Price: _Optional[float] = ..., Greeks: _Optional[_Union[OutputStrategyLegGreeks, _Mapping]] = ..., NAV: _Optional[float] = ..., MorningNAV: _Optional[float] = ..., DayPnL: _Optional[float] = ..., DayPnL_Utilization: _Optional[float] = ..., QuantityOpenedToday: _Optional[float] = ..., QuantityClosedToday: _Optional[float] = ...) -> None: ...

class OutputStrategyLegGreeks(_message.Message):
    __slots__ = ("Delta", "Vega", "ImpliedVolatility")
    DELTA_FIELD_NUMBER: _ClassVar[int]
    VEGA_FIELD_NUMBER: _ClassVar[int]
    IMPLIEDVOLATILITY_FIELD_NUMBER: _ClassVar[int]
    Delta: float
    Vega: float
    ImpliedVolatility: float
    def __init__(self, Delta: _Optional[float] = ..., Vega: _Optional[float] = ..., ImpliedVolatility: _Optional[float] = ...) -> None: ...

class BpStressTestInput(_message.Message):
    __slots__ = ("UnderlyingPriceShockInputs", "VolatilityShockInputs", "BpRiskProfiles")
    UNDERLYINGPRICESHOCKINPUTS_FIELD_NUMBER: _ClassVar[int]
    VOLATILITYSHOCKINPUTS_FIELD_NUMBER: _ClassVar[int]
    BPRISKPROFILES_FIELD_NUMBER: _ClassVar[int]
    UnderlyingPriceShockInputs: _containers.RepeatedCompositeFieldContainer[BpUnderlyingPriceShockInput]
    VolatilityShockInputs: _containers.RepeatedCompositeFieldContainer[BpVolatilityShockInput]
    BpRiskProfiles: _containers.RepeatedCompositeFieldContainer[BpRiskProfile]
    def __init__(self, UnderlyingPriceShockInputs: _Optional[_Iterable[_Union[BpUnderlyingPriceShockInput, _Mapping]]] = ..., VolatilityShockInputs: _Optional[_Iterable[_Union[BpVolatilityShockInput, _Mapping]]] = ..., BpRiskProfiles: _Optional[_Iterable[_Union[BpRiskProfile, _Mapping]]] = ...) -> None: ...

class BpUnderlyingPriceShockInput(_message.Message):
    __slots__ = ("ApplyAcrossPortfolio", "UnderlyingSymbol", "PercentDown", "PercentUp")
    APPLYACROSSPORTFOLIO_FIELD_NUMBER: _ClassVar[int]
    UNDERLYINGSYMBOL_FIELD_NUMBER: _ClassVar[int]
    PERCENTDOWN_FIELD_NUMBER: _ClassVar[int]
    PERCENTUP_FIELD_NUMBER: _ClassVar[int]
    ApplyAcrossPortfolio: bool
    UnderlyingSymbol: str
    PercentDown: float
    PercentUp: float
    def __init__(self, ApplyAcrossPortfolio: bool = ..., UnderlyingSymbol: _Optional[str] = ..., PercentDown: _Optional[float] = ..., PercentUp: _Optional[float] = ...) -> None: ...

class BpVolatilityShockInput(_message.Message):
    __slots__ = ("ApplyAcrossPortfolio", "UnderlyingSymbol", "ApplyTimeToExpirationFactor", "PercentDown", "PercentUp")
    APPLYACROSSPORTFOLIO_FIELD_NUMBER: _ClassVar[int]
    UNDERLYINGSYMBOL_FIELD_NUMBER: _ClassVar[int]
    APPLYTIMETOEXPIRATIONFACTOR_FIELD_NUMBER: _ClassVar[int]
    PERCENTDOWN_FIELD_NUMBER: _ClassVar[int]
    PERCENTUP_FIELD_NUMBER: _ClassVar[int]
    ApplyAcrossPortfolio: bool
    UnderlyingSymbol: str
    ApplyTimeToExpirationFactor: int
    PercentDown: float
    PercentUp: float
    def __init__(self, ApplyAcrossPortfolio: bool = ..., UnderlyingSymbol: _Optional[str] = ..., ApplyTimeToExpirationFactor: _Optional[int] = ..., PercentDown: _Optional[float] = ..., PercentUp: _Optional[float] = ...) -> None: ...

class StressTestOutput(_message.Message):
    __slots__ = ("Scenarios", "MaxNetExposure")
    SCENARIOS_FIELD_NUMBER: _ClassVar[int]
    MAXNETEXPOSURE_FIELD_NUMBER: _ClassVar[int]
    Scenarios: _containers.RepeatedCompositeFieldContainer[OutputScenario]
    MaxNetExposure: float
    def __init__(self, Scenarios: _Optional[_Iterable[_Union[OutputScenario, _Mapping]]] = ..., MaxNetExposure: _Optional[float] = ...) -> None: ...

class OutputScenario(_message.Message):
    __slots__ = ("BpValuesResponse", "ScenarioIndex", "ScenarioDescription", "NetExposure")
    BPVALUESRESPONSE_FIELD_NUMBER: _ClassVar[int]
    SCENARIOINDEX_FIELD_NUMBER: _ClassVar[int]
    SCENARIODESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    NETEXPOSURE_FIELD_NUMBER: _ClassVar[int]
    BpValuesResponse: BpValuesResponse
    ScenarioIndex: int
    ScenarioDescription: str
    NetExposure: float
    def __init__(self, BpValuesResponse: _Optional[_Union[BpValuesResponse, _Mapping]] = ..., ScenarioIndex: _Optional[int] = ..., ScenarioDescription: _Optional[str] = ..., NetExposure: _Optional[float] = ...) -> None: ...

class OutputGroupingStressTest(_message.Message):
    __slots__ = ("AppliedIVShockDirection", "AppliedIVShockValue")
    APPLIEDIVSHOCKDIRECTION_FIELD_NUMBER: _ClassVar[int]
    APPLIEDIVSHOCKVALUE_FIELD_NUMBER: _ClassVar[int]
    AppliedIVShockDirection: float
    AppliedIVShockValue: float
    def __init__(self, AppliedIVShockDirection: _Optional[float] = ..., AppliedIVShockValue: _Optional[float] = ...) -> None: ...

class BpRiskProfile(_message.Message):
    __slots__ = ("RiskProfileId", "Name", "Scenarios")
    RISKPROFILEID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SCENARIOS_FIELD_NUMBER: _ClassVar[int]
    RiskProfileId: int
    Name: str
    Scenarios: _containers.RepeatedCompositeFieldContainer[BpScenario]
    def __init__(self, RiskProfileId: _Optional[int] = ..., Name: _Optional[str] = ..., Scenarios: _Optional[_Iterable[_Union[BpScenario, _Mapping]]] = ...) -> None: ...

class BpScenario(_message.Message):
    __slots__ = ("UnderlyingPriceShockInputs", "VolatilityShockInputs")
    UNDERLYINGPRICESHOCKINPUTS_FIELD_NUMBER: _ClassVar[int]
    VOLATILITYSHOCKINPUTS_FIELD_NUMBER: _ClassVar[int]
    UnderlyingPriceShockInputs: _containers.RepeatedCompositeFieldContainer[BpUnderlyingPriceShockInput]
    VolatilityShockInputs: _containers.RepeatedCompositeFieldContainer[BpVolatilityShockInput]
    def __init__(self, UnderlyingPriceShockInputs: _Optional[_Iterable[_Union[BpUnderlyingPriceShockInput, _Mapping]]] = ..., VolatilityShockInputs: _Optional[_Iterable[_Union[BpVolatilityShockInput, _Mapping]]] = ...) -> None: ...

class BpAccountWhatIfAdjustment(_message.Message):
    __slots__ = ("AccountNumber", "BpWhatIfAdjustedProducts")
    ACCOUNTNUMBER_FIELD_NUMBER: _ClassVar[int]
    BPWHATIFADJUSTEDPRODUCTS_FIELD_NUMBER: _ClassVar[int]
    AccountNumber: str
    BpWhatIfAdjustedProducts: _containers.RepeatedCompositeFieldContainer[BpWhatIfAdjustedProduct]
    def __init__(self, AccountNumber: _Optional[str] = ..., BpWhatIfAdjustedProducts: _Optional[_Iterable[_Union[BpWhatIfAdjustedProduct, _Mapping]]] = ...) -> None: ...

class BpWhatIfAdjustedProduct(_message.Message):
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
