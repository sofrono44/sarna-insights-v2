# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api_hub_service.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from .. import bp_pb2 as bp__pb2
from .. import quotes_pb2 as quotes__pb2
from .. import accounts_pb2 as accounts__pb2
try:
  common__pb2 = accounts__pb2.common__pb2
except AttributeError:
  common__pb2 = accounts__pb2.common_pb2
from .. import orders_pb2 as orders__pb2
from .. import order_execution_logs_pb2 as order__execution__logs__pb2
from .. import positions_pb2 as positions__pb2
from .. import balances_pb2 as balances__pb2
from .. import trading_pb2 as trading__pb2
from .. import securities_master_pb2 as securities__master__pb2
from .. import account_application_pb2 as account__application__pb2
try:
  common__pb2 = account__application__pb2.common__pb2
except AttributeError:
  common__pb2 = account__application__pb2.common_pb2
try:
  market__data__entitlement__pb2 = account__application__pb2.market__data__entitlement__pb2
except AttributeError:
  market__data__entitlement__pb2 = account__application__pb2.market_data_entitlement_pb2
try:
  common__pb2 = account__application__pb2.common__pb2
except AttributeError:
  common__pb2 = account__application__pb2.common_pb2
from .. import glossary_pb2 as glossary__pb2
from .. import commissions_pb2 as commissions__pb2
from .. import subscriptions_pb2 as subscriptions__pb2
from .. import ux_messages_pb2 as ux__messages__pb2
from .. import user_data_pb2 as user__data__pb2
from .. import market_data_entitlement_pb2 as market__data__entitlement__pb2
try:
  common__pb2 = market__data__entitlement__pb2.common__pb2
except AttributeError:
  common__pb2 = market__data__entitlement__pb2.common_pb2
from .. import trading_level_change_pb2 as trading__level__change__pb2
from .. import account_ach_pb2 as account__ach__pb2
from .. import sessions_pb2 as sessions__pb2
from .. import search_pb2 as search__pb2
from .. import time_machine_pb2 as time__machine__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x61pi_hub_service.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x08\x62p.proto\x1a\x0cquotes.proto\x1a\x0e\x61\x63\x63ounts.proto\x1a\x0corders.proto\x1a\x1aorder_execution_logs.proto\x1a\x0fpositions.proto\x1a\x0e\x62\x61lances.proto\x1a\rtrading.proto\x1a\x17securities_master.proto\x1a\x19\x61\x63\x63ount_application.proto\x1a\x0eglossary.proto\x1a\x11\x63ommissions.proto\x1a\x13subscriptions.proto\x1a\x11ux_messages.proto\x1a\x0fuser_data.proto\x1a\x1dmarket_data_entitlement.proto\x1a\x1atrading_level_change.proto\x1a\x11\x61\x63\x63ount_ach.proto\x1a\x0esessions.proto\x1a\x0csearch.proto\x1a\x12time_machine.proto2^\n\x0fSessionsService\x12K\n\x06\x43reate\x12\x15.CreateSessionRequest\x1a\x14.SessionInfoResponse\"\x14\x82\xd3\xe4\x93\x02\x0e\"\t/sessions:\x01*2i\n\x0fMessagesService\x12V\n\x03Get\x12\x15.GetUxMessagesRequest\x1a\x16.GetUxMessagesResponse\" \x82\xd3\xe4\x93\x02\x1a\x12\x18/messages/{LanguageCode}2\x9e\x02\n\x17SecuritiesMasterService\x12\x61\n\x03Get\x12\x16.google.protobuf.Empty\x1a\x1d.SecuritiesMasterDataResponse\"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/securities-master/equities\x12\x9f\x01\n\nGetOptions\x12\x1c.SecuritiesMasterDataRequest\x1a\x1d.SecuritiesMasterDataResponse\"T\x82\xd3\xe4\x93\x02N\x12\x1a/securities-master/optionsZ0\x12./securities-master/options/{UnderlyingSymbols}2~\n\x12\x43ommissionsService\x12h\n\x03Get\x12\x1c.CommissionPromoClaimRequest\x1a\x1d.CommissionPromoClaimResponse\"$\x82\xd3\xe4\x93\x02\x1e\"\x19/commissions/promo-claims:\x01*2\x98\x01\n\x0fGlossaryService\x12\x84\x01\n\x03Get\x12\x14.GetProvincesRequest\x1a\x11.GlossaryResponse\"T\x82\xd3\xe4\x93\x02N\x12\x1f/glossary/{CountryId}/provincesZ+\x12)/glossary/countries/{CountryId}/provinces2\xa9\x04\n\x14SubscriptionsService\x12W\n\nUserStatus\x12\x17.UserStatusCheckRequest\x1a\x18.UserStatusCheckResponse\"\x16\x82\xd3\xe4\x93\x02\x10\x12\x0e/subscriptions\x12\xa9\x01\n\x16SubscriptionActivation\x12*.UserPlatformSubscriptionActivationRequest\x1a+.UserPlatformSubscriptionActivationResponse\"6\x82\xd3\xe4\x93\x02\x30\"+/subscriptions/{UserPlatformSubscriptionId}:\x01*\x12\xac\x01\n\x18SubscriptionDeactivation\x12,.UserPlatformSubscriptionDeactivationRequest\x1a-.UserPlatformSubscriptionDeactivationResponse\"3\x82\xd3\xe4\x93\x02-*+/subscriptions/{UserPlatformSubscriptionId}\x12]\n\nPromoClaim\x12\x12.PromoClaimRequest\x1a\x13.PromoClaimResponse\"&\x82\xd3\xe4\x93\x02 \"\x1b/subscriptions/promo-claims:\x01*2I\n\x0cTradeService\x12\x39\n\x05Trade\x12\r.TradeRequest\x1a\x0e.TradeResponse\"\x11\x82\xd3\xe4\x93\x02\x0b\"\x06/trade:\x01*2\xc7\x02\n\x0f\x42\x61lancesService\x12\x45\n\x03Get\x12\x14.BalancesInfoRequest\x1a\x15.BalancesInfoResponse\"\x11\x82\xd3\xe4\x93\x02\x0b\x12\t/balances\x12\x8e\x01\n\nGetBalance\x12\x17.BalanceCashInfoRequest\x1a\x18.BalanceCashInfoResponse\"M\x82\xd3\xe4\x93\x02G\x12 /balances/account/id/{AccountId}Z#\x12!/balances/account/{AccountNumber}\x12\\\n\x06\x41\x64just\x12\x19.BalanceAdjustmentRequest\x1a\x1a.BalanceAdjustmentResponse\"\x1b\x82\xd3\xe4\x93\x02\x15\"\x10/balances/adjust:\x01*2\xdc\x04\n\x19OrderExecutionLogsService\x12~\n\x0cGetByOrderId\x12!.OrderExecutionLogsSearchCriteria\x1a\x1b.OrderExecutionLogsResponse\".\x82\xd3\xe4\x93\x02(\x12&/order-execution-logs/orders/{OrderId}\x12\x92\x01\n\x11GetByAccountToday\x12!.OrderExecutionLogsSearchCriteria\x1a\x1b.OrderExecutionLogsResponse\"=\x82\xd3\xe4\x93\x02\x37\x12\x35/order-execution-logs/accounts/{AccountNumbers}/today\x12\x9c\x01\n\x16GetByAccountHistorical\x12!.OrderExecutionLogsSearchCriteria\x1a\x1b.OrderExecutionLogsResponse\"B\x82\xd3\xe4\x93\x02<\x12:/order-execution-logs/accounts/{AccountNumbers}/historical\x12\x8a\x01\n\x0fGetAllByAccount\x12!.OrderExecutionLogsSearchCriteria\x1a\x1b.OrderExecutionLogsResponse\"7\x82\xd3\xe4\x93\x02\x31\x12//order-execution-logs/accounts/{AccountNumbers}2\xe4\x03\n\rQuotesService\x12I\n\x08GetQuote\x12\x14.GetQuoteRequestInfo\x1a\x0e.QuoteResponse\"\x17\x82\xd3\xe4\x93\x02\x11\x12\x0f/quote/{Symbol}\x12X\n\tGetQuotes\x12\x15.GetQuotesRequestInfo\x1a\x0e.QuoteResponse\"$\x82\xd3\xe4\x93\x02\x1e\x12\x07/quotesZ\x13\x12\x11/quotes/{Symbols}\x12O\n\x0bGetNetQuote\x12\x18.GetNetQuoteRequestInfos\x1a\x0e.QuoteResponse\"\x16\x82\xd3\xe4\x93\x02\x10\"\x0b/net-quotes:\x01*\x12k\n\x0eGetChainQuotes\x12\x1a.GetChainQuotesRequestInfo\x1a\x13.ChainQuoteResponse\"(\x82\xd3\xe4\x93\x02\"\x12 /chain-quotes/{UnderlyingSymbol}\x12p\n\x0eGetExpirations\x12\x16.GetExpirationsRequest\x1a\x17.GetExpirationsResponse\"-\x82\xd3\xe4\x93\x02\'\x12%/quotes-expiration/{UnderlyingSymbol}2_\n\x10PositionsService\x12K\n\x03Get\x12\x15.PositionsInfoRequest\x1a\x16.PositionsInfoResponse\"\x15\x82\xd3\xe4\x93\x02\x0f\"\n/positions:\x01*2S\n\rOrdersService\x12\x42\n\x03Get\x12\x12.OrdersInfoRequest\x1a\x13.OrdersInfoResponse\"\x12\x82\xd3\xe4\x93\x02\x0c\"\x07/orders:\x01*2`\n\x12\x42uyingPowerService\x12J\n\x03Get\x12\x13.BuyingPowerRequest\x1a\x14.BuyingPowerResponse\"\x18\x82\xd3\xe4\x93\x02\x12\"\r/buying-power:\x01*2\xe3\x0c\n\x0f\x41\x63\x63ountsService\x12N\n\x0c\x41\x63\x63ountsInfo\x12\x14.AccountsInfoRequest\x1a\x15.AccountsInfoResponse\"\x11\x82\xd3\xe4\x93\x02\x0b\x12\t/accounts\x12u\n\x10\x43reateSubaccount\x12\x18.CreateSubaccountRequest\x1a\x19.CreateSubaccountResponse\",\x82\xd3\xe4\x93\x02&\"!/accounts/{AccountId}/subaccounts:\x01*\x12\x81\x01\n\x10\x44\x65leteSubaccount\x12\x18.DeleteSubaccountRequest\x1a\x19.DeleteSubaccountResponse\"8\x82\xd3\xe4\x93\x02\x32*0/accounts/{AccountId}/subaccounts/{SubaccountId}\x12\xaa\x01\n\x0eUpdateNickname\x12\x16.UpdateNicknameRequest\x1a\x15.AccountsInfoResponse\"i\x82\xd3\xe4\x93\x02\x63\"\x1e/accounts/{AccountId}/nickname:\x01*Z>\"9/accounts/{AccountId}/subaccounts/{SubaccountId}/nickname:\x01*\x12]\n\x0f\x43reateVTAccount\x12\x17.CreateVTAccountRequest\x1a\x18.CreateVTAccountResponse\"\x17\x82\xd3\xe4\x93\x02\x11\"\x0c/accounts-vt:\x01*\x12\x95\x01\n\x12GetAccountActivity\x12\x1b.GetAccountsActivityRequest\x1a\x1c.GetAccountsActivityResponse\"D\x82\xd3\xe4\x93\x02>\x12#/accounts/{AccountNumbers}/activityZ\x17\"\x12/accounts/activity:\x01*\x12\x8f\x01\n\x18\x41skForTradingLevelChange\x12 .AskForTradingLevelChangeRequest\x1a!.AskForTradingLevelChangeResponse\".\x82\xd3\xe4\x93\x02(\"#/accounts/{AccountId}/trading-level:\x01*\x12{\n\x13SubaccountsTransfer\x12\x1b.SubaccountsTransferRequest\x1a\x1c.SubaccountsTransferResponse\")\x82\xd3\xe4\x93\x02#\"\x1e/accounts/{AccountId}/transfer:\x01*\x12\x61\n\x10\x43reateAbaAccount\x12\x18.CreateAbaAccountRequest\x1a\x19.CreateAbaAccountResponse\"\x18\x82\xd3\xe4\x93\x02\x12\"\r/aba-accounts:\x01*\x12]\n\x10\x42rowseAbaAccount\x12\x16.google.protobuf.Empty\x1a\x1a.BrowseAbaAccountsResponse\"\x15\x82\xd3\xe4\x93\x02\x0f\x12\r/aba-accounts\x12p\n\x18\x43reateAccountAchTransfer\x12 .CreateAccountAchTransferRequest\x1a!.CreateAccountAchTransferResponse\"\x0f\x82\xd3\xe4\x93\x02\t\"\x04/ach:\x01*\x12\\\n\tLinkGroup\x12\x18.LinkAccountGroupRequest\x1a\x19.LinkAccountGroupResponse\"\x1a\x82\xd3\xe4\x93\x02\x14\"\x0f/account-groups:\x01*\x12^\n\x0bUnlinkGroup\x12\x18.LinkAccountGroupRequest\x1a\x19.LinkAccountGroupResponse\"\x1a\x82\xd3\xe4\x93\x02\x14\"\x0f/account-groups:\x01*\x12`\n\x0b\x43hangeGroup\x12\x1a.ChangeAccountGroupRequest\x1a\x19.LinkAccountGroupResponse\"\x1a\x82\xd3\xe4\x93\x02\x14\"\x0f/account-groups:\x01*2\xe8\r\n\x1a\x41\x63\x63ountApplicationsService\x12\x81\x01\n\x0eValidatePerson\x12 .AccountApplicationPersonRequest\x1a\x1b.AccountApplicationResponse\"0\x82\xd3\xe4\x93\x02*\"%/account-applications/validate/person:\x01*\x12\x84\x01\n\x0fValidateAccount\x12!.AccountApplicationAccountRequest\x1a\x1b.AccountApplicationResponse\"1\x82\xd3\xe4\x93\x02+\"&/account-applications/validate/account:\x01*\x12\x8a\x01\n\x11ValidateAddresses\x12#.AccountApplicationAddressesRequest\x1a\x1b.AccountApplicationResponse\"3\x82\xd3\xe4\x93\x02-\"(/account-applications/validate/addresses:\x01*\x12\xa3\x01\n\x19ValidateInvestmentProfile\x12+.AccountApplicationInvestmentProfileRequest\x1a\x1b.AccountApplicationResponse\"<\x82\xd3\xe4\x93\x02\x36\"1/account-applications/validate/investment-profile:\x01*\x12t\n\x12ValidateEmployment\x12\x0b.Employment\x1a\x1b.AccountApplicationResponse\"4\x82\xd3\xe4\x93\x02.\")/account-applications/validate/employment:\x01*\x12\x8a\x01\n\x19ValidateFederalDisclosure\x12\x12.FederalDisclosure\x1a\x1b.AccountApplicationResponse\"<\x82\xd3\xe4\x93\x02\x36\"1/account-applications/validate/federal-disclosure:\x01*\x12\x9c\x01\n\x19ValidateSecurityQuestions\x12$.SecurityQuestionUserResponseRequest\x1a\x1b.AccountApplicationResponse\"<\x82\xd3\xe4\x93\x02\x36\"1/account-applications/validate/security-questions:\x01*\x12\x8e\x01\n\x16ValidateTrustedContact\x12\x1c.CreateTrustedContactRequest\x1a\x1b.AccountApplicationResponse\"9\x82\xd3\xe4\x93\x02\x33\"./account-applications/validate/trusted-contact:\x01*\x12\x9d\x01\n*ValidateMarketDataEntitlementFormResponses\x12#.MarketDataEntitlementFormResponses\x1a\x1b.AccountApplicationResponse\"-\x82\xd3\xe4\x93\x02\'\"\"/account-applications/validate/mde:\x01*\x12\x9e\x01\n\x1dValidateOtherBrokerageAccount\x12\x1d.ExternalBrokerageAccountInfo\x1a\x1b.AccountApplicationResponse\"A\x82\xd3\xe4\x93\x02;\"6/account-applications/validate/other-brokerage-account:\x01*\x12\xa5\x01\n\x19\x43reateVerificationSession\x12\x33.AccountApplicationCreateVerificationSessionRequest\x1a\x1c.VerificationSessionResponse\"5\x82\xd3\xe4\x93\x02/\"*/account-applications/verification-session:\x01*\x12p\n\rCreateAccount\x12 .CreateAccountApplicationRequest\x1a\x1b.AccountApplicationResponse\" \x82\xd3\xe4\x93\x02\x1a\"\x15/account-applications:\x01*2\xa2\x0f\n\x0cUsersService\x12Y\n\x0eGetUserProfile\x12\x16.google.protobuf.Empty\x1a\x17.GetUserProfileResponse\"\x16\x82\xd3\xe4\x93\x02\x10\x12\x0e/users/profile\x12U\n\x11UpdateUserProfile\x12\x0c.UserProfile\x1a\x17.GetUserProfileResponse\"\x19\x82\xd3\xe4\x93\x02\x13\x1a\x0e/users/profile:\x01*\x12\\\n\x0fUpdateUserEmail\x12\x17.UpdateUserEmailRequest\x1a\x17.GetUserProfileResponse\"\x17\x82\xd3\xe4\x93\x02\x11\x1a\x0c/users/email:\x01*\x12p\n\x14GetInvestmentProfile\x12\x16.google.protobuf.Empty\x1a\x1d.GetInvestmentProfileResponse\"!\x82\xd3\xe4\x93\x02\x1b\x12\x19/users/investment-profile\x12\x8e\x01\n\x1fGetExternalBrokerageAccountInfo\x12\x16.google.protobuf.Empty\x1a(.GetExternalBrokerageAccountInfoResponse\")\x82\xd3\xe4\x93\x02#\x12!/users/external-brokerage-account\x12\x62\n\x17GetAllSecurityQuestions\x12\x16.google.protobuf.Empty\x1a\x12.SecurityQuestions\"\x1b\x82\xd3\xe4\x93\x02\x15\x12\x13/security-questions\x12\x85\x01\n GetSecurityQuestionUserResponses\x12\x16.google.protobuf.Empty\x1a&.SecurityQuestionUserResponsesResponse\"!\x82\xd3\xe4\x93\x02\x1b\x12\x19/users/security-questions\x12\x99\x01\n#UpdateSecurityQuestionUserResponses\x12$.SecurityQuestionUserResponseRequest\x1a&.SecurityQuestionUserResponsesResponse\"$\x82\xd3\xe4\x93\x02\x1e\x1a\x19/users/security-questions:\x01*\x12m\n\x16GetAllMdeFormQuestions\x12\x16.google.protobuf.Empty\x1a#.MarketDataEntitlementFormQuestions\"\x16\x82\xd3\xe4\x93\x02\x10\x12\x0e/mde-questions\x12n\n\x13GetMdeFormResponses\x12\x16.google.protobuf.Empty\x1a+.MarketDataEntitlementFormResponsesResponse\"\x12\x82\xd3\xe4\x93\x02\x0c\x12\n/users/mde\x12\x85\x01\n\x1aUpdateMdeFormUserResponses\x12#.MarketDataEntitlementFormResponses\x1a+.MarketDataEntitlementFormResponsesResponse\"\x15\x82\xd3\xe4\x93\x02\x0f\x1a\n/users/mde:\x01*\x12~\n#DeleteMdeFormQuestionsUserResponses\x12\x16.google.protobuf.Empty\x1a+.MarketDataEntitlementFormResponsesResponse\"\x12\x82\xd3\xe4\x93\x02\x0c*\n/users/mde\x12\x8a\x01\n\x1eGetUserNotificationPreferences\x12\x16.google.protobuf.Empty\x1a\'.GetUserNotificationPreferencesResponse\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/users/notification-preferences\x12\xa3\x01\n!UpdateUserNotificationPreferences\x12).UpdateUserNotificationPreferencesRequest\x1a\'.GetUserNotificationPreferencesResponse\"*\x82\xd3\xe4\x93\x02$\x1a\x1f/users/notification-preferences:\x01*\x12i\n\x12GetUserPreferences\x12\x1a.GetUserPreferencesRequest\x1a\x1b.GetUserPreferencesResponse\"\x1a\x82\xd3\xe4\x93\x02\x14\x12\x12/users/preferences\x12r\n\x15UpdateUserPreferences\x12\x1d.UpdateUserPreferencesRequest\x1a\x1b.GetUserPreferencesResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\x1a\x12/users/preferences:\x01*2\xbc\x01\n\rSearchService\x12\x44\n\x06Search\x12\x0e.SearchRequest\x1a\x16.SearchServiceResponse\"\x12\x82\xd3\xe4\x93\x02\x0c\"\x07/search:\x01*\x12\x65\n\rGetDefinition\x12\x16.google.protobuf.Empty\x1a .SearchServiceDefinitionResponse\"\x1a\x82\xd3\xe4\x93\x02\x14\x12\x12/search/definition2\xd1\x01\n\x12TimeMachineService\x12W\n\x04List\x12\x19.TimeMachineBrowseRequest\x1a\x1a.TimeMachineBrowseResponse\"\x18\x82\xd3\xe4\x93\x02\x12\"\r/time-machine:\x01*\x12\x62\n\x03Get\x12\x1b.TimeMachineDownloadRequest\x1a\x1c.TimeMachineDownloadResponse\" \x82\xd3\xe4\x93\x02\x1a\x12\x18/time-machine/{FileName}B\x16\xaa\x02\x13\x44TS.Libs.Protos.Apib\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api_hub_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\252\002\023DTS.Libs.Protos.Api'
  _globals['_SESSIONSSERVICE'].methods_by_name['Create']._options = None
  _globals['_SESSIONSSERVICE'].methods_by_name['Create']._serialized_options = b'\202\323\344\223\002\016\"\t/sessions:\001*'
  _globals['_MESSAGESSERVICE'].methods_by_name['Get']._options = None
  _globals['_MESSAGESSERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\002\032\022\030/messages/{LanguageCode}'
  _globals['_SECURITIESMASTERSERVICE'].methods_by_name['Get']._options = None
  _globals['_SECURITIESMASTERSERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\002\035\022\033/securities-master/equities'
  _globals['_SECURITIESMASTERSERVICE'].methods_by_name['GetOptions']._options = None
  _globals['_SECURITIESMASTERSERVICE'].methods_by_name['GetOptions']._serialized_options = b'\202\323\344\223\002N\022\032/securities-master/optionsZ0\022./securities-master/options/{UnderlyingSymbols}'
  _globals['_COMMISSIONSSERVICE'].methods_by_name['Get']._options = None
  _globals['_COMMISSIONSSERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\002\036\"\031/commissions/promo-claims:\001*'
  _globals['_GLOSSARYSERVICE'].methods_by_name['Get']._options = None
  _globals['_GLOSSARYSERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\002N\022\037/glossary/{CountryId}/provincesZ+\022)/glossary/countries/{CountryId}/provinces'
  _globals['_SUBSCRIPTIONSSERVICE'].methods_by_name['UserStatus']._options = None
  _globals['_SUBSCRIPTIONSSERVICE'].methods_by_name['UserStatus']._serialized_options = b'\202\323\344\223\002\020\022\016/subscriptions'
  _globals['_SUBSCRIPTIONSSERVICE'].methods_by_name['SubscriptionActivation']._options = None
  _globals['_SUBSCRIPTIONSSERVICE'].methods_by_name['SubscriptionActivation']._serialized_options = b'\202\323\344\223\0020\"+/subscriptions/{UserPlatformSubscriptionId}:\001*'
  _globals['_SUBSCRIPTIONSSERVICE'].methods_by_name['SubscriptionDeactivation']._options = None
  _globals['_SUBSCRIPTIONSSERVICE'].methods_by_name['SubscriptionDeactivation']._serialized_options = b'\202\323\344\223\002-*+/subscriptions/{UserPlatformSubscriptionId}'
  _globals['_SUBSCRIPTIONSSERVICE'].methods_by_name['PromoClaim']._options = None
  _globals['_SUBSCRIPTIONSSERVICE'].methods_by_name['PromoClaim']._serialized_options = b'\202\323\344\223\002 \"\033/subscriptions/promo-claims:\001*'
  _globals['_TRADESERVICE'].methods_by_name['Trade']._options = None
  _globals['_TRADESERVICE'].methods_by_name['Trade']._serialized_options = b'\202\323\344\223\002\013\"\006/trade:\001*'
  _globals['_BALANCESSERVICE'].methods_by_name['Get']._options = None
  _globals['_BALANCESSERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\002\013\022\t/balances'
  _globals['_BALANCESSERVICE'].methods_by_name['GetBalance']._options = None
  _globals['_BALANCESSERVICE'].methods_by_name['GetBalance']._serialized_options = b'\202\323\344\223\002G\022 /balances/account/id/{AccountId}Z#\022!/balances/account/{AccountNumber}'
  _globals['_BALANCESSERVICE'].methods_by_name['Adjust']._options = None
  _globals['_BALANCESSERVICE'].methods_by_name['Adjust']._serialized_options = b'\202\323\344\223\002\025\"\020/balances/adjust:\001*'
  _globals['_ORDEREXECUTIONLOGSSERVICE'].methods_by_name['GetByOrderId']._options = None
  _globals['_ORDEREXECUTIONLOGSSERVICE'].methods_by_name['GetByOrderId']._serialized_options = b'\202\323\344\223\002(\022&/order-execution-logs/orders/{OrderId}'
  _globals['_ORDEREXECUTIONLOGSSERVICE'].methods_by_name['GetByAccountToday']._options = None
  _globals['_ORDEREXECUTIONLOGSSERVICE'].methods_by_name['GetByAccountToday']._serialized_options = b'\202\323\344\223\0027\0225/order-execution-logs/accounts/{AccountNumbers}/today'
  _globals['_ORDEREXECUTIONLOGSSERVICE'].methods_by_name['GetByAccountHistorical']._options = None
  _globals['_ORDEREXECUTIONLOGSSERVICE'].methods_by_name['GetByAccountHistorical']._serialized_options = b'\202\323\344\223\002<\022:/order-execution-logs/accounts/{AccountNumbers}/historical'
  _globals['_ORDEREXECUTIONLOGSSERVICE'].methods_by_name['GetAllByAccount']._options = None
  _globals['_ORDEREXECUTIONLOGSSERVICE'].methods_by_name['GetAllByAccount']._serialized_options = b'\202\323\344\223\0021\022//order-execution-logs/accounts/{AccountNumbers}'
  _globals['_QUOTESSERVICE'].methods_by_name['GetQuote']._options = None
  _globals['_QUOTESSERVICE'].methods_by_name['GetQuote']._serialized_options = b'\202\323\344\223\002\021\022\017/quote/{Symbol}'
  _globals['_QUOTESSERVICE'].methods_by_name['GetQuotes']._options = None
  _globals['_QUOTESSERVICE'].methods_by_name['GetQuotes']._serialized_options = b'\202\323\344\223\002\036\022\007/quotesZ\023\022\021/quotes/{Symbols}'
  _globals['_QUOTESSERVICE'].methods_by_name['GetNetQuote']._options = None
  _globals['_QUOTESSERVICE'].methods_by_name['GetNetQuote']._serialized_options = b'\202\323\344\223\002\020\"\013/net-quotes:\001*'
  _globals['_QUOTESSERVICE'].methods_by_name['GetChainQuotes']._options = None
  _globals['_QUOTESSERVICE'].methods_by_name['GetChainQuotes']._serialized_options = b'\202\323\344\223\002\"\022 /chain-quotes/{UnderlyingSymbol}'
  _globals['_QUOTESSERVICE'].methods_by_name['GetExpirations']._options = None
  _globals['_QUOTESSERVICE'].methods_by_name['GetExpirations']._serialized_options = b'\202\323\344\223\002\'\022%/quotes-expiration/{UnderlyingSymbol}'
  _globals['_POSITIONSSERVICE'].methods_by_name['Get']._options = None
  _globals['_POSITIONSSERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\002\017\"\n/positions:\001*'
  _globals['_ORDERSSERVICE'].methods_by_name['Get']._options = None
  _globals['_ORDERSSERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\002\014\"\007/orders:\001*'
  _globals['_BUYINGPOWERSERVICE'].methods_by_name['Get']._options = None
  _globals['_BUYINGPOWERSERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\002\022\"\r/buying-power:\001*'
  _globals['_ACCOUNTSSERVICE'].methods_by_name['AccountsInfo']._options = None
  _globals['_ACCOUNTSSERVICE'].methods_by_name['AccountsInfo']._serialized_options = b'\202\323\344\223\002\013\022\t/accounts'
  _globals['_ACCOUNTSSERVICE'].methods_by_name['CreateSubaccount']._options = None
  _globals['_ACCOUNTSSERVICE'].methods_by_name['CreateSubaccount']._serialized_options = b'\202\323\344\223\002&\"!/accounts/{AccountId}/subaccounts:\001*'
  _globals['_ACCOUNTSSERVICE'].methods_by_name['DeleteSubaccount']._options = None
  _globals['_ACCOUNTSSERVICE'].methods_by_name['DeleteSubaccount']._serialized_options = b'\202\323\344\223\0022*0/accounts/{AccountId}/subaccounts/{SubaccountId}'
  _globals['_ACCOUNTSSERVICE'].methods_by_name['UpdateNickname']._options = None
  _globals['_ACCOUNTSSERVICE'].methods_by_name['UpdateNickname']._serialized_options = b'\202\323\344\223\002c\"\036/accounts/{AccountId}/nickname:\001*Z>\"9/accounts/{AccountId}/subaccounts/{SubaccountId}/nickname:\001*'
  _globals['_ACCOUNTSSERVICE'].methods_by_name['CreateVTAccount']._options = None
  _globals['_ACCOUNTSSERVICE'].methods_by_name['CreateVTAccount']._serialized_options = b'\202\323\344\223\002\021\"\014/accounts-vt:\001*'
  _globals['_ACCOUNTSSERVICE'].methods_by_name['GetAccountActivity']._options = None
  _globals['_ACCOUNTSSERVICE'].methods_by_name['GetAccountActivity']._serialized_options = b'\202\323\344\223\002>\022#/accounts/{AccountNumbers}/activityZ\027\"\022/accounts/activity:\001*'
  _globals['_ACCOUNTSSERVICE'].methods_by_name['AskForTradingLevelChange']._options = None
  _globals['_ACCOUNTSSERVICE'].methods_by_name['AskForTradingLevelChange']._serialized_options = b'\202\323\344\223\002(\"#/accounts/{AccountId}/trading-level:\001*'
  _globals['_ACCOUNTSSERVICE'].methods_by_name['SubaccountsTransfer']._options = None
  _globals['_ACCOUNTSSERVICE'].methods_by_name['SubaccountsTransfer']._serialized_options = b'\202\323\344\223\002#\"\036/accounts/{AccountId}/transfer:\001*'
  _globals['_ACCOUNTSSERVICE'].methods_by_name['CreateAbaAccount']._options = None
  _globals['_ACCOUNTSSERVICE'].methods_by_name['CreateAbaAccount']._serialized_options = b'\202\323\344\223\002\022\"\r/aba-accounts:\001*'
  _globals['_ACCOUNTSSERVICE'].methods_by_name['BrowseAbaAccount']._options = None
  _globals['_ACCOUNTSSERVICE'].methods_by_name['BrowseAbaAccount']._serialized_options = b'\202\323\344\223\002\017\022\r/aba-accounts'
  _globals['_ACCOUNTSSERVICE'].methods_by_name['CreateAccountAchTransfer']._options = None
  _globals['_ACCOUNTSSERVICE'].methods_by_name['CreateAccountAchTransfer']._serialized_options = b'\202\323\344\223\002\t\"\004/ach:\001*'
  _globals['_ACCOUNTSSERVICE'].methods_by_name['LinkGroup']._options = None
  _globals['_ACCOUNTSSERVICE'].methods_by_name['LinkGroup']._serialized_options = b'\202\323\344\223\002\024\"\017/account-groups:\001*'
  _globals['_ACCOUNTSSERVICE'].methods_by_name['UnlinkGroup']._options = None
  _globals['_ACCOUNTSSERVICE'].methods_by_name['UnlinkGroup']._serialized_options = b'\202\323\344\223\002\024\"\017/account-groups:\001*'
  _globals['_ACCOUNTSSERVICE'].methods_by_name['ChangeGroup']._options = None
  _globals['_ACCOUNTSSERVICE'].methods_by_name['ChangeGroup']._serialized_options = b'\202\323\344\223\002\024\"\017/account-groups:\001*'
  _globals['_ACCOUNTAPPLICATIONSSERVICE'].methods_by_name['ValidatePerson']._options = None
  _globals['_ACCOUNTAPPLICATIONSSERVICE'].methods_by_name['ValidatePerson']._serialized_options = b'\202\323\344\223\002*\"%/account-applications/validate/person:\001*'
  _globals['_ACCOUNTAPPLICATIONSSERVICE'].methods_by_name['ValidateAccount']._options = None
  _globals['_ACCOUNTAPPLICATIONSSERVICE'].methods_by_name['ValidateAccount']._serialized_options = b'\202\323\344\223\002+\"&/account-applications/validate/account:\001*'
  _globals['_ACCOUNTAPPLICATIONSSERVICE'].methods_by_name['ValidateAddresses']._options = None
  _globals['_ACCOUNTAPPLICATIONSSERVICE'].methods_by_name['ValidateAddresses']._serialized_options = b'\202\323\344\223\002-\"(/account-applications/validate/addresses:\001*'
  _globals['_ACCOUNTAPPLICATIONSSERVICE'].methods_by_name['ValidateInvestmentProfile']._options = None
  _globals['_ACCOUNTAPPLICATIONSSERVICE'].methods_by_name['ValidateInvestmentProfile']._serialized_options = b'\202\323\344\223\0026\"1/account-applications/validate/investment-profile:\001*'
  _globals['_ACCOUNTAPPLICATIONSSERVICE'].methods_by_name['ValidateEmployment']._options = None
  _globals['_ACCOUNTAPPLICATIONSSERVICE'].methods_by_name['ValidateEmployment']._serialized_options = b'\202\323\344\223\002.\")/account-applications/validate/employment:\001*'
  _globals['_ACCOUNTAPPLICATIONSSERVICE'].methods_by_name['ValidateFederalDisclosure']._options = None
  _globals['_ACCOUNTAPPLICATIONSSERVICE'].methods_by_name['ValidateFederalDisclosure']._serialized_options = b'\202\323\344\223\0026\"1/account-applications/validate/federal-disclosure:\001*'
  _globals['_ACCOUNTAPPLICATIONSSERVICE'].methods_by_name['ValidateSecurityQuestions']._options = None
  _globals['_ACCOUNTAPPLICATIONSSERVICE'].methods_by_name['ValidateSecurityQuestions']._serialized_options = b'\202\323\344\223\0026\"1/account-applications/validate/security-questions:\001*'
  _globals['_ACCOUNTAPPLICATIONSSERVICE'].methods_by_name['ValidateTrustedContact']._options = None
  _globals['_ACCOUNTAPPLICATIONSSERVICE'].methods_by_name['ValidateTrustedContact']._serialized_options = b'\202\323\344\223\0023\"./account-applications/validate/trusted-contact:\001*'
  _globals['_ACCOUNTAPPLICATIONSSERVICE'].methods_by_name['ValidateMarketDataEntitlementFormResponses']._options = None
  _globals['_ACCOUNTAPPLICATIONSSERVICE'].methods_by_name['ValidateMarketDataEntitlementFormResponses']._serialized_options = b'\202\323\344\223\002\'\"\"/account-applications/validate/mde:\001*'
  _globals['_ACCOUNTAPPLICATIONSSERVICE'].methods_by_name['ValidateOtherBrokerageAccount']._options = None
  _globals['_ACCOUNTAPPLICATIONSSERVICE'].methods_by_name['ValidateOtherBrokerageAccount']._serialized_options = b'\202\323\344\223\002;\"6/account-applications/validate/other-brokerage-account:\001*'
  _globals['_ACCOUNTAPPLICATIONSSERVICE'].methods_by_name['CreateVerificationSession']._options = None
  _globals['_ACCOUNTAPPLICATIONSSERVICE'].methods_by_name['CreateVerificationSession']._serialized_options = b'\202\323\344\223\002/\"*/account-applications/verification-session:\001*'
  _globals['_ACCOUNTAPPLICATIONSSERVICE'].methods_by_name['CreateAccount']._options = None
  _globals['_ACCOUNTAPPLICATIONSSERVICE'].methods_by_name['CreateAccount']._serialized_options = b'\202\323\344\223\002\032\"\025/account-applications:\001*'
  _globals['_USERSSERVICE'].methods_by_name['GetUserProfile']._options = None
  _globals['_USERSSERVICE'].methods_by_name['GetUserProfile']._serialized_options = b'\202\323\344\223\002\020\022\016/users/profile'
  _globals['_USERSSERVICE'].methods_by_name['UpdateUserProfile']._options = None
  _globals['_USERSSERVICE'].methods_by_name['UpdateUserProfile']._serialized_options = b'\202\323\344\223\002\023\032\016/users/profile:\001*'
  _globals['_USERSSERVICE'].methods_by_name['UpdateUserEmail']._options = None
  _globals['_USERSSERVICE'].methods_by_name['UpdateUserEmail']._serialized_options = b'\202\323\344\223\002\021\032\014/users/email:\001*'
  _globals['_USERSSERVICE'].methods_by_name['GetInvestmentProfile']._options = None
  _globals['_USERSSERVICE'].methods_by_name['GetInvestmentProfile']._serialized_options = b'\202\323\344\223\002\033\022\031/users/investment-profile'
  _globals['_USERSSERVICE'].methods_by_name['GetExternalBrokerageAccountInfo']._options = None
  _globals['_USERSSERVICE'].methods_by_name['GetExternalBrokerageAccountInfo']._serialized_options = b'\202\323\344\223\002#\022!/users/external-brokerage-account'
  _globals['_USERSSERVICE'].methods_by_name['GetAllSecurityQuestions']._options = None
  _globals['_USERSSERVICE'].methods_by_name['GetAllSecurityQuestions']._serialized_options = b'\202\323\344\223\002\025\022\023/security-questions'
  _globals['_USERSSERVICE'].methods_by_name['GetSecurityQuestionUserResponses']._options = None
  _globals['_USERSSERVICE'].methods_by_name['GetSecurityQuestionUserResponses']._serialized_options = b'\202\323\344\223\002\033\022\031/users/security-questions'
  _globals['_USERSSERVICE'].methods_by_name['UpdateSecurityQuestionUserResponses']._options = None
  _globals['_USERSSERVICE'].methods_by_name['UpdateSecurityQuestionUserResponses']._serialized_options = b'\202\323\344\223\002\036\032\031/users/security-questions:\001*'
  _globals['_USERSSERVICE'].methods_by_name['GetAllMdeFormQuestions']._options = None
  _globals['_USERSSERVICE'].methods_by_name['GetAllMdeFormQuestions']._serialized_options = b'\202\323\344\223\002\020\022\016/mde-questions'
  _globals['_USERSSERVICE'].methods_by_name['GetMdeFormResponses']._options = None
  _globals['_USERSSERVICE'].methods_by_name['GetMdeFormResponses']._serialized_options = b'\202\323\344\223\002\014\022\n/users/mde'
  _globals['_USERSSERVICE'].methods_by_name['UpdateMdeFormUserResponses']._options = None
  _globals['_USERSSERVICE'].methods_by_name['UpdateMdeFormUserResponses']._serialized_options = b'\202\323\344\223\002\017\032\n/users/mde:\001*'
  _globals['_USERSSERVICE'].methods_by_name['DeleteMdeFormQuestionsUserResponses']._options = None
  _globals['_USERSSERVICE'].methods_by_name['DeleteMdeFormQuestionsUserResponses']._serialized_options = b'\202\323\344\223\002\014*\n/users/mde'
  _globals['_USERSSERVICE'].methods_by_name['GetUserNotificationPreferences']._options = None
  _globals['_USERSSERVICE'].methods_by_name['GetUserNotificationPreferences']._serialized_options = b'\202\323\344\223\002!\022\037/users/notification-preferences'
  _globals['_USERSSERVICE'].methods_by_name['UpdateUserNotificationPreferences']._options = None
  _globals['_USERSSERVICE'].methods_by_name['UpdateUserNotificationPreferences']._serialized_options = b'\202\323\344\223\002$\032\037/users/notification-preferences:\001*'
  _globals['_USERSSERVICE'].methods_by_name['GetUserPreferences']._options = None
  _globals['_USERSSERVICE'].methods_by_name['GetUserPreferences']._serialized_options = b'\202\323\344\223\002\024\022\022/users/preferences'
  _globals['_USERSSERVICE'].methods_by_name['UpdateUserPreferences']._options = None
  _globals['_USERSSERVICE'].methods_by_name['UpdateUserPreferences']._serialized_options = b'\202\323\344\223\002\027\032\022/users/preferences:\001*'
  _globals['_SEARCHSERVICE'].methods_by_name['Search']._options = None
  _globals['_SEARCHSERVICE'].methods_by_name['Search']._serialized_options = b'\202\323\344\223\002\014\"\007/search:\001*'
  _globals['_SEARCHSERVICE'].methods_by_name['GetDefinition']._options = None
  _globals['_SEARCHSERVICE'].methods_by_name['GetDefinition']._serialized_options = b'\202\323\344\223\002\024\022\022/search/definition'
  _globals['_TIMEMACHINESERVICE'].methods_by_name['List']._options = None
  _globals['_TIMEMACHINESERVICE'].methods_by_name['List']._serialized_options = b'\202\323\344\223\002\022\"\r/time-machine:\001*'
  _globals['_TIMEMACHINESERVICE'].methods_by_name['Get']._options = None
  _globals['_TIMEMACHINESERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\002\032\022\030/time-machine/{FileName}'
  _globals['_SESSIONSSERVICE']._serialized_start=486
  _globals['_SESSIONSSERVICE']._serialized_end=580
  _globals['_MESSAGESSERVICE']._serialized_start=582
  _globals['_MESSAGESSERVICE']._serialized_end=687
  _globals['_SECURITIESMASTERSERVICE']._serialized_start=690
  _globals['_SECURITIESMASTERSERVICE']._serialized_end=976
  _globals['_COMMISSIONSSERVICE']._serialized_start=978
  _globals['_COMMISSIONSSERVICE']._serialized_end=1104
  _globals['_GLOSSARYSERVICE']._serialized_start=1107
  _globals['_GLOSSARYSERVICE']._serialized_end=1259
  _globals['_SUBSCRIPTIONSSERVICE']._serialized_start=1262
  _globals['_SUBSCRIPTIONSSERVICE']._serialized_end=1815
  _globals['_TRADESERVICE']._serialized_start=1817
  _globals['_TRADESERVICE']._serialized_end=1890
  _globals['_BALANCESSERVICE']._serialized_start=1893
  _globals['_BALANCESSERVICE']._serialized_end=2220
  _globals['_ORDEREXECUTIONLOGSSERVICE']._serialized_start=2223
  _globals['_ORDEREXECUTIONLOGSSERVICE']._serialized_end=2827
  _globals['_QUOTESSERVICE']._serialized_start=2830
  _globals['_QUOTESSERVICE']._serialized_end=3314
  _globals['_POSITIONSSERVICE']._serialized_start=3316
  _globals['_POSITIONSSERVICE']._serialized_end=3411
  _globals['_ORDERSSERVICE']._serialized_start=3413
  _globals['_ORDERSSERVICE']._serialized_end=3496
  _globals['_BUYINGPOWERSERVICE']._serialized_start=3498
  _globals['_BUYINGPOWERSERVICE']._serialized_end=3594
  _globals['_ACCOUNTSSERVICE']._serialized_start=3597
  _globals['_ACCOUNTSSERVICE']._serialized_end=5232
  _globals['_ACCOUNTAPPLICATIONSSERVICE']._serialized_start=5235
  _globals['_ACCOUNTAPPLICATIONSSERVICE']._serialized_end=7003
  _globals['_USERSSERVICE']._serialized_start=7006
  _globals['_USERSSERVICE']._serialized_end=8960
  _globals['_SEARCHSERVICE']._serialized_start=8963
  _globals['_SEARCHSERVICE']._serialized_end=9151
  _globals['_TIMEMACHINESERVICE']._serialized_start=9154
  _globals['_TIMEMACHINESERVICE']._serialized_end=9363
# @@protoc_insertion_point(module_scope)
