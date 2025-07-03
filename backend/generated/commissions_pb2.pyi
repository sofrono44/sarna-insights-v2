from google.protobuf import timestamp_pb2 as _timestamp_pb2
import api_hub_enums_pb2 as _api_hub_enums_pb2
import commissions_enums_pb2 as _commissions_enums_pb2
import orders_enums_pb2 as _orders_enums_pb2
import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommissionRequest(_message.Message):
    __slots__ = ("CommissionRequestType", "CommissionPromoClaimRequest")
    COMMISSIONREQUESTTYPE_FIELD_NUMBER: _ClassVar[int]
    COMMISSIONPROMOCLAIMREQUEST_FIELD_NUMBER: _ClassVar[int]
    CommissionRequestType: _api_hub_enums_pb2.EnumCommissionRequestType
    CommissionPromoClaimRequest: CommissionPromoClaimRequest
    def __init__(self, CommissionRequestType: _Optional[_Union[_api_hub_enums_pb2.EnumCommissionRequestType, str]] = ..., CommissionPromoClaimRequest: _Optional[_Union[CommissionPromoClaimRequest, _Mapping]] = ...) -> None: ...

class CommissionPromoClaimRequest(_message.Message):
    __slots__ = ("PromoCode",)
    PROMOCODE_FIELD_NUMBER: _ClassVar[int]
    PromoCode: str
    def __init__(self, PromoCode: _Optional[str] = ...) -> None: ...

class CommissionResponse(_message.Message):
    __slots__ = ("CommissionPromoClaimResponse",)
    COMMISSIONPROMOCLAIMRESPONSE_FIELD_NUMBER: _ClassVar[int]
    CommissionPromoClaimResponse: CommissionPromoClaimResponse
    def __init__(self, CommissionPromoClaimResponse: _Optional[_Union[CommissionPromoClaimResponse, _Mapping]] = ...) -> None: ...

class CommissionPromoClaimResponse(_message.Message):
    __slots__ = ("PromoCommissionClaimSuccess", "CommissionsAppliedToUserAccounts", "Warnings", "Errors")
    PROMOCOMMISSIONCLAIMSUCCESS_FIELD_NUMBER: _ClassVar[int]
    COMMISSIONSAPPLIEDTOUSERACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    PromoCommissionClaimSuccess: bool
    CommissionsAppliedToUserAccounts: _containers.RepeatedCompositeFieldContainer[Commission]
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, PromoCommissionClaimSuccess: bool = ..., CommissionsAppliedToUserAccounts: _Optional[_Iterable[_Union[Commission, _Mapping]]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class Commission(_message.Message):
    __slots__ = ("CommissionId", "CommissionSchedule", "SecurityType", "CommissionFreePositionClosing", "Minimum", "Maximum", "BaseQuantity", "decimal", "PercentageOfPrincipal", "SecondaryMinimum", "SecondaryMaximum", "SecondaryPerUnit", "SecondaryBaseQuantity", "Description", "LastModifiedUserId", "CreatedTime", "LastModifiedTime", "IsSoftDeleted")
    COMMISSIONID_FIELD_NUMBER: _ClassVar[int]
    COMMISSIONSCHEDULE_FIELD_NUMBER: _ClassVar[int]
    SECURITYTYPE_FIELD_NUMBER: _ClassVar[int]
    COMMISSIONFREEPOSITIONCLOSING_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_FIELD_NUMBER: _ClassVar[int]
    BASEQUANTITY_FIELD_NUMBER: _ClassVar[int]
    DECIMAL_FIELD_NUMBER: _ClassVar[int]
    PERCENTAGEOFPRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    SECONDARYMINIMUM_FIELD_NUMBER: _ClassVar[int]
    SECONDARYMAXIMUM_FIELD_NUMBER: _ClassVar[int]
    SECONDARYPERUNIT_FIELD_NUMBER: _ClassVar[int]
    SECONDARYBASEQUANTITY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LASTMODIFIEDUSERID_FIELD_NUMBER: _ClassVar[int]
    CREATEDTIME_FIELD_NUMBER: _ClassVar[int]
    LASTMODIFIEDTIME_FIELD_NUMBER: _ClassVar[int]
    ISSOFTDELETED_FIELD_NUMBER: _ClassVar[int]
    CommissionId: int
    CommissionSchedule: _commissions_enums_pb2.EnumCommissionSchedule
    SecurityType: _orders_enums_pb2.EnumSecurityType
    CommissionFreePositionClosing: bool
    Minimum: float
    Maximum: float
    BaseQuantity: int
    decimal: float
    PercentageOfPrincipal: float
    SecondaryMinimum: float
    SecondaryMaximum: float
    SecondaryPerUnit: float
    SecondaryBaseQuantity: int
    Description: str
    LastModifiedUserId: int
    CreatedTime: _timestamp_pb2.Timestamp
    LastModifiedTime: _timestamp_pb2.Timestamp
    IsSoftDeleted: bool
    def __init__(self, CommissionId: _Optional[int] = ..., CommissionSchedule: _Optional[_Union[_commissions_enums_pb2.EnumCommissionSchedule, str]] = ..., SecurityType: _Optional[_Union[_orders_enums_pb2.EnumSecurityType, str]] = ..., CommissionFreePositionClosing: bool = ..., Minimum: _Optional[float] = ..., Maximum: _Optional[float] = ..., BaseQuantity: _Optional[int] = ..., decimal: _Optional[float] = ..., PercentageOfPrincipal: _Optional[float] = ..., SecondaryMinimum: _Optional[float] = ..., SecondaryMaximum: _Optional[float] = ..., SecondaryPerUnit: _Optional[float] = ..., SecondaryBaseQuantity: _Optional[int] = ..., Description: _Optional[str] = ..., LastModifiedUserId: _Optional[int] = ..., CreatedTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., LastModifiedTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., IsSoftDeleted: bool = ...) -> None: ...

class CommissionAccountOverride(_message.Message):
    __slots__ = ("AccountId", "CommissionId", "UserPlatformSubscriptionId", "CommissionPromotionId", "OverrideExpiration", "LastModifiedUserId", "CreatedTime", "Commission")
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    COMMISSIONID_FIELD_NUMBER: _ClassVar[int]
    USERPLATFORMSUBSCRIPTIONID_FIELD_NUMBER: _ClassVar[int]
    COMMISSIONPROMOTIONID_FIELD_NUMBER: _ClassVar[int]
    OVERRIDEEXPIRATION_FIELD_NUMBER: _ClassVar[int]
    LASTMODIFIEDUSERID_FIELD_NUMBER: _ClassVar[int]
    CREATEDTIME_FIELD_NUMBER: _ClassVar[int]
    COMMISSION_FIELD_NUMBER: _ClassVar[int]
    AccountId: int
    CommissionId: int
    UserPlatformSubscriptionId: int
    CommissionPromotionId: int
    OverrideExpiration: _timestamp_pb2.Timestamp
    LastModifiedUserId: int
    CreatedTime: _timestamp_pb2.Timestamp
    Commission: Commission
    def __init__(self, AccountId: _Optional[int] = ..., CommissionId: _Optional[int] = ..., UserPlatformSubscriptionId: _Optional[int] = ..., CommissionPromotionId: _Optional[int] = ..., OverrideExpiration: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., LastModifiedUserId: _Optional[int] = ..., CreatedTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., Commission: _Optional[_Union[Commission, _Mapping]] = ...) -> None: ...
