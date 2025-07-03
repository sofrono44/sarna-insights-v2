import accounts_pb2 as _accounts_pb2
import common_pb2 as _common_pb2
import user_pb2 as _user_pb2
import search_pb2 as _search_pb2
from admin import admin_management_enums_pb2 as _admin_management_enums_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AccountsSearchRequest(_message.Message):
    __slots__ = ("SearchCriteria",)
    SEARCHCRITERIA_FIELD_NUMBER: _ClassVar[int]
    SearchCriteria: _search_pb2.SearchCriteria
    def __init__(self, SearchCriteria: _Optional[_Union[_search_pb2.SearchCriteria, _Mapping]] = ...) -> None: ...

class AccountsSearchResponse(_message.Message):
    __slots__ = ("Items", "Warnings", "Errors", "SearchCriteria", "Page")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    SEARCHCRITERIA_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    Items: _containers.RepeatedCompositeFieldContainer[AccountInfo]
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    SearchCriteria: _search_pb2.SearchCriteria
    Page: _search_pb2.PageResponse
    def __init__(self, Items: _Optional[_Iterable[_Union[AccountInfo, _Mapping]]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ..., SearchCriteria: _Optional[_Union[_search_pb2.SearchCriteria, _Mapping]] = ..., Page: _Optional[_Union[_search_pb2.PageResponse, _Mapping]] = ...) -> None: ...

class UpdateAccountRequest(_message.Message):
    __slots__ = ("Account", "IsEmployeeAccount", "IsRiskMonitoringEnabled")
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    ISEMPLOYEEACCOUNT_FIELD_NUMBER: _ClassVar[int]
    ISRISKMONITORINGENABLED_FIELD_NUMBER: _ClassVar[int]
    Account: _accounts_pb2.Account
    IsEmployeeAccount: bool
    IsRiskMonitoringEnabled: bool
    def __init__(self, Account: _Optional[_Union[_accounts_pb2.Account, _Mapping]] = ..., IsEmployeeAccount: bool = ..., IsRiskMonitoringEnabled: bool = ...) -> None: ...

class AccountInfo(_message.Message):
    __slots__ = ("Account",)
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    Account: _accounts_pb2.Account
    def __init__(self, Account: _Optional[_Union[_accounts_pb2.Account, _Mapping]] = ...) -> None: ...

class UsersSearchRequest(_message.Message):
    __slots__ = ("Query",)
    QUERY_FIELD_NUMBER: _ClassVar[int]
    Query: str
    def __init__(self, Query: _Optional[str] = ...) -> None: ...

class UsersSearchResponse(_message.Message):
    __slots__ = ("Items", "Warnings", "Errors")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    Items: _containers.RepeatedCompositeFieldContainer[_user_pb2.User]
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, Items: _Optional[_Iterable[_Union[_user_pb2.User, _Mapping]]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class GetUserAccountsRequest(_message.Message):
    __slots__ = ("UserId",)
    USERID_FIELD_NUMBER: _ClassVar[int]
    UserId: int
    def __init__(self, UserId: _Optional[int] = ...) -> None: ...

class GetUserAccountsResponse(_message.Message):
    __slots__ = ("Items", "Warnings", "Errors")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    Items: _containers.RepeatedCompositeFieldContainer[_accounts_pb2.Account]
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, Items: _Optional[_Iterable[_Union[_accounts_pb2.Account, _Mapping]]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class GetAccountRequest(_message.Message):
    __slots__ = ("AccountId", "AccountNumber")
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTNUMBER_FIELD_NUMBER: _ClassVar[int]
    AccountId: int
    AccountNumber: str
    def __init__(self, AccountId: _Optional[int] = ..., AccountNumber: _Optional[str] = ...) -> None: ...

class GetAccountResponse(_message.Message):
    __slots__ = ("Account", "IsEmployeeAccount", "IsRiskMonitoringEnabled", "Warnings", "Errors")
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    ISEMPLOYEEACCOUNT_FIELD_NUMBER: _ClassVar[int]
    ISRISKMONITORINGENABLED_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    Account: _accounts_pb2.Account
    IsEmployeeAccount: bool
    IsRiskMonitoringEnabled: bool
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, Account: _Optional[_Union[_accounts_pb2.Account, _Mapping]] = ..., IsEmployeeAccount: bool = ..., IsRiskMonitoringEnabled: bool = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class GetSecurityQuestionsRequest(_message.Message):
    __slots__ = ("UserId",)
    USERID_FIELD_NUMBER: _ClassVar[int]
    UserId: int
    def __init__(self, UserId: _Optional[int] = ...) -> None: ...

class UpdateUserStatusRequest(_message.Message):
    __slots__ = ("IsBlocked", "UserId")
    ISBLOCKED_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    IsBlocked: bool
    UserId: int
    def __init__(self, IsBlocked: bool = ..., UserId: _Optional[int] = ...) -> None: ...

class GetUserStatusRequest(_message.Message):
    __slots__ = ("UserId",)
    USERID_FIELD_NUMBER: _ClassVar[int]
    UserId: int
    def __init__(self, UserId: _Optional[int] = ...) -> None: ...

class GetUserStatusResponse(_message.Message):
    __slots__ = ("IsBlocked", "Warnings", "Errors")
    ISBLOCKED_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    IsBlocked: bool
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, IsBlocked: bool = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class UpdateUserIsEmployeeStatusRequest(_message.Message):
    __slots__ = ("IsEmployee", "UserId")
    ISEMPLOYEE_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    IsEmployee: bool
    UserId: int
    def __init__(self, IsEmployee: bool = ..., UserId: _Optional[int] = ...) -> None: ...

class GetUserRequest(_message.Message):
    __slots__ = ("UserId",)
    USERID_FIELD_NUMBER: _ClassVar[int]
    UserId: int
    def __init__(self, UserId: _Optional[int] = ...) -> None: ...

class LinkUserToAccountRequest(_message.Message):
    __slots__ = ("UserId", "AccountNumber")
    USERID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTNUMBER_FIELD_NUMBER: _ClassVar[int]
    UserId: int
    AccountNumber: str
    def __init__(self, UserId: _Optional[int] = ..., AccountNumber: _Optional[str] = ...) -> None: ...

class GetUserResponse(_message.Message):
    __slots__ = ("User", "Warnings", "Errors")
    USER_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    User: _user_pb2.User
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, User: _Optional[_Union[_user_pb2.User, _Mapping]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class SendEmailToUserRequest(_message.Message):
    __slots__ = ("UserId", "AccountId", "EmailType", "AdditionalInfo")
    USERID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    EMAILTYPE_FIELD_NUMBER: _ClassVar[int]
    ADDITIONALINFO_FIELD_NUMBER: _ClassVar[int]
    UserId: int
    AccountId: int
    EmailType: _admin_management_enums_pb2.EnumAdminEmailType
    AdditionalInfo: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, UserId: _Optional[int] = ..., AccountId: _Optional[int] = ..., EmailType: _Optional[_Union[_admin_management_enums_pb2.EnumAdminEmailType, str]] = ..., AdditionalInfo: _Optional[_Iterable[str]] = ...) -> None: ...

class SendEmailToUserResponse(_message.Message):
    __slots__ = ("EmailSent", "Warnings", "Errors")
    EMAILSENT_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    EmailSent: bool
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, EmailSent: bool = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class ManageUserRequest(_message.Message):
    __slots__ = ("User",)
    USER_FIELD_NUMBER: _ClassVar[int]
    User: _user_pb2.User
    def __init__(self, User: _Optional[_Union[_user_pb2.User, _Mapping]] = ...) -> None: ...

class ManageUserResponse(_message.Message):
    __slots__ = ("UserId", "IsSuccess", "Warnings", "Errors")
    USERID_FIELD_NUMBER: _ClassVar[int]
    ISSUCCESS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    UserId: int
    IsSuccess: bool
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, UserId: _Optional[int] = ..., IsSuccess: bool = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class BranchesRequest(_message.Message):
    __slots__ = ("BranchId",)
    BRANCHID_FIELD_NUMBER: _ClassVar[int]
    BranchId: int
    def __init__(self, BranchId: _Optional[int] = ...) -> None: ...

class GetBranchesResponse(_message.Message):
    __slots__ = ("Branches", "Warnings", "Errors")
    BRANCHES_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    Branches: _containers.RepeatedCompositeFieldContainer[Branch]
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, Branches: _Optional[_Iterable[_Union[Branch, _Mapping]]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class ManageBranchResponse(_message.Message):
    __slots__ = ("BranchId", "IsSuccess", "Warnings", "Errors")
    BRANCHID_FIELD_NUMBER: _ClassVar[int]
    ISSUCCESS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    BranchId: int
    IsSuccess: bool
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, BranchId: _Optional[int] = ..., IsSuccess: bool = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class Branch(_message.Message):
    __slots__ = ("BranchId", "BranchName", "BranchCode", "ParentBranchId", "ClearingHouseId", "CountryCode")
    BRANCHID_FIELD_NUMBER: _ClassVar[int]
    BRANCHNAME_FIELD_NUMBER: _ClassVar[int]
    BRANCHCODE_FIELD_NUMBER: _ClassVar[int]
    PARENTBRANCHID_FIELD_NUMBER: _ClassVar[int]
    CLEARINGHOUSEID_FIELD_NUMBER: _ClassVar[int]
    COUNTRYCODE_FIELD_NUMBER: _ClassVar[int]
    BranchId: int
    BranchName: str
    BranchCode: str
    ParentBranchId: int
    ClearingHouseId: int
    CountryCode: str
    def __init__(self, BranchId: _Optional[int] = ..., BranchName: _Optional[str] = ..., BranchCode: _Optional[str] = ..., ParentBranchId: _Optional[int] = ..., ClearingHouseId: _Optional[int] = ..., CountryCode: _Optional[str] = ...) -> None: ...

class UploadMorningFileRequest(_message.Message):
    __slots__ = ("FileType", "FileName", "FileContent", "FileSize")
    FILETYPE_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    FILECONTENT_FIELD_NUMBER: _ClassVar[int]
    FILESIZE_FIELD_NUMBER: _ClassVar[int]
    FileType: _admin_management_enums_pb2.EnumAdminFileType
    FileName: str
    FileContent: bytes
    FileSize: int
    def __init__(self, FileType: _Optional[_Union[_admin_management_enums_pb2.EnumAdminFileType, str]] = ..., FileName: _Optional[str] = ..., FileContent: _Optional[bytes] = ..., FileSize: _Optional[int] = ...) -> None: ...

class UploadMorningFileResponse(_message.Message):
    __slots__ = ("IsSucceed", "SavedFileName", "Warnings", "Errors")
    ISSUCCEED_FIELD_NUMBER: _ClassVar[int]
    SAVEDFILENAME_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    IsSucceed: bool
    SavedFileName: str
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, IsSucceed: bool = ..., SavedFileName: _Optional[str] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class AccountGroupsResponse(_message.Message):
    __slots__ = ("AccountGroups", "Warnings", "Errors")
    ACCOUNTGROUPS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    AccountGroups: _containers.RepeatedCompositeFieldContainer[AccountGroup]
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, AccountGroups: _Optional[_Iterable[_Union[AccountGroup, _Mapping]]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class AccountGroupRequest(_message.Message):
    __slots__ = ("AccountGroupId",)
    ACCOUNTGROUPID_FIELD_NUMBER: _ClassVar[int]
    AccountGroupId: int
    def __init__(self, AccountGroupId: _Optional[int] = ...) -> None: ...

class AccountGroupResponse(_message.Message):
    __slots__ = ("AccountGroup", "Warnings", "Errors")
    ACCOUNTGROUP_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    AccountGroup: AccountGroup
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, AccountGroup: _Optional[_Union[AccountGroup, _Mapping]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class ManageAccountGroupsResponse(_message.Message):
    __slots__ = ("AccountGroupId", "Warnings", "Errors")
    ACCOUNTGROUPID_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    AccountGroupId: int
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, AccountGroupId: _Optional[int] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class DeleteAccountGroupRequest(_message.Message):
    __slots__ = ("AccountGroupId",)
    ACCOUNTGROUPID_FIELD_NUMBER: _ClassVar[int]
    AccountGroupId: int
    def __init__(self, AccountGroupId: _Optional[int] = ...) -> None: ...

class DeleteAccountGroupResponse(_message.Message):
    __slots__ = ("IsSuccess", "Warnings", "Errors")
    ISSUCCESS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    IsSuccess: bool
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, IsSuccess: bool = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class AccountGroup(_message.Message):
    __slots__ = ("AccountGroupId", "Name", "BranchId", "Accounts", "AccountsCount", "RepresentativeId", "IsRiskMonitoringEnabled", "RiskProfileId", "AccountFilter")
    ACCOUNTGROUPID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    BRANCHID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTSCOUNT_FIELD_NUMBER: _ClassVar[int]
    REPRESENTATIVEID_FIELD_NUMBER: _ClassVar[int]
    ISRISKMONITORINGENABLED_FIELD_NUMBER: _ClassVar[int]
    RISKPROFILEID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTFILTER_FIELD_NUMBER: _ClassVar[int]
    AccountGroupId: int
    Name: str
    BranchId: int
    Accounts: _containers.RepeatedCompositeFieldContainer[_accounts_pb2.Account]
    AccountsCount: int
    RepresentativeId: int
    IsRiskMonitoringEnabled: bool
    RiskProfileId: int
    AccountFilter: _search_pb2.FilterGroup
    def __init__(self, AccountGroupId: _Optional[int] = ..., Name: _Optional[str] = ..., BranchId: _Optional[int] = ..., Accounts: _Optional[_Iterable[_Union[_accounts_pb2.Account, _Mapping]]] = ..., AccountsCount: _Optional[int] = ..., RepresentativeId: _Optional[int] = ..., IsRiskMonitoringEnabled: bool = ..., RiskProfileId: _Optional[int] = ..., AccountFilter: _Optional[_Union[_search_pb2.FilterGroup, _Mapping]] = ...) -> None: ...
