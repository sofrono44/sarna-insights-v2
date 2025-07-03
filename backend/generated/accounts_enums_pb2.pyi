from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EnumAccountType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumAccountType_Undefined: _ClassVar[EnumAccountType]
    EnumAccountType_Individual: _ClassVar[EnumAccountType]
    EnumAccountType_TraditionalI_R_A: _ClassVar[EnumAccountType]
    EnumAccountType_RothI_R_A: _ClassVar[EnumAccountType]
    EnumAccountType_ErrorAccount: _ClassVar[EnumAccountType]
    EnumAccountType_DepositAccount: _ClassVar[EnumAccountType]
    EnumAccountType_PayoutAccount: _ClassVar[EnumAccountType]
    EnumAccountType_TestAccountWithoutSuppression: _ClassVar[EnumAccountType]
    EnumAccountType_TestAccountWithSuppression: _ClassVar[EnumAccountType]
    EnumAccountType_RisklessPrincipal: _ClassVar[EnumAccountType]
    EnumAccountType_ForAllocationToCustomersAtO_C_C: _ClassVar[EnumAccountType]
    EnumAccountType_ProfitAndLossAccount: _ClassVar[EnumAccountType]
    EnumAccountType_EducationI_R_A: _ClassVar[EnumAccountType]
    EnumAccountType_CoverdellE_S_A: _ClassVar[EnumAccountType]
    EnumAccountType_CollegeSavings529Plan: _ClassVar[EnumAccountType]
    EnumAccountType_SimpleI_R_A: _ClassVar[EnumAccountType]
    EnumAccountType_S_E_P: _ClassVar[EnumAccountType]
    EnumAccountType_Keogh: _ClassVar[EnumAccountType]
    EnumAccountType_Spousal: _ClassVar[EnumAccountType]
    EnumAccountType_Dealer: _ClassVar[EnumAccountType]
    EnumAccountType_Clearing: _ClassVar[EnumAccountType]
    EnumAccountType_Suspense: _ClassVar[EnumAccountType]
    EnumAccountType_TradeAwayInventoryAccount: _ClassVar[EnumAccountType]

class EnumAccountStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumAccountStatus_Undefined: _ClassVar[EnumAccountStatus]
    EnumAccountStatus_Active: _ClassVar[EnumAccountStatus]
    EnumAccountStatus_PendingKyc: _ClassVar[EnumAccountStatus]
    EnumAccountStatus_KycVerified: _ClassVar[EnumAccountStatus]
    EnumAccountStatus_PendingClearingConfirmation: _ClassVar[EnumAccountStatus]
    EnumAccountStatus_Blocked: _ClassVar[EnumAccountStatus]
    EnumAccountStatus_PendingDocuments: _ClassVar[EnumAccountStatus]
    EnumAccountStatus_ClosingTransactionsOnly: _ClassVar[EnumAccountStatus]

class EnumPositionTransferOrderType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumPositionTransferOrderType_Undefined: _ClassVar[EnumPositionTransferOrderType]
    EnumPositionTransferOrderType_FIFO: _ClassVar[EnumPositionTransferOrderType]
    EnumPositionTransferOrderType_LIFO: _ClassVar[EnumPositionTransferOrderType]
EnumAccountType_Undefined: EnumAccountType
EnumAccountType_Individual: EnumAccountType
EnumAccountType_TraditionalI_R_A: EnumAccountType
EnumAccountType_RothI_R_A: EnumAccountType
EnumAccountType_ErrorAccount: EnumAccountType
EnumAccountType_DepositAccount: EnumAccountType
EnumAccountType_PayoutAccount: EnumAccountType
EnumAccountType_TestAccountWithoutSuppression: EnumAccountType
EnumAccountType_TestAccountWithSuppression: EnumAccountType
EnumAccountType_RisklessPrincipal: EnumAccountType
EnumAccountType_ForAllocationToCustomersAtO_C_C: EnumAccountType
EnumAccountType_ProfitAndLossAccount: EnumAccountType
EnumAccountType_EducationI_R_A: EnumAccountType
EnumAccountType_CoverdellE_S_A: EnumAccountType
EnumAccountType_CollegeSavings529Plan: EnumAccountType
EnumAccountType_SimpleI_R_A: EnumAccountType
EnumAccountType_S_E_P: EnumAccountType
EnumAccountType_Keogh: EnumAccountType
EnumAccountType_Spousal: EnumAccountType
EnumAccountType_Dealer: EnumAccountType
EnumAccountType_Clearing: EnumAccountType
EnumAccountType_Suspense: EnumAccountType
EnumAccountType_TradeAwayInventoryAccount: EnumAccountType
EnumAccountStatus_Undefined: EnumAccountStatus
EnumAccountStatus_Active: EnumAccountStatus
EnumAccountStatus_PendingKyc: EnumAccountStatus
EnumAccountStatus_KycVerified: EnumAccountStatus
EnumAccountStatus_PendingClearingConfirmation: EnumAccountStatus
EnumAccountStatus_Blocked: EnumAccountStatus
EnumAccountStatus_PendingDocuments: EnumAccountStatus
EnumAccountStatus_ClosingTransactionsOnly: EnumAccountStatus
EnumPositionTransferOrderType_Undefined: EnumPositionTransferOrderType
EnumPositionTransferOrderType_FIFO: EnumPositionTransferOrderType
EnumPositionTransferOrderType_LIFO: EnumPositionTransferOrderType
