from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EnumRequestedPositionsLots(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumRequestedPositionsLots_Undefined: _ClassVar[EnumRequestedPositionsLots]
    EnumRequestedPositionsLots_OpenPositions: _ClassVar[EnumRequestedPositionsLots]
    EnumRequestedPositionsLots_ClosedPositions: _ClassVar[EnumRequestedPositionsLots]
    EnumRequestedPositionsLots_PairLots: _ClassVar[EnumRequestedPositionsLots]
    EnumRequestedPositionsLots_UnpairLots: _ClassVar[EnumRequestedPositionsLots]
    EnumRequestedPositionsLots_AutoPairLots: _ClassVar[EnumRequestedPositionsLots]
EnumRequestedPositionsLots_Undefined: EnumRequestedPositionsLots
EnumRequestedPositionsLots_OpenPositions: EnumRequestedPositionsLots
EnumRequestedPositionsLots_ClosedPositions: EnumRequestedPositionsLots
EnumRequestedPositionsLots_PairLots: EnumRequestedPositionsLots
EnumRequestedPositionsLots_UnpairLots: EnumRequestedPositionsLots
EnumRequestedPositionsLots_AutoPairLots: EnumRequestedPositionsLots
