import common_pb2 as _common_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
import account_ach_enums_pb2 as _account_ach_enums_pb2
import account_ach_sdr_enums_pb2 as _account_ach_sdr_enums_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateAbaAccountRequest(_message.Message):
    __slots__ = ("AbaAccount",)
    ABAACCOUNT_FIELD_NUMBER: _ClassVar[int]
    AbaAccount: AbaAccount
    def __init__(self, AbaAccount: _Optional[_Union[AbaAccount, _Mapping]] = ...) -> None: ...

class CreateAbaAccountResponse(_message.Message):
    __slots__ = ("Status", "Warnings", "Errors")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    Status: bool
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, Status: bool = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class BrowseAbaAccountsResponse(_message.Message):
    __slots__ = ("AbaAccounts", "Warnings", "Errors")
    ABAACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    AbaAccounts: _containers.RepeatedCompositeFieldContainer[AbaAccount]
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, AbaAccounts: _Optional[_Iterable[_Union[AbaAccount, _Mapping]]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class AbaAccount(_message.Message):
    __slots__ = ("AbaAccountId", "Name", "RoutingNumber", "AccountNumber", "Type", "OwnerType")
    ABAACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ROUTINGNUMBER_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTNUMBER_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    OWNERTYPE_FIELD_NUMBER: _ClassVar[int]
    AbaAccountId: int
    Name: str
    RoutingNumber: str
    AccountNumber: str
    Type: _account_ach_sdr_enums_pb2.EnumAbaAccountType
    OwnerType: _account_ach_sdr_enums_pb2.EnumAbaAccountOwnerType
    def __init__(self, AbaAccountId: _Optional[int] = ..., Name: _Optional[str] = ..., RoutingNumber: _Optional[str] = ..., AccountNumber: _Optional[str] = ..., Type: _Optional[_Union[_account_ach_sdr_enums_pb2.EnumAbaAccountType, str]] = ..., OwnerType: _Optional[_Union[_account_ach_sdr_enums_pb2.EnumAbaAccountOwnerType, str]] = ...) -> None: ...

class CreateAccountAchTransferRequest(_message.Message):
    __slots__ = ("AccountAchTransaction",)
    ACCOUNTACHTRANSACTION_FIELD_NUMBER: _ClassVar[int]
    AccountAchTransaction: AccountAchTransaction
    def __init__(self, AccountAchTransaction: _Optional[_Union[AccountAchTransaction, _Mapping]] = ...) -> None: ...

class CreateAccountAchTransferResponse(_message.Message):
    __slots__ = ("Status", "Warnings", "Errors")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    Status: bool
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, Status: bool = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class AccountAchTransaction(_message.Message):
    __slots__ = ("AccountAchTransactionId", "AccountId", "AbaAccountId", "Type", "amount", "Status", "CreatedTime", "LastModifiedTime")
    ACCOUNTACHTRANSACTIONID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    ABAACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATEDTIME_FIELD_NUMBER: _ClassVar[int]
    LASTMODIFIEDTIME_FIELD_NUMBER: _ClassVar[int]
    AccountAchTransactionId: int
    AccountId: int
    AbaAccountId: int
    Type: _account_ach_enums_pb2.EnumAccountAchTransactionType
    amount: float
    Status: _account_ach_enums_pb2.EnumAccountAchTransactionStatus
    CreatedTime: _timestamp_pb2.Timestamp
    LastModifiedTime: _timestamp_pb2.Timestamp
    def __init__(self, AccountAchTransactionId: _Optional[int] = ..., AccountId: _Optional[int] = ..., AbaAccountId: _Optional[int] = ..., Type: _Optional[_Union[_account_ach_enums_pb2.EnumAccountAchTransactionType, str]] = ..., amount: _Optional[float] = ..., Status: _Optional[_Union[_account_ach_enums_pb2.EnumAccountAchTransactionStatus, str]] = ..., CreatedTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., LastModifiedTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
