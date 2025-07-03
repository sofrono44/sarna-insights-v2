from google.protobuf import empty_pb2 as _empty_pb2
import common_pb2 as _common_pb2
import notifications_enums_pb2 as _notifications_enums_pb2
import account_application_enums_pb2 as _account_application_enums_pb2
import user_data_enums_pb2 as _user_data_enums_pb2
import account_application_pb2 as _account_application_pb2
import common_pb2 as _common_pb2_1
import market_data_entitlement_pb2 as _market_data_entitlement_pb2
import market_data_entitlement_pb2 as _market_data_entitlement_pb2_1
import common_pb2 as _common_pb2_1_1
import sessions_enums_pb2 as _sessions_enums_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserDataRequest(_message.Message):
    __slots__ = ("UserDataRequestType", "GetUserProfile", "UpdateUserProfileRequest", "UpdateUserEmailRequest", "GetInvestmentProfile", "GetAllSecurityQuestions", "GetAllMdeFormQuestions", "UpdateMdeFormUserResponses", "GetMdeFormResponses", "DeleteMdeFormQuestionsUserResponses", "GetSecurityQuestionUserResponses", "UpdateSecurityQuestionUserResponses", "GetUserNotificationPreferences", "UpdateUserNotificationPreferencesRequest", "GetUserPreferencesRequest", "UpdateUserPreferencesRequest")
    USERDATAREQUESTTYPE_FIELD_NUMBER: _ClassVar[int]
    GETUSERPROFILE_FIELD_NUMBER: _ClassVar[int]
    UPDATEUSERPROFILEREQUEST_FIELD_NUMBER: _ClassVar[int]
    UPDATEUSEREMAILREQUEST_FIELD_NUMBER: _ClassVar[int]
    GETINVESTMENTPROFILE_FIELD_NUMBER: _ClassVar[int]
    GETALLSECURITYQUESTIONS_FIELD_NUMBER: _ClassVar[int]
    GETALLMDEFORMQUESTIONS_FIELD_NUMBER: _ClassVar[int]
    UPDATEMDEFORMUSERRESPONSES_FIELD_NUMBER: _ClassVar[int]
    GETMDEFORMRESPONSES_FIELD_NUMBER: _ClassVar[int]
    DELETEMDEFORMQUESTIONSUSERRESPONSES_FIELD_NUMBER: _ClassVar[int]
    GETSECURITYQUESTIONUSERRESPONSES_FIELD_NUMBER: _ClassVar[int]
    UPDATESECURITYQUESTIONUSERRESPONSES_FIELD_NUMBER: _ClassVar[int]
    GETUSERNOTIFICATIONPREFERENCES_FIELD_NUMBER: _ClassVar[int]
    UPDATEUSERNOTIFICATIONPREFERENCESREQUEST_FIELD_NUMBER: _ClassVar[int]
    GETUSERPREFERENCESREQUEST_FIELD_NUMBER: _ClassVar[int]
    UPDATEUSERPREFERENCESREQUEST_FIELD_NUMBER: _ClassVar[int]
    UserDataRequestType: _user_data_enums_pb2.EnumUserDataRequestType
    GetUserProfile: _empty_pb2.Empty
    UpdateUserProfileRequest: UpdateUserProfileRequest
    UpdateUserEmailRequest: UpdateUserEmailRequest
    GetInvestmentProfile: _empty_pb2.Empty
    GetAllSecurityQuestions: _empty_pb2.Empty
    GetAllMdeFormQuestions: _empty_pb2.Empty
    UpdateMdeFormUserResponses: _market_data_entitlement_pb2_1.MarketDataEntitlementFormResponses
    GetMdeFormResponses: _empty_pb2.Empty
    DeleteMdeFormQuestionsUserResponses: _empty_pb2.Empty
    GetSecurityQuestionUserResponses: _empty_pb2.Empty
    UpdateSecurityQuestionUserResponses: _account_application_pb2.SecurityQuestionUserResponseRequest
    GetUserNotificationPreferences: _empty_pb2.Empty
    UpdateUserNotificationPreferencesRequest: UpdateUserNotificationPreferencesRequest
    GetUserPreferencesRequest: GetUserPreferencesRequest
    UpdateUserPreferencesRequest: UpdateUserPreferencesRequest
    def __init__(self, UserDataRequestType: _Optional[_Union[_user_data_enums_pb2.EnumUserDataRequestType, str]] = ..., GetUserProfile: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., UpdateUserProfileRequest: _Optional[_Union[UpdateUserProfileRequest, _Mapping]] = ..., UpdateUserEmailRequest: _Optional[_Union[UpdateUserEmailRequest, _Mapping]] = ..., GetInvestmentProfile: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., GetAllSecurityQuestions: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., GetAllMdeFormQuestions: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., UpdateMdeFormUserResponses: _Optional[_Union[_market_data_entitlement_pb2_1.MarketDataEntitlementFormResponses, _Mapping]] = ..., GetMdeFormResponses: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., DeleteMdeFormQuestionsUserResponses: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., GetSecurityQuestionUserResponses: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., UpdateSecurityQuestionUserResponses: _Optional[_Union[_account_application_pb2.SecurityQuestionUserResponseRequest, _Mapping]] = ..., GetUserNotificationPreferences: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., UpdateUserNotificationPreferencesRequest: _Optional[_Union[UpdateUserNotificationPreferencesRequest, _Mapping]] = ..., GetUserPreferencesRequest: _Optional[_Union[GetUserPreferencesRequest, _Mapping]] = ..., UpdateUserPreferencesRequest: _Optional[_Union[UpdateUserPreferencesRequest, _Mapping]] = ...) -> None: ...

class UserDataResponse(_message.Message):
    __slots__ = ("GetUserProfileResponse", "GetInvestmentProfileResponse", "SecurityQuestions", "MarketDataEntitlementFormQuestions", "MarketDataEntitlementFormResponses", "SecurityQuestionUserResponse", "GetUserNotificationPreferencesResponse", "GetUserPreferencesResponse", "GetExternalBrokerageAccountInfoResponse")
    GETUSERPROFILERESPONSE_FIELD_NUMBER: _ClassVar[int]
    GETINVESTMENTPROFILERESPONSE_FIELD_NUMBER: _ClassVar[int]
    SECURITYQUESTIONS_FIELD_NUMBER: _ClassVar[int]
    MARKETDATAENTITLEMENTFORMQUESTIONS_FIELD_NUMBER: _ClassVar[int]
    MARKETDATAENTITLEMENTFORMRESPONSES_FIELD_NUMBER: _ClassVar[int]
    SECURITYQUESTIONUSERRESPONSE_FIELD_NUMBER: _ClassVar[int]
    GETUSERNOTIFICATIONPREFERENCESRESPONSE_FIELD_NUMBER: _ClassVar[int]
    GETUSERPREFERENCESRESPONSE_FIELD_NUMBER: _ClassVar[int]
    GETEXTERNALBROKERAGEACCOUNTINFORESPONSE_FIELD_NUMBER: _ClassVar[int]
    GetUserProfileResponse: GetUserProfileResponse
    GetInvestmentProfileResponse: _account_application_pb2.GetInvestmentProfileResponse
    SecurityQuestions: _account_application_pb2.SecurityQuestions
    MarketDataEntitlementFormQuestions: _market_data_entitlement_pb2_1.MarketDataEntitlementFormQuestions
    MarketDataEntitlementFormResponses: _market_data_entitlement_pb2_1.MarketDataEntitlementFormResponses
    SecurityQuestionUserResponse: _account_application_pb2.SecurityQuestionUserResponseRequest
    GetUserNotificationPreferencesResponse: GetUserNotificationPreferencesResponse
    GetUserPreferencesResponse: GetUserPreferencesResponse
    GetExternalBrokerageAccountInfoResponse: _account_application_pb2.GetExternalBrokerageAccountInfoResponse
    def __init__(self, GetUserProfileResponse: _Optional[_Union[GetUserProfileResponse, _Mapping]] = ..., GetInvestmentProfileResponse: _Optional[_Union[_account_application_pb2.GetInvestmentProfileResponse, _Mapping]] = ..., SecurityQuestions: _Optional[_Union[_account_application_pb2.SecurityQuestions, _Mapping]] = ..., MarketDataEntitlementFormQuestions: _Optional[_Union[_market_data_entitlement_pb2_1.MarketDataEntitlementFormQuestions, _Mapping]] = ..., MarketDataEntitlementFormResponses: _Optional[_Union[_market_data_entitlement_pb2_1.MarketDataEntitlementFormResponses, _Mapping]] = ..., SecurityQuestionUserResponse: _Optional[_Union[_account_application_pb2.SecurityQuestionUserResponseRequest, _Mapping]] = ..., GetUserNotificationPreferencesResponse: _Optional[_Union[GetUserNotificationPreferencesResponse, _Mapping]] = ..., GetUserPreferencesResponse: _Optional[_Union[GetUserPreferencesResponse, _Mapping]] = ..., GetExternalBrokerageAccountInfoResponse: _Optional[_Union[_account_application_pb2.GetExternalBrokerageAccountInfoResponse, _Mapping]] = ...) -> None: ...

class GetUserProfileResponse(_message.Message):
    __slots__ = ("Profile", "Warnings", "Errors")
    PROFILE_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    Profile: UserProfile
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2_1_1.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2_1_1.ResponseError]
    def __init__(self, Profile: _Optional[_Union[UserProfile, _Mapping]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2_1_1.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2_1_1.ResponseError, _Mapping]]] = ...) -> None: ...

class UserProfile(_message.Message):
    __slots__ = ("FirstName", "MiddleName", "LastName", "Suffix", "PhoneNumbers", "NationalIdNumber", "Addresses")
    FIRSTNAME_FIELD_NUMBER: _ClassVar[int]
    MIDDLENAME_FIELD_NUMBER: _ClassVar[int]
    LASTNAME_FIELD_NUMBER: _ClassVar[int]
    SUFFIX_FIELD_NUMBER: _ClassVar[int]
    PHONENUMBERS_FIELD_NUMBER: _ClassVar[int]
    NATIONALIDNUMBER_FIELD_NUMBER: _ClassVar[int]
    ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    FirstName: str
    MiddleName: str
    LastName: str
    Suffix: str
    PhoneNumbers: _containers.RepeatedCompositeFieldContainer[PhoneNumber]
    NationalIdNumber: str
    Addresses: _containers.RepeatedCompositeFieldContainer[Address]
    def __init__(self, FirstName: _Optional[str] = ..., MiddleName: _Optional[str] = ..., LastName: _Optional[str] = ..., Suffix: _Optional[str] = ..., PhoneNumbers: _Optional[_Iterable[_Union[PhoneNumber, _Mapping]]] = ..., NationalIdNumber: _Optional[str] = ..., Addresses: _Optional[_Iterable[_Union[Address, _Mapping]]] = ...) -> None: ...

class Address(_message.Message):
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

class PhoneNumber(_message.Message):
    __slots__ = ("PhoneNumber", "PhoneType")
    PHONENUMBER_FIELD_NUMBER: _ClassVar[int]
    PHONETYPE_FIELD_NUMBER: _ClassVar[int]
    PhoneNumber: str
    PhoneType: _account_application_enums_pb2.EnumPhoneType
    def __init__(self, PhoneNumber: _Optional[str] = ..., PhoneType: _Optional[_Union[_account_application_enums_pb2.EnumPhoneType, str]] = ...) -> None: ...

class UpdateUserProfileRequest(_message.Message):
    __slots__ = ("Profile",)
    PROFILE_FIELD_NUMBER: _ClassVar[int]
    Profile: UserProfile
    def __init__(self, Profile: _Optional[_Union[UserProfile, _Mapping]] = ...) -> None: ...

class UpdateUserEmailRequest(_message.Message):
    __slots__ = ("Email",)
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    Email: str
    def __init__(self, Email: _Optional[str] = ...) -> None: ...

class GetUserNotificationPreferencesResponse(_message.Message):
    __slots__ = ("NotificationPreferences", "Warnings", "Errors")
    NOTIFICATIONPREFERENCES_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    NotificationPreferences: _containers.RepeatedCompositeFieldContainer[NotificationPreferences]
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2_1_1.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2_1_1.ResponseError]
    def __init__(self, NotificationPreferences: _Optional[_Iterable[_Union[NotificationPreferences, _Mapping]]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2_1_1.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2_1_1.ResponseError, _Mapping]]] = ...) -> None: ...

class NotificationPreferences(_message.Message):
    __slots__ = ("EventType", "Email", "Push")
    EVENTTYPE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PUSH_FIELD_NUMBER: _ClassVar[int]
    EventType: _notifications_enums_pb2.EnumNotificationType
    Email: bool
    Push: bool
    def __init__(self, EventType: _Optional[_Union[_notifications_enums_pb2.EnumNotificationType, str]] = ..., Email: bool = ..., Push: bool = ...) -> None: ...

class UpdateUserNotificationPreferencesRequest(_message.Message):
    __slots__ = ("NotificationPreferences",)
    NOTIFICATIONPREFERENCES_FIELD_NUMBER: _ClassVar[int]
    NotificationPreferences: _containers.RepeatedCompositeFieldContainer[NotificationPreferences]
    def __init__(self, NotificationPreferences: _Optional[_Iterable[_Union[NotificationPreferences, _Mapping]]] = ...) -> None: ...

class GetUserPreferencesRequest(_message.Message):
    __slots__ = ("PreferenceTypes",)
    PREFERENCETYPES_FIELD_NUMBER: _ClassVar[int]
    PreferenceTypes: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, PreferenceTypes: _Optional[_Iterable[int]] = ...) -> None: ...

class GetUserPreferencesResponse(_message.Message):
    __slots__ = ("Preferences", "LanguageCode", "CountryCode", "UserPermissions", "Warnings", "Errors")
    PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    LANGUAGECODE_FIELD_NUMBER: _ClassVar[int]
    COUNTRYCODE_FIELD_NUMBER: _ClassVar[int]
    USERPERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    Preferences: _containers.RepeatedCompositeFieldContainer[Preferences]
    LanguageCode: str
    CountryCode: str
    UserPermissions: _containers.RepeatedScalarFieldContainer[_sessions_enums_pb2.EnumUserPermission]
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2_1_1.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2_1_1.ResponseError]
    def __init__(self, Preferences: _Optional[_Iterable[_Union[Preferences, _Mapping]]] = ..., LanguageCode: _Optional[str] = ..., CountryCode: _Optional[str] = ..., UserPermissions: _Optional[_Iterable[_Union[_sessions_enums_pb2.EnumUserPermission, str]]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2_1_1.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2_1_1.ResponseError, _Mapping]]] = ...) -> None: ...

class Preferences(_message.Message):
    __slots__ = ("Type", "Value")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    Type: int
    Value: str
    def __init__(self, Type: _Optional[int] = ..., Value: _Optional[str] = ...) -> None: ...

class UpdateUserPreferencesRequest(_message.Message):
    __slots__ = ("Preferences", "LanguageCode")
    PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    LANGUAGECODE_FIELD_NUMBER: _ClassVar[int]
    Preferences: _containers.RepeatedCompositeFieldContainer[Preferences]
    LanguageCode: str
    def __init__(self, Preferences: _Optional[_Iterable[_Union[Preferences, _Mapping]]] = ..., LanguageCode: _Optional[str] = ...) -> None: ...
