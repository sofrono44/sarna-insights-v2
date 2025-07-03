import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetProvincesRequest(_message.Message):
    __slots__ = ("CountryId",)
    COUNTRYID_FIELD_NUMBER: _ClassVar[int]
    CountryId: int
    def __init__(self, CountryId: _Optional[int] = ...) -> None: ...

class GlossaryResponse(_message.Message):
    __slots__ = ("Provinces", "Warnings", "Errors")
    PROVINCES_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    Provinces: _containers.RepeatedCompositeFieldContainer[Province]
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, Provinces: _Optional[_Iterable[_Union[Province, _Mapping]]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class Province(_message.Message):
    __slots__ = ("ProvinceId", "Name")
    PROVINCEID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ProvinceId: int
    Name: str
    def __init__(self, ProvinceId: _Optional[int] = ..., Name: _Optional[str] = ...) -> None: ...
