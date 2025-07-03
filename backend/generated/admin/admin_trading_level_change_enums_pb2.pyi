from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EnumAccountApprovalStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumAccountApprovalStatus_Undefined: _ClassVar[EnumAccountApprovalStatus]
    EnumAccountApprovalStatus_Pending: _ClassVar[EnumAccountApprovalStatus]
    EnumAccountApprovalStatus_Approved: _ClassVar[EnumAccountApprovalStatus]
    EnumAccountApprovalStatus_Rejected: _ClassVar[EnumAccountApprovalStatus]
    EnumAccountApprovalStatus_Canceled: _ClassVar[EnumAccountApprovalStatus]
EnumAccountApprovalStatus_Undefined: EnumAccountApprovalStatus
EnumAccountApprovalStatus_Pending: EnumAccountApprovalStatus
EnumAccountApprovalStatus_Approved: EnumAccountApprovalStatus
EnumAccountApprovalStatus_Rejected: EnumAccountApprovalStatus
EnumAccountApprovalStatus_Canceled: EnumAccountApprovalStatus
