import sessions_pb2 as _sessions_pb2
import bp_pb2 as _bp_pb2
import quotes_pb2 as _quotes_pb2
import accounts_pb2 as _accounts_pb2
import common_pb2 as _common_pb2
import orders_pb2 as _orders_pb2
import order_execution_logs_pb2 as _order_execution_logs_pb2
import positions_pb2 as _positions_pb2
import balances_pb2 as _balances_pb2
import trading_pb2 as _trading_pb2
import securities_master_pb2 as _securities_master_pb2
import common_pb2 as _common_pb2_1
import account_application_pb2 as _account_application_pb2
import common_pb2 as _common_pb2_1_1
import market_data_entitlement_pb2 as _market_data_entitlement_pb2
import glossary_pb2 as _glossary_pb2
import subscriptions_pb2 as _subscriptions_pb2
import ux_messages_pb2 as _ux_messages_pb2
import user_data_pb2 as _user_data_pb2
import commissions_pb2 as _commissions_pb2
import search_pb2 as _search_pb2
import time_machine_pb2 as _time_machine_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ApiResponse(_message.Message):
    __slots__ = ("SessionInfoResponse", "AccountsResponse", "BalancesInfoResponse", "QuoteResponse", "OrdersInfoResponse", "OrderExecutionLogsResponse", "PositionsInfoResponse", "BuyingPowerResponse", "SecuritiesMasterDataResponse", "TradeResponse", "AccountApplicationResponse", "GlossaryResponse", "CommissionResponse", "SubscriptionResponse", "ChainQuoteResponse", "GetExpirationsResponse", "GetUxMessagesResponse", "UserDataResponse", "BalanceAdjustmentResponse", "BalanceCashInfoResponse", "SearchServiceResponse", "SearchServiceDefinitionResponse", "TimeMachineRecentResponse", "TimeMachineDownloadResponse", "Warnings", "Errors")
    SESSIONINFORESPONSE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTSRESPONSE_FIELD_NUMBER: _ClassVar[int]
    BALANCESINFORESPONSE_FIELD_NUMBER: _ClassVar[int]
    QUOTERESPONSE_FIELD_NUMBER: _ClassVar[int]
    ORDERSINFORESPONSE_FIELD_NUMBER: _ClassVar[int]
    ORDEREXECUTIONLOGSRESPONSE_FIELD_NUMBER: _ClassVar[int]
    POSITIONSINFORESPONSE_FIELD_NUMBER: _ClassVar[int]
    BUYINGPOWERRESPONSE_FIELD_NUMBER: _ClassVar[int]
    SECURITIESMASTERDATARESPONSE_FIELD_NUMBER: _ClassVar[int]
    TRADERESPONSE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTAPPLICATIONRESPONSE_FIELD_NUMBER: _ClassVar[int]
    GLOSSARYRESPONSE_FIELD_NUMBER: _ClassVar[int]
    COMMISSIONRESPONSE_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTIONRESPONSE_FIELD_NUMBER: _ClassVar[int]
    CHAINQUOTERESPONSE_FIELD_NUMBER: _ClassVar[int]
    GETEXPIRATIONSRESPONSE_FIELD_NUMBER: _ClassVar[int]
    GETUXMESSAGESRESPONSE_FIELD_NUMBER: _ClassVar[int]
    USERDATARESPONSE_FIELD_NUMBER: _ClassVar[int]
    BALANCEADJUSTMENTRESPONSE_FIELD_NUMBER: _ClassVar[int]
    BALANCECASHINFORESPONSE_FIELD_NUMBER: _ClassVar[int]
    SEARCHSERVICERESPONSE_FIELD_NUMBER: _ClassVar[int]
    SEARCHSERVICEDEFINITIONRESPONSE_FIELD_NUMBER: _ClassVar[int]
    TIMEMACHINERECENTRESPONSE_FIELD_NUMBER: _ClassVar[int]
    TIMEMACHINEDOWNLOADRESPONSE_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    SessionInfoResponse: _sessions_pb2.SessionInfoResponse
    AccountsResponse: _accounts_pb2.AccountsResponse
    BalancesInfoResponse: _balances_pb2.BalancesInfoResponse
    QuoteResponse: _quotes_pb2.QuoteResponse
    OrdersInfoResponse: _orders_pb2.OrdersInfoResponse
    OrderExecutionLogsResponse: _order_execution_logs_pb2.OrderExecutionLogsResponse
    PositionsInfoResponse: _positions_pb2.PositionsInfoResponse
    BuyingPowerResponse: _bp_pb2.BuyingPowerResponse
    SecuritiesMasterDataResponse: _securities_master_pb2.SecuritiesMasterDataResponse
    TradeResponse: _trading_pb2.TradeResponse
    AccountApplicationResponse: _account_application_pb2.AccountApplicationResponse
    GlossaryResponse: _glossary_pb2.GlossaryResponse
    CommissionResponse: _commissions_pb2.CommissionResponse
    SubscriptionResponse: _subscriptions_pb2.SubscriptionResponse
    ChainQuoteResponse: _quotes_pb2.ChainQuoteResponse
    GetExpirationsResponse: _quotes_pb2.GetExpirationsResponse
    GetUxMessagesResponse: _ux_messages_pb2.GetUxMessagesResponse
    UserDataResponse: _user_data_pb2.UserDataResponse
    BalanceAdjustmentResponse: _balances_pb2.BalanceAdjustmentResponse
    BalanceCashInfoResponse: _balances_pb2.BalanceCashInfoResponse
    SearchServiceResponse: _search_pb2.SearchServiceResponse
    SearchServiceDefinitionResponse: _search_pb2.SearchServiceDefinitionResponse
    TimeMachineRecentResponse: _time_machine_pb2.TimeMachineBrowseResponse
    TimeMachineDownloadResponse: _time_machine_pb2.TimeMachineDownloadResponse
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2_1_1.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2_1_1.ResponseError]
    def __init__(self, SessionInfoResponse: _Optional[_Union[_sessions_pb2.SessionInfoResponse, _Mapping]] = ..., AccountsResponse: _Optional[_Union[_accounts_pb2.AccountsResponse, _Mapping]] = ..., BalancesInfoResponse: _Optional[_Union[_balances_pb2.BalancesInfoResponse, _Mapping]] = ..., QuoteResponse: _Optional[_Union[_quotes_pb2.QuoteResponse, _Mapping]] = ..., OrdersInfoResponse: _Optional[_Union[_orders_pb2.OrdersInfoResponse, _Mapping]] = ..., OrderExecutionLogsResponse: _Optional[_Union[_order_execution_logs_pb2.OrderExecutionLogsResponse, _Mapping]] = ..., PositionsInfoResponse: _Optional[_Union[_positions_pb2.PositionsInfoResponse, _Mapping]] = ..., BuyingPowerResponse: _Optional[_Union[_bp_pb2.BuyingPowerResponse, _Mapping]] = ..., SecuritiesMasterDataResponse: _Optional[_Union[_securities_master_pb2.SecuritiesMasterDataResponse, _Mapping]] = ..., TradeResponse: _Optional[_Union[_trading_pb2.TradeResponse, _Mapping]] = ..., AccountApplicationResponse: _Optional[_Union[_account_application_pb2.AccountApplicationResponse, _Mapping]] = ..., GlossaryResponse: _Optional[_Union[_glossary_pb2.GlossaryResponse, _Mapping]] = ..., CommissionResponse: _Optional[_Union[_commissions_pb2.CommissionResponse, _Mapping]] = ..., SubscriptionResponse: _Optional[_Union[_subscriptions_pb2.SubscriptionResponse, _Mapping]] = ..., ChainQuoteResponse: _Optional[_Union[_quotes_pb2.ChainQuoteResponse, _Mapping]] = ..., GetExpirationsResponse: _Optional[_Union[_quotes_pb2.GetExpirationsResponse, _Mapping]] = ..., GetUxMessagesResponse: _Optional[_Union[_ux_messages_pb2.GetUxMessagesResponse, _Mapping]] = ..., UserDataResponse: _Optional[_Union[_user_data_pb2.UserDataResponse, _Mapping]] = ..., BalanceAdjustmentResponse: _Optional[_Union[_balances_pb2.BalanceAdjustmentResponse, _Mapping]] = ..., BalanceCashInfoResponse: _Optional[_Union[_balances_pb2.BalanceCashInfoResponse, _Mapping]] = ..., SearchServiceResponse: _Optional[_Union[_search_pb2.SearchServiceResponse, _Mapping]] = ..., SearchServiceDefinitionResponse: _Optional[_Union[_search_pb2.SearchServiceDefinitionResponse, _Mapping]] = ..., TimeMachineRecentResponse: _Optional[_Union[_time_machine_pb2.TimeMachineBrowseResponse, _Mapping]] = ..., TimeMachineDownloadResponse: _Optional[_Union[_time_machine_pb2.TimeMachineDownloadResponse, _Mapping]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2_1_1.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2_1_1.ResponseError, _Mapping]]] = ...) -> None: ...

class ErrorResponse(_message.Message):
    __slots__ = ("Warnings", "Errors")
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2_1_1.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2_1_1.ResponseError]
    def __init__(self, Warnings: _Optional[_Iterable[_Union[_common_pb2_1_1.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2_1_1.ResponseError, _Mapping]]] = ...) -> None: ...
