from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EnumUserType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumUserType_Undefined: _ClassVar[EnumUserType]
    EnumUserType_Individual: _ClassVar[EnumUserType]
    EnumUserType_Representative: _ClassVar[EnumUserType]
    EnumUserType_BranchAdmin: _ClassVar[EnumUserType]
    EnumUserType_SuperAdmin: _ClassVar[EnumUserType]
    EnumUserType_SoftwareApp: _ClassVar[EnumUserType]

class EnumVerificationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumVerificationStatus_Undefined: _ClassVar[EnumVerificationStatus]
    EnumVerificationStatus_Created: _ClassVar[EnumVerificationStatus]
    EnumVerificationStatus_Review: _ClassVar[EnumVerificationStatus]
    EnumVerificationStatus_Declined: _ClassVar[EnumVerificationStatus]
    EnumVerificationStatus_Failed: _ClassVar[EnumVerificationStatus]
    EnumVerificationStatus_Approved: _ClassVar[EnumVerificationStatus]

class EnumUserPermission(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumUserPermission_Undefined: _ClassVar[EnumUserPermission]
    EnumUserPermission_StockRealTimeQuote: _ClassVar[EnumUserPermission]
    EnumUserPermission_OptionRealTimeQuote: _ClassVar[EnumUserPermission]
    EnumUserPermission_AccountAccess: _ClassVar[EnumUserPermission]
    EnumUserPermission_UserAccess: _ClassVar[EnumUserPermission]
    EnumUserPermission_ManageSuperAdmin: _ClassVar[EnumUserPermission]
    EnumUserPermission_FileUpload: _ClassVar[EnumUserPermission]
EnumUserType_Undefined: EnumUserType
EnumUserType_Individual: EnumUserType
EnumUserType_Representative: EnumUserType
EnumUserType_BranchAdmin: EnumUserType
EnumUserType_SuperAdmin: EnumUserType
EnumUserType_SoftwareApp: EnumUserType
EnumVerificationStatus_Undefined: EnumVerificationStatus
EnumVerificationStatus_Created: EnumVerificationStatus
EnumVerificationStatus_Review: EnumVerificationStatus
EnumVerificationStatus_Declined: EnumVerificationStatus
EnumVerificationStatus_Failed: EnumVerificationStatus
EnumVerificationStatus_Approved: EnumVerificationStatus
EnumUserPermission_Undefined: EnumUserPermission
EnumUserPermission_StockRealTimeQuote: EnumUserPermission
EnumUserPermission_OptionRealTimeQuote: EnumUserPermission
EnumUserPermission_AccountAccess: EnumUserPermission
EnumUserPermission_UserAccess: EnumUserPermission
EnumUserPermission_ManageSuperAdmin: EnumUserPermission
EnumUserPermission_FileUpload: EnumUserPermission
