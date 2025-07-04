# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: account_maintenance_fee.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from . import account_maintenance_fee_enums_pb2 as account__maintenance__fee__enums__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x61\x63\x63ount_maintenance_fee.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a#account_maintenance_fee_enums.proto\"e\n\x19\x41\x63\x63ountMaintenanceFeeInfo\x12\x11\n\tAccountId\x18\x01 \x01(\x05\x12\x35\n\x15\x41\x63\x63ountMaintenanceFee\x18\x02 \x01(\x0b\x32\x16.AccountMaintenanceFee\"\xee\x03\n\x15\x41\x63\x63ountMaintenanceFee\x12\x1f\n\x17\x41\x63\x63ountMaintenanceFeeId\x18\x01 \x01(\x05\x12I\n\x1d\x41\x63\x63ountMaintenanceFeeSchedule\x18\x02 \x01(\x0e\x32\".EnumAccountMaintenanceFeeSchedule\x12\x11\n\tFeeAmount\x18\x03 \x01(\x01\x12\x17\n\x0f\x46\x65\x65PeriodInDays\x18\x04 \x01(\x05\x12\x19\n\x11MinNumberOfTrades\x18\x05 \x01(\x05\x12%\n\x1dMinNumberOfTradesPeriodInDays\x18\x06 \x01(\x05\x12\x1f\n\x17MinLevelOfAccountAssets\x18\x07 \x01(\x01\x12+\n#MinLevelOfAccountAssetsPeriodInDays\x18\x08 \x01(\x05\x12\x13\n\x0b\x44\x65scription\x18\t \x01(\t\x12/\n\x0b\x43reatedTime\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x34\n\x10LastModifiedTime\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1a\n\x12LastModifiedUserId\x18\x0c \x01(\x05\x12\x15\n\rIsSoftDeleted\x18\r \x01(\x08\x42)\xaa\x02&DTS.Libs.Protos.AccountMaintenanceFeesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'account_maintenance_fee_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\252\002&DTS.Libs.Protos.AccountMaintenanceFees'
  _globals['_ACCOUNTMAINTENANCEFEEINFO']._serialized_start=103
  _globals['_ACCOUNTMAINTENANCEFEEINFO']._serialized_end=204
  _globals['_ACCOUNTMAINTENANCEFEE']._serialized_start=207
  _globals['_ACCOUNTMAINTENANCEFEE']._serialized_end=701
# @@protoc_insertion_point(module_scope)
