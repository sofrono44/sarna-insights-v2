# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common_enums.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12\x63ommon_enums.proto*S\n\x0b\x45numAppMode\x12\x19\n\x15\x45numAppMode_Undefined\x10\x00\x12\x14\n\x10\x45numAppMode_Real\x10\x01\x12\x13\n\x0f\x45numAppMode_V_T\x10\x02*\xe2\x02\n\x17\x45numClearingAccountType\x12%\n!EnumClearingAccountType_Undefined\x10\x00\x12 \n\x1c\x45numClearingAccountType_Cash\x10\x01\x12&\n\"EnumClearingAccountType_MarginLong\x10\x02\x12\'\n#EnumClearingAccountType_MarginShort\x10\x03\x12(\n$EnumClearingAccountType_TEFRA_Buffer\x10\x04\x12,\n(EnumClearingAccountType_When_Issued_Cash\x10\x05\x12*\n&EnumClearingAccountType_Firm_Specified\x10\x06\x12)\n%EnumClearingAccountType_Miscellaneous\x10\x07*@\n\x0c\x45numCurrency\x12\x1a\n\x16\x45numCurrency_Undefined\x10\x00\x12\x14\n\x10\x45numCurrency_USD\x10\x01*\xfc\x02\n\x13\x45numAccountRiskType\x12!\n\x1d\x45numAccountRiskType_Undefined\x10\x00\x12!\n\x1d\x45numAccountRiskType_RegT_Cash\x10\x01\x12*\n&EnumAccountRiskType_RegT_LimitedMargin\x10\x02\x12#\n\x1f\x45numAccountRiskType_RegT_Margin\x10\x03\x12\x1e\n\x1a\x45numAccountRiskType_PM_CPM\x10\x04\x12\x1d\n\x19\x45numAccountRiskType_PM_BD\x10\x05\x12\x1d\n\x19\x45numAccountRiskType_PM_MM\x10\x06\x12\'\n#EnumAccountRiskType_SPAN_Speculator\x10\x07\x12\"\n\x1e\x45numAccountRiskType_SPAN_Hedge\x10\x08\x12#\n\x1f\x45numAccountRiskType_SPAN_Member\x10\t*\xa0\x01\n\x10\x45numMaturityTerm\x12\x1e\n\x1a\x45numMaturityTerm_Undefined\x10\x00\x12\x18\n\x14\x45numMaturityTerm_All\x10\x01\x12\x19\n\x15\x45numMaturityTerm_Long\x10\x02\x12\x1b\n\x17\x45numMaturityTerm_Medium\x10\x03\x12\x1a\n\x16\x45numMaturityTerm_Short\x10\x04*\xbe\x03\n\x16\x45numOptionPricingModel\x12$\n EnumOptionPricingModel_Undefined\x10\x00\x12.\n*EnumOptionPricingModel_OptionChainAnalysis\x10\x01\x12 \n\x1c\x45numOptionPricingModel_Delta\x10\x02\x12-\n)EnumOptionPricingModel_OCC_PriceMovements\x10\x03\x12;\n7EnumOptionPricingModel_OCC_PriceMovementsWithLiveGreeks\x10\x04\x12\'\n#EnumOptionPricingModel_BlackScholes\x10\x05\x12\x36\n2EnumOptionPricingModel_BlackScholesWithBod_Pricing\x10\x06\x12\'\n#EnumOptionPricingModel_BinomialTree\x10\x07\x12\x36\n2EnumOptionPricingModel_BinomialTreeWithBod_Pricing\x10\x08*\xdd\x02\n\x16\x45numExternalDataSource\x12$\n EnumExternalDataSource_Undefined\x10\x00\x12%\n!EnumExternalDataSource_B_B_H_Bank\x10\x01\x12#\n\x1f\x45numExternalDataSource_U_S_Bank\x10\x02\x12%\n!EnumExternalDataSource_U_M_B_Bank\x10\x03\x12)\n%EnumExternalDataSource_FifthThirdBank\x10\x04\x12#\n\x1f\x45numExternalDataSource_CitiBank\x10\x05\x12+\n\'EnumExternalDataSource_B_N_Y_MellonBank\x10\x06\x12-\n)EnumExternalDataSource_TradeAwayExecution\x10\x07\x42\x18\xaa\x02\x15\x44TS.Libs.Common.Enumsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'common_enums_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\252\002\025DTS.Libs.Common.Enums'
  _globals['_ENUMAPPMODE']._serialized_start=22
  _globals['_ENUMAPPMODE']._serialized_end=105
  _globals['_ENUMCLEARINGACCOUNTTYPE']._serialized_start=108
  _globals['_ENUMCLEARINGACCOUNTTYPE']._serialized_end=462
  _globals['_ENUMCURRENCY']._serialized_start=464
  _globals['_ENUMCURRENCY']._serialized_end=528
  _globals['_ENUMACCOUNTRISKTYPE']._serialized_start=531
  _globals['_ENUMACCOUNTRISKTYPE']._serialized_end=911
  _globals['_ENUMMATURITYTERM']._serialized_start=914
  _globals['_ENUMMATURITYTERM']._serialized_end=1074
  _globals['_ENUMOPTIONPRICINGMODEL']._serialized_start=1077
  _globals['_ENUMOPTIONPRICINGMODEL']._serialized_end=1523
  _globals['_ENUMEXTERNALDATASOURCE']._serialized_start=1526
  _globals['_ENUMEXTERNALDATASOURCE']._serialized_end=1875
# @@protoc_insertion_point(module_scope)
