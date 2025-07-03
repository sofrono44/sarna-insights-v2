import common_pb2 as _common_pb2
import orders_enums_pb2 as _orders_enums_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SecuritiesMasterDataRequest(_message.Message):
    __slots__ = ("GetAllEquities", "UnderlyingSymbols")
    GETALLEQUITIES_FIELD_NUMBER: _ClassVar[int]
    UNDERLYINGSYMBOLS_FIELD_NUMBER: _ClassVar[int]
    GetAllEquities: bool
    UnderlyingSymbols: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, GetAllEquities: bool = ..., UnderlyingSymbols: _Optional[_Iterable[str]] = ...) -> None: ...

class SecuritiesMasterDataResponse(_message.Message):
    __slots__ = ("HasData", "Equities", "EquityOptionsListInfoByUnderlyingSymbol", "Warnings", "Errors")
    class EquityOptionsListInfoByUnderlyingSymbolEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: EquityOptionsListInfo
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[EquityOptionsListInfo, _Mapping]] = ...) -> None: ...
    HASDATA_FIELD_NUMBER: _ClassVar[int]
    EQUITIES_FIELD_NUMBER: _ClassVar[int]
    EQUITYOPTIONSLISTINFOBYUNDERLYINGSYMBOL_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    HasData: bool
    Equities: _containers.RepeatedCompositeFieldContainer[Equity]
    EquityOptionsListInfoByUnderlyingSymbol: _containers.MessageMap[str, EquityOptionsListInfo]
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, HasData: bool = ..., Equities: _Optional[_Iterable[_Union[Equity, _Mapping]]] = ..., EquityOptionsListInfoByUnderlyingSymbol: _Optional[_Mapping[str, EquityOptionsListInfo]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class Equity(_message.Message):
    __slots__ = ("Symbol", "Description", "IsOptionable", "PreviousDayClosePrice")
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ISOPTIONABLE_FIELD_NUMBER: _ClassVar[int]
    PREVIOUSDAYCLOSEPRICE_FIELD_NUMBER: _ClassVar[int]
    Symbol: str
    Description: str
    IsOptionable: bool
    PreviousDayClosePrice: float
    def __init__(self, Symbol: _Optional[str] = ..., Description: _Optional[str] = ..., IsOptionable: bool = ..., PreviousDayClosePrice: _Optional[float] = ...) -> None: ...

class EquityOptionsListInfo(_message.Message):
    __slots__ = ("EquityOptions", "RootSymbols")
    EQUITYOPTIONS_FIELD_NUMBER: _ClassVar[int]
    ROOTSYMBOLS_FIELD_NUMBER: _ClassVar[int]
    EquityOptions: _containers.RepeatedCompositeFieldContainer[EquityOption]
    RootSymbols: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, EquityOptions: _Optional[_Iterable[_Union[EquityOption, _Mapping]]] = ..., RootSymbols: _Optional[_Iterable[str]] = ...) -> None: ...

class EquityOption(_message.Message):
    __slots__ = ("Symbol", "UnderlyingSymbol", "RootSymbol", "PreviousDayClosePrice", "CallOrPut", "Expiration", "StrikePrice", "Multiplier", "ContractSize")
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    UNDERLYINGSYMBOL_FIELD_NUMBER: _ClassVar[int]
    ROOTSYMBOL_FIELD_NUMBER: _ClassVar[int]
    PREVIOUSDAYCLOSEPRICE_FIELD_NUMBER: _ClassVar[int]
    CALLORPUT_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    STRIKEPRICE_FIELD_NUMBER: _ClassVar[int]
    MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
    CONTRACTSIZE_FIELD_NUMBER: _ClassVar[int]
    Symbol: str
    UnderlyingSymbol: str
    RootSymbol: str
    PreviousDayClosePrice: float
    CallOrPut: _orders_enums_pb2.EnumCallOrPut
    Expiration: _timestamp_pb2.Timestamp
    StrikePrice: float
    Multiplier: float
    ContractSize: float
    def __init__(self, Symbol: _Optional[str] = ..., UnderlyingSymbol: _Optional[str] = ..., RootSymbol: _Optional[str] = ..., PreviousDayClosePrice: _Optional[float] = ..., CallOrPut: _Optional[_Union[_orders_enums_pb2.EnumCallOrPut, str]] = ..., Expiration: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., StrikePrice: _Optional[float] = ..., Multiplier: _Optional[float] = ..., ContractSize: _Optional[float] = ...) -> None: ...
