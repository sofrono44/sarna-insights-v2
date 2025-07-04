# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import sessions_enums_pb2 as sessions__enums__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nuser.proto\x1a\x14sessions_enums.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xfd\x02\n\x04User\x12\n\n\x02Id\x18\x01 \x01(\x05\x12\x0c\n\x04Name\x18\x02 \x01(\t\x12\r\n\x05\x45mail\x18\x03 \x01(\t\x12\x12\n\nIsEmployee\x18\x04 \x01(\x08\x12\x11\n\tFirstName\x18\x05 \x01(\t\x12\x10\n\x08LastName\x18\x06 \x01(\t\x12\x10\n\x08Username\x18\x07 \x01(\t\x12\x13\n\x0b\x43ountryCode\x18\x08 \x01(\t\x12\x14\n\x0cLanguageCode\x18\t \x01(\t\x12\x10\n\x08\x42ranchId\x18\n \x01(\x05\x12\x18\n\x10RepresentativeId\x18\x0b \x01(\x05\x12\x10\n\x08Password\x18\x0c \x01(\t\x12\x1c\n\x14RequestResetPassword\x18\r \x01(\x08\x12\x1f\n\x08UserRole\x18\x0e \x01(\x0e\x32\r.EnumUserType\x12(\n\x0fUserPermissions\x18\x0f \x03(\x0b\x32\x0f.UserPermission\x12/\n\x0b\x44\x61teOfBirth\x18\x10 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"}\n\x0eUserPermission\x12\x0e\n\x06UserId\x18\x01 \x01(\x05\x12/\n\x12UserPermissionType\x18\x02 \x01(\x0e\x32\x13.EnumUserPermission\x12\x10\n\x08\x42ranchId\x18\x03 \x01(\x05\x12\x18\n\x10RepresentativeId\x18\x04 \x01(\x05\x42\x18\xaa\x02\x15\x44TS.Libs.Protos.Usersb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'user_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\252\002\025DTS.Libs.Protos.Users'
  _globals['_USER']._serialized_start=70
  _globals['_USER']._serialized_end=451
  _globals['_USERPERMISSION']._serialized_start=453
  _globals['_USERPERMISSION']._serialized_end=578
# @@protoc_insertion_point(module_scope)
