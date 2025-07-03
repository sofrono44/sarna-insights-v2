import common_enums_pb2 as _common_enums_pb2
import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListExternalAccountMappingsResponse(_message.Message):
    __slots__ = ("ExternalAccountMappings", "Warnings", "Errors")
    EXTERNALACCOUNTMAPPINGS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    ExternalAccountMappings: _containers.RepeatedCompositeFieldContainer[ExternalAccountMapping]
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, ExternalAccountMappings: _Optional[_Iterable[_Union[ExternalAccountMapping, _Mapping]]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class GetExternalAccountMappingsRequest(_message.Message):
    __slots__ = ("ExternalAccountMappingId",)
    EXTERNALACCOUNTMAPPINGID_FIELD_NUMBER: _ClassVar[int]
    ExternalAccountMappingId: int
    def __init__(self, ExternalAccountMappingId: _Optional[int] = ...) -> None: ...

class GetExternalAccountMappingsResponse(_message.Message):
    __slots__ = ("ExternalAccountMapping", "Warnings", "Errors")
    EXTERNALACCOUNTMAPPING_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    ExternalAccountMapping: ExternalAccountMapping
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, ExternalAccountMapping: _Optional[_Union[ExternalAccountMapping, _Mapping]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class ManageExternalAccountMappingsRequest(_message.Message):
    __slots__ = ("ExternalAccountMapping",)
    EXTERNALACCOUNTMAPPING_FIELD_NUMBER: _ClassVar[int]
    ExternalAccountMapping: ExternalAccountMapping
    def __init__(self, ExternalAccountMapping: _Optional[_Union[ExternalAccountMapping, _Mapping]] = ...) -> None: ...

class ManageExternalAccountMappingsResponse(_message.Message):
    __slots__ = ("ExternalAccountMappingId", "Warnings", "Errors")
    EXTERNALACCOUNTMAPPINGID_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    ExternalAccountMappingId: int
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, ExternalAccountMappingId: _Optional[int] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class DeleteExternalAccountMappingsRequest(_message.Message):
    __slots__ = ("ExternalAccountMappingId",)
    EXTERNALACCOUNTMAPPINGID_FIELD_NUMBER: _ClassVar[int]
    ExternalAccountMappingId: int
    def __init__(self, ExternalAccountMappingId: _Optional[int] = ...) -> None: ...

class ExternalAccountMapping(_message.Message):
    __slots__ = ("ExternalAccountMappingId", "ExternalAccountNumber", "AccountNumber", "ExternalDataSource", "ClearingAccountType", "Allocation")
    EXTERNALACCOUNTMAPPINGID_FIELD_NUMBER: _ClassVar[int]
    EXTERNALACCOUNTNUMBER_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTNUMBER_FIELD_NUMBER: _ClassVar[int]
    EXTERNALDATASOURCE_FIELD_NUMBER: _ClassVar[int]
    CLEARINGACCOUNTTYPE_FIELD_NUMBER: _ClassVar[int]
    ALLOCATION_FIELD_NUMBER: _ClassVar[int]
    ExternalAccountMappingId: int
    ExternalAccountNumber: str
    AccountNumber: str
    ExternalDataSource: _common_enums_pb2.EnumExternalDataSource
    ClearingAccountType: _common_enums_pb2.EnumClearingAccountType
    Allocation: float
    def __init__(self, ExternalAccountMappingId: _Optional[int] = ..., ExternalAccountNumber: _Optional[str] = ..., AccountNumber: _Optional[str] = ..., ExternalDataSource: _Optional[_Union[_common_enums_pb2.EnumExternalDataSource, str]] = ..., ClearingAccountType: _Optional[_Union[_common_enums_pb2.EnumClearingAccountType, str]] = ..., Allocation: _Optional[float] = ...) -> None: ...
