from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EnumQuoteDataType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumQuoteDataType_Undefined: _ClassVar[EnumQuoteDataType]
    EnumQuoteDataType_ChainQuotes: _ClassVar[EnumQuoteDataType]
    EnumQuoteDataType_OptionQuote: _ClassVar[EnumQuoteDataType]
    EnumQuoteDataType_StockQuote: _ClassVar[EnumQuoteDataType]
    EnumQuoteDataType_FixedIncomeQuote: _ClassVar[EnumQuoteDataType]
EnumQuoteDataType_Undefined: EnumQuoteDataType
EnumQuoteDataType_ChainQuotes: EnumQuoteDataType
EnumQuoteDataType_OptionQuote: EnumQuoteDataType
EnumQuoteDataType_StockQuote: EnumQuoteDataType
EnumQuoteDataType_FixedIncomeQuote: EnumQuoteDataType
