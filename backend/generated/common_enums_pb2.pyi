from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EnumAppMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumAppMode_Undefined: _ClassVar[EnumAppMode]
    EnumAppMode_Real: _ClassVar[EnumAppMode]
    EnumAppMode_V_T: _ClassVar[EnumAppMode]

class EnumClearingAccountType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumClearingAccountType_Undefined: _ClassVar[EnumClearingAccountType]
    EnumClearingAccountType_Cash: _ClassVar[EnumClearingAccountType]
    EnumClearingAccountType_MarginLong: _ClassVar[EnumClearingAccountType]
    EnumClearingAccountType_MarginShort: _ClassVar[EnumClearingAccountType]
    EnumClearingAccountType_TEFRA_Buffer: _ClassVar[EnumClearingAccountType]
    EnumClearingAccountType_When_Issued_Cash: _ClassVar[EnumClearingAccountType]
    EnumClearingAccountType_Firm_Specified: _ClassVar[EnumClearingAccountType]
    EnumClearingAccountType_Miscellaneous: _ClassVar[EnumClearingAccountType]

class EnumCurrency(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumCurrency_Undefined: _ClassVar[EnumCurrency]
    EnumCurrency_USD: _ClassVar[EnumCurrency]

class EnumAccountRiskType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumAccountRiskType_Undefined: _ClassVar[EnumAccountRiskType]
    EnumAccountRiskType_RegT_Cash: _ClassVar[EnumAccountRiskType]
    EnumAccountRiskType_RegT_LimitedMargin: _ClassVar[EnumAccountRiskType]
    EnumAccountRiskType_RegT_Margin: _ClassVar[EnumAccountRiskType]
    EnumAccountRiskType_PM_CPM: _ClassVar[EnumAccountRiskType]
    EnumAccountRiskType_PM_BD: _ClassVar[EnumAccountRiskType]
    EnumAccountRiskType_PM_MM: _ClassVar[EnumAccountRiskType]
    EnumAccountRiskType_SPAN_Speculator: _ClassVar[EnumAccountRiskType]
    EnumAccountRiskType_SPAN_Hedge: _ClassVar[EnumAccountRiskType]
    EnumAccountRiskType_SPAN_Member: _ClassVar[EnumAccountRiskType]

class EnumMaturityTerm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumMaturityTerm_Undefined: _ClassVar[EnumMaturityTerm]
    EnumMaturityTerm_All: _ClassVar[EnumMaturityTerm]
    EnumMaturityTerm_Long: _ClassVar[EnumMaturityTerm]
    EnumMaturityTerm_Medium: _ClassVar[EnumMaturityTerm]
    EnumMaturityTerm_Short: _ClassVar[EnumMaturityTerm]

class EnumOptionPricingModel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumOptionPricingModel_Undefined: _ClassVar[EnumOptionPricingModel]
    EnumOptionPricingModel_OptionChainAnalysis: _ClassVar[EnumOptionPricingModel]
    EnumOptionPricingModel_Delta: _ClassVar[EnumOptionPricingModel]
    EnumOptionPricingModel_OCC_PriceMovements: _ClassVar[EnumOptionPricingModel]
    EnumOptionPricingModel_OCC_PriceMovementsWithLiveGreeks: _ClassVar[EnumOptionPricingModel]
    EnumOptionPricingModel_BlackScholes: _ClassVar[EnumOptionPricingModel]
    EnumOptionPricingModel_BlackScholesWithBod_Pricing: _ClassVar[EnumOptionPricingModel]
    EnumOptionPricingModel_BinomialTree: _ClassVar[EnumOptionPricingModel]
    EnumOptionPricingModel_BinomialTreeWithBod_Pricing: _ClassVar[EnumOptionPricingModel]

class EnumExternalDataSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumExternalDataSource_Undefined: _ClassVar[EnumExternalDataSource]
    EnumExternalDataSource_B_B_H_Bank: _ClassVar[EnumExternalDataSource]
    EnumExternalDataSource_U_S_Bank: _ClassVar[EnumExternalDataSource]
    EnumExternalDataSource_U_M_B_Bank: _ClassVar[EnumExternalDataSource]
    EnumExternalDataSource_FifthThirdBank: _ClassVar[EnumExternalDataSource]
    EnumExternalDataSource_CitiBank: _ClassVar[EnumExternalDataSource]
    EnumExternalDataSource_B_N_Y_MellonBank: _ClassVar[EnumExternalDataSource]
    EnumExternalDataSource_TradeAwayExecution: _ClassVar[EnumExternalDataSource]
EnumAppMode_Undefined: EnumAppMode
EnumAppMode_Real: EnumAppMode
EnumAppMode_V_T: EnumAppMode
EnumClearingAccountType_Undefined: EnumClearingAccountType
EnumClearingAccountType_Cash: EnumClearingAccountType
EnumClearingAccountType_MarginLong: EnumClearingAccountType
EnumClearingAccountType_MarginShort: EnumClearingAccountType
EnumClearingAccountType_TEFRA_Buffer: EnumClearingAccountType
EnumClearingAccountType_When_Issued_Cash: EnumClearingAccountType
EnumClearingAccountType_Firm_Specified: EnumClearingAccountType
EnumClearingAccountType_Miscellaneous: EnumClearingAccountType
EnumCurrency_Undefined: EnumCurrency
EnumCurrency_USD: EnumCurrency
EnumAccountRiskType_Undefined: EnumAccountRiskType
EnumAccountRiskType_RegT_Cash: EnumAccountRiskType
EnumAccountRiskType_RegT_LimitedMargin: EnumAccountRiskType
EnumAccountRiskType_RegT_Margin: EnumAccountRiskType
EnumAccountRiskType_PM_CPM: EnumAccountRiskType
EnumAccountRiskType_PM_BD: EnumAccountRiskType
EnumAccountRiskType_PM_MM: EnumAccountRiskType
EnumAccountRiskType_SPAN_Speculator: EnumAccountRiskType
EnumAccountRiskType_SPAN_Hedge: EnumAccountRiskType
EnumAccountRiskType_SPAN_Member: EnumAccountRiskType
EnumMaturityTerm_Undefined: EnumMaturityTerm
EnumMaturityTerm_All: EnumMaturityTerm
EnumMaturityTerm_Long: EnumMaturityTerm
EnumMaturityTerm_Medium: EnumMaturityTerm
EnumMaturityTerm_Short: EnumMaturityTerm
EnumOptionPricingModel_Undefined: EnumOptionPricingModel
EnumOptionPricingModel_OptionChainAnalysis: EnumOptionPricingModel
EnumOptionPricingModel_Delta: EnumOptionPricingModel
EnumOptionPricingModel_OCC_PriceMovements: EnumOptionPricingModel
EnumOptionPricingModel_OCC_PriceMovementsWithLiveGreeks: EnumOptionPricingModel
EnumOptionPricingModel_BlackScholes: EnumOptionPricingModel
EnumOptionPricingModel_BlackScholesWithBod_Pricing: EnumOptionPricingModel
EnumOptionPricingModel_BinomialTree: EnumOptionPricingModel
EnumOptionPricingModel_BinomialTreeWithBod_Pricing: EnumOptionPricingModel
EnumExternalDataSource_Undefined: EnumExternalDataSource
EnumExternalDataSource_B_B_H_Bank: EnumExternalDataSource
EnumExternalDataSource_U_S_Bank: EnumExternalDataSource
EnumExternalDataSource_U_M_B_Bank: EnumExternalDataSource
EnumExternalDataSource_FifthThirdBank: EnumExternalDataSource
EnumExternalDataSource_CitiBank: EnumExternalDataSource
EnumExternalDataSource_B_N_Y_MellonBank: EnumExternalDataSource
EnumExternalDataSource_TradeAwayExecution: EnumExternalDataSource
