from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EnumAccountApplicationRequestType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumAccountApplicationRequestType_Undefined: _ClassVar[EnumAccountApplicationRequestType]
    EnumAccountApplicationRequestType_ValidatePerson: _ClassVar[EnumAccountApplicationRequestType]
    EnumAccountApplicationRequestType_ValidateAccount: _ClassVar[EnumAccountApplicationRequestType]
    EnumAccountApplicationRequestType_ValidateAddress: _ClassVar[EnumAccountApplicationRequestType]
    EnumAccountApplicationRequestType_ValidateApproximateAnnualIncome: _ClassVar[EnumAccountApplicationRequestType]
    EnumAccountApplicationRequestType_ValidateInvestmentObjective: _ClassVar[EnumAccountApplicationRequestType]
    EnumAccountApplicationRequestType_ValidateTotalNetWorth: _ClassVar[EnumAccountApplicationRequestType]
    EnumAccountApplicationRequestType_ValidateInvestingExperience: _ClassVar[EnumAccountApplicationRequestType]
    EnumAccountApplicationRequestType_ValidateRiskTolerance: _ClassVar[EnumAccountApplicationRequestType]
    EnumAccountApplicationRequestType_ValidateEmployment: _ClassVar[EnumAccountApplicationRequestType]
    EnumAccountApplicationRequestType_ValidateFederalDisclosure: _ClassVar[EnumAccountApplicationRequestType]
    EnumAccountApplicationRequestType_ValidateSecurityQuestions: _ClassVar[EnumAccountApplicationRequestType]
    EnumAccountApplicationRequestType_ValidateTrustedContact: _ClassVar[EnumAccountApplicationRequestType]
    EnumAccountApplicationRequestType_CreateVerificationSession: _ClassVar[EnumAccountApplicationRequestType]
    EnumAccountApplicationRequestType_CreateAccount: _ClassVar[EnumAccountApplicationRequestType]
    EnumAccountApplicationRequestType_CreateAdditionalAccount: _ClassVar[EnumAccountApplicationRequestType]
    EnumAccountApplicationRequestType_ValidateMarketDataEntitlementFormResponses: _ClassVar[EnumAccountApplicationRequestType]
    EnumAccountApplicationRequestType_ValidateExternalBrokerageAccountRequest: _ClassVar[EnumAccountApplicationRequestType]

class EnumAccountApplicationInvestmentProfileRequestType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumAccountApplicationInvestmentProfileRequestType_Undefined: _ClassVar[EnumAccountApplicationInvestmentProfileRequestType]
    EnumAccountApplicationInvestmentProfileRequestType_ValidateApproximateAnnualIncome: _ClassVar[EnumAccountApplicationInvestmentProfileRequestType]
    EnumAccountApplicationInvestmentProfileRequestType_ValidateInvestmentObjective: _ClassVar[EnumAccountApplicationInvestmentProfileRequestType]
    EnumAccountApplicationInvestmentProfileRequestType_ValidateTotalNetWorth: _ClassVar[EnumAccountApplicationInvestmentProfileRequestType]
    EnumAccountApplicationInvestmentProfileRequestType_ValidateInvestingExperience: _ClassVar[EnumAccountApplicationInvestmentProfileRequestType]
    EnumAccountApplicationInvestmentProfileRequestType_ValidateRiskTolerance: _ClassVar[EnumAccountApplicationInvestmentProfileRequestType]

class EnumTrustedContactRelationshipType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumTrustedContactRelationshipType_Undefined: _ClassVar[EnumTrustedContactRelationshipType]
    EnumTrustedContactRelationshipType_Spouse: _ClassVar[EnumTrustedContactRelationshipType]
    EnumTrustedContactRelationshipType_Child: _ClassVar[EnumTrustedContactRelationshipType]
    EnumTrustedContactRelationshipType_Other: _ClassVar[EnumTrustedContactRelationshipType]

class EnumFederalDisclosure(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumFederalDisclosure_Undefined: _ClassVar[EnumFederalDisclosure]
    EnumFederalDisclosure_BrokerDealerAffiliation: _ClassVar[EnumFederalDisclosure]
    EnumFederalDisclosure_PubliclyTradedCompany: _ClassVar[EnumFederalDisclosure]
    EnumFederalDisclosure_PublicOfficial: _ClassVar[EnumFederalDisclosure]
    EnumFederalDisclosure_None: _ClassVar[EnumFederalDisclosure]

class EnumNationalIdNumberType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumNationalIdNumberType_Undefined: _ClassVar[EnumNationalIdNumberType]
    EnumNationalIdNumberType_U_S_S_S_N: _ClassVar[EnumNationalIdNumberType]
    EnumNationalIdNumberType_U_S_TaxI_D: _ClassVar[EnumNationalIdNumberType]
    EnumNationalIdNumberType_C_A_U_C_I: _ClassVar[EnumNationalIdNumberType]
    EnumNationalIdNumberType_C_A_S_I_N: _ClassVar[EnumNationalIdNumberType]
    EnumNationalIdNumberType_P_L_Pesel: _ClassVar[EnumNationalIdNumberType]
    EnumNationalIdNumberType_P_L_N_I_P: _ClassVar[EnumNationalIdNumberType]

class EnumMaritalStatusType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumMaritalStatusType_Undefined: _ClassVar[EnumMaritalStatusType]
    EnumMaritalStatusType_Single: _ClassVar[EnumMaritalStatusType]
    EnumMaritalStatusType_Married: _ClassVar[EnumMaritalStatusType]
    EnumMaritalStatusType_DivorcedOrSeparated: _ClassVar[EnumMaritalStatusType]
    EnumMaritalStatusType_Widowed: _ClassVar[EnumMaritalStatusType]

class EnumUSCitizenshipStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumUSCitizenshipStatus_Undefined: _ClassVar[EnumUSCitizenshipStatus]
    EnumUSCitizenshipStatus_U_S_A: _ClassVar[EnumUSCitizenshipStatus]
    EnumUSCitizenshipStatus_U_S_ResidentAlien: _ClassVar[EnumUSCitizenshipStatus]
    EnumUSCitizenshipStatus_NonU_S_ResidentAlien: _ClassVar[EnumUSCitizenshipStatus]

class EnumNationality(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumNationality_Undefined: _ClassVar[EnumNationality]
    EnumNationality_American: _ClassVar[EnumNationality]
    EnumNationality_Polish: _ClassVar[EnumNationality]
    EnumNationality_Canadian: _ClassVar[EnumNationality]

class EnumEmploymentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumEmploymentType_Undefined: _ClassVar[EnumEmploymentType]
    EnumEmploymentType_Employed: _ClassVar[EnumEmploymentType]
    EnumEmploymentType_SelfEmployed: _ClassVar[EnumEmploymentType]
    EnumEmploymentType_Unemployed: _ClassVar[EnumEmploymentType]
    EnumEmploymentType_Retirement: _ClassVar[EnumEmploymentType]
    EnumEmploymentType_Student: _ClassVar[EnumEmploymentType]

class EnumOccupationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumOccupationType_Undefined: _ClassVar[EnumOccupationType]
    EnumOccupationType_ManagerOrBusinessOwner: _ClassVar[EnumOccupationType]
    EnumOccupationType_Professional: _ClassVar[EnumOccupationType]
    EnumOccupationType_TechnicianAndAssociateProfessional: _ClassVar[EnumOccupationType]
    EnumOccupationType_ClericalSupportWorker: _ClassVar[EnumOccupationType]
    EnumOccupationType_ServiceAndSalesWorker: _ClassVar[EnumOccupationType]
    EnumOccupationType_AgriculturalForestryAndFisheryWorker: _ClassVar[EnumOccupationType]
    EnumOccupationType_CraftAndRelatedTradesWorker: _ClassVar[EnumOccupationType]
    EnumOccupationType_ElementaryOccupation: _ClassVar[EnumOccupationType]
    EnumOccupationType_ArmedForcesOccupations: _ClassVar[EnumOccupationType]
    EnumOccupationType_Other: _ClassVar[EnumOccupationType]

class EnumInvestmentObjectiveType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumInvestmentObjectiveType_Undefined: _ClassVar[EnumInvestmentObjectiveType]
    EnumInvestmentObjectiveType_Level1: _ClassVar[EnumInvestmentObjectiveType]
    EnumInvestmentObjectiveType_Level2: _ClassVar[EnumInvestmentObjectiveType]
    EnumInvestmentObjectiveType_Level3: _ClassVar[EnumInvestmentObjectiveType]
    EnumInvestmentObjectiveType_Level4: _ClassVar[EnumInvestmentObjectiveType]

class EnumInvestingExperienceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumInvestingExperienceType_Undefined: _ClassVar[EnumInvestingExperienceType]
    EnumInvestingExperienceType_NoneInvestingExperience: _ClassVar[EnumInvestingExperienceType]
    EnumInvestingExperienceType_Limited: _ClassVar[EnumInvestingExperienceType]
    EnumInvestingExperienceType_Good: _ClassVar[EnumInvestingExperienceType]
    EnumInvestingExperienceType_Extensive: _ClassVar[EnumInvestingExperienceType]

class EnumRiskToleranceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumRiskToleranceType_Undefined: _ClassVar[EnumRiskToleranceType]
    EnumRiskToleranceType_Low: _ClassVar[EnumRiskToleranceType]
    EnumRiskToleranceType_MediumLow: _ClassVar[EnumRiskToleranceType]
    EnumRiskToleranceType_MediumHigh: _ClassVar[EnumRiskToleranceType]
    EnumRiskToleranceType_High: _ClassVar[EnumRiskToleranceType]

class EnumAddressType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumAddressType_Undefined: _ClassVar[EnumAddressType]
    EnumAddressType_Mailing: _ClassVar[EnumAddressType]
    EnumAddressType_Permanent: _ClassVar[EnumAddressType]
    EnumAddressType_MailingSameAsPermanent: _ClassVar[EnumAddressType]

class EnumPhoneType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumPhoneType_Undefined: _ClassVar[EnumPhoneType]
    EnumPhoneType_Primary: _ClassVar[EnumPhoneType]

class EnumEducationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumEducationType_Undefined: _ClassVar[EnumEducationType]
    EnumEducationType_HighSchool: _ClassVar[EnumEducationType]
    EnumEducationType_College: _ClassVar[EnumEducationType]
    EnumEducationType_AssociateDegree: _ClassVar[EnumEducationType]
    EnumEducationType_Bachelor: _ClassVar[EnumEducationType]
    EnumEducationType_Masters: _ClassVar[EnumEducationType]
    EnumEducationType_Professional: _ClassVar[EnumEducationType]

class EnumCommoditiesType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumCommoditiesType_Undefined: _ClassVar[EnumCommoditiesType]
    EnumCommoditiesType_FinancialOrCurrency: _ClassVar[EnumCommoditiesType]
    EnumCommoditiesType_Metals: _ClassVar[EnumCommoditiesType]
    EnumCommoditiesType_Ags: _ClassVar[EnumCommoditiesType]
    EnumCommoditiesType_StockIndices: _ClassVar[EnumCommoditiesType]
    EnumCommoditiesType_Other: _ClassVar[EnumCommoditiesType]

class EnumNatureOfTrading(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumNatureOfTrading_Undefined: _ClassVar[EnumNatureOfTrading]
    EnumNatureOfTrading_Discretionary: _ClassVar[EnumNatureOfTrading]
    EnumNatureOfTrading_NonDiscretionary: _ClassVar[EnumNatureOfTrading]

class EnumTradingObjective(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumTradingObjective_Undefined: _ClassVar[EnumTradingObjective]
    EnumTradingObjective_Speculation: _ClassVar[EnumTradingObjective]
    EnumTradingObjective_Hedging: _ClassVar[EnumTradingObjective]
EnumAccountApplicationRequestType_Undefined: EnumAccountApplicationRequestType
EnumAccountApplicationRequestType_ValidatePerson: EnumAccountApplicationRequestType
EnumAccountApplicationRequestType_ValidateAccount: EnumAccountApplicationRequestType
EnumAccountApplicationRequestType_ValidateAddress: EnumAccountApplicationRequestType
EnumAccountApplicationRequestType_ValidateApproximateAnnualIncome: EnumAccountApplicationRequestType
EnumAccountApplicationRequestType_ValidateInvestmentObjective: EnumAccountApplicationRequestType
EnumAccountApplicationRequestType_ValidateTotalNetWorth: EnumAccountApplicationRequestType
EnumAccountApplicationRequestType_ValidateInvestingExperience: EnumAccountApplicationRequestType
EnumAccountApplicationRequestType_ValidateRiskTolerance: EnumAccountApplicationRequestType
EnumAccountApplicationRequestType_ValidateEmployment: EnumAccountApplicationRequestType
EnumAccountApplicationRequestType_ValidateFederalDisclosure: EnumAccountApplicationRequestType
EnumAccountApplicationRequestType_ValidateSecurityQuestions: EnumAccountApplicationRequestType
EnumAccountApplicationRequestType_ValidateTrustedContact: EnumAccountApplicationRequestType
EnumAccountApplicationRequestType_CreateVerificationSession: EnumAccountApplicationRequestType
EnumAccountApplicationRequestType_CreateAccount: EnumAccountApplicationRequestType
EnumAccountApplicationRequestType_CreateAdditionalAccount: EnumAccountApplicationRequestType
EnumAccountApplicationRequestType_ValidateMarketDataEntitlementFormResponses: EnumAccountApplicationRequestType
EnumAccountApplicationRequestType_ValidateExternalBrokerageAccountRequest: EnumAccountApplicationRequestType
EnumAccountApplicationInvestmentProfileRequestType_Undefined: EnumAccountApplicationInvestmentProfileRequestType
EnumAccountApplicationInvestmentProfileRequestType_ValidateApproximateAnnualIncome: EnumAccountApplicationInvestmentProfileRequestType
EnumAccountApplicationInvestmentProfileRequestType_ValidateInvestmentObjective: EnumAccountApplicationInvestmentProfileRequestType
EnumAccountApplicationInvestmentProfileRequestType_ValidateTotalNetWorth: EnumAccountApplicationInvestmentProfileRequestType
EnumAccountApplicationInvestmentProfileRequestType_ValidateInvestingExperience: EnumAccountApplicationInvestmentProfileRequestType
EnumAccountApplicationInvestmentProfileRequestType_ValidateRiskTolerance: EnumAccountApplicationInvestmentProfileRequestType
EnumTrustedContactRelationshipType_Undefined: EnumTrustedContactRelationshipType
EnumTrustedContactRelationshipType_Spouse: EnumTrustedContactRelationshipType
EnumTrustedContactRelationshipType_Child: EnumTrustedContactRelationshipType
EnumTrustedContactRelationshipType_Other: EnumTrustedContactRelationshipType
EnumFederalDisclosure_Undefined: EnumFederalDisclosure
EnumFederalDisclosure_BrokerDealerAffiliation: EnumFederalDisclosure
EnumFederalDisclosure_PubliclyTradedCompany: EnumFederalDisclosure
EnumFederalDisclosure_PublicOfficial: EnumFederalDisclosure
EnumFederalDisclosure_None: EnumFederalDisclosure
EnumNationalIdNumberType_Undefined: EnumNationalIdNumberType
EnumNationalIdNumberType_U_S_S_S_N: EnumNationalIdNumberType
EnumNationalIdNumberType_U_S_TaxI_D: EnumNationalIdNumberType
EnumNationalIdNumberType_C_A_U_C_I: EnumNationalIdNumberType
EnumNationalIdNumberType_C_A_S_I_N: EnumNationalIdNumberType
EnumNationalIdNumberType_P_L_Pesel: EnumNationalIdNumberType
EnumNationalIdNumberType_P_L_N_I_P: EnumNationalIdNumberType
EnumMaritalStatusType_Undefined: EnumMaritalStatusType
EnumMaritalStatusType_Single: EnumMaritalStatusType
EnumMaritalStatusType_Married: EnumMaritalStatusType
EnumMaritalStatusType_DivorcedOrSeparated: EnumMaritalStatusType
EnumMaritalStatusType_Widowed: EnumMaritalStatusType
EnumUSCitizenshipStatus_Undefined: EnumUSCitizenshipStatus
EnumUSCitizenshipStatus_U_S_A: EnumUSCitizenshipStatus
EnumUSCitizenshipStatus_U_S_ResidentAlien: EnumUSCitizenshipStatus
EnumUSCitizenshipStatus_NonU_S_ResidentAlien: EnumUSCitizenshipStatus
EnumNationality_Undefined: EnumNationality
EnumNationality_American: EnumNationality
EnumNationality_Polish: EnumNationality
EnumNationality_Canadian: EnumNationality
EnumEmploymentType_Undefined: EnumEmploymentType
EnumEmploymentType_Employed: EnumEmploymentType
EnumEmploymentType_SelfEmployed: EnumEmploymentType
EnumEmploymentType_Unemployed: EnumEmploymentType
EnumEmploymentType_Retirement: EnumEmploymentType
EnumEmploymentType_Student: EnumEmploymentType
EnumOccupationType_Undefined: EnumOccupationType
EnumOccupationType_ManagerOrBusinessOwner: EnumOccupationType
EnumOccupationType_Professional: EnumOccupationType
EnumOccupationType_TechnicianAndAssociateProfessional: EnumOccupationType
EnumOccupationType_ClericalSupportWorker: EnumOccupationType
EnumOccupationType_ServiceAndSalesWorker: EnumOccupationType
EnumOccupationType_AgriculturalForestryAndFisheryWorker: EnumOccupationType
EnumOccupationType_CraftAndRelatedTradesWorker: EnumOccupationType
EnumOccupationType_ElementaryOccupation: EnumOccupationType
EnumOccupationType_ArmedForcesOccupations: EnumOccupationType
EnumOccupationType_Other: EnumOccupationType
EnumInvestmentObjectiveType_Undefined: EnumInvestmentObjectiveType
EnumInvestmentObjectiveType_Level1: EnumInvestmentObjectiveType
EnumInvestmentObjectiveType_Level2: EnumInvestmentObjectiveType
EnumInvestmentObjectiveType_Level3: EnumInvestmentObjectiveType
EnumInvestmentObjectiveType_Level4: EnumInvestmentObjectiveType
EnumInvestingExperienceType_Undefined: EnumInvestingExperienceType
EnumInvestingExperienceType_NoneInvestingExperience: EnumInvestingExperienceType
EnumInvestingExperienceType_Limited: EnumInvestingExperienceType
EnumInvestingExperienceType_Good: EnumInvestingExperienceType
EnumInvestingExperienceType_Extensive: EnumInvestingExperienceType
EnumRiskToleranceType_Undefined: EnumRiskToleranceType
EnumRiskToleranceType_Low: EnumRiskToleranceType
EnumRiskToleranceType_MediumLow: EnumRiskToleranceType
EnumRiskToleranceType_MediumHigh: EnumRiskToleranceType
EnumRiskToleranceType_High: EnumRiskToleranceType
EnumAddressType_Undefined: EnumAddressType
EnumAddressType_Mailing: EnumAddressType
EnumAddressType_Permanent: EnumAddressType
EnumAddressType_MailingSameAsPermanent: EnumAddressType
EnumPhoneType_Undefined: EnumPhoneType
EnumPhoneType_Primary: EnumPhoneType
EnumEducationType_Undefined: EnumEducationType
EnumEducationType_HighSchool: EnumEducationType
EnumEducationType_College: EnumEducationType
EnumEducationType_AssociateDegree: EnumEducationType
EnumEducationType_Bachelor: EnumEducationType
EnumEducationType_Masters: EnumEducationType
EnumEducationType_Professional: EnumEducationType
EnumCommoditiesType_Undefined: EnumCommoditiesType
EnumCommoditiesType_FinancialOrCurrency: EnumCommoditiesType
EnumCommoditiesType_Metals: EnumCommoditiesType
EnumCommoditiesType_Ags: EnumCommoditiesType
EnumCommoditiesType_StockIndices: EnumCommoditiesType
EnumCommoditiesType_Other: EnumCommoditiesType
EnumNatureOfTrading_Undefined: EnumNatureOfTrading
EnumNatureOfTrading_Discretionary: EnumNatureOfTrading
EnumNatureOfTrading_NonDiscretionary: EnumNatureOfTrading
EnumTradingObjective_Undefined: EnumTradingObjective
EnumTradingObjective_Speculation: EnumTradingObjective
EnumTradingObjective_Hedging: EnumTradingObjective
