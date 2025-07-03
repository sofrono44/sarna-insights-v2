from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
from common_pb2 import ResponseError as ResponseError
from common_pb2 import ResponseWarning as ResponseWarning
from common_pb2 import ResponseMessage as ResponseMessage
from common_pb2 import MOVEShockInput as MOVEShockInput
from common_pb2 import MOVECreditSpreadShockInput as MOVECreditSpreadShockInput
from common_pb2 import YieldShockInput as YieldShockInput

DESCRIPTOR: _descriptor.FileDescriptor

class BpSymbolRequirementSearchRequest(_message.Message):
    __slots__ = ("SecurityIdentifiers", "IncludeOverrideHistory")
    SECURITYIDENTIFIERS_FIELD_NUMBER: _ClassVar[int]
    INCLUDEOVERRIDEHISTORY_FIELD_NUMBER: _ClassVar[int]
    SecurityIdentifiers: _containers.RepeatedScalarFieldContainer[str]
    IncludeOverrideHistory: bool
    def __init__(self, SecurityIdentifiers: _Optional[_Iterable[str]] = ..., IncludeOverrideHistory: bool = ...) -> None: ...

class BpSymbolRequirementOverrideRequest(_message.Message):
    __slots__ = ("BpSymbolRequirements",)
    BPSYMBOLREQUIREMENTS_FIELD_NUMBER: _ClassVar[int]
    BpSymbolRequirements: _containers.RepeatedCompositeFieldContainer[BpSymbolRequirement]
    def __init__(self, BpSymbolRequirements: _Optional[_Iterable[_Union[BpSymbolRequirement, _Mapping]]] = ...) -> None: ...

class BpSymbolRequirementDeleteRequest(_message.Message):
    __slots__ = ("SecurityIdentifiers",)
    SECURITYIDENTIFIERS_FIELD_NUMBER: _ClassVar[int]
    SecurityIdentifiers: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, SecurityIdentifiers: _Optional[_Iterable[str]] = ...) -> None: ...

class BpSymbolRequirementListResponse(_message.Message):
    __slots__ = ("BpSymbolIdentifiers", "Warnings", "Errors")
    BPSYMBOLIDENTIFIERS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    BpSymbolIdentifiers: _containers.RepeatedCompositeFieldContainer[BpSymbolIdentifier]
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, BpSymbolIdentifiers: _Optional[_Iterable[_Union[BpSymbolIdentifier, _Mapping]]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class BpSymbolIdentifier(_message.Message):
    __slots__ = ("Symbol", "Cusip", "ExternalSecurityId")
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    CUSIP_FIELD_NUMBER: _ClassVar[int]
    EXTERNALSECURITYID_FIELD_NUMBER: _ClassVar[int]
    Symbol: str
    Cusip: str
    ExternalSecurityId: str
    def __init__(self, Symbol: _Optional[str] = ..., Cusip: _Optional[str] = ..., ExternalSecurityId: _Optional[str] = ...) -> None: ...

class BpSymbolRequirementResponse(_message.Message):
    __slots__ = ("BpSymbolRequirements", "Warnings", "Errors")
    BPSYMBOLREQUIREMENTS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    BpSymbolRequirements: _containers.RepeatedCompositeFieldContainer[BpSymbolRequirement]
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, BpSymbolRequirements: _Optional[_Iterable[_Union[BpSymbolRequirement, _Mapping]]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class BpSymbolRequirement(_message.Message):
    __slots__ = ("Symbol", "Cusip", "ExternalSecurityId", "RegtMaintReqLong", "RegtMaintReqShort", "FirmMaintReqLong", "FirmMaintReqShort", "RegtPrincipalLong", "RegtPrincipalShort", "FirmPrincipalLong", "FirmPrincipalShort", "MinMaintPointsLong", "MinMaintPointsShort", "EtfAddlMarginPercentage", "MarginCode", "IsAdminOverride", "LastModifiedUserId", "LastModifiedTime", "IsDeleted", "IsPMEligible", "FetchedFromSM")
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    CUSIP_FIELD_NUMBER: _ClassVar[int]
    EXTERNALSECURITYID_FIELD_NUMBER: _ClassVar[int]
    REGTMAINTREQLONG_FIELD_NUMBER: _ClassVar[int]
    REGTMAINTREQSHORT_FIELD_NUMBER: _ClassVar[int]
    FIRMMAINTREQLONG_FIELD_NUMBER: _ClassVar[int]
    FIRMMAINTREQSHORT_FIELD_NUMBER: _ClassVar[int]
    REGTPRINCIPALLONG_FIELD_NUMBER: _ClassVar[int]
    REGTPRINCIPALSHORT_FIELD_NUMBER: _ClassVar[int]
    FIRMPRINCIPALLONG_FIELD_NUMBER: _ClassVar[int]
    FIRMPRINCIPALSHORT_FIELD_NUMBER: _ClassVar[int]
    MINMAINTPOINTSLONG_FIELD_NUMBER: _ClassVar[int]
    MINMAINTPOINTSSHORT_FIELD_NUMBER: _ClassVar[int]
    ETFADDLMARGINPERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    MARGINCODE_FIELD_NUMBER: _ClassVar[int]
    ISADMINOVERRIDE_FIELD_NUMBER: _ClassVar[int]
    LASTMODIFIEDUSERID_FIELD_NUMBER: _ClassVar[int]
    LASTMODIFIEDTIME_FIELD_NUMBER: _ClassVar[int]
    ISDELETED_FIELD_NUMBER: _ClassVar[int]
    ISPMELIGIBLE_FIELD_NUMBER: _ClassVar[int]
    FETCHEDFROMSM_FIELD_NUMBER: _ClassVar[int]
    Symbol: str
    Cusip: str
    ExternalSecurityId: str
    RegtMaintReqLong: _wrappers_pb2.DoubleValue
    RegtMaintReqShort: _wrappers_pb2.DoubleValue
    FirmMaintReqLong: _wrappers_pb2.DoubleValue
    FirmMaintReqShort: _wrappers_pb2.DoubleValue
    RegtPrincipalLong: _wrappers_pb2.DoubleValue
    RegtPrincipalShort: _wrappers_pb2.DoubleValue
    FirmPrincipalLong: _wrappers_pb2.DoubleValue
    FirmPrincipalShort: _wrappers_pb2.DoubleValue
    MinMaintPointsLong: _wrappers_pb2.DoubleValue
    MinMaintPointsShort: _wrappers_pb2.DoubleValue
    EtfAddlMarginPercentage: _wrappers_pb2.DoubleValue
    MarginCode: int
    IsAdminOverride: bool
    LastModifiedUserId: int
    LastModifiedTime: _timestamp_pb2.Timestamp
    IsDeleted: bool
    IsPMEligible: _wrappers_pb2.BoolValue
    FetchedFromSM: bool
    def __init__(self, Symbol: _Optional[str] = ..., Cusip: _Optional[str] = ..., ExternalSecurityId: _Optional[str] = ..., RegtMaintReqLong: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., RegtMaintReqShort: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., FirmMaintReqLong: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., FirmMaintReqShort: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., RegtPrincipalLong: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., RegtPrincipalShort: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., FirmPrincipalLong: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., FirmPrincipalShort: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., MinMaintPointsLong: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., MinMaintPointsShort: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., EtfAddlMarginPercentage: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., MarginCode: _Optional[int] = ..., IsAdminOverride: bool = ..., LastModifiedUserId: _Optional[int] = ..., LastModifiedTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., IsDeleted: bool = ..., IsPMEligible: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., FetchedFromSM: bool = ...) -> None: ...
