import sessions_enums_pb2 as _sessions_enums_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class User(_message.Message):
    __slots__ = ("Id", "Name", "Email", "IsEmployee", "FirstName", "LastName", "Username", "CountryCode", "LanguageCode", "BranchId", "RepresentativeId", "Password", "RequestResetPassword", "UserRole", "UserPermissions", "DateOfBirth")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ISEMPLOYEE_FIELD_NUMBER: _ClassVar[int]
    FIRSTNAME_FIELD_NUMBER: _ClassVar[int]
    LASTNAME_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    COUNTRYCODE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGECODE_FIELD_NUMBER: _ClassVar[int]
    BRANCHID_FIELD_NUMBER: _ClassVar[int]
    REPRESENTATIVEID_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    REQUESTRESETPASSWORD_FIELD_NUMBER: _ClassVar[int]
    USERROLE_FIELD_NUMBER: _ClassVar[int]
    USERPERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    DATEOFBIRTH_FIELD_NUMBER: _ClassVar[int]
    Id: int
    Name: str
    Email: str
    IsEmployee: bool
    FirstName: str
    LastName: str
    Username: str
    CountryCode: str
    LanguageCode: str
    BranchId: int
    RepresentativeId: int
    Password: str
    RequestResetPassword: bool
    UserRole: _sessions_enums_pb2.EnumUserType
    UserPermissions: _containers.RepeatedCompositeFieldContainer[UserPermission]
    DateOfBirth: _timestamp_pb2.Timestamp
    def __init__(self, Id: _Optional[int] = ..., Name: _Optional[str] = ..., Email: _Optional[str] = ..., IsEmployee: bool = ..., FirstName: _Optional[str] = ..., LastName: _Optional[str] = ..., Username: _Optional[str] = ..., CountryCode: _Optional[str] = ..., LanguageCode: _Optional[str] = ..., BranchId: _Optional[int] = ..., RepresentativeId: _Optional[int] = ..., Password: _Optional[str] = ..., RequestResetPassword: bool = ..., UserRole: _Optional[_Union[_sessions_enums_pb2.EnumUserType, str]] = ..., UserPermissions: _Optional[_Iterable[_Union[UserPermission, _Mapping]]] = ..., DateOfBirth: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class UserPermission(_message.Message):
    __slots__ = ("UserId", "UserPermissionType", "BranchId", "RepresentativeId")
    USERID_FIELD_NUMBER: _ClassVar[int]
    USERPERMISSIONTYPE_FIELD_NUMBER: _ClassVar[int]
    BRANCHID_FIELD_NUMBER: _ClassVar[int]
    REPRESENTATIVEID_FIELD_NUMBER: _ClassVar[int]
    UserId: int
    UserPermissionType: _sessions_enums_pb2.EnumUserPermission
    BranchId: int
    RepresentativeId: int
    def __init__(self, UserId: _Optional[int] = ..., UserPermissionType: _Optional[_Union[_sessions_enums_pb2.EnumUserPermission, str]] = ..., BranchId: _Optional[int] = ..., RepresentativeId: _Optional[int] = ...) -> None: ...
