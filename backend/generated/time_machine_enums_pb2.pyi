from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EnumTimeMachineRetention(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumTimeMachineRetention_Undefined: _ClassVar[EnumTimeMachineRetention]
    EnumTimeMachineRetention_Disabled: _ClassVar[EnumTimeMachineRetention]
    EnumTimeMachineRetention_Short: _ClassVar[EnumTimeMachineRetention]
    EnumTimeMachineRetention_Long: _ClassVar[EnumTimeMachineRetention]

class EnumTimeMachineRequestOrigin(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumTimeMachineRequestOrigin_Undefined: _ClassVar[EnumTimeMachineRequestOrigin]
    EnumTimeMachineRequestOrigin_Monitor: _ClassVar[EnumTimeMachineRequestOrigin]
    EnumTimeMachineRequestOrigin_ReviewOrder: _ClassVar[EnumTimeMachineRequestOrigin]
    EnumTimeMachineRequestOrigin_InitiateOrderExecution: _ClassVar[EnumTimeMachineRequestOrigin]
    EnumTimeMachineRequestOrigin_PairingRequest: _ClassVar[EnumTimeMachineRequestOrigin]
    EnumTimeMachineRequestOrigin_P_M_Report: _ClassVar[EnumTimeMachineRequestOrigin]
    EnumTimeMachineRequestOrigin_RiskManager: _ClassVar[EnumTimeMachineRequestOrigin]
    EnumTimeMachineRequestOrigin_PreTransferCheck: _ClassVar[EnumTimeMachineRequestOrigin]
    EnumTimeMachineRequestOrigin_B_P_Check: _ClassVar[EnumTimeMachineRequestOrigin]

class EnumBpType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumBpType_Undefined: _ClassVar[EnumBpType]
    EnumBpType_Bp: _ClassVar[EnumBpType]
    EnumBpType_Pmbp: _ClassVar[EnumBpType]
EnumTimeMachineRetention_Undefined: EnumTimeMachineRetention
EnumTimeMachineRetention_Disabled: EnumTimeMachineRetention
EnumTimeMachineRetention_Short: EnumTimeMachineRetention
EnumTimeMachineRetention_Long: EnumTimeMachineRetention
EnumTimeMachineRequestOrigin_Undefined: EnumTimeMachineRequestOrigin
EnumTimeMachineRequestOrigin_Monitor: EnumTimeMachineRequestOrigin
EnumTimeMachineRequestOrigin_ReviewOrder: EnumTimeMachineRequestOrigin
EnumTimeMachineRequestOrigin_InitiateOrderExecution: EnumTimeMachineRequestOrigin
EnumTimeMachineRequestOrigin_PairingRequest: EnumTimeMachineRequestOrigin
EnumTimeMachineRequestOrigin_P_M_Report: EnumTimeMachineRequestOrigin
EnumTimeMachineRequestOrigin_RiskManager: EnumTimeMachineRequestOrigin
EnumTimeMachineRequestOrigin_PreTransferCheck: EnumTimeMachineRequestOrigin
EnumTimeMachineRequestOrigin_B_P_Check: EnumTimeMachineRequestOrigin
EnumBpType_Undefined: EnumBpType
EnumBpType_Bp: EnumBpType
EnumBpType_Pmbp: EnumBpType
