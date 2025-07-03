from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EnumDividendType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumDividendType_Undefined: _ClassVar[EnumDividendType]
    EnumDividendType_Change: _ClassVar[EnumDividendType]
    EnumDividendType_Duplicate: _ClassVar[EnumDividendType]
    EnumDividendType_New: _ClassVar[EnumDividendType]

class EnumDividendPaymentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumDividendPaymentType_Undefined: _ClassVar[EnumDividendPaymentType]
    EnumDividendPaymentType_FixedIncome_Interest: _ClassVar[EnumDividendPaymentType]
    EnumDividendPaymentType_Cash_Dividend: _ClassVar[EnumDividendPaymentType]
    EnumDividendPaymentType_Qualified: _ClassVar[EnumDividendPaymentType]
    EnumDividendPaymentType_Stock_Dividend: _ClassVar[EnumDividendPaymentType]
    EnumDividendPaymentType_Stock_Split: _ClassVar[EnumDividendPaymentType]
    EnumDividendPaymentType_Reverse_Split: _ClassVar[EnumDividendPaymentType]
    EnumDividendPaymentType_Medium_Cap_Gain: _ClassVar[EnumDividendPaymentType]
    EnumDividendPaymentType_Long_Cap_Gain: _ClassVar[EnumDividendPaymentType]
    EnumDividendPaymentType_Royalties: _ClassVar[EnumDividendPaymentType]
EnumDividendType_Undefined: EnumDividendType
EnumDividendType_Change: EnumDividendType
EnumDividendType_Duplicate: EnumDividendType
EnumDividendType_New: EnumDividendType
EnumDividendPaymentType_Undefined: EnumDividendPaymentType
EnumDividendPaymentType_FixedIncome_Interest: EnumDividendPaymentType
EnumDividendPaymentType_Cash_Dividend: EnumDividendPaymentType
EnumDividendPaymentType_Qualified: EnumDividendPaymentType
EnumDividendPaymentType_Stock_Dividend: EnumDividendPaymentType
EnumDividendPaymentType_Stock_Split: EnumDividendPaymentType
EnumDividendPaymentType_Reverse_Split: EnumDividendPaymentType
EnumDividendPaymentType_Medium_Cap_Gain: EnumDividendPaymentType
EnumDividendPaymentType_Long_Cap_Gain: EnumDividendPaymentType
EnumDividendPaymentType_Royalties: EnumDividendPaymentType
