from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EnumPriceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumPriceType_Undefined: _ClassVar[EnumPriceType]
    EnumPriceType_Market: _ClassVar[EnumPriceType]
    EnumPriceType_Limit: _ClassVar[EnumPriceType]
    EnumPriceType_Stop: _ClassVar[EnumPriceType]
    EnumPriceType_StopLimit: _ClassVar[EnumPriceType]
    EnumPriceType_MarketOnClose: _ClassVar[EnumPriceType]
    EnumPriceType_Even: _ClassVar[EnumPriceType]
    EnumPriceType_WithOrWithout: _ClassVar[EnumPriceType]
    EnumPriceType_LimitOrBetter: _ClassVar[EnumPriceType]
    EnumPriceType_LimitWithOrWithout: _ClassVar[EnumPriceType]
    EnumPriceType_OnBasis: _ClassVar[EnumPriceType]

class EnumStrategyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumStrategyType_Undefined: _ClassVar[EnumStrategyType]
    EnumStrategyType_Stock: _ClassVar[EnumStrategyType]
    EnumStrategyType_SingleOption: _ClassVar[EnumStrategyType]
    EnumStrategyType_FixedIncome: _ClassVar[EnumStrategyType]
    EnumStrategyType_MutualFund: _ClassVar[EnumStrategyType]
    EnumStrategyType_CoveredCall: _ClassVar[EnumStrategyType]
    EnumStrategyType_MarriedPut: _ClassVar[EnumStrategyType]
    EnumStrategyType_SyntheticCombo: _ClassVar[EnumStrategyType]
    EnumStrategyType_Vertical: _ClassVar[EnumStrategyType]
    EnumStrategyType_Calendar: _ClassVar[EnumStrategyType]
    EnumStrategyType_Straddle: _ClassVar[EnumStrategyType]
    EnumStrategyType_Strangle: _ClassVar[EnumStrategyType]
    EnumStrategyType_HedgeCollar: _ClassVar[EnumStrategyType]
    EnumStrategyType_CallSpread: _ClassVar[EnumStrategyType]
    EnumStrategyType_PutSpread: _ClassVar[EnumStrategyType]
    EnumStrategyType_Diagonal: _ClassVar[EnumStrategyType]
    EnumStrategyType_Combo: _ClassVar[EnumStrategyType]
    EnumStrategyType_Conversion: _ClassVar[EnumStrategyType]
    EnumStrategyType_Collar: _ClassVar[EnumStrategyType]
    EnumStrategyType_Butterfly: _ClassVar[EnumStrategyType]
    EnumStrategyType_Condor: _ClassVar[EnumStrategyType]
    EnumStrategyType_IronButterfly: _ClassVar[EnumStrategyType]
    EnumStrategyType_IronCondor: _ClassVar[EnumStrategyType]
    EnumStrategyType_Box: _ClassVar[EnumStrategyType]
    EnumStrategyType_CustomOptionSpread: _ClassVar[EnumStrategyType]
    EnumStrategyType_CustomCoveredStock: _ClassVar[EnumStrategyType]
    EnumStrategyType_UniversalSpread: _ClassVar[EnumStrategyType]

class EnumOrderStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumOrderStatus_Undefined: _ClassVar[EnumOrderStatus]
    EnumOrderStatus_New: _ClassVar[EnumOrderStatus]
    EnumOrderStatus_PartiallyFilled: _ClassVar[EnumOrderStatus]
    EnumOrderStatus_Filled: _ClassVar[EnumOrderStatus]
    EnumOrderStatus_DoneForDay: _ClassVar[EnumOrderStatus]
    EnumOrderStatus_Cancelled: _ClassVar[EnumOrderStatus]
    EnumOrderStatus_Replaced: _ClassVar[EnumOrderStatus]
    EnumOrderStatus_PendingCancel: _ClassVar[EnumOrderStatus]
    EnumOrderStatus_Stopped: _ClassVar[EnumOrderStatus]
    EnumOrderStatus_Rejected: _ClassVar[EnumOrderStatus]
    EnumOrderStatus_Suspended: _ClassVar[EnumOrderStatus]
    EnumOrderStatus_PendingNew: _ClassVar[EnumOrderStatus]
    EnumOrderStatus_Calculated: _ClassVar[EnumOrderStatus]
    EnumOrderStatus_Expired: _ClassVar[EnumOrderStatus]
    EnumOrderStatus_PendingReplace: _ClassVar[EnumOrderStatus]
    EnumOrderStatus_Saved: _ClassVar[EnumOrderStatus]
    EnumOrderStatus_FilledPriceAdjustment: _ClassVar[EnumOrderStatus]
    EnumOrderStatus_PositionClosed: _ClassVar[EnumOrderStatus]
    EnumOrderStatus_Corrected: _ClassVar[EnumOrderStatus]
    EnumOrderStatus_Busted: _ClassVar[EnumOrderStatus]
    EnumOrderStatus_Initiated: _ClassVar[EnumOrderStatus]
    EnumOrderStatus_ReplaceInitiated: _ClassVar[EnumOrderStatus]
    EnumOrderStatus_CancelInitiated: _ClassVar[EnumOrderStatus]
    EnumOrderStatus_CancelRejected: _ClassVar[EnumOrderStatus]
    EnumOrderStatus_ReplaceRejected: _ClassVar[EnumOrderStatus]
    EnumOrderStatus_AssignGroupToG_T_PostExecAllocation: _ClassVar[EnumOrderStatus]
    EnumOrderStatus_ConvertPostExecToIntraExecAllocation: _ClassVar[EnumOrderStatus]
    EnumOrderStatus_OffMarketHourOrdersSentToMarket: _ClassVar[EnumOrderStatus]
    EnumOrderStatus_InternallyCancelled: _ClassVar[EnumOrderStatus]

class EnumOrderInitiationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumOrderInitiationType_Undefined: _ClassVar[EnumOrderInitiationType]
    EnumOrderInitiationType_Place: _ClassVar[EnumOrderInitiationType]
    EnumOrderInitiationType_Replace: _ClassVar[EnumOrderInitiationType]
    EnumOrderInitiationType_Cancel: _ClassVar[EnumOrderInitiationType]
    EnumOrderInitiationType_G_T_AssignGroupToPostExecWithGroupUnassigned: _ClassVar[EnumOrderInitiationType]
    EnumOrderInitiationType_G_T_ConvertPostExecToIntraExecAllocation: _ClassVar[EnumOrderInitiationType]
    EnumOrderInitiationType_ReviewPlace: _ClassVar[EnumOrderInitiationType]
    EnumOrderInitiationType_ReviewReplace: _ClassVar[EnumOrderInitiationType]
    EnumOrderInitiationType_ReviewCancel: _ClassVar[EnumOrderInitiationType]

class EnumPlacedAs(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumPlacedAs_Undefined: _ClassVar[EnumPlacedAs]
    EnumPlacedAs_Unsolicited: _ClassVar[EnumPlacedAs]
    EnumPlacedAs_Solicited: _ClassVar[EnumPlacedAs]
    EnumPlacedAs_Discretionary: _ClassVar[EnumPlacedAs]

class EnumPositionEffect(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumPositionEffect_Undefined: _ClassVar[EnumPositionEffect]
    EnumPositionEffect_Open: _ClassVar[EnumPositionEffect]
    EnumPositionEffect_Close: _ClassVar[EnumPositionEffect]

class EnumSpreadPositionEffect(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumSpreadPositionEffect_Undefined: _ClassVar[EnumSpreadPositionEffect]
    EnumSpreadPositionEffect_Open: _ClassVar[EnumSpreadPositionEffect]
    EnumSpreadPositionEffect_Close: _ClassVar[EnumSpreadPositionEffect]
    EnumSpreadPositionEffect_Mixed: _ClassVar[EnumSpreadPositionEffect]

class EnumOrderDuration(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumOrderDuration_Undefined: _ClassVar[EnumOrderDuration]
    EnumOrderDuration_Day: _ClassVar[EnumOrderDuration]
    EnumOrderDuration_G_T_C: _ClassVar[EnumOrderDuration]
    EnumOrderDuration_O_P_G: _ClassVar[EnumOrderDuration]
    EnumOrderDuration_I_O_C: _ClassVar[EnumOrderDuration]
    EnumOrderDuration_F_O_K: _ClassVar[EnumOrderDuration]
    EnumOrderDuration_G_T_X: _ClassVar[EnumOrderDuration]
    EnumOrderDuration_G_T_D: _ClassVar[EnumOrderDuration]
    EnumOrderDuration_A_T_C: _ClassVar[EnumOrderDuration]

class EnumOrderAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumOrderAction_Undefined: _ClassVar[EnumOrderAction]
    EnumOrderAction_Buy: _ClassVar[EnumOrderAction]
    EnumOrderAction_Sell: _ClassVar[EnumOrderAction]

class EnumCallOrPut(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumCallOrPut_Undefined: _ClassVar[EnumCallOrPut]
    EnumCallOrPut_Call: _ClassVar[EnumCallOrPut]
    EnumCallOrPut_Put: _ClassVar[EnumCallOrPut]

class EnumExecutedAs(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumExecutedAs_Undefined: _ClassVar[EnumExecutedAs]
    EnumExecutedAs_Agent: _ClassVar[EnumExecutedAs]
    EnumExecutedAs_Principal: _ClassVar[EnumExecutedAs]

class EnumLegSecType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumLegSecType_Undefined: _ClassVar[EnumLegSecType]
    EnumLegSecType_Stock: _ClassVar[EnumLegSecType]
    EnumLegSecType_Option: _ClassVar[EnumLegSecType]
    EnumLegSecType_MutualFund: _ClassVar[EnumLegSecType]
    EnumLegSecType_FixedIncome: _ClassVar[EnumLegSecType]

class EnumSecurityType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumSecurityType_Undefined: _ClassVar[EnumSecurityType]
    EnumSecurityType_Stock: _ClassVar[EnumSecurityType]
    EnumSecurityType_Option: _ClassVar[EnumSecurityType]
    EnumSecurityType_MutualFund: _ClassVar[EnumSecurityType]
    EnumSecurityType_FixedIncome: _ClassVar[EnumSecurityType]
    EnumSecurityType_PreciousMetal: _ClassVar[EnumSecurityType]
    EnumSecurityType_Right: _ClassVar[EnumSecurityType]
    EnumSecurityType_Warrant: _ClassVar[EnumSecurityType]
    EnumSecurityType_UIT: _ClassVar[EnumSecurityType]
    EnumSecurityType_PreferredStock: _ClassVar[EnumSecurityType]
    EnumSecurityType_Future: _ClassVar[EnumSecurityType]
    EnumSecurityType_FutureOption: _ClassVar[EnumSecurityType]
    EnumSecurityType_MoneyMarketFund: _ClassVar[EnumSecurityType]
    EnumSecurityType_ExternalCash: _ClassVar[EnumSecurityType]
    EnumSecurityType_AmericanDepositoryReceipt: _ClassVar[EnumSecurityType]

class EnumOrderAllocationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumOrderAllocationType_Undefined: _ClassVar[EnumOrderAllocationType]
    EnumOrderAllocationType_Regular: _ClassVar[EnumOrderAllocationType]
    EnumOrderAllocationType_G_T_Child: _ClassVar[EnumOrderAllocationType]
    EnumOrderAllocationType_G_T_InventoryIntraExecutionProportionalPriceAllocation: _ClassVar[EnumOrderAllocationType]
    EnumOrderAllocationType_G_T_InventoryIntraExecutionEvenPriceAllocation: _ClassVar[EnumOrderAllocationType]
    EnumOrderAllocationType_G_T_InventoryPostExecutionAllocationGroupAssigned: _ClassVar[EnumOrderAllocationType]
    EnumOrderAllocationType_G_T_InventoryPostExecutionAllocationGroupUnassigned: _ClassVar[EnumOrderAllocationType]
    EnumOrderAllocationType_G_T_NonInventoryParent: _ClassVar[EnumOrderAllocationType]
    EnumOrderAllocationType_G_T_NonInventoryChild: _ClassVar[EnumOrderAllocationType]

class EnumOrdersInfoRequestType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumOrdersInfoRequestType_Undefined: _ClassVar[EnumOrdersInfoRequestType]
    EnumOrdersInfoRequestType_CurrentOrders: _ClassVar[EnumOrdersInfoRequestType]
    EnumOrdersInfoRequestType_HistoricalOrders: _ClassVar[EnumOrdersInfoRequestType]

class EnumOrderActionWithPositionEffect(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumOrderActionWithPositionEffect_Undefined: _ClassVar[EnumOrderActionWithPositionEffect]
    EnumOrderActionWithPositionEffect_Buy: _ClassVar[EnumOrderActionWithPositionEffect]
    EnumOrderActionWithPositionEffect_Sell: _ClassVar[EnumOrderActionWithPositionEffect]
    EnumOrderActionWithPositionEffect_SellShort: _ClassVar[EnumOrderActionWithPositionEffect]
    EnumOrderActionWithPositionEffect_BuyToOpen: _ClassVar[EnumOrderActionWithPositionEffect]
    EnumOrderActionWithPositionEffect_BuyToClose: _ClassVar[EnumOrderActionWithPositionEffect]
    EnumOrderActionWithPositionEffect_SellToOpen: _ClassVar[EnumOrderActionWithPositionEffect]
    EnumOrderActionWithPositionEffect_SellToClose: _ClassVar[EnumOrderActionWithPositionEffect]
    EnumOrderActionWithPositionEffect_BuyToCover: _ClassVar[EnumOrderActionWithPositionEffect]

class EnumExecutionRoute(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumExecutionRoute_Undefined: _ClassVar[EnumExecutionRoute]
    EnumExecutionRoute_IntegTest: _ClassVar[EnumExecutionRoute]
    EnumExecutionRoute_MarketProviderSim: _ClassVar[EnumExecutionRoute]
    EnumExecutionRoute_Instinet: _ClassVar[EnumExecutionRoute]
    EnumExecutionRoute_ClearingFirmDrops: _ClassVar[EnumExecutionRoute]
    EnumExecutionRoute_ExternalOMS: _ClassVar[EnumExecutionRoute]
    EnumExecutionRoute_LiquidityBook: _ClassVar[EnumExecutionRoute]

class EnumExchangeTape(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumExchangeTape_Undefined: _ClassVar[EnumExchangeTape]
    EnumExchangeTape_A: _ClassVar[EnumExchangeTape]
    EnumExchangeTape_B: _ClassVar[EnumExchangeTape]
    EnumExchangeTape_C: _ClassVar[EnumExchangeTape]
EnumPriceType_Undefined: EnumPriceType
EnumPriceType_Market: EnumPriceType
EnumPriceType_Limit: EnumPriceType
EnumPriceType_Stop: EnumPriceType
EnumPriceType_StopLimit: EnumPriceType
EnumPriceType_MarketOnClose: EnumPriceType
EnumPriceType_Even: EnumPriceType
EnumPriceType_WithOrWithout: EnumPriceType
EnumPriceType_LimitOrBetter: EnumPriceType
EnumPriceType_LimitWithOrWithout: EnumPriceType
EnumPriceType_OnBasis: EnumPriceType
EnumStrategyType_Undefined: EnumStrategyType
EnumStrategyType_Stock: EnumStrategyType
EnumStrategyType_SingleOption: EnumStrategyType
EnumStrategyType_FixedIncome: EnumStrategyType
EnumStrategyType_MutualFund: EnumStrategyType
EnumStrategyType_CoveredCall: EnumStrategyType
EnumStrategyType_MarriedPut: EnumStrategyType
EnumStrategyType_SyntheticCombo: EnumStrategyType
EnumStrategyType_Vertical: EnumStrategyType
EnumStrategyType_Calendar: EnumStrategyType
EnumStrategyType_Straddle: EnumStrategyType
EnumStrategyType_Strangle: EnumStrategyType
EnumStrategyType_HedgeCollar: EnumStrategyType
EnumStrategyType_CallSpread: EnumStrategyType
EnumStrategyType_PutSpread: EnumStrategyType
EnumStrategyType_Diagonal: EnumStrategyType
EnumStrategyType_Combo: EnumStrategyType
EnumStrategyType_Conversion: EnumStrategyType
EnumStrategyType_Collar: EnumStrategyType
EnumStrategyType_Butterfly: EnumStrategyType
EnumStrategyType_Condor: EnumStrategyType
EnumStrategyType_IronButterfly: EnumStrategyType
EnumStrategyType_IronCondor: EnumStrategyType
EnumStrategyType_Box: EnumStrategyType
EnumStrategyType_CustomOptionSpread: EnumStrategyType
EnumStrategyType_CustomCoveredStock: EnumStrategyType
EnumStrategyType_UniversalSpread: EnumStrategyType
EnumOrderStatus_Undefined: EnumOrderStatus
EnumOrderStatus_New: EnumOrderStatus
EnumOrderStatus_PartiallyFilled: EnumOrderStatus
EnumOrderStatus_Filled: EnumOrderStatus
EnumOrderStatus_DoneForDay: EnumOrderStatus
EnumOrderStatus_Cancelled: EnumOrderStatus
EnumOrderStatus_Replaced: EnumOrderStatus
EnumOrderStatus_PendingCancel: EnumOrderStatus
EnumOrderStatus_Stopped: EnumOrderStatus
EnumOrderStatus_Rejected: EnumOrderStatus
EnumOrderStatus_Suspended: EnumOrderStatus
EnumOrderStatus_PendingNew: EnumOrderStatus
EnumOrderStatus_Calculated: EnumOrderStatus
EnumOrderStatus_Expired: EnumOrderStatus
EnumOrderStatus_PendingReplace: EnumOrderStatus
EnumOrderStatus_Saved: EnumOrderStatus
EnumOrderStatus_FilledPriceAdjustment: EnumOrderStatus
EnumOrderStatus_PositionClosed: EnumOrderStatus
EnumOrderStatus_Corrected: EnumOrderStatus
EnumOrderStatus_Busted: EnumOrderStatus
EnumOrderStatus_Initiated: EnumOrderStatus
EnumOrderStatus_ReplaceInitiated: EnumOrderStatus
EnumOrderStatus_CancelInitiated: EnumOrderStatus
EnumOrderStatus_CancelRejected: EnumOrderStatus
EnumOrderStatus_ReplaceRejected: EnumOrderStatus
EnumOrderStatus_AssignGroupToG_T_PostExecAllocation: EnumOrderStatus
EnumOrderStatus_ConvertPostExecToIntraExecAllocation: EnumOrderStatus
EnumOrderStatus_OffMarketHourOrdersSentToMarket: EnumOrderStatus
EnumOrderStatus_InternallyCancelled: EnumOrderStatus
EnumOrderInitiationType_Undefined: EnumOrderInitiationType
EnumOrderInitiationType_Place: EnumOrderInitiationType
EnumOrderInitiationType_Replace: EnumOrderInitiationType
EnumOrderInitiationType_Cancel: EnumOrderInitiationType
EnumOrderInitiationType_G_T_AssignGroupToPostExecWithGroupUnassigned: EnumOrderInitiationType
EnumOrderInitiationType_G_T_ConvertPostExecToIntraExecAllocation: EnumOrderInitiationType
EnumOrderInitiationType_ReviewPlace: EnumOrderInitiationType
EnumOrderInitiationType_ReviewReplace: EnumOrderInitiationType
EnumOrderInitiationType_ReviewCancel: EnumOrderInitiationType
EnumPlacedAs_Undefined: EnumPlacedAs
EnumPlacedAs_Unsolicited: EnumPlacedAs
EnumPlacedAs_Solicited: EnumPlacedAs
EnumPlacedAs_Discretionary: EnumPlacedAs
EnumPositionEffect_Undefined: EnumPositionEffect
EnumPositionEffect_Open: EnumPositionEffect
EnumPositionEffect_Close: EnumPositionEffect
EnumSpreadPositionEffect_Undefined: EnumSpreadPositionEffect
EnumSpreadPositionEffect_Open: EnumSpreadPositionEffect
EnumSpreadPositionEffect_Close: EnumSpreadPositionEffect
EnumSpreadPositionEffect_Mixed: EnumSpreadPositionEffect
EnumOrderDuration_Undefined: EnumOrderDuration
EnumOrderDuration_Day: EnumOrderDuration
EnumOrderDuration_G_T_C: EnumOrderDuration
EnumOrderDuration_O_P_G: EnumOrderDuration
EnumOrderDuration_I_O_C: EnumOrderDuration
EnumOrderDuration_F_O_K: EnumOrderDuration
EnumOrderDuration_G_T_X: EnumOrderDuration
EnumOrderDuration_G_T_D: EnumOrderDuration
EnumOrderDuration_A_T_C: EnumOrderDuration
EnumOrderAction_Undefined: EnumOrderAction
EnumOrderAction_Buy: EnumOrderAction
EnumOrderAction_Sell: EnumOrderAction
EnumCallOrPut_Undefined: EnumCallOrPut
EnumCallOrPut_Call: EnumCallOrPut
EnumCallOrPut_Put: EnumCallOrPut
EnumExecutedAs_Undefined: EnumExecutedAs
EnumExecutedAs_Agent: EnumExecutedAs
EnumExecutedAs_Principal: EnumExecutedAs
EnumLegSecType_Undefined: EnumLegSecType
EnumLegSecType_Stock: EnumLegSecType
EnumLegSecType_Option: EnumLegSecType
EnumLegSecType_MutualFund: EnumLegSecType
EnumLegSecType_FixedIncome: EnumLegSecType
EnumSecurityType_Undefined: EnumSecurityType
EnumSecurityType_Stock: EnumSecurityType
EnumSecurityType_Option: EnumSecurityType
EnumSecurityType_MutualFund: EnumSecurityType
EnumSecurityType_FixedIncome: EnumSecurityType
EnumSecurityType_PreciousMetal: EnumSecurityType
EnumSecurityType_Right: EnumSecurityType
EnumSecurityType_Warrant: EnumSecurityType
EnumSecurityType_UIT: EnumSecurityType
EnumSecurityType_PreferredStock: EnumSecurityType
EnumSecurityType_Future: EnumSecurityType
EnumSecurityType_FutureOption: EnumSecurityType
EnumSecurityType_MoneyMarketFund: EnumSecurityType
EnumSecurityType_ExternalCash: EnumSecurityType
EnumSecurityType_AmericanDepositoryReceipt: EnumSecurityType
EnumOrderAllocationType_Undefined: EnumOrderAllocationType
EnumOrderAllocationType_Regular: EnumOrderAllocationType
EnumOrderAllocationType_G_T_Child: EnumOrderAllocationType
EnumOrderAllocationType_G_T_InventoryIntraExecutionProportionalPriceAllocation: EnumOrderAllocationType
EnumOrderAllocationType_G_T_InventoryIntraExecutionEvenPriceAllocation: EnumOrderAllocationType
EnumOrderAllocationType_G_T_InventoryPostExecutionAllocationGroupAssigned: EnumOrderAllocationType
EnumOrderAllocationType_G_T_InventoryPostExecutionAllocationGroupUnassigned: EnumOrderAllocationType
EnumOrderAllocationType_G_T_NonInventoryParent: EnumOrderAllocationType
EnumOrderAllocationType_G_T_NonInventoryChild: EnumOrderAllocationType
EnumOrdersInfoRequestType_Undefined: EnumOrdersInfoRequestType
EnumOrdersInfoRequestType_CurrentOrders: EnumOrdersInfoRequestType
EnumOrdersInfoRequestType_HistoricalOrders: EnumOrdersInfoRequestType
EnumOrderActionWithPositionEffect_Undefined: EnumOrderActionWithPositionEffect
EnumOrderActionWithPositionEffect_Buy: EnumOrderActionWithPositionEffect
EnumOrderActionWithPositionEffect_Sell: EnumOrderActionWithPositionEffect
EnumOrderActionWithPositionEffect_SellShort: EnumOrderActionWithPositionEffect
EnumOrderActionWithPositionEffect_BuyToOpen: EnumOrderActionWithPositionEffect
EnumOrderActionWithPositionEffect_BuyToClose: EnumOrderActionWithPositionEffect
EnumOrderActionWithPositionEffect_SellToOpen: EnumOrderActionWithPositionEffect
EnumOrderActionWithPositionEffect_SellToClose: EnumOrderActionWithPositionEffect
EnumOrderActionWithPositionEffect_BuyToCover: EnumOrderActionWithPositionEffect
EnumExecutionRoute_Undefined: EnumExecutionRoute
EnumExecutionRoute_IntegTest: EnumExecutionRoute
EnumExecutionRoute_MarketProviderSim: EnumExecutionRoute
EnumExecutionRoute_Instinet: EnumExecutionRoute
EnumExecutionRoute_ClearingFirmDrops: EnumExecutionRoute
EnumExecutionRoute_ExternalOMS: EnumExecutionRoute
EnumExecutionRoute_LiquidityBook: EnumExecutionRoute
EnumExchangeTape_Undefined: EnumExchangeTape
EnumExchangeTape_A: EnumExchangeTape
EnumExchangeTape_B: EnumExchangeTape
EnumExchangeTape_C: EnumExchangeTape
