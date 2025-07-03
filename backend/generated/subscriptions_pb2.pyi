import common_pb2 as _common_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
import api_hub_enums_pb2 as _api_hub_enums_pb2
import commissions_pb2 as _commissions_pb2
import account_maintenance_fee_pb2 as _account_maintenance_fee_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SubscriptionRequest(_message.Message):
    __slots__ = ("SubscriptionRequestType", "UserStatusCheckRequest", "UserPlatformSubscriptionActivationRequest", "UserPlatformSubscriptionDeactivationRequest", "PromoClaimRequest")
    SUBSCRIPTIONREQUESTTYPE_FIELD_NUMBER: _ClassVar[int]
    USERSTATUSCHECKREQUEST_FIELD_NUMBER: _ClassVar[int]
    USERPLATFORMSUBSCRIPTIONACTIVATIONREQUEST_FIELD_NUMBER: _ClassVar[int]
    USERPLATFORMSUBSCRIPTIONDEACTIVATIONREQUEST_FIELD_NUMBER: _ClassVar[int]
    PROMOCLAIMREQUEST_FIELD_NUMBER: _ClassVar[int]
    SubscriptionRequestType: _api_hub_enums_pb2.EnumSubscriptionRequestType
    UserStatusCheckRequest: UserStatusCheckRequest
    UserPlatformSubscriptionActivationRequest: UserPlatformSubscriptionActivationRequest
    UserPlatformSubscriptionDeactivationRequest: UserPlatformSubscriptionDeactivationRequest
    PromoClaimRequest: PromoClaimRequest
    def __init__(self, SubscriptionRequestType: _Optional[_Union[_api_hub_enums_pb2.EnumSubscriptionRequestType, str]] = ..., UserStatusCheckRequest: _Optional[_Union[UserStatusCheckRequest, _Mapping]] = ..., UserPlatformSubscriptionActivationRequest: _Optional[_Union[UserPlatformSubscriptionActivationRequest, _Mapping]] = ..., UserPlatformSubscriptionDeactivationRequest: _Optional[_Union[UserPlatformSubscriptionDeactivationRequest, _Mapping]] = ..., PromoClaimRequest: _Optional[_Union[PromoClaimRequest, _Mapping]] = ...) -> None: ...

class UserStatusCheckRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UserPlatformSubscriptionActivationRequest(_message.Message):
    __slots__ = ("UserPlatformSubscriptionId", "AccountIdToCharge", "IsReplaceOfActiveSubscription")
    USERPLATFORMSUBSCRIPTIONID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTIDTOCHARGE_FIELD_NUMBER: _ClassVar[int]
    ISREPLACEOFACTIVESUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    UserPlatformSubscriptionId: int
    AccountIdToCharge: int
    IsReplaceOfActiveSubscription: bool
    def __init__(self, UserPlatformSubscriptionId: _Optional[int] = ..., AccountIdToCharge: _Optional[int] = ..., IsReplaceOfActiveSubscription: bool = ...) -> None: ...

class UserPlatformSubscriptionDeactivationRequest(_message.Message):
    __slots__ = ("UserPlatformSubscriptionId",)
    USERPLATFORMSUBSCRIPTIONID_FIELD_NUMBER: _ClassVar[int]
    UserPlatformSubscriptionId: int
    def __init__(self, UserPlatformSubscriptionId: _Optional[int] = ...) -> None: ...

class PromoClaimRequest(_message.Message):
    __slots__ = ("PromoCode",)
    PROMOCODE_FIELD_NUMBER: _ClassVar[int]
    PromoCode: str
    def __init__(self, PromoCode: _Optional[str] = ...) -> None: ...

class SubscriptionResponse(_message.Message):
    __slots__ = ("UserStatusCheckResponse", "UserPlatformSubscriptionActivationResponse", "UserPlatformSubscriptionDeactivationResponse", "PromoClaimResponse")
    USERSTATUSCHECKRESPONSE_FIELD_NUMBER: _ClassVar[int]
    USERPLATFORMSUBSCRIPTIONACTIVATIONRESPONSE_FIELD_NUMBER: _ClassVar[int]
    USERPLATFORMSUBSCRIPTIONDEACTIVATIONRESPONSE_FIELD_NUMBER: _ClassVar[int]
    PROMOCLAIMRESPONSE_FIELD_NUMBER: _ClassVar[int]
    UserStatusCheckResponse: UserStatusCheckResponse
    UserPlatformSubscriptionActivationResponse: UserPlatformSubscriptionActivationResponse
    UserPlatformSubscriptionDeactivationResponse: UserPlatformSubscriptionDeactivationResponse
    PromoClaimResponse: PromoClaimResponse
    def __init__(self, UserStatusCheckResponse: _Optional[_Union[UserStatusCheckResponse, _Mapping]] = ..., UserPlatformSubscriptionActivationResponse: _Optional[_Union[UserPlatformSubscriptionActivationResponse, _Mapping]] = ..., UserPlatformSubscriptionDeactivationResponse: _Optional[_Union[UserPlatformSubscriptionDeactivationResponse, _Mapping]] = ..., PromoClaimResponse: _Optional[_Union[PromoClaimResponse, _Mapping]] = ...) -> None: ...

class UserStatusCheckResponse(_message.Message):
    __slots__ = ("ActiveSubscription", "AvailableSubscriptions", "AvailableUpgrades", "BasicPlanInfo", "ResponseMessages", "Warnings", "Errors")
    ACTIVESUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    AVAILABLESUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    AVAILABLEUPGRADES_FIELD_NUMBER: _ClassVar[int]
    BASICPLANINFO_FIELD_NUMBER: _ClassVar[int]
    RESPONSEMESSAGES_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    ActiveSubscription: UserPlatformSubscriptionActivatedUser
    AvailableSubscriptions: _containers.RepeatedCompositeFieldContainer[AvailableSubscriptionInfo]
    AvailableUpgrades: _containers.RepeatedCompositeFieldContainer[SubscriptionUpgradeInfo]
    BasicPlanInfo: BasicPlanInfo
    ResponseMessages: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseMessage]
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, ActiveSubscription: _Optional[_Union[UserPlatformSubscriptionActivatedUser, _Mapping]] = ..., AvailableSubscriptions: _Optional[_Iterable[_Union[AvailableSubscriptionInfo, _Mapping]]] = ..., AvailableUpgrades: _Optional[_Iterable[_Union[SubscriptionUpgradeInfo, _Mapping]]] = ..., BasicPlanInfo: _Optional[_Union[BasicPlanInfo, _Mapping]] = ..., ResponseMessages: _Optional[_Iterable[_Union[_common_pb2.ResponseMessage, _Mapping]]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class UserPlatformSubscriptionActivationResponse(_message.Message):
    __slots__ = ("IsActivationSuccess", "ActivatedSubscription", "ResponseMessages", "Warnings", "Errors")
    ISACTIVATIONSUCCESS_FIELD_NUMBER: _ClassVar[int]
    ACTIVATEDSUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    RESPONSEMESSAGES_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    IsActivationSuccess: bool
    ActivatedSubscription: UserPlatformSubscriptionActivatedUser
    ResponseMessages: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseMessage]
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, IsActivationSuccess: bool = ..., ActivatedSubscription: _Optional[_Union[UserPlatformSubscriptionActivatedUser, _Mapping]] = ..., ResponseMessages: _Optional[_Iterable[_Union[_common_pb2.ResponseMessage, _Mapping]]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class UserPlatformSubscriptionDeactivationResponse(_message.Message):
    __slots__ = ("IsDeactivationSuccess", "DeactivatedSubscription", "ResponseMessages", "Warnings", "Errors")
    ISDEACTIVATIONSUCCESS_FIELD_NUMBER: _ClassVar[int]
    DEACTIVATEDSUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    RESPONSEMESSAGES_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    IsDeactivationSuccess: bool
    DeactivatedSubscription: UserPlatformSubscriptionActivatedUser
    ResponseMessages: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseMessage]
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, IsDeactivationSuccess: bool = ..., DeactivatedSubscription: _Optional[_Union[UserPlatformSubscriptionActivatedUser, _Mapping]] = ..., ResponseMessages: _Optional[_Iterable[_Union[_common_pb2.ResponseMessage, _Mapping]]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class PromoClaimResponse(_message.Message):
    __slots__ = ("PromoClaimSuccess", "PromoSubscriptionsAvailableToUser", "ResponseMessages", "Warnings", "Errors")
    PROMOCLAIMSUCCESS_FIELD_NUMBER: _ClassVar[int]
    PROMOSUBSCRIPTIONSAVAILABLETOUSER_FIELD_NUMBER: _ClassVar[int]
    RESPONSEMESSAGES_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    PromoClaimSuccess: bool
    PromoSubscriptionsAvailableToUser: _containers.RepeatedCompositeFieldContainer[UserPlatformSubscription]
    ResponseMessages: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseMessage]
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, PromoClaimSuccess: bool = ..., PromoSubscriptionsAvailableToUser: _Optional[_Iterable[_Union[UserPlatformSubscription, _Mapping]]] = ..., ResponseMessages: _Optional[_Iterable[_Union[_common_pb2.ResponseMessage, _Mapping]]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class UserPlatformSubscriptionActivatedUser(_message.Message):
    __slots__ = ("UserId", "UserPlatformSubscriptionId", "SubscriptionExpiration", "IsAutoRenewEnabled", "AccountMaintenanceFeeChargeId", "UserPlatformSubscriptionPromotionId", "LastModifiedUserId", "CreatedTime", "LastModifiedTime", "Subscription")
    USERID_FIELD_NUMBER: _ClassVar[int]
    USERPLATFORMSUBSCRIPTIONID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTIONEXPIRATION_FIELD_NUMBER: _ClassVar[int]
    ISAUTORENEWENABLED_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTMAINTENANCEFEECHARGEID_FIELD_NUMBER: _ClassVar[int]
    USERPLATFORMSUBSCRIPTIONPROMOTIONID_FIELD_NUMBER: _ClassVar[int]
    LASTMODIFIEDUSERID_FIELD_NUMBER: _ClassVar[int]
    CREATEDTIME_FIELD_NUMBER: _ClassVar[int]
    LASTMODIFIEDTIME_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    UserId: int
    UserPlatformSubscriptionId: int
    SubscriptionExpiration: _timestamp_pb2.Timestamp
    IsAutoRenewEnabled: bool
    AccountMaintenanceFeeChargeId: int
    UserPlatformSubscriptionPromotionId: int
    LastModifiedUserId: int
    CreatedTime: _timestamp_pb2.Timestamp
    LastModifiedTime: _timestamp_pb2.Timestamp
    Subscription: UserPlatformSubscription
    def __init__(self, UserId: _Optional[int] = ..., UserPlatformSubscriptionId: _Optional[int] = ..., SubscriptionExpiration: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., IsAutoRenewEnabled: bool = ..., AccountMaintenanceFeeChargeId: _Optional[int] = ..., UserPlatformSubscriptionPromotionId: _Optional[int] = ..., LastModifiedUserId: _Optional[int] = ..., CreatedTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., LastModifiedTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., Subscription: _Optional[_Union[UserPlatformSubscription, _Mapping]] = ...) -> None: ...

class UserPlatformSubscription(_message.Message):
    __slots__ = ("UserPlatformSubscriptionId", "SubscriptionPeriodInDays", "SubscriptionFee", "RealTimeQuotesNonProEntitlement", "RealTimeQuotesProEntitlement", "ApplyCommissionsToLinkedAccounts", "LastModifiedUserId", "CreatedTime", "LastModifiedTime", "Description", "IsSoftDeleted", "Commissions", "FreeTrialInDays", "FreeTrialForNewSubscribersOnly")
    USERPLATFORMSUBSCRIPTIONID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTIONPERIODINDAYS_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTIONFEE_FIELD_NUMBER: _ClassVar[int]
    REALTIMEQUOTESNONPROENTITLEMENT_FIELD_NUMBER: _ClassVar[int]
    REALTIMEQUOTESPROENTITLEMENT_FIELD_NUMBER: _ClassVar[int]
    APPLYCOMMISSIONSTOLINKEDACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    LASTMODIFIEDUSERID_FIELD_NUMBER: _ClassVar[int]
    CREATEDTIME_FIELD_NUMBER: _ClassVar[int]
    LASTMODIFIEDTIME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ISSOFTDELETED_FIELD_NUMBER: _ClassVar[int]
    COMMISSIONS_FIELD_NUMBER: _ClassVar[int]
    FREETRIALINDAYS_FIELD_NUMBER: _ClassVar[int]
    FREETRIALFORNEWSUBSCRIBERSONLY_FIELD_NUMBER: _ClassVar[int]
    UserPlatformSubscriptionId: int
    SubscriptionPeriodInDays: int
    SubscriptionFee: float
    RealTimeQuotesNonProEntitlement: bool
    RealTimeQuotesProEntitlement: bool
    ApplyCommissionsToLinkedAccounts: bool
    LastModifiedUserId: int
    CreatedTime: _timestamp_pb2.Timestamp
    LastModifiedTime: _timestamp_pb2.Timestamp
    Description: str
    IsSoftDeleted: bool
    Commissions: _containers.RepeatedCompositeFieldContainer[_commissions_pb2.Commission]
    FreeTrialInDays: int
    FreeTrialForNewSubscribersOnly: bool
    def __init__(self, UserPlatformSubscriptionId: _Optional[int] = ..., SubscriptionPeriodInDays: _Optional[int] = ..., SubscriptionFee: _Optional[float] = ..., RealTimeQuotesNonProEntitlement: bool = ..., RealTimeQuotesProEntitlement: bool = ..., ApplyCommissionsToLinkedAccounts: bool = ..., LastModifiedUserId: _Optional[int] = ..., CreatedTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., LastModifiedTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., Description: _Optional[str] = ..., IsSoftDeleted: bool = ..., Commissions: _Optional[_Iterable[_Union[_commissions_pb2.Commission, _Mapping]]] = ..., FreeTrialInDays: _Optional[int] = ..., FreeTrialForNewSubscribersOnly: bool = ...) -> None: ...

class SubscriptionUpgradeInfo(_message.Message):
    __slots__ = ("Subscription", "DueDate", "DueAmount", "SubscriptionCredit", "AccountChargeFreeDays")
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DUEDATE_FIELD_NUMBER: _ClassVar[int]
    DUEAMOUNT_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTIONCREDIT_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTCHARGEFREEDAYS_FIELD_NUMBER: _ClassVar[int]
    Subscription: UserPlatformSubscription
    DueDate: _timestamp_pb2.Timestamp
    DueAmount: float
    SubscriptionCredit: float
    AccountChargeFreeDays: float
    def __init__(self, Subscription: _Optional[_Union[UserPlatformSubscription, _Mapping]] = ..., DueDate: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., DueAmount: _Optional[float] = ..., SubscriptionCredit: _Optional[float] = ..., AccountChargeFreeDays: _Optional[float] = ...) -> None: ...

class BasicPlanInfo(_message.Message):
    __slots__ = ("CommissionDefaults", "CommissionAccountOverrides", "CommissionLabels", "AccountMaintenanceFeeInfos", "AccountMaintenanceFeeLabels", "RealTimeQuotesNonProEntitlement", "StartDate")
    COMMISSIONDEFAULTS_FIELD_NUMBER: _ClassVar[int]
    COMMISSIONACCOUNTOVERRIDES_FIELD_NUMBER: _ClassVar[int]
    COMMISSIONLABELS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTMAINTENANCEFEEINFOS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTMAINTENANCEFEELABELS_FIELD_NUMBER: _ClassVar[int]
    REALTIMEQUOTESNONPROENTITLEMENT_FIELD_NUMBER: _ClassVar[int]
    STARTDATE_FIELD_NUMBER: _ClassVar[int]
    CommissionDefaults: _containers.RepeatedCompositeFieldContainer[_commissions_pb2.Commission]
    CommissionAccountOverrides: _containers.RepeatedCompositeFieldContainer[_commissions_pb2.CommissionAccountOverride]
    CommissionLabels: _containers.RepeatedScalarFieldContainer[str]
    AccountMaintenanceFeeInfos: _containers.RepeatedCompositeFieldContainer[_account_maintenance_fee_pb2.AccountMaintenanceFeeInfo]
    AccountMaintenanceFeeLabels: _containers.RepeatedScalarFieldContainer[str]
    RealTimeQuotesNonProEntitlement: bool
    StartDate: _timestamp_pb2.Timestamp
    def __init__(self, CommissionDefaults: _Optional[_Iterable[_Union[_commissions_pb2.Commission, _Mapping]]] = ..., CommissionAccountOverrides: _Optional[_Iterable[_Union[_commissions_pb2.CommissionAccountOverride, _Mapping]]] = ..., CommissionLabels: _Optional[_Iterable[str]] = ..., AccountMaintenanceFeeInfos: _Optional[_Iterable[_Union[_account_maintenance_fee_pb2.AccountMaintenanceFeeInfo, _Mapping]]] = ..., AccountMaintenanceFeeLabels: _Optional[_Iterable[str]] = ..., RealTimeQuotesNonProEntitlement: bool = ..., StartDate: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AvailableSubscriptionInfo(_message.Message):
    __slots__ = ("Subscription", "AccountMaintenanceFeeInfos")
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTMAINTENANCEFEEINFOS_FIELD_NUMBER: _ClassVar[int]
    Subscription: UserPlatformSubscription
    AccountMaintenanceFeeInfos: _containers.RepeatedCompositeFieldContainer[_account_maintenance_fee_pb2.AccountMaintenanceFeeInfo]
    def __init__(self, Subscription: _Optional[_Union[UserPlatformSubscription, _Mapping]] = ..., AccountMaintenanceFeeInfos: _Optional[_Iterable[_Union[_account_maintenance_fee_pb2.AccountMaintenanceFeeInfo, _Mapping]]] = ...) -> None: ...
