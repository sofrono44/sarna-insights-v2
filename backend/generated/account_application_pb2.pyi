from google.protobuf import timestamp_pb2 as _timestamp_pb2
import common_pb2 as _common_pb2
import accounts_enums_pb2 as _accounts_enums_pb2
import account_application_enums_pb2 as _account_application_enums_pb2
import common_enums_pb2 as _common_enums_pb2
import market_data_entitlement_pb2 as _market_data_entitlement_pb2
import common_pb2 as _common_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
from common_pb2 import ResponseError as ResponseError
from common_pb2 import ResponseWarning as ResponseWarning
from common_pb2 import ResponseMessage as ResponseMessage
from common_pb2 import MOVEShockInput as MOVEShockInput
from common_pb2 import MOVECreditSpreadShockInput as MOVECreditSpreadShockInput
from common_pb2 import YieldShockInput as YieldShockInput
from market_data_entitlement_pb2 import MarketDataEntitlementFormQuestions as MarketDataEntitlementFormQuestions
from market_data_entitlement_pb2 import MarketDataEntitlementFormQuestion as MarketDataEntitlementFormQuestion
from market_data_entitlement_pb2 import MarketDataEntitlementFormResponsesResponse as MarketDataEntitlementFormResponsesResponse
from market_data_entitlement_pb2 import MarketDataEntitlementFormResponses as MarketDataEntitlementFormResponses
from market_data_entitlement_pb2 import MarketDataEntitlementFormResponse as MarketDataEntitlementFormResponse

DESCRIPTOR: _descriptor.FileDescriptor

class EnumCreateAccountApplicationRequestType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumCreateAccountApplicationRequestType_Undefined: _ClassVar[EnumCreateAccountApplicationRequestType]
    EnumCreateAccountApplicationRequestType_CreateAccount: _ClassVar[EnumCreateAccountApplicationRequestType]
    EnumCreateAccountApplicationRequestType_CreateAdditionalAccount: _ClassVar[EnumCreateAccountApplicationRequestType]
EnumCreateAccountApplicationRequestType_Undefined: EnumCreateAccountApplicationRequestType
EnumCreateAccountApplicationRequestType_CreateAccount: EnumCreateAccountApplicationRequestType
EnumCreateAccountApplicationRequestType_CreateAdditionalAccount: EnumCreateAccountApplicationRequestType

class CreateAccountApplicationRequest(_message.Message):
    __slots__ = ("RequestType", "Person", "SecurityQuestions", "TrustedContact", "Addresses", "MarketDataEntitlementFormResponses", "Account", "Employment", "FederalDisclosures", "ApproximateAnnualIncome", "InvestmentObjective", "TotalNetWorth", "InvestingExperienceStocks", "InvestingExperienceOptions", "InvestingExperienceFutures", "RiskTolerance", "Consent", "AccountApplicationSummary", "LiquidNetWorth", "ExternalBrokerageAccountInfo")
    REQUESTTYPE_FIELD_NUMBER: _ClassVar[int]
    PERSON_FIELD_NUMBER: _ClassVar[int]
    SECURITYQUESTIONS_FIELD_NUMBER: _ClassVar[int]
    TRUSTEDCONTACT_FIELD_NUMBER: _ClassVar[int]
    ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    MARKETDATAENTITLEMENTFORMRESPONSES_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    EMPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    FEDERALDISCLOSURES_FIELD_NUMBER: _ClassVar[int]
    APPROXIMATEANNUALINCOME_FIELD_NUMBER: _ClassVar[int]
    INVESTMENTOBJECTIVE_FIELD_NUMBER: _ClassVar[int]
    TOTALNETWORTH_FIELD_NUMBER: _ClassVar[int]
    INVESTINGEXPERIENCESTOCKS_FIELD_NUMBER: _ClassVar[int]
    INVESTINGEXPERIENCEOPTIONS_FIELD_NUMBER: _ClassVar[int]
    INVESTINGEXPERIENCEFUTURES_FIELD_NUMBER: _ClassVar[int]
    RISKTOLERANCE_FIELD_NUMBER: _ClassVar[int]
    CONSENT_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTAPPLICATIONSUMMARY_FIELD_NUMBER: _ClassVar[int]
    LIQUIDNETWORTH_FIELD_NUMBER: _ClassVar[int]
    EXTERNALBROKERAGEACCOUNTINFO_FIELD_NUMBER: _ClassVar[int]
    RequestType: EnumCreateAccountApplicationRequestType
    Person: AccountApplicationPersonRequest
    SecurityQuestions: SecurityQuestionUserResponseRequest
    TrustedContact: CreateTrustedContactRequest
    Addresses: _containers.RepeatedCompositeFieldContainer[CreateAddressRequest]
    MarketDataEntitlementFormResponses: _market_data_entitlement_pb2.MarketDataEntitlementFormResponses
    Account: AccountApplicationAccountRequest
    Employment: Employment
    FederalDisclosures: FederalDisclosure
    ApproximateAnnualIncome: int
    InvestmentObjective: _account_application_enums_pb2.EnumInvestmentObjectiveType
    TotalNetWorth: int
    InvestingExperienceStocks: _account_application_enums_pb2.EnumInvestingExperienceType
    InvestingExperienceOptions: _account_application_enums_pb2.EnumInvestingExperienceType
    InvestingExperienceFutures: _account_application_enums_pb2.EnumInvestingExperienceType
    RiskTolerance: _account_application_enums_pb2.EnumRiskToleranceType
    Consent: ConsentRequest
    AccountApplicationSummary: str
    LiquidNetWorth: int
    ExternalBrokerageAccountInfo: ExternalBrokerageAccountInfo
    def __init__(self, RequestType: _Optional[_Union[EnumCreateAccountApplicationRequestType, str]] = ..., Person: _Optional[_Union[AccountApplicationPersonRequest, _Mapping]] = ..., SecurityQuestions: _Optional[_Union[SecurityQuestionUserResponseRequest, _Mapping]] = ..., TrustedContact: _Optional[_Union[CreateTrustedContactRequest, _Mapping]] = ..., Addresses: _Optional[_Iterable[_Union[CreateAddressRequest, _Mapping]]] = ..., MarketDataEntitlementFormResponses: _Optional[_Union[_market_data_entitlement_pb2.MarketDataEntitlementFormResponses, _Mapping]] = ..., Account: _Optional[_Union[AccountApplicationAccountRequest, _Mapping]] = ..., Employment: _Optional[_Union[Employment, _Mapping]] = ..., FederalDisclosures: _Optional[_Union[FederalDisclosure, _Mapping]] = ..., ApproximateAnnualIncome: _Optional[int] = ..., InvestmentObjective: _Optional[_Union[_account_application_enums_pb2.EnumInvestmentObjectiveType, str]] = ..., TotalNetWorth: _Optional[int] = ..., InvestingExperienceStocks: _Optional[_Union[_account_application_enums_pb2.EnumInvestingExperienceType, str]] = ..., InvestingExperienceOptions: _Optional[_Union[_account_application_enums_pb2.EnumInvestingExperienceType, str]] = ..., InvestingExperienceFutures: _Optional[_Union[_account_application_enums_pb2.EnumInvestingExperienceType, str]] = ..., RiskTolerance: _Optional[_Union[_account_application_enums_pb2.EnumRiskToleranceType, str]] = ..., Consent: _Optional[_Union[ConsentRequest, _Mapping]] = ..., AccountApplicationSummary: _Optional[str] = ..., LiquidNetWorth: _Optional[int] = ..., ExternalBrokerageAccountInfo: _Optional[_Union[ExternalBrokerageAccountInfo, _Mapping]] = ...) -> None: ...

class AccountApplicationAddressesRequest(_message.Message):
    __slots__ = ("DateOfBirth", "Addresses")
    DATEOFBIRTH_FIELD_NUMBER: _ClassVar[int]
    ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    DateOfBirth: _timestamp_pb2.Timestamp
    Addresses: _containers.RepeatedCompositeFieldContainer[CreateAddressRequest]
    def __init__(self, DateOfBirth: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., Addresses: _Optional[_Iterable[_Union[CreateAddressRequest, _Mapping]]] = ...) -> None: ...

class AccountApplicationInvestmentProfileRequest(_message.Message):
    __slots__ = ("ApproximateAnnualIncome", "InvestmentObjective", "TotalNetWorth", "InvestingExperienceStocks", "InvestingExperienceOptions", "InvestingExperienceFutures", "RiskTolerance", "InvestmentProfileRequestType", "LiquidNetWorth")
    APPROXIMATEANNUALINCOME_FIELD_NUMBER: _ClassVar[int]
    INVESTMENTOBJECTIVE_FIELD_NUMBER: _ClassVar[int]
    TOTALNETWORTH_FIELD_NUMBER: _ClassVar[int]
    INVESTINGEXPERIENCESTOCKS_FIELD_NUMBER: _ClassVar[int]
    INVESTINGEXPERIENCEOPTIONS_FIELD_NUMBER: _ClassVar[int]
    INVESTINGEXPERIENCEFUTURES_FIELD_NUMBER: _ClassVar[int]
    RISKTOLERANCE_FIELD_NUMBER: _ClassVar[int]
    INVESTMENTPROFILEREQUESTTYPE_FIELD_NUMBER: _ClassVar[int]
    LIQUIDNETWORTH_FIELD_NUMBER: _ClassVar[int]
    ApproximateAnnualIncome: int
    InvestmentObjective: _account_application_enums_pb2.EnumInvestmentObjectiveType
    TotalNetWorth: int
    InvestingExperienceStocks: _account_application_enums_pb2.EnumInvestingExperienceType
    InvestingExperienceOptions: _account_application_enums_pb2.EnumInvestingExperienceType
    InvestingExperienceFutures: _account_application_enums_pb2.EnumInvestingExperienceType
    RiskTolerance: _account_application_enums_pb2.EnumRiskToleranceType
    InvestmentProfileRequestType: _account_application_enums_pb2.EnumAccountApplicationInvestmentProfileRequestType
    LiquidNetWorth: int
    def __init__(self, ApproximateAnnualIncome: _Optional[int] = ..., InvestmentObjective: _Optional[_Union[_account_application_enums_pb2.EnumInvestmentObjectiveType, str]] = ..., TotalNetWorth: _Optional[int] = ..., InvestingExperienceStocks: _Optional[_Union[_account_application_enums_pb2.EnumInvestingExperienceType, str]] = ..., InvestingExperienceOptions: _Optional[_Union[_account_application_enums_pb2.EnumInvestingExperienceType, str]] = ..., InvestingExperienceFutures: _Optional[_Union[_account_application_enums_pb2.EnumInvestingExperienceType, str]] = ..., RiskTolerance: _Optional[_Union[_account_application_enums_pb2.EnumRiskToleranceType, str]] = ..., InvestmentProfileRequestType: _Optional[_Union[_account_application_enums_pb2.EnumAccountApplicationInvestmentProfileRequestType, str]] = ..., LiquidNetWorth: _Optional[int] = ...) -> None: ...

class VerificationSessionResponse(_message.Message):
    __slots__ = ("VerificationSessionId", "CreatedTime", "ValidationUrl", "Warnings", "Errors")
    VERIFICATIONSESSIONID_FIELD_NUMBER: _ClassVar[int]
    CREATEDTIME_FIELD_NUMBER: _ClassVar[int]
    VALIDATIONURL_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    VerificationSessionId: str
    CreatedTime: _timestamp_pb2.Timestamp
    ValidationUrl: str
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2_1.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2_1.ResponseError]
    def __init__(self, VerificationSessionId: _Optional[str] = ..., CreatedTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ValidationUrl: _Optional[str] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2_1.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2_1.ResponseError, _Mapping]]] = ...) -> None: ...

class GetInvestmentProfileResponse(_message.Message):
    __slots__ = ("Employment", "FederalDisclosures", "ApproximateAnnualIncome", "InvestmentObjective", "TotalNetWorth", "InvestingExperienceStocks", "InvestingExperienceOptions", "InvestingExperienceFutures", "RiskTolerance", "LiquidNetWorth", "Warnings", "Errors")
    EMPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    FEDERALDISCLOSURES_FIELD_NUMBER: _ClassVar[int]
    APPROXIMATEANNUALINCOME_FIELD_NUMBER: _ClassVar[int]
    INVESTMENTOBJECTIVE_FIELD_NUMBER: _ClassVar[int]
    TOTALNETWORTH_FIELD_NUMBER: _ClassVar[int]
    INVESTINGEXPERIENCESTOCKS_FIELD_NUMBER: _ClassVar[int]
    INVESTINGEXPERIENCEOPTIONS_FIELD_NUMBER: _ClassVar[int]
    INVESTINGEXPERIENCEFUTURES_FIELD_NUMBER: _ClassVar[int]
    RISKTOLERANCE_FIELD_NUMBER: _ClassVar[int]
    LIQUIDNETWORTH_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    Employment: Employment
    FederalDisclosures: FederalDisclosure
    ApproximateAnnualIncome: int
    InvestmentObjective: _account_application_enums_pb2.EnumInvestmentObjectiveType
    TotalNetWorth: int
    InvestingExperienceStocks: _account_application_enums_pb2.EnumInvestingExperienceType
    InvestingExperienceOptions: _account_application_enums_pb2.EnumInvestingExperienceType
    InvestingExperienceFutures: _account_application_enums_pb2.EnumInvestingExperienceType
    RiskTolerance: _account_application_enums_pb2.EnumRiskToleranceType
    LiquidNetWorth: int
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2_1.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2_1.ResponseError]
    def __init__(self, Employment: _Optional[_Union[Employment, _Mapping]] = ..., FederalDisclosures: _Optional[_Union[FederalDisclosure, _Mapping]] = ..., ApproximateAnnualIncome: _Optional[int] = ..., InvestmentObjective: _Optional[_Union[_account_application_enums_pb2.EnumInvestmentObjectiveType, str]] = ..., TotalNetWorth: _Optional[int] = ..., InvestingExperienceStocks: _Optional[_Union[_account_application_enums_pb2.EnumInvestingExperienceType, str]] = ..., InvestingExperienceOptions: _Optional[_Union[_account_application_enums_pb2.EnumInvestingExperienceType, str]] = ..., InvestingExperienceFutures: _Optional[_Union[_account_application_enums_pb2.EnumInvestingExperienceType, str]] = ..., RiskTolerance: _Optional[_Union[_account_application_enums_pb2.EnumRiskToleranceType, str]] = ..., LiquidNetWorth: _Optional[int] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2_1.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2_1.ResponseError, _Mapping]]] = ...) -> None: ...

class AccountApplicationResponse(_message.Message):
    __slots__ = ("Warnings", "Errors")
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2_1.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2_1.ResponseError]
    def __init__(self, Warnings: _Optional[_Iterable[_Union[_common_pb2_1.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2_1.ResponseError, _Mapping]]] = ...) -> None: ...

class AccountApplicationCreateVerificationSessionRequest(_message.Message):
    __slots__ = ("Person", "Addresses", "AccountApplicationSummary")
    PERSON_FIELD_NUMBER: _ClassVar[int]
    ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTAPPLICATIONSUMMARY_FIELD_NUMBER: _ClassVar[int]
    Person: AccountApplicationPersonRequest
    Addresses: _containers.RepeatedCompositeFieldContainer[CreateAddressRequest]
    AccountApplicationSummary: str
    def __init__(self, Person: _Optional[_Union[AccountApplicationPersonRequest, _Mapping]] = ..., Addresses: _Optional[_Iterable[_Union[CreateAddressRequest, _Mapping]]] = ..., AccountApplicationSummary: _Optional[str] = ...) -> None: ...

class ConsentRequest(_message.Message):
    __slots__ = ("DisclosuresAndAccountInformation", "TermsAndConditions", "W8BenForm", "W9Form", "OptionsAccountDisclosureAndAgreement", "ClearingHouseMarginAgreement", "ClearingHouseLetterA", "ClearingHouseDisclosureStatement", "FuturesAccountDisclosureAndAgreement1", "FuturesAccountDisclosureAndAgreement2")
    DISCLOSURESANDACCOUNTINFORMATION_FIELD_NUMBER: _ClassVar[int]
    TERMSANDCONDITIONS_FIELD_NUMBER: _ClassVar[int]
    W8BENFORM_FIELD_NUMBER: _ClassVar[int]
    W9FORM_FIELD_NUMBER: _ClassVar[int]
    OPTIONSACCOUNTDISCLOSUREANDAGREEMENT_FIELD_NUMBER: _ClassVar[int]
    CLEARINGHOUSEMARGINAGREEMENT_FIELD_NUMBER: _ClassVar[int]
    CLEARINGHOUSELETTERA_FIELD_NUMBER: _ClassVar[int]
    CLEARINGHOUSEDISCLOSURESTATEMENT_FIELD_NUMBER: _ClassVar[int]
    FUTURESACCOUNTDISCLOSUREANDAGREEMENT1_FIELD_NUMBER: _ClassVar[int]
    FUTURESACCOUNTDISCLOSUREANDAGREEMENT2_FIELD_NUMBER: _ClassVar[int]
    DisclosuresAndAccountInformation: bool
    TermsAndConditions: bool
    W8BenForm: bool
    W9Form: bool
    OptionsAccountDisclosureAndAgreement: bool
    ClearingHouseMarginAgreement: bool
    ClearingHouseLetterA: bool
    ClearingHouseDisclosureStatement: bool
    FuturesAccountDisclosureAndAgreement1: bool
    FuturesAccountDisclosureAndAgreement2: bool
    def __init__(self, DisclosuresAndAccountInformation: bool = ..., TermsAndConditions: bool = ..., W8BenForm: bool = ..., W9Form: bool = ..., OptionsAccountDisclosureAndAgreement: bool = ..., ClearingHouseMarginAgreement: bool = ..., ClearingHouseLetterA: bool = ..., ClearingHouseDisclosureStatement: bool = ..., FuturesAccountDisclosureAndAgreement1: bool = ..., FuturesAccountDisclosureAndAgreement2: bool = ...) -> None: ...

class Person(_message.Message):
    __slots__ = ("PersonId",)
    PERSONID_FIELD_NUMBER: _ClassVar[int]
    PersonId: int
    def __init__(self, PersonId: _Optional[int] = ...) -> None: ...

class CreateTrustedContactRequest(_message.Message):
    __slots__ = ("FirstName", "LastName", "Relationship", "Email", "Address", "AddressLineTwo", "City", "State", "ZipPostalCode", "Country", "PhoneNumber")
    FIRSTNAME_FIELD_NUMBER: _ClassVar[int]
    LASTNAME_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIP_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ADDRESSLINETWO_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ZIPPOSTALCODE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    PHONENUMBER_FIELD_NUMBER: _ClassVar[int]
    FirstName: str
    LastName: str
    Relationship: _account_application_enums_pb2.EnumTrustedContactRelationshipType
    Email: str
    Address: str
    AddressLineTwo: str
    City: str
    State: int
    ZipPostalCode: str
    Country: int
    PhoneNumber: str
    def __init__(self, FirstName: _Optional[str] = ..., LastName: _Optional[str] = ..., Relationship: _Optional[_Union[_account_application_enums_pb2.EnumTrustedContactRelationshipType, str]] = ..., Email: _Optional[str] = ..., Address: _Optional[str] = ..., AddressLineTwo: _Optional[str] = ..., City: _Optional[str] = ..., State: _Optional[int] = ..., ZipPostalCode: _Optional[str] = ..., Country: _Optional[int] = ..., PhoneNumber: _Optional[str] = ...) -> None: ...

class AccountApplicationPersonRequest(_message.Message):
    __slots__ = ("FirstName", "MiddleName", "LastName", "Suffix", "DateOfBirth", "MaritalStatus", "USCitizenshipStatus", "IdentificationNumber", "TaxationCountry", "Citizenship", "Language", "IrsWithholding", "Phones", "NumberOfDependents", "EducationType")
    FIRSTNAME_FIELD_NUMBER: _ClassVar[int]
    MIDDLENAME_FIELD_NUMBER: _ClassVar[int]
    LASTNAME_FIELD_NUMBER: _ClassVar[int]
    SUFFIX_FIELD_NUMBER: _ClassVar[int]
    DATEOFBIRTH_FIELD_NUMBER: _ClassVar[int]
    MARITALSTATUS_FIELD_NUMBER: _ClassVar[int]
    USCITIZENSHIPSTATUS_FIELD_NUMBER: _ClassVar[int]
    IDENTIFICATIONNUMBER_FIELD_NUMBER: _ClassVar[int]
    TAXATIONCOUNTRY_FIELD_NUMBER: _ClassVar[int]
    CITIZENSHIP_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    IRSWITHHOLDING_FIELD_NUMBER: _ClassVar[int]
    PHONES_FIELD_NUMBER: _ClassVar[int]
    NUMBEROFDEPENDENTS_FIELD_NUMBER: _ClassVar[int]
    EDUCATIONTYPE_FIELD_NUMBER: _ClassVar[int]
    FirstName: str
    MiddleName: str
    LastName: str
    Suffix: str
    DateOfBirth: _timestamp_pb2.Timestamp
    MaritalStatus: _account_application_enums_pb2.EnumMaritalStatusType
    USCitizenshipStatus: _account_application_enums_pb2.EnumUSCitizenshipStatus
    IdentificationNumber: str
    TaxationCountry: int
    Citizenship: int
    Language: int
    IrsWithholding: bool
    Phones: _containers.RepeatedCompositeFieldContainer[Phone]
    NumberOfDependents: int
    EducationType: _account_application_enums_pb2.EnumEducationType
    def __init__(self, FirstName: _Optional[str] = ..., MiddleName: _Optional[str] = ..., LastName: _Optional[str] = ..., Suffix: _Optional[str] = ..., DateOfBirth: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., MaritalStatus: _Optional[_Union[_account_application_enums_pb2.EnumMaritalStatusType, str]] = ..., USCitizenshipStatus: _Optional[_Union[_account_application_enums_pb2.EnumUSCitizenshipStatus, str]] = ..., IdentificationNumber: _Optional[str] = ..., TaxationCountry: _Optional[int] = ..., Citizenship: _Optional[int] = ..., Language: _Optional[int] = ..., IrsWithholding: bool = ..., Phones: _Optional[_Iterable[_Union[Phone, _Mapping]]] = ..., NumberOfDependents: _Optional[int] = ..., EducationType: _Optional[_Union[_account_application_enums_pb2.EnumEducationType, str]] = ...) -> None: ...

class SecurityQuestions(_message.Message):
    __slots__ = ("SecurityQuestion", "Warnings", "Errors")
    SECURITYQUESTION_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    SecurityQuestion: _containers.RepeatedCompositeFieldContainer[SecurityQuestion]
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2_1.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2_1.ResponseError]
    def __init__(self, SecurityQuestion: _Optional[_Iterable[_Union[SecurityQuestion, _Mapping]]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2_1.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2_1.ResponseError, _Mapping]]] = ...) -> None: ...

class SecurityQuestion(_message.Message):
    __slots__ = ("Key", "Question")
    KEY_FIELD_NUMBER: _ClassVar[int]
    QUESTION_FIELD_NUMBER: _ClassVar[int]
    Key: str
    Question: str
    def __init__(self, Key: _Optional[str] = ..., Question: _Optional[str] = ...) -> None: ...

class SecurityQuestionUserResponseRequest(_message.Message):
    __slots__ = ("Question1Key", "Answer1", "Question2Key", "Answer2", "Question3Key", "Answer3")
    QUESTION1KEY_FIELD_NUMBER: _ClassVar[int]
    ANSWER1_FIELD_NUMBER: _ClassVar[int]
    QUESTION2KEY_FIELD_NUMBER: _ClassVar[int]
    ANSWER2_FIELD_NUMBER: _ClassVar[int]
    QUESTION3KEY_FIELD_NUMBER: _ClassVar[int]
    ANSWER3_FIELD_NUMBER: _ClassVar[int]
    Question1Key: str
    Answer1: str
    Question2Key: str
    Answer2: str
    Question3Key: str
    Answer3: str
    def __init__(self, Question1Key: _Optional[str] = ..., Answer1: _Optional[str] = ..., Question2Key: _Optional[str] = ..., Answer2: _Optional[str] = ..., Question3Key: _Optional[str] = ..., Answer3: _Optional[str] = ...) -> None: ...

class SecurityQuestionUserResponsesResponse(_message.Message):
    __slots__ = ("SecurityQuestionUserResponse", "Warnings", "Errors")
    SECURITYQUESTIONUSERRESPONSE_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    SecurityQuestionUserResponse: SecurityQuestionUserResponseRequest
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2_1.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2_1.ResponseError]
    def __init__(self, SecurityQuestionUserResponse: _Optional[_Union[SecurityQuestionUserResponseRequest, _Mapping]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2_1.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2_1.ResponseError, _Mapping]]] = ...) -> None: ...

class FederalDisclosure(_message.Message):
    __slots__ = ("FederalDisclosures",)
    FEDERALDISCLOSURES_FIELD_NUMBER: _ClassVar[int]
    FederalDisclosures: _containers.RepeatedScalarFieldContainer[_account_application_enums_pb2.EnumFederalDisclosure]
    def __init__(self, FederalDisclosures: _Optional[_Iterable[_Union[_account_application_enums_pb2.EnumFederalDisclosure, str]]] = ...) -> None: ...

class CreateAddressRequest(_message.Message):
    __slots__ = ("Address", "AddressLineTwo", "City", "State", "ZipPostalCode", "Country", "AddressType")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ADDRESSLINETWO_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ZIPPOSTALCODE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    ADDRESSTYPE_FIELD_NUMBER: _ClassVar[int]
    Address: str
    AddressLineTwo: str
    City: str
    State: int
    ZipPostalCode: str
    Country: int
    AddressType: _account_application_enums_pb2.EnumAddressType
    def __init__(self, Address: _Optional[str] = ..., AddressLineTwo: _Optional[str] = ..., City: _Optional[str] = ..., State: _Optional[int] = ..., ZipPostalCode: _Optional[str] = ..., Country: _Optional[int] = ..., AddressType: _Optional[_Union[_account_application_enums_pb2.EnumAddressType, str]] = ...) -> None: ...

class Phone(_message.Message):
    __slots__ = ("PhoneNumber", "PhoneType")
    PHONENUMBER_FIELD_NUMBER: _ClassVar[int]
    PHONETYPE_FIELD_NUMBER: _ClassVar[int]
    PhoneNumber: str
    PhoneType: _account_application_enums_pb2.EnumPhoneType
    def __init__(self, PhoneNumber: _Optional[str] = ..., PhoneType: _Optional[_Union[_account_application_enums_pb2.EnumPhoneType, str]] = ...) -> None: ...

class Employment(_message.Message):
    __slots__ = ("Type", "EmployerName", "Occupation", "CustomOccupation", "Position", "EmployerAddress", "NatureOfBusiness")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    EMPLOYERNAME_FIELD_NUMBER: _ClassVar[int]
    OCCUPATION_FIELD_NUMBER: _ClassVar[int]
    CUSTOMOCCUPATION_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    EMPLOYERADDRESS_FIELD_NUMBER: _ClassVar[int]
    NATUREOFBUSINESS_FIELD_NUMBER: _ClassVar[int]
    Type: _account_application_enums_pb2.EnumEmploymentType
    EmployerName: str
    Occupation: _account_application_enums_pb2.EnumOccupationType
    CustomOccupation: str
    Position: str
    EmployerAddress: str
    NatureOfBusiness: str
    def __init__(self, Type: _Optional[_Union[_account_application_enums_pb2.EnumEmploymentType, str]] = ..., EmployerName: _Optional[str] = ..., Occupation: _Optional[_Union[_account_application_enums_pb2.EnumOccupationType, str]] = ..., CustomOccupation: _Optional[str] = ..., Position: _Optional[str] = ..., EmployerAddress: _Optional[str] = ..., NatureOfBusiness: _Optional[str] = ...) -> None: ...

class AccountApplicationAccountRequest(_message.Message):
    __slots__ = ("AccountType", "Nickname", "TradingOptions", "TradingFutures", "AccountRiskType")
    ACCOUNTTYPE_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    TRADINGOPTIONS_FIELD_NUMBER: _ClassVar[int]
    TRADINGFUTURES_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTRISKTYPE_FIELD_NUMBER: _ClassVar[int]
    AccountType: _accounts_enums_pb2.EnumAccountType
    Nickname: str
    TradingOptions: bool
    TradingFutures: bool
    AccountRiskType: _common_enums_pb2.EnumAccountRiskType
    def __init__(self, AccountType: _Optional[_Union[_accounts_enums_pb2.EnumAccountType, str]] = ..., Nickname: _Optional[str] = ..., TradingOptions: bool = ..., TradingFutures: bool = ..., AccountRiskType: _Optional[_Union[_common_enums_pb2.EnumAccountRiskType, str]] = ...) -> None: ...

class GetExternalBrokerageAccountInfoResponse(_message.Message):
    __slots__ = ("ExternalBrokerageAccountInfo", "Warnings", "Errors")
    EXTERNALBROKERAGEACCOUNTINFO_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    ExternalBrokerageAccountInfo: ExternalBrokerageAccountInfo
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2_1.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2_1.ResponseError]
    def __init__(self, ExternalBrokerageAccountInfo: _Optional[_Union[ExternalBrokerageAccountInfo, _Mapping]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2_1.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2_1.ResponseError, _Mapping]]] = ...) -> None: ...

class ExternalBrokerageAccountInfo(_message.Message):
    __slots__ = ("ExternalBrokerageAccountDetails", "TradingObjective", "CommoditiesType", "NatureOfTrading", "CommoditiesOther")
    EXTERNALBROKERAGEACCOUNTDETAILS_FIELD_NUMBER: _ClassVar[int]
    TRADINGOBJECTIVE_FIELD_NUMBER: _ClassVar[int]
    COMMODITIESTYPE_FIELD_NUMBER: _ClassVar[int]
    NATUREOFTRADING_FIELD_NUMBER: _ClassVar[int]
    COMMODITIESOTHER_FIELD_NUMBER: _ClassVar[int]
    ExternalBrokerageAccountDetails: _containers.RepeatedCompositeFieldContainer[ExternalBrokerageAccountDetail]
    TradingObjective: _account_application_enums_pb2.EnumTradingObjective
    CommoditiesType: _account_application_enums_pb2.EnumCommoditiesType
    NatureOfTrading: _account_application_enums_pb2.EnumNatureOfTrading
    CommoditiesOther: str
    def __init__(self, ExternalBrokerageAccountDetails: _Optional[_Iterable[_Union[ExternalBrokerageAccountDetail, _Mapping]]] = ..., TradingObjective: _Optional[_Union[_account_application_enums_pb2.EnumTradingObjective, str]] = ..., CommoditiesType: _Optional[_Union[_account_application_enums_pb2.EnumCommoditiesType, str]] = ..., NatureOfTrading: _Optional[_Union[_account_application_enums_pb2.EnumNatureOfTrading, str]] = ..., CommoditiesOther: _Optional[str] = ...) -> None: ...

class ExternalBrokerageAccountDetail(_message.Message):
    __slots__ = ("AccountName", "IsActive", "AverageEquity")
    ACCOUNTNAME_FIELD_NUMBER: _ClassVar[int]
    ISACTIVE_FIELD_NUMBER: _ClassVar[int]
    AVERAGEEQUITY_FIELD_NUMBER: _ClassVar[int]
    AccountName: str
    IsActive: bool
    AverageEquity: int
    def __init__(self, AccountName: _Optional[str] = ..., IsActive: bool = ..., AverageEquity: _Optional[int] = ...) -> None: ...
