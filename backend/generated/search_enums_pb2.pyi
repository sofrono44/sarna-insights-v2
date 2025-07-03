from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EnumSearchType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumSearchType_Undefined: _ClassVar[EnumSearchType]
    EnumSearchType_Orders: _ClassVar[EnumSearchType]
    EnumSearchType_Accounts: _ClassVar[EnumSearchType]
    EnumSearchType_OpenPositionLots: _ClassVar[EnumSearchType]
    EnumSearchType_Users: _ClassVar[EnumSearchType]

class EnumSearchServiceResponse(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumSearchServiceResponse_Undefined: _ClassVar[EnumSearchServiceResponse]
    EnumSearchServiceResponse_Success: _ClassVar[EnumSearchServiceResponse]
    EnumSearchServiceResponse_Failure: _ClassVar[EnumSearchServiceResponse]

class EnumJoinOperator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumJoinOperator_Undefined: _ClassVar[EnumJoinOperator]
    EnumJoinOperator_And: _ClassVar[EnumJoinOperator]
    EnumJoinOperator_Or: _ClassVar[EnumJoinOperator]

class EnumOperator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumOperator_Undefined: _ClassVar[EnumOperator]
    EnumOperator_Equal: _ClassVar[EnumOperator]
    EnumOperator_NotEqual: _ClassVar[EnumOperator]
    EnumOperator_GreaterThan: _ClassVar[EnumOperator]
    EnumOperator_LessThan: _ClassVar[EnumOperator]
    EnumOperator_GreaterThanOrEqual: _ClassVar[EnumOperator]
    EnumOperator_LessThanOrEqual: _ClassVar[EnumOperator]
    EnumOperator_Like: _ClassVar[EnumOperator]
    EnumOperator_NotLike: _ClassVar[EnumOperator]
    EnumOperator_StartsWith: _ClassVar[EnumOperator]
    EnumOperator_EndsWith: _ClassVar[EnumOperator]
    EnumOperator_In: _ClassVar[EnumOperator]
    EnumOperator_NotIn: _ClassVar[EnumOperator]

class EnumField(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumField_Undefined: _ClassVar[EnumField]
    EnumField_OrderId: _ClassVar[EnumField]
    EnumField_UnderlyingSymbol: _ClassVar[EnumField]
    EnumField_PriceType: _ClassVar[EnumField]
    EnumField_OrderStatus: _ClassVar[EnumField]
    EnumField_Quantity: _ClassVar[EnumField]
    EnumField_Symbol: _ClassVar[EnumField]
    EnumField_Cusip: _ClassVar[EnumField]
    EnumField_PositionEffectId: _ClassVar[EnumField]
    EnumField_OrderActionId: _ClassVar[EnumField]
    EnumField_LegSecTypeId: _ClassVar[EnumField]
    EnumField_AccountId: _ClassVar[EnumField]
    EnumField_AccountNumber: _ClassVar[EnumField]
    EnumField_AccountTypeId: _ClassVar[EnumField]
    EnumField_AccountRiskType: _ClassVar[EnumField]
    EnumField_Nickname: _ClassVar[EnumField]
    EnumField_CreatedTime: _ClassVar[EnumField]
    EnumField_AccountBranchId: _ClassVar[EnumField]
    EnumField_AccountRepresentativeId: _ClassVar[EnumField]
    EnumField_AccountStatus: _ClassVar[EnumField]
    EnumField_NetLiq: _ClassVar[EnumField]
    EnumField_Requirement: _ClassVar[EnumField]
    EnumField_CreditUtilization: _ClassVar[EnumField]
    EnumField_DayPnL: _ClassVar[EnumField]
    EnumField_DayPnL_Utilization: _ClassVar[EnumField]
    EnumField_ExcessLiquidity: _ClassVar[EnumField]
    EnumField_Cash: _ClassVar[EnumField]
    EnumField_MorningCash: _ClassVar[EnumField]
    EnumField_AccountValue: _ClassVar[EnumField]
    EnumField_MorningBuyingPower: _ClassVar[EnumField]
    EnumField_Sma: _ClassVar[EnumField]
    EnumField_OpenQuantity: _ClassVar[EnumField]
    EnumField_ClosedQuantity: _ClassVar[EnumField]
    EnumField_OpenPrice: _ClassVar[EnumField]
    EnumField_ExpirationDate: _ClassVar[EnumField]
    EnumField_StrikePrice: _ClassVar[EnumField]
    EnumField_SecurityTypeId: _ClassVar[EnumField]
    EnumField_CallOrPut: _ClassVar[EnumField]
    EnumField_PositionDirection: _ClassVar[EnumField]
    EnumField_CreditLimit: _ClassVar[EnumField]
    EnumField_IsRiskMonitoringEnabled: _ClassVar[EnumField]
    EnumField_PersonId: _ClassVar[EnumField]
    EnumField_PersonName: _ClassVar[EnumField]
    EnumField_UserId: _ClassVar[EnumField]
    EnumField_UserName: _ClassVar[EnumField]
    EnumField_UserEmail: _ClassVar[EnumField]
    EnumField_UserType: _ClassVar[EnumField]
    EnumField_IsBlocked: _ClassVar[EnumField]
    EnumField_IsEmployee: _ClassVar[EnumField]
    EnumField_UserBranchId: _ClassVar[EnumField]
    EnumField_UserRepresentativeId: _ClassVar[EnumField]
    EnumField_Custom: _ClassVar[EnumField]

class EnumSortDirection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumSortDirection_Undefined: _ClassVar[EnumSortDirection]
    EnumSortDirection_Asc: _ClassVar[EnumSortDirection]
    EnumSortDirection_Desc: _ClassVar[EnumSortDirection]

class EnumFieldType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumFieldType_Undefined: _ClassVar[EnumFieldType]
    EnumFieldType_String: _ClassVar[EnumFieldType]
    EnumFieldType_Int: _ClassVar[EnumFieldType]
    EnumFieldType_Double: _ClassVar[EnumFieldType]
    EnumFieldType_Date: _ClassVar[EnumFieldType]
EnumSearchType_Undefined: EnumSearchType
EnumSearchType_Orders: EnumSearchType
EnumSearchType_Accounts: EnumSearchType
EnumSearchType_OpenPositionLots: EnumSearchType
EnumSearchType_Users: EnumSearchType
EnumSearchServiceResponse_Undefined: EnumSearchServiceResponse
EnumSearchServiceResponse_Success: EnumSearchServiceResponse
EnumSearchServiceResponse_Failure: EnumSearchServiceResponse
EnumJoinOperator_Undefined: EnumJoinOperator
EnumJoinOperator_And: EnumJoinOperator
EnumJoinOperator_Or: EnumJoinOperator
EnumOperator_Undefined: EnumOperator
EnumOperator_Equal: EnumOperator
EnumOperator_NotEqual: EnumOperator
EnumOperator_GreaterThan: EnumOperator
EnumOperator_LessThan: EnumOperator
EnumOperator_GreaterThanOrEqual: EnumOperator
EnumOperator_LessThanOrEqual: EnumOperator
EnumOperator_Like: EnumOperator
EnumOperator_NotLike: EnumOperator
EnumOperator_StartsWith: EnumOperator
EnumOperator_EndsWith: EnumOperator
EnumOperator_In: EnumOperator
EnumOperator_NotIn: EnumOperator
EnumField_Undefined: EnumField
EnumField_OrderId: EnumField
EnumField_UnderlyingSymbol: EnumField
EnumField_PriceType: EnumField
EnumField_OrderStatus: EnumField
EnumField_Quantity: EnumField
EnumField_Symbol: EnumField
EnumField_Cusip: EnumField
EnumField_PositionEffectId: EnumField
EnumField_OrderActionId: EnumField
EnumField_LegSecTypeId: EnumField
EnumField_AccountId: EnumField
EnumField_AccountNumber: EnumField
EnumField_AccountTypeId: EnumField
EnumField_AccountRiskType: EnumField
EnumField_Nickname: EnumField
EnumField_CreatedTime: EnumField
EnumField_AccountBranchId: EnumField
EnumField_AccountRepresentativeId: EnumField
EnumField_AccountStatus: EnumField
EnumField_NetLiq: EnumField
EnumField_Requirement: EnumField
EnumField_CreditUtilization: EnumField
EnumField_DayPnL: EnumField
EnumField_DayPnL_Utilization: EnumField
EnumField_ExcessLiquidity: EnumField
EnumField_Cash: EnumField
EnumField_MorningCash: EnumField
EnumField_AccountValue: EnumField
EnumField_MorningBuyingPower: EnumField
EnumField_Sma: EnumField
EnumField_OpenQuantity: EnumField
EnumField_ClosedQuantity: EnumField
EnumField_OpenPrice: EnumField
EnumField_ExpirationDate: EnumField
EnumField_StrikePrice: EnumField
EnumField_SecurityTypeId: EnumField
EnumField_CallOrPut: EnumField
EnumField_PositionDirection: EnumField
EnumField_CreditLimit: EnumField
EnumField_IsRiskMonitoringEnabled: EnumField
EnumField_PersonId: EnumField
EnumField_PersonName: EnumField
EnumField_UserId: EnumField
EnumField_UserName: EnumField
EnumField_UserEmail: EnumField
EnumField_UserType: EnumField
EnumField_IsBlocked: EnumField
EnumField_IsEmployee: EnumField
EnumField_UserBranchId: EnumField
EnumField_UserRepresentativeId: EnumField
EnumField_Custom: EnumField
EnumSortDirection_Undefined: EnumSortDirection
EnumSortDirection_Asc: EnumSortDirection
EnumSortDirection_Desc: EnumSortDirection
EnumFieldType_Undefined: EnumFieldType
EnumFieldType_String: EnumFieldType
EnumFieldType_Int: EnumFieldType
EnumFieldType_Double: EnumFieldType
EnumFieldType_Date: EnumFieldType
