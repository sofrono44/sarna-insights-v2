import accounts_pb2 as _accounts_pb2
import common_pb2 as _common_pb2
from admin import admin_risk_profiles_enums_pb2 as _admin_risk_profiles_enums_pb2
import pmbp_pb2 as _pmbp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RiskProfilesRequest(_message.Message):
    __slots__ = ("RiskProfileId", "RiskApplicabilityType")
    RISKPROFILEID_FIELD_NUMBER: _ClassVar[int]
    RISKAPPLICABILITYTYPE_FIELD_NUMBER: _ClassVar[int]
    RiskProfileId: int
    RiskApplicabilityType: _admin_risk_profiles_enums_pb2.EnumRiskApplicabilityType
    def __init__(self, RiskProfileId: _Optional[int] = ..., RiskApplicabilityType: _Optional[_Union[_admin_risk_profiles_enums_pb2.EnumRiskApplicabilityType, str]] = ...) -> None: ...

class RiskProfilesResponse(_message.Message):
    __slots__ = ("AdminRiskProfiles", "Warnings", "Errors")
    ADMINRISKPROFILES_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    AdminRiskProfiles: _containers.RepeatedCompositeFieldContainer[AdminRiskProfile]
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, AdminRiskProfiles: _Optional[_Iterable[_Union[AdminRiskProfile, _Mapping]]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class RiskProfileUpdateRequest(_message.Message):
    __slots__ = ("AdminRiskProfile",)
    ADMINRISKPROFILE_FIELD_NUMBER: _ClassVar[int]
    AdminRiskProfile: AdminRiskProfile
    def __init__(self, AdminRiskProfile: _Optional[_Union[AdminRiskProfile, _Mapping]] = ...) -> None: ...

class RiskProfileUpdateResponse(_message.Message):
    __slots__ = ("RiskProfileId", "Warnings", "Errors")
    RISKPROFILEID_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    RiskProfileId: int
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, RiskProfileId: _Optional[int] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class RiskProfileDeleteRequest(_message.Message):
    __slots__ = ("RiskProfileId",)
    RISKPROFILEID_FIELD_NUMBER: _ClassVar[int]
    RiskProfileId: int
    def __init__(self, RiskProfileId: _Optional[int] = ...) -> None: ...

class RiskProfileCloneRequest(_message.Message):
    __slots__ = ("RiskProfileId", "Name")
    RISKPROFILEID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RiskProfileId: int
    Name: str
    def __init__(self, RiskProfileId: _Optional[int] = ..., Name: _Optional[str] = ...) -> None: ...

class RiskProfileDeleteResponse(_message.Message):
    __slots__ = ("Success", "Warnings", "Errors")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    Success: bool
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, Success: bool = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class AdminRiskProfile(_message.Message):
    __slots__ = ("RiskProfileId", "Name", "IsDefaultHouseProfile", "IsDefaultMonitoringProfile", "RiskApplicabilityType", "IncludeOpenOrders", "AdminRiskProfileScenarios")
    RISKPROFILEID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ISDEFAULTHOUSEPROFILE_FIELD_NUMBER: _ClassVar[int]
    ISDEFAULTMONITORINGPROFILE_FIELD_NUMBER: _ClassVar[int]
    RISKAPPLICABILITYTYPE_FIELD_NUMBER: _ClassVar[int]
    INCLUDEOPENORDERS_FIELD_NUMBER: _ClassVar[int]
    ADMINRISKPROFILESCENARIOS_FIELD_NUMBER: _ClassVar[int]
    RiskProfileId: int
    Name: str
    IsDefaultHouseProfile: bool
    IsDefaultMonitoringProfile: bool
    RiskApplicabilityType: _admin_risk_profiles_enums_pb2.EnumRiskApplicabilityType
    IncludeOpenOrders: bool
    AdminRiskProfileScenarios: _containers.RepeatedCompositeFieldContainer[AdminRiskProfileScenario]
    def __init__(self, RiskProfileId: _Optional[int] = ..., Name: _Optional[str] = ..., IsDefaultHouseProfile: bool = ..., IsDefaultMonitoringProfile: bool = ..., RiskApplicabilityType: _Optional[_Union[_admin_risk_profiles_enums_pb2.EnumRiskApplicabilityType, str]] = ..., IncludeOpenOrders: bool = ..., AdminRiskProfileScenarios: _Optional[_Iterable[_Union[AdminRiskProfileScenario, _Mapping]]] = ...) -> None: ...

class AdminRiskProfileScenario(_message.Message):
    __slots__ = ("SortOrder", "UnderlyingPriceShockInputs", "VolatilityShockInputs", "YieldShockInputs", "MOVEShockInputs", "MOVECreditSpreadShockInputs")
    SORTORDER_FIELD_NUMBER: _ClassVar[int]
    UNDERLYINGPRICESHOCKINPUTS_FIELD_NUMBER: _ClassVar[int]
    VOLATILITYSHOCKINPUTS_FIELD_NUMBER: _ClassVar[int]
    YIELDSHOCKINPUTS_FIELD_NUMBER: _ClassVar[int]
    MOVESHOCKINPUTS_FIELD_NUMBER: _ClassVar[int]
    MOVECREDITSPREADSHOCKINPUTS_FIELD_NUMBER: _ClassVar[int]
    SortOrder: int
    UnderlyingPriceShockInputs: _containers.RepeatedCompositeFieldContainer[_pmbp_pb2.PmBpUnderlyingPriceShockInput]
    VolatilityShockInputs: _containers.RepeatedCompositeFieldContainer[_pmbp_pb2.PmBpVolatilityShockInput]
    YieldShockInputs: _containers.RepeatedCompositeFieldContainer[_common_pb2.YieldShockInput]
    MOVEShockInputs: _containers.RepeatedCompositeFieldContainer[_common_pb2.MOVEShockInput]
    MOVECreditSpreadShockInputs: _containers.RepeatedCompositeFieldContainer[_common_pb2.MOVECreditSpreadShockInput]
    def __init__(self, SortOrder: _Optional[int] = ..., UnderlyingPriceShockInputs: _Optional[_Iterable[_Union[_pmbp_pb2.PmBpUnderlyingPriceShockInput, _Mapping]]] = ..., VolatilityShockInputs: _Optional[_Iterable[_Union[_pmbp_pb2.PmBpVolatilityShockInput, _Mapping]]] = ..., YieldShockInputs: _Optional[_Iterable[_Union[_common_pb2.YieldShockInput, _Mapping]]] = ..., MOVEShockInputs: _Optional[_Iterable[_Union[_common_pb2.MOVEShockInput, _Mapping]]] = ..., MOVECreditSpreadShockInputs: _Optional[_Iterable[_Union[_common_pb2.MOVECreditSpreadShockInput, _Mapping]]] = ...) -> None: ...

class ShockInput(_message.Message):
    __slots__ = ("ApplyAcrossPortfolio", "PxPercentUp", "PxPercentDown", "IVPercentUp", "IVPercentDown", "UnderlyingSymbol", "ApplyTimeToExpirationFactor", "ProductGroupId", "ClassGroupId", "BasketId")
    APPLYACROSSPORTFOLIO_FIELD_NUMBER: _ClassVar[int]
    PXPERCENTUP_FIELD_NUMBER: _ClassVar[int]
    PXPERCENTDOWN_FIELD_NUMBER: _ClassVar[int]
    IVPERCENTUP_FIELD_NUMBER: _ClassVar[int]
    IVPERCENTDOWN_FIELD_NUMBER: _ClassVar[int]
    UNDERLYINGSYMBOL_FIELD_NUMBER: _ClassVar[int]
    APPLYTIMETOEXPIRATIONFACTOR_FIELD_NUMBER: _ClassVar[int]
    PRODUCTGROUPID_FIELD_NUMBER: _ClassVar[int]
    CLASSGROUPID_FIELD_NUMBER: _ClassVar[int]
    BASKETID_FIELD_NUMBER: _ClassVar[int]
    ApplyAcrossPortfolio: bool
    PxPercentUp: float
    PxPercentDown: float
    IVPercentUp: float
    IVPercentDown: float
    UnderlyingSymbol: str
    ApplyTimeToExpirationFactor: int
    ProductGroupId: str
    ClassGroupId: str
    BasketId: str
    def __init__(self, ApplyAcrossPortfolio: bool = ..., PxPercentUp: _Optional[float] = ..., PxPercentDown: _Optional[float] = ..., IVPercentUp: _Optional[float] = ..., IVPercentDown: _Optional[float] = ..., UnderlyingSymbol: _Optional[str] = ..., ApplyTimeToExpirationFactor: _Optional[int] = ..., ProductGroupId: _Optional[str] = ..., ClassGroupId: _Optional[str] = ..., BasketId: _Optional[str] = ...) -> None: ...
