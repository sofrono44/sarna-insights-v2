from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EnumOrderPriceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumOrderPriceType_Undefined: _ClassVar[EnumOrderPriceType]
    EnumOrderPriceType_Market: _ClassVar[EnumOrderPriceType]
    EnumOrderPriceType_Limit: _ClassVar[EnumOrderPriceType]
    EnumOrderPriceType_Stop: _ClassVar[EnumOrderPriceType]
    EnumOrderPriceType_StopLimit: _ClassVar[EnumOrderPriceType]
    EnumOrderPriceType_MarketOnClose: _ClassVar[EnumOrderPriceType]
    EnumOrderPriceType_Even: _ClassVar[EnumOrderPriceType]
    EnumOrderPriceType_WithOrWithout: _ClassVar[EnumOrderPriceType]
    EnumOrderPriceType_LimitOrBetter: _ClassVar[EnumOrderPriceType]
    EnumOrderPriceType_LimitWithOrWithout: _ClassVar[EnumOrderPriceType]
    EnumOrderPriceType_OnBasis: _ClassVar[EnumOrderPriceType]

class EnumOrderPositionEffect(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumOrderPositionEffect_Undefined: _ClassVar[EnumOrderPositionEffect]
    EnumOrderPositionEffect_Open: _ClassVar[EnumOrderPositionEffect]
    EnumOrderPositionEffect_Close: _ClassVar[EnumOrderPositionEffect]
EnumOrderPriceType_Undefined: EnumOrderPriceType
EnumOrderPriceType_Market: EnumOrderPriceType
EnumOrderPriceType_Limit: EnumOrderPriceType
EnumOrderPriceType_Stop: EnumOrderPriceType
EnumOrderPriceType_StopLimit: EnumOrderPriceType
EnumOrderPriceType_MarketOnClose: EnumOrderPriceType
EnumOrderPriceType_Even: EnumOrderPriceType
EnumOrderPriceType_WithOrWithout: EnumOrderPriceType
EnumOrderPriceType_LimitOrBetter: EnumOrderPriceType
EnumOrderPriceType_LimitWithOrWithout: EnumOrderPriceType
EnumOrderPriceType_OnBasis: EnumOrderPriceType
EnumOrderPositionEffect_Undefined: EnumOrderPositionEffect
EnumOrderPositionEffect_Open: EnumOrderPositionEffect
EnumOrderPositionEffect_Close: EnumOrderPositionEffect
