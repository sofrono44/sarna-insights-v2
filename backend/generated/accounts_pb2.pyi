from google.protobuf import timestamp_pb2 as _timestamp_pb2
import common_pb2 as _common_pb2
import accounts_enums_pb2 as _accounts_enums_pb2
import common_bp_enums_pb2 as _common_bp_enums_pb2
import bh_accounts_enums_pb2 as _bh_accounts_enums_pb2
import dividends_enums_pb2 as _dividends_enums_pb2
import common_enums_pb2 as _common_enums_pb2
import account_cash_transactions_enums_pb2 as _account_cash_transactions_enums_pb2
import account_ach_pb2 as _account_ach_pb2
import trading_level_change_pb2 as _trading_level_change_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
from common_pb2 import ResponseError as ResponseError
from common_pb2 import ResponseWarning as ResponseWarning
from common_pb2 import ResponseMessage as ResponseMessage
from common_pb2 import MOVEShockInput as MOVEShockInput
from common_pb2 import MOVECreditSpreadShockInput as MOVECreditSpreadShockInput
from common_pb2 import YieldShockInput as YieldShockInput

DESCRIPTOR: _descriptor.FileDescriptor

class AccountsRequest(_message.Message):
    __slots__ = ("AccountsRequestType", "AccountsInfoRequest", "CreateSubaccountRequest", "DeleteSubaccountRequest", "UpdateNicknameRequest", "CreateVTAccountRequest", "GetAccountActivityRequest", "SubaccountsTransferRequest", "CreateAbaAccountRequest", "CreateAccountAchTransferRequest", "AskForTradingLevelChangeRequest", "LinkAccountGroupRequest", "ChangeAccountGroupRequest")
    ACCOUNTSREQUESTTYPE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTSINFOREQUEST_FIELD_NUMBER: _ClassVar[int]
    CREATESUBACCOUNTREQUEST_FIELD_NUMBER: _ClassVar[int]
    DELETESUBACCOUNTREQUEST_FIELD_NUMBER: _ClassVar[int]
    UPDATENICKNAMEREQUEST_FIELD_NUMBER: _ClassVar[int]
    CREATEVTACCOUNTREQUEST_FIELD_NUMBER: _ClassVar[int]
    GETACCOUNTACTIVITYREQUEST_FIELD_NUMBER: _ClassVar[int]
    SUBACCOUNTSTRANSFERREQUEST_FIELD_NUMBER: _ClassVar[int]
    CREATEABAACCOUNTREQUEST_FIELD_NUMBER: _ClassVar[int]
    CREATEACCOUNTACHTRANSFERREQUEST_FIELD_NUMBER: _ClassVar[int]
    ASKFORTRADINGLEVELCHANGEREQUEST_FIELD_NUMBER: _ClassVar[int]
    LINKACCOUNTGROUPREQUEST_FIELD_NUMBER: _ClassVar[int]
    CHANGEACCOUNTGROUPREQUEST_FIELD_NUMBER: _ClassVar[int]
    AccountsRequestType: _bh_accounts_enums_pb2.EnumAccountsRequestType
    AccountsInfoRequest: AccountsInfoRequest
    CreateSubaccountRequest: CreateSubaccountRequest
    DeleteSubaccountRequest: DeleteSubaccountRequest
    UpdateNicknameRequest: UpdateNicknameRequest
    CreateVTAccountRequest: CreateVTAccountRequest
    GetAccountActivityRequest: GetAccountsActivityRequest
    SubaccountsTransferRequest: SubaccountsTransferRequest
    CreateAbaAccountRequest: _account_ach_pb2.CreateAbaAccountRequest
    CreateAccountAchTransferRequest: _account_ach_pb2.CreateAccountAchTransferRequest
    AskForTradingLevelChangeRequest: _trading_level_change_pb2.AskForTradingLevelChangeRequest
    LinkAccountGroupRequest: LinkAccountGroupRequest
    ChangeAccountGroupRequest: ChangeAccountGroupRequest
    def __init__(self, AccountsRequestType: _Optional[_Union[_bh_accounts_enums_pb2.EnumAccountsRequestType, str]] = ..., AccountsInfoRequest: _Optional[_Union[AccountsInfoRequest, _Mapping]] = ..., CreateSubaccountRequest: _Optional[_Union[CreateSubaccountRequest, _Mapping]] = ..., DeleteSubaccountRequest: _Optional[_Union[DeleteSubaccountRequest, _Mapping]] = ..., UpdateNicknameRequest: _Optional[_Union[UpdateNicknameRequest, _Mapping]] = ..., CreateVTAccountRequest: _Optional[_Union[CreateVTAccountRequest, _Mapping]] = ..., GetAccountActivityRequest: _Optional[_Union[GetAccountsActivityRequest, _Mapping]] = ..., SubaccountsTransferRequest: _Optional[_Union[SubaccountsTransferRequest, _Mapping]] = ..., CreateAbaAccountRequest: _Optional[_Union[_account_ach_pb2.CreateAbaAccountRequest, _Mapping]] = ..., CreateAccountAchTransferRequest: _Optional[_Union[_account_ach_pb2.CreateAccountAchTransferRequest, _Mapping]] = ..., AskForTradingLevelChangeRequest: _Optional[_Union[_trading_level_change_pb2.AskForTradingLevelChangeRequest, _Mapping]] = ..., LinkAccountGroupRequest: _Optional[_Union[LinkAccountGroupRequest, _Mapping]] = ..., ChangeAccountGroupRequest: _Optional[_Union[ChangeAccountGroupRequest, _Mapping]] = ...) -> None: ...

class AccountsResponse(_message.Message):
    __slots__ = ("HasData", "AccountsInfoResponse", "CreateSubaccountResponse", "DeleteSubaccountResponse", "CreatedForVT", "GetAccountsActivityResponse", "SubaccountsTransferResponse", "CreateAbaAccountResponse", "BrowseAbaAccountsResponse", "CreateAccountAchTransferResponse", "LinkAccountGroupResponse")
    HASDATA_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTSINFORESPONSE_FIELD_NUMBER: _ClassVar[int]
    CREATESUBACCOUNTRESPONSE_FIELD_NUMBER: _ClassVar[int]
    DELETESUBACCOUNTRESPONSE_FIELD_NUMBER: _ClassVar[int]
    CREATEDFORVT_FIELD_NUMBER: _ClassVar[int]
    GETACCOUNTSACTIVITYRESPONSE_FIELD_NUMBER: _ClassVar[int]
    SUBACCOUNTSTRANSFERRESPONSE_FIELD_NUMBER: _ClassVar[int]
    CREATEABAACCOUNTRESPONSE_FIELD_NUMBER: _ClassVar[int]
    BROWSEABAACCOUNTSRESPONSE_FIELD_NUMBER: _ClassVar[int]
    CREATEACCOUNTACHTRANSFERRESPONSE_FIELD_NUMBER: _ClassVar[int]
    LINKACCOUNTGROUPRESPONSE_FIELD_NUMBER: _ClassVar[int]
    HasData: bool
    AccountsInfoResponse: AccountsInfoResponse
    CreateSubaccountResponse: CreateSubaccountResponse
    DeleteSubaccountResponse: DeleteSubaccountResponse
    CreatedForVT: CreateVTAccountResponse
    GetAccountsActivityResponse: GetAccountsActivityResponse
    SubaccountsTransferResponse: SubaccountsTransferResponse
    CreateAbaAccountResponse: _account_ach_pb2.CreateAbaAccountResponse
    BrowseAbaAccountsResponse: _account_ach_pb2.BrowseAbaAccountsResponse
    CreateAccountAchTransferResponse: _account_ach_pb2.CreateAccountAchTransferResponse
    LinkAccountGroupResponse: LinkAccountGroupResponse
    def __init__(self, HasData: bool = ..., AccountsInfoResponse: _Optional[_Union[AccountsInfoResponse, _Mapping]] = ..., CreateSubaccountResponse: _Optional[_Union[CreateSubaccountResponse, _Mapping]] = ..., DeleteSubaccountResponse: _Optional[_Union[DeleteSubaccountResponse, _Mapping]] = ..., CreatedForVT: _Optional[_Union[CreateVTAccountResponse, _Mapping]] = ..., GetAccountsActivityResponse: _Optional[_Union[GetAccountsActivityResponse, _Mapping]] = ..., SubaccountsTransferResponse: _Optional[_Union[SubaccountsTransferResponse, _Mapping]] = ..., CreateAbaAccountResponse: _Optional[_Union[_account_ach_pb2.CreateAbaAccountResponse, _Mapping]] = ..., BrowseAbaAccountsResponse: _Optional[_Union[_account_ach_pb2.BrowseAbaAccountsResponse, _Mapping]] = ..., CreateAccountAchTransferResponse: _Optional[_Union[_account_ach_pb2.CreateAccountAchTransferResponse, _Mapping]] = ..., LinkAccountGroupResponse: _Optional[_Union[LinkAccountGroupResponse, _Mapping]] = ...) -> None: ...

class AccountsInfoRequest(_message.Message):
    __slots__ = ("AccountIDs", "AccountNumbers")
    ACCOUNTIDS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTNUMBERS_FIELD_NUMBER: _ClassVar[int]
    AccountIDs: _containers.RepeatedScalarFieldContainer[int]
    AccountNumbers: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, AccountIDs: _Optional[_Iterable[int]] = ..., AccountNumbers: _Optional[_Iterable[str]] = ...) -> None: ...

class AccountsInfoResponse(_message.Message):
    __slots__ = ("HasData", "Accounts", "Warnings", "Errors")
    HASDATA_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    HasData: bool
    Accounts: _containers.RepeatedCompositeFieldContainer[Account]
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, HasData: bool = ..., Accounts: _Optional[_Iterable[_Union[Account, _Mapping]]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class Account(_message.Message):
    __slots__ = ("AccountId", "AccountNumber", "AccountType", "AccountTypeDescription", "Subaccounts", "AccountStatus", "TradingLevel", "Nickname", "CreatedTime", "RecommendedTradingLevel", "PmBpLeverageFactor", "AccountGroups", "BranchId", "AccountRiskType")
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTNUMBER_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTTYPE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTTYPEDESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SUBACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTSTATUS_FIELD_NUMBER: _ClassVar[int]
    TRADINGLEVEL_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    CREATEDTIME_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDEDTRADINGLEVEL_FIELD_NUMBER: _ClassVar[int]
    PMBPLEVERAGEFACTOR_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTGROUPS_FIELD_NUMBER: _ClassVar[int]
    BRANCHID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTRISKTYPE_FIELD_NUMBER: _ClassVar[int]
    AccountId: int
    AccountNumber: str
    AccountType: _accounts_enums_pb2.EnumAccountType
    AccountTypeDescription: str
    Subaccounts: _containers.RepeatedCompositeFieldContainer[Subaccount]
    AccountStatus: _accounts_enums_pb2.EnumAccountStatus
    TradingLevel: _common_bp_enums_pb2.EnumBpOptionTradingLevel
    Nickname: str
    CreatedTime: _timestamp_pb2.Timestamp
    RecommendedTradingLevel: _common_bp_enums_pb2.EnumBpOptionTradingLevel
    PmBpLeverageFactor: float
    AccountGroups: _containers.RepeatedCompositeFieldContainer[AccountGroupLight]
    BranchId: int
    AccountRiskType: _common_enums_pb2.EnumAccountRiskType
    def __init__(self, AccountId: _Optional[int] = ..., AccountNumber: _Optional[str] = ..., AccountType: _Optional[_Union[_accounts_enums_pb2.EnumAccountType, str]] = ..., AccountTypeDescription: _Optional[str] = ..., Subaccounts: _Optional[_Iterable[_Union[Subaccount, _Mapping]]] = ..., AccountStatus: _Optional[_Union[_accounts_enums_pb2.EnumAccountStatus, str]] = ..., TradingLevel: _Optional[_Union[_common_bp_enums_pb2.EnumBpOptionTradingLevel, str]] = ..., Nickname: _Optional[str] = ..., CreatedTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., RecommendedTradingLevel: _Optional[_Union[_common_bp_enums_pb2.EnumBpOptionTradingLevel, str]] = ..., PmBpLeverageFactor: _Optional[float] = ..., AccountGroups: _Optional[_Iterable[_Union[AccountGroupLight, _Mapping]]] = ..., BranchId: _Optional[int] = ..., AccountRiskType: _Optional[_Union[_common_enums_pb2.EnumAccountRiskType, str]] = ...) -> None: ...

class Subaccount(_message.Message):
    __slots__ = ("SubaccountId", "IsMaster", "Code", "Nickname")
    SUBACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    ISMASTER_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    SubaccountId: int
    IsMaster: bool
    Code: str
    Nickname: str
    def __init__(self, SubaccountId: _Optional[int] = ..., IsMaster: bool = ..., Code: _Optional[str] = ..., Nickname: _Optional[str] = ...) -> None: ...

class CreateSubaccountRequest(_message.Message):
    __slots__ = ("AccountId", "Nickname", "InitialCash")
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    INITIALCASH_FIELD_NUMBER: _ClassVar[int]
    AccountId: int
    Nickname: str
    InitialCash: float
    def __init__(self, AccountId: _Optional[int] = ..., Nickname: _Optional[str] = ..., InitialCash: _Optional[float] = ...) -> None: ...

class CreateSubaccountResponse(_message.Message):
    __slots__ = ("HasData", "Account", "Warnings", "Errors")
    HASDATA_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    HasData: bool
    Account: Account
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, HasData: bool = ..., Account: _Optional[_Union[Account, _Mapping]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class DeleteSubaccountRequest(_message.Message):
    __slots__ = ("AccountId", "SubaccountId")
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    SUBACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    AccountId: int
    SubaccountId: int
    def __init__(self, AccountId: _Optional[int] = ..., SubaccountId: _Optional[int] = ...) -> None: ...

class DeleteSubaccountResponse(_message.Message):
    __slots__ = ("HasData", "Account", "Warnings", "Errors")
    HASDATA_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    HasData: bool
    Account: Account
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, HasData: bool = ..., Account: _Optional[_Union[Account, _Mapping]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class UpdateNicknameRequest(_message.Message):
    __slots__ = ("AccountId", "Nickname", "SubaccountId")
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    SUBACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    AccountId: int
    Nickname: str
    SubaccountId: int
    def __init__(self, AccountId: _Optional[int] = ..., Nickname: _Optional[str] = ..., SubaccountId: _Optional[int] = ...) -> None: ...

class CreateVTAccountRequest(_message.Message):
    __slots__ = ("Nickname",)
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    Nickname: str
    def __init__(self, Nickname: _Optional[str] = ...) -> None: ...

class CreateVTAccountResponse(_message.Message):
    __slots__ = ("AccountId", "Warnings", "Errors")
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    AccountId: int
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, AccountId: _Optional[int] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class GetAccountsActivityRequest(_message.Message):
    __slots__ = ("AccountIDs", "AccountNumbers", "From", "To")
    ACCOUNTIDS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTNUMBERS_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    AccountIDs: _containers.RepeatedScalarFieldContainer[int]
    AccountNumbers: _containers.RepeatedScalarFieldContainer[str]
    From: _timestamp_pb2.Timestamp
    To: _timestamp_pb2.Timestamp
    def __init__(self, AccountIDs: _Optional[_Iterable[int]] = ..., AccountNumbers: _Optional[_Iterable[str]] = ..., From: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., To: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetAccountsActivityResponse(_message.Message):
    __slots__ = ("Trades", "Dividends", "AccountCashTransactions", "SubaccountTransfers", "Warnings", "Errors")
    TRADES_FIELD_NUMBER: _ClassVar[int]
    DIVIDENDS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTCASHTRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    SUBACCOUNTTRANSFERS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    Trades: _containers.RepeatedCompositeFieldContainer[Trade]
    Dividends: _containers.RepeatedCompositeFieldContainer[Dividend]
    AccountCashTransactions: _containers.RepeatedCompositeFieldContainer[AccountCashTransaction]
    SubaccountTransfers: _containers.RepeatedCompositeFieldContainer[SubaccountTransfer]
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, Trades: _Optional[_Iterable[_Union[Trade, _Mapping]]] = ..., Dividends: _Optional[_Iterable[_Union[Dividend, _Mapping]]] = ..., AccountCashTransactions: _Optional[_Iterable[_Union[AccountCashTransaction, _Mapping]]] = ..., SubaccountTransfers: _Optional[_Iterable[_Union[SubaccountTransfer, _Mapping]]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class Trade(_message.Message):
    __slots__ = ("TradeId", "AccountId", "Symbol", "Cusip", "Description", "Quantity", "Price", "Principal", "NetAmount", "TaxFee", "SecFee", "NASDFee", "Commission", "TradeTime", "SettlementDate", "SecurityTypeId", "PositionEffectId", "ExternalTradeId", "ClOrderId", "CreatedTime", "OrderAction")
    TRADEID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    CUSIP_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    NETAMOUNT_FIELD_NUMBER: _ClassVar[int]
    TAXFEE_FIELD_NUMBER: _ClassVar[int]
    SECFEE_FIELD_NUMBER: _ClassVar[int]
    NASDFEE_FIELD_NUMBER: _ClassVar[int]
    COMMISSION_FIELD_NUMBER: _ClassVar[int]
    TRADETIME_FIELD_NUMBER: _ClassVar[int]
    SETTLEMENTDATE_FIELD_NUMBER: _ClassVar[int]
    SECURITYTYPEID_FIELD_NUMBER: _ClassVar[int]
    POSITIONEFFECTID_FIELD_NUMBER: _ClassVar[int]
    EXTERNALTRADEID_FIELD_NUMBER: _ClassVar[int]
    CLORDERID_FIELD_NUMBER: _ClassVar[int]
    CREATEDTIME_FIELD_NUMBER: _ClassVar[int]
    ORDERACTION_FIELD_NUMBER: _ClassVar[int]
    TradeId: int
    AccountId: int
    Symbol: str
    Cusip: str
    Description: str
    Quantity: float
    Price: float
    Principal: float
    NetAmount: float
    TaxFee: float
    SecFee: float
    NASDFee: float
    Commission: float
    TradeTime: _timestamp_pb2.Timestamp
    SettlementDate: _timestamp_pb2.Timestamp
    SecurityTypeId: int
    PositionEffectId: int
    ExternalTradeId: str
    ClOrderId: str
    CreatedTime: _timestamp_pb2.Timestamp
    OrderAction: int
    def __init__(self, TradeId: _Optional[int] = ..., AccountId: _Optional[int] = ..., Symbol: _Optional[str] = ..., Cusip: _Optional[str] = ..., Description: _Optional[str] = ..., Quantity: _Optional[float] = ..., Price: _Optional[float] = ..., Principal: _Optional[float] = ..., NetAmount: _Optional[float] = ..., TaxFee: _Optional[float] = ..., SecFee: _Optional[float] = ..., NASDFee: _Optional[float] = ..., Commission: _Optional[float] = ..., TradeTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., SettlementDate: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., SecurityTypeId: _Optional[int] = ..., PositionEffectId: _Optional[int] = ..., ExternalTradeId: _Optional[str] = ..., ClOrderId: _Optional[str] = ..., CreatedTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., OrderAction: _Optional[int] = ...) -> None: ...

class Dividend(_message.Message):
    __slots__ = ("DividendId", "AccountId", "ClearingAccountType", "Symbol", "Cusip", "DividendAccrued", "DividendRate", "Quantity", "DividendPaymentType", "DividendType", "Currency", "EntryDate", "ExDate", "RecordDate", "PayDate")
    DIVIDENDID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    CLEARINGACCOUNTTYPE_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    CUSIP_FIELD_NUMBER: _ClassVar[int]
    DIVIDENDACCRUED_FIELD_NUMBER: _ClassVar[int]
    DIVIDENDRATE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    DIVIDENDPAYMENTTYPE_FIELD_NUMBER: _ClassVar[int]
    DIVIDENDTYPE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    ENTRYDATE_FIELD_NUMBER: _ClassVar[int]
    EXDATE_FIELD_NUMBER: _ClassVar[int]
    RECORDDATE_FIELD_NUMBER: _ClassVar[int]
    PAYDATE_FIELD_NUMBER: _ClassVar[int]
    DividendId: int
    AccountId: int
    ClearingAccountType: _common_enums_pb2.EnumClearingAccountType
    Symbol: str
    Cusip: str
    DividendAccrued: float
    DividendRate: float
    Quantity: float
    DividendPaymentType: _dividends_enums_pb2.EnumDividendPaymentType
    DividendType: _dividends_enums_pb2.EnumDividendType
    Currency: _common_enums_pb2.EnumCurrency
    EntryDate: _timestamp_pb2.Timestamp
    ExDate: _timestamp_pb2.Timestamp
    RecordDate: _timestamp_pb2.Timestamp
    PayDate: _timestamp_pb2.Timestamp
    def __init__(self, DividendId: _Optional[int] = ..., AccountId: _Optional[int] = ..., ClearingAccountType: _Optional[_Union[_common_enums_pb2.EnumClearingAccountType, str]] = ..., Symbol: _Optional[str] = ..., Cusip: _Optional[str] = ..., DividendAccrued: _Optional[float] = ..., DividendRate: _Optional[float] = ..., Quantity: _Optional[float] = ..., DividendPaymentType: _Optional[_Union[_dividends_enums_pb2.EnumDividendPaymentType, str]] = ..., DividendType: _Optional[_Union[_dividends_enums_pb2.EnumDividendType, str]] = ..., Currency: _Optional[_Union[_common_enums_pb2.EnumCurrency, str]] = ..., EntryDate: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ExDate: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., RecordDate: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., PayDate: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AccountCashTransaction(_message.Message):
    __slots__ = ("AccountId", "ActivityDate", "Description", "Source", "AccountCashTransactionType", "NetAmount", "Symbol", "Cusip", "Quantity")
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    ACTIVITYDATE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTCASHTRANSACTIONTYPE_FIELD_NUMBER: _ClassVar[int]
    NETAMOUNT_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    CUSIP_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    AccountId: int
    ActivityDate: _timestamp_pb2.Timestamp
    Description: str
    Source: str
    AccountCashTransactionType: _account_cash_transactions_enums_pb2.EnumAccountCashTransactionType
    NetAmount: float
    Symbol: str
    Cusip: str
    Quantity: float
    def __init__(self, AccountId: _Optional[int] = ..., ActivityDate: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., Description: _Optional[str] = ..., Source: _Optional[str] = ..., AccountCashTransactionType: _Optional[_Union[_account_cash_transactions_enums_pb2.EnumAccountCashTransactionType, str]] = ..., NetAmount: _Optional[float] = ..., Symbol: _Optional[str] = ..., Cusip: _Optional[str] = ..., Quantity: _Optional[float] = ...) -> None: ...

class SubaccountTransfer(_message.Message):
    __slots__ = ("AccountId", "SubaccountIdSource", "SubaccountIdDestination", "UserId", "Symbol", "Quantity", "Cash", "OpenPositionLotId", "CreatedTime")
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    SUBACCOUNTIDSOURCE_FIELD_NUMBER: _ClassVar[int]
    SUBACCOUNTIDDESTINATION_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    CASH_FIELD_NUMBER: _ClassVar[int]
    OPENPOSITIONLOTID_FIELD_NUMBER: _ClassVar[int]
    CREATEDTIME_FIELD_NUMBER: _ClassVar[int]
    AccountId: int
    SubaccountIdSource: int
    SubaccountIdDestination: int
    UserId: int
    Symbol: str
    Quantity: float
    Cash: float
    OpenPositionLotId: int
    CreatedTime: _timestamp_pb2.Timestamp
    def __init__(self, AccountId: _Optional[int] = ..., SubaccountIdSource: _Optional[int] = ..., SubaccountIdDestination: _Optional[int] = ..., UserId: _Optional[int] = ..., Symbol: _Optional[str] = ..., Quantity: _Optional[float] = ..., Cash: _Optional[float] = ..., OpenPositionLotId: _Optional[int] = ..., CreatedTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SubaccountsTransferRequest(_message.Message):
    __slots__ = ("AccountId", "SubaccountIdDestination", "Positions", "PositionsBySymbolAndQuantity", "PositionTransferOrderType", "CashTransfer")
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    SUBACCOUNTIDDESTINATION_FIELD_NUMBER: _ClassVar[int]
    POSITIONS_FIELD_NUMBER: _ClassVar[int]
    POSITIONSBYSYMBOLANDQUANTITY_FIELD_NUMBER: _ClassVar[int]
    POSITIONTRANSFERORDERTYPE_FIELD_NUMBER: _ClassVar[int]
    CASHTRANSFER_FIELD_NUMBER: _ClassVar[int]
    AccountId: int
    SubaccountIdDestination: int
    Positions: _containers.RepeatedCompositeFieldContainer[PositionTransfer]
    PositionsBySymbolAndQuantity: _containers.RepeatedCompositeFieldContainer[PositionBySymbolAndQuantityTransfer]
    PositionTransferOrderType: _accounts_enums_pb2.EnumPositionTransferOrderType
    CashTransfer: CashTransfer
    def __init__(self, AccountId: _Optional[int] = ..., SubaccountIdDestination: _Optional[int] = ..., Positions: _Optional[_Iterable[_Union[PositionTransfer, _Mapping]]] = ..., PositionsBySymbolAndQuantity: _Optional[_Iterable[_Union[PositionBySymbolAndQuantityTransfer, _Mapping]]] = ..., PositionTransferOrderType: _Optional[_Union[_accounts_enums_pb2.EnumPositionTransferOrderType, str]] = ..., CashTransfer: _Optional[_Union[CashTransfer, _Mapping]] = ...) -> None: ...

class CashTransfer(_message.Message):
    __slots__ = ("CashAmount", "SubaccountIdSource")
    CASHAMOUNT_FIELD_NUMBER: _ClassVar[int]
    SUBACCOUNTIDSOURCE_FIELD_NUMBER: _ClassVar[int]
    CashAmount: float
    SubaccountIdSource: int
    def __init__(self, CashAmount: _Optional[float] = ..., SubaccountIdSource: _Optional[int] = ...) -> None: ...

class PositionTransfer(_message.Message):
    __slots__ = ("OpenPositionLotId", "QuantityToTransfer", "SubaccountIdSource")
    OPENPOSITIONLOTID_FIELD_NUMBER: _ClassVar[int]
    QUANTITYTOTRANSFER_FIELD_NUMBER: _ClassVar[int]
    SUBACCOUNTIDSOURCE_FIELD_NUMBER: _ClassVar[int]
    OpenPositionLotId: int
    QuantityToTransfer: int
    SubaccountIdSource: int
    def __init__(self, OpenPositionLotId: _Optional[int] = ..., QuantityToTransfer: _Optional[int] = ..., SubaccountIdSource: _Optional[int] = ...) -> None: ...

class SubaccountsTransferResponse(_message.Message):
    __slots__ = ("Status", "Warnings", "Errors")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    Status: bool
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, Status: bool = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class PositionBySymbolAndQuantityTransfer(_message.Message):
    __slots__ = ("Symbol", "QuantityToTransfer", "OrderType", "SubaccountIdSource")
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    QUANTITYTOTRANSFER_FIELD_NUMBER: _ClassVar[int]
    ORDERTYPE_FIELD_NUMBER: _ClassVar[int]
    SUBACCOUNTIDSOURCE_FIELD_NUMBER: _ClassVar[int]
    Symbol: str
    QuantityToTransfer: float
    OrderType: int
    SubaccountIdSource: int
    def __init__(self, Symbol: _Optional[str] = ..., QuantityToTransfer: _Optional[float] = ..., OrderType: _Optional[int] = ..., SubaccountIdSource: _Optional[int] = ...) -> None: ...

class LinkAccountGroupRequest(_message.Message):
    __slots__ = ("AccountGroupId", "AccountIds", "AccountNumbers")
    ACCOUNTGROUPID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTIDS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTNUMBERS_FIELD_NUMBER: _ClassVar[int]
    AccountGroupId: int
    AccountIds: _containers.RepeatedScalarFieldContainer[int]
    AccountNumbers: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, AccountGroupId: _Optional[int] = ..., AccountIds: _Optional[_Iterable[int]] = ..., AccountNumbers: _Optional[_Iterable[str]] = ...) -> None: ...

class ChangeAccountGroupRequest(_message.Message):
    __slots__ = ("OldAccountGroupId", "NewAccountGroupId", "AccountId", "AccountNumber")
    OLDACCOUNTGROUPID_FIELD_NUMBER: _ClassVar[int]
    NEWACCOUNTGROUPID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTNUMBER_FIELD_NUMBER: _ClassVar[int]
    OldAccountGroupId: int
    NewAccountGroupId: int
    AccountId: int
    AccountNumber: str
    def __init__(self, OldAccountGroupId: _Optional[int] = ..., NewAccountGroupId: _Optional[int] = ..., AccountId: _Optional[int] = ..., AccountNumber: _Optional[str] = ...) -> None: ...

class LinkAccountGroupResponse(_message.Message):
    __slots__ = ("Success", "Warnings", "Errors")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    Success: bool
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, Success: bool = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class AccountGroupLight(_message.Message):
    __slots__ = ("AccountGroupId", "Name")
    ACCOUNTGROUPID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    AccountGroupId: int
    Name: str
    def __init__(self, AccountGroupId: _Optional[int] = ..., Name: _Optional[str] = ...) -> None: ...
