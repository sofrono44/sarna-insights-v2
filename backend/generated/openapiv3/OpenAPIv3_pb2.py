# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: openapiv3/OpenAPIv3.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19openapiv3/OpenAPIv3.proto\x12\nopenapi.v3\x1a\x19google/protobuf/any.proto\"t\n\x18\x41\x64\x64itionalPropertiesItem\x12<\n\x13schema_or_reference\x18\x01 \x01(\x0b\x32\x1d.openapi.v3.SchemaOrReferenceH\x00\x12\x11\n\x07\x62oolean\x18\x02 \x01(\x08H\x00\x42\x07\n\x05oneof\"8\n\x03\x41ny\x12#\n\x05value\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x0c\n\x04yaml\x18\x02 \x01(\t\"h\n\x0f\x41nyOrExpression\x12\x1e\n\x03\x61ny\x18\x01 \x01(\x0b\x32\x0f.openapi.v3.AnyH\x00\x12,\n\nexpression\x18\x02 \x01(\x0b\x32\x16.openapi.v3.ExpressionH\x00\x42\x07\n\x05oneof\"j\n\x08\x43\x61llback\x12\'\n\x04path\x18\x01 \x03(\x0b\x32\x19.openapi.v3.NamedPathItem\x12\x35\n\x17specification_extension\x18\x02 \x03(\x0b\x32\x14.openapi.v3.NamedAny\"t\n\x13\x43\x61llbackOrReference\x12(\n\x08\x63\x61llback\x18\x01 \x01(\x0b\x32\x14.openapi.v3.CallbackH\x00\x12*\n\treference\x18\x02 \x01(\x0b\x32\x15.openapi.v3.ReferenceH\x00\x42\x07\n\x05oneof\"\\\n\x15\x43\x61llbacksOrReferences\x12\x43\n\x15\x61\x64\x64itional_properties\x18\x01 \x03(\x0b\x32$.openapi.v3.NamedCallbackOrReference\"\xaf\x04\n\nComponents\x12\x30\n\x07schemas\x18\x01 \x01(\x0b\x32\x1f.openapi.v3.SchemasOrReferences\x12\x34\n\tresponses\x18\x02 \x01(\x0b\x32!.openapi.v3.ResponsesOrReferences\x12\x36\n\nparameters\x18\x03 \x01(\x0b\x32\".openapi.v3.ParametersOrReferences\x12\x32\n\x08\x65xamples\x18\x04 \x01(\x0b\x32 .openapi.v3.ExamplesOrReferences\x12=\n\x0erequest_bodies\x18\x05 \x01(\x0b\x32%.openapi.v3.RequestBodiesOrReferences\x12\x30\n\x07headers\x18\x06 \x01(\x0b\x32\x1f.openapi.v3.HeadersOrReferences\x12\x41\n\x10security_schemes\x18\x07 \x01(\x0b\x32\'.openapi.v3.SecuritySchemesOrReferences\x12,\n\x05links\x18\x08 \x01(\x0b\x32\x1d.openapi.v3.LinksOrReferences\x12\x34\n\tcallbacks\x18\t \x01(\x0b\x32!.openapi.v3.CallbacksOrReferences\x12\x35\n\x17specification_extension\x18\n \x03(\x0b\x32\x14.openapi.v3.NamedAny\"j\n\x07\x43ontact\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x35\n\x17specification_extension\x18\x04 \x03(\x0b\x32\x14.openapi.v3.NamedAny\"M\n\x0b\x44\x65\x66\x61ultType\x12\x10\n\x06number\x18\x01 \x01(\x01H\x00\x12\x11\n\x07\x62oolean\x18\x02 \x01(\x08H\x00\x12\x10\n\x06string\x18\x03 \x01(\tH\x00\x42\x07\n\x05oneof\"\x83\x01\n\rDiscriminator\x12\x15\n\rproperty_name\x18\x01 \x01(\t\x12$\n\x07mapping\x18\x02 \x01(\x0b\x32\x13.openapi.v3.Strings\x12\x35\n\x17specification_extension\x18\x03 \x03(\x0b\x32\x14.openapi.v3.NamedAny\"\xe8\x02\n\x08\x44ocument\x12\x0f\n\x07openapi\x18\x01 \x01(\t\x12\x1e\n\x04info\x18\x02 \x01(\x0b\x32\x10.openapi.v3.Info\x12#\n\x07servers\x18\x03 \x03(\x0b\x32\x12.openapi.v3.Server\x12 \n\x05paths\x18\x04 \x01(\x0b\x32\x11.openapi.v3.Paths\x12*\n\ncomponents\x18\x05 \x01(\x0b\x32\x16.openapi.v3.Components\x12\x31\n\x08security\x18\x06 \x03(\x0b\x32\x1f.openapi.v3.SecurityRequirement\x12\x1d\n\x04tags\x18\x07 \x03(\x0b\x32\x0f.openapi.v3.Tag\x12/\n\rexternal_docs\x18\x08 \x01(\x0b\x32\x18.openapi.v3.ExternalDocs\x12\x35\n\x17specification_extension\x18\t \x03(\x0b\x32\x14.openapi.v3.NamedAny\"\xc1\x01\n\x08\x45ncoding\x12\x14\n\x0c\x63ontent_type\x18\x01 \x01(\t\x12\x30\n\x07headers\x18\x02 \x01(\x0b\x32\x1f.openapi.v3.HeadersOrReferences\x12\r\n\x05style\x18\x03 \x01(\t\x12\x0f\n\x07\x65xplode\x18\x04 \x01(\x08\x12\x16\n\x0e\x61llow_reserved\x18\x05 \x01(\x08\x12\x35\n\x17specification_extension\x18\x06 \x03(\x0b\x32\x14.openapi.v3.NamedAny\"E\n\tEncodings\x12\x38\n\x15\x61\x64\x64itional_properties\x18\x01 \x03(\x0b\x32\x19.openapi.v3.NamedEncoding\"\x9e\x01\n\x07\x45xample\x12\x0f\n\x07summary\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x1e\n\x05value\x18\x03 \x01(\x0b\x32\x0f.openapi.v3.Any\x12\x16\n\x0e\x65xternal_value\x18\x04 \x01(\t\x12\x35\n\x17specification_extension\x18\x05 \x03(\x0b\x32\x14.openapi.v3.NamedAny\"q\n\x12\x45xampleOrReference\x12&\n\x07\x65xample\x18\x01 \x01(\x0b\x32\x13.openapi.v3.ExampleH\x00\x12*\n\treference\x18\x02 \x01(\x0b\x32\x15.openapi.v3.ReferenceH\x00\x42\x07\n\x05oneof\"Z\n\x14\x45xamplesOrReferences\x12\x42\n\x15\x61\x64\x64itional_properties\x18\x01 \x03(\x0b\x32#.openapi.v3.NamedExampleOrReference\"A\n\nExpression\x12\x33\n\x15\x61\x64\x64itional_properties\x18\x01 \x03(\x0b\x32\x14.openapi.v3.NamedAny\"g\n\x0c\x45xternalDocs\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x35\n\x17specification_extension\x18\x03 \x03(\x0b\x32\x14.openapi.v3.NamedAny\"\xfb\x02\n\x06Header\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x10\n\x08required\x18\x02 \x01(\x08\x12\x12\n\ndeprecated\x18\x03 \x01(\x08\x12\x19\n\x11\x61llow_empty_value\x18\x04 \x01(\x08\x12\r\n\x05style\x18\x05 \x01(\t\x12\x0f\n\x07\x65xplode\x18\x06 \x01(\x08\x12\x16\n\x0e\x61llow_reserved\x18\x07 \x01(\x08\x12-\n\x06schema\x18\x08 \x01(\x0b\x32\x1d.openapi.v3.SchemaOrReference\x12 \n\x07\x65xample\x18\t \x01(\x0b\x32\x0f.openapi.v3.Any\x12\x32\n\x08\x65xamples\x18\n \x01(\x0b\x32 .openapi.v3.ExamplesOrReferences\x12\'\n\x07\x63ontent\x18\x0b \x01(\x0b\x32\x16.openapi.v3.MediaTypes\x12\x35\n\x17specification_extension\x18\x0c \x03(\x0b\x32\x14.openapi.v3.NamedAny\"n\n\x11HeaderOrReference\x12$\n\x06header\x18\x01 \x01(\x0b\x32\x12.openapi.v3.HeaderH\x00\x12*\n\treference\x18\x02 \x01(\x0b\x32\x15.openapi.v3.ReferenceH\x00\x42\x07\n\x05oneof\"X\n\x13HeadersOrReferences\x12\x41\n\x15\x61\x64\x64itional_properties\x18\x01 \x03(\x0b\x32\".openapi.v3.NamedHeaderOrReference\"\xe9\x01\n\x04Info\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x18\n\x10terms_of_service\x18\x03 \x01(\t\x12$\n\x07\x63ontact\x18\x04 \x01(\x0b\x32\x13.openapi.v3.Contact\x12$\n\x07license\x18\x05 \x01(\x0b\x32\x13.openapi.v3.License\x12\x0f\n\x07version\x18\x06 \x01(\t\x12\x35\n\x17specification_extension\x18\x07 \x03(\x0b\x32\x14.openapi.v3.NamedAny\x12\x0f\n\x07summary\x18\x08 \x01(\t\"G\n\tItemsItem\x12:\n\x13schema_or_reference\x18\x01 \x03(\x0b\x32\x1d.openapi.v3.SchemaOrReference\"[\n\x07License\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x35\n\x17specification_extension\x18\x03 \x03(\x0b\x32\x14.openapi.v3.NamedAny\"\x87\x02\n\x04Link\x12\x15\n\roperation_ref\x18\x01 \x01(\t\x12\x14\n\x0coperation_id\x18\x02 \x01(\t\x12/\n\nparameters\x18\x03 \x01(\x0b\x32\x1b.openapi.v3.AnyOrExpression\x12\x31\n\x0crequest_body\x18\x04 \x01(\x0b\x32\x1b.openapi.v3.AnyOrExpression\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\"\n\x06server\x18\x06 \x01(\x0b\x32\x12.openapi.v3.Server\x12\x35\n\x17specification_extension\x18\x07 \x03(\x0b\x32\x14.openapi.v3.NamedAny\"h\n\x0fLinkOrReference\x12 \n\x04link\x18\x01 \x01(\x0b\x32\x10.openapi.v3.LinkH\x00\x12*\n\treference\x18\x02 \x01(\x0b\x32\x15.openapi.v3.ReferenceH\x00\x42\x07\n\x05oneof\"T\n\x11LinksOrReferences\x12?\n\x15\x61\x64\x64itional_properties\x18\x01 \x03(\x0b\x32 .openapi.v3.NamedLinkOrReference\"\xf0\x01\n\tMediaType\x12-\n\x06schema\x18\x01 \x01(\x0b\x32\x1d.openapi.v3.SchemaOrReference\x12 \n\x07\x65xample\x18\x02 \x01(\x0b\x32\x0f.openapi.v3.Any\x12\x32\n\x08\x65xamples\x18\x03 \x01(\x0b\x32 .openapi.v3.ExamplesOrReferences\x12\'\n\x08\x65ncoding\x18\x04 \x01(\x0b\x32\x15.openapi.v3.Encodings\x12\x35\n\x17specification_extension\x18\x05 \x03(\x0b\x32\x14.openapi.v3.NamedAny\"G\n\nMediaTypes\x12\x39\n\x15\x61\x64\x64itional_properties\x18\x01 \x03(\x0b\x32\x1a.openapi.v3.NamedMediaType\"8\n\x08NamedAny\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1e\n\x05value\x18\x02 \x01(\x0b\x32\x0f.openapi.v3.Any\"X\n\x18NamedCallbackOrReference\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\x05value\x18\x02 \x01(\x0b\x32\x1f.openapi.v3.CallbackOrReference\"B\n\rNamedEncoding\x12\x0c\n\x04name\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.openapi.v3.Encoding\"V\n\x17NamedExampleOrReference\x12\x0c\n\x04name\x18\x01 \x01(\t\x12-\n\x05value\x18\x02 \x01(\x0b\x32\x1e.openapi.v3.ExampleOrReference\"T\n\x16NamedHeaderOrReference\x12\x0c\n\x04name\x18\x01 \x01(\t\x12,\n\x05value\x18\x02 \x01(\x0b\x32\x1d.openapi.v3.HeaderOrReference\"P\n\x14NamedLinkOrReference\x12\x0c\n\x04name\x18\x01 \x01(\t\x12*\n\x05value\x18\x02 \x01(\x0b\x32\x1b.openapi.v3.LinkOrReference\"D\n\x0eNamedMediaType\x12\x0c\n\x04name\x18\x01 \x01(\t\x12$\n\x05value\x18\x02 \x01(\x0b\x32\x15.openapi.v3.MediaType\"Z\n\x19NamedParameterOrReference\x12\x0c\n\x04name\x18\x01 \x01(\t\x12/\n\x05value\x18\x02 \x01(\x0b\x32 .openapi.v3.ParameterOrReference\"B\n\rNamedPathItem\x12\x0c\n\x04name\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.openapi.v3.PathItem\"^\n\x1bNamedRequestBodyOrReference\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x31\n\x05value\x18\x02 \x01(\x0b\x32\".openapi.v3.RequestBodyOrReference\"X\n\x18NamedResponseOrReference\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\x05value\x18\x02 \x01(\x0b\x32\x1f.openapi.v3.ResponseOrReference\"T\n\x16NamedSchemaOrReference\x12\x0c\n\x04name\x18\x01 \x01(\t\x12,\n\x05value\x18\x02 \x01(\x0b\x32\x1d.openapi.v3.SchemaOrReference\"d\n\x1eNamedSecuritySchemeOrReference\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x34\n\x05value\x18\x02 \x01(\x0b\x32%.openapi.v3.SecuritySchemeOrReference\"N\n\x13NamedServerVariable\x12\x0c\n\x04name\x18\x01 \x01(\t\x12)\n\x05value\x18\x02 \x01(\x0b\x32\x1a.openapi.v3.ServerVariable\"*\n\x0bNamedString\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"H\n\x10NamedStringArray\x12\x0c\n\x04name\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.openapi.v3.StringArray\"\xaa\x01\n\tOauthFlow\x12\x19\n\x11\x61uthorization_url\x18\x01 \x01(\t\x12\x11\n\ttoken_url\x18\x02 \x01(\t\x12\x13\n\x0brefresh_url\x18\x03 \x01(\t\x12#\n\x06scopes\x18\x04 \x01(\x0b\x32\x13.openapi.v3.Strings\x12\x35\n\x17specification_extension\x18\x05 \x03(\x0b\x32\x14.openapi.v3.NamedAny\"\xfb\x01\n\nOauthFlows\x12\'\n\x08implicit\x18\x01 \x01(\x0b\x32\x15.openapi.v3.OauthFlow\x12\'\n\x08password\x18\x02 \x01(\x0b\x32\x15.openapi.v3.OauthFlow\x12\x31\n\x12\x63lient_credentials\x18\x03 \x01(\x0b\x32\x15.openapi.v3.OauthFlow\x12\x31\n\x12\x61uthorization_code\x18\x04 \x01(\x0b\x32\x15.openapi.v3.OauthFlow\x12\x35\n\x17specification_extension\x18\x05 \x03(\x0b\x32\x14.openapi.v3.NamedAny\"=\n\x06Object\x12\x33\n\x15\x61\x64\x64itional_properties\x18\x01 \x03(\x0b\x32\x14.openapi.v3.NamedAny\"\xf9\x03\n\tOperation\x12\x0c\n\x04tags\x18\x01 \x03(\t\x12\x0f\n\x07summary\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12/\n\rexternal_docs\x18\x04 \x01(\x0b\x32\x18.openapi.v3.ExternalDocs\x12\x14\n\x0coperation_id\x18\x05 \x01(\t\x12\x34\n\nparameters\x18\x06 \x03(\x0b\x32 .openapi.v3.ParameterOrReference\x12\x38\n\x0crequest_body\x18\x07 \x01(\x0b\x32\".openapi.v3.RequestBodyOrReference\x12(\n\tresponses\x18\x08 \x01(\x0b\x32\x15.openapi.v3.Responses\x12\x34\n\tcallbacks\x18\t \x01(\x0b\x32!.openapi.v3.CallbacksOrReferences\x12\x12\n\ndeprecated\x18\n \x01(\x08\x12\x31\n\x08security\x18\x0b \x03(\x0b\x32\x1f.openapi.v3.SecurityRequirement\x12#\n\x07servers\x18\x0c \x03(\x0b\x32\x12.openapi.v3.Server\x12\x35\n\x17specification_extension\x18\r \x03(\x0b\x32\x14.openapi.v3.NamedAny\"\x98\x03\n\tParameter\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02in\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x10\n\x08required\x18\x04 \x01(\x08\x12\x12\n\ndeprecated\x18\x05 \x01(\x08\x12\x19\n\x11\x61llow_empty_value\x18\x06 \x01(\x08\x12\r\n\x05style\x18\x07 \x01(\t\x12\x0f\n\x07\x65xplode\x18\x08 \x01(\x08\x12\x16\n\x0e\x61llow_reserved\x18\t \x01(\x08\x12-\n\x06schema\x18\n \x01(\x0b\x32\x1d.openapi.v3.SchemaOrReference\x12 \n\x07\x65xample\x18\x0b \x01(\x0b\x32\x0f.openapi.v3.Any\x12\x32\n\x08\x65xamples\x18\x0c \x01(\x0b\x32 .openapi.v3.ExamplesOrReferences\x12\'\n\x07\x63ontent\x18\r \x01(\x0b\x32\x16.openapi.v3.MediaTypes\x12\x35\n\x17specification_extension\x18\x0e \x03(\x0b\x32\x14.openapi.v3.NamedAny\"w\n\x14ParameterOrReference\x12*\n\tparameter\x18\x01 \x01(\x0b\x32\x15.openapi.v3.ParameterH\x00\x12*\n\treference\x18\x02 \x01(\x0b\x32\x15.openapi.v3.ReferenceH\x00\x42\x07\n\x05oneof\"^\n\x16ParametersOrReferences\x12\x44\n\x15\x61\x64\x64itional_properties\x18\x01 \x03(\x0b\x32%.openapi.v3.NamedParameterOrReference\"\xfd\x03\n\x08PathItem\x12\x0c\n\x04_ref\x18\x01 \x01(\t\x12\x0f\n\x07summary\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\"\n\x03get\x18\x04 \x01(\x0b\x32\x15.openapi.v3.Operation\x12\"\n\x03put\x18\x05 \x01(\x0b\x32\x15.openapi.v3.Operation\x12#\n\x04post\x18\x06 \x01(\x0b\x32\x15.openapi.v3.Operation\x12%\n\x06\x64\x65lete\x18\x07 \x01(\x0b\x32\x15.openapi.v3.Operation\x12&\n\x07options\x18\x08 \x01(\x0b\x32\x15.openapi.v3.Operation\x12#\n\x04head\x18\t \x01(\x0b\x32\x15.openapi.v3.Operation\x12$\n\x05patch\x18\n \x01(\x0b\x32\x15.openapi.v3.Operation\x12$\n\x05trace\x18\x0b \x01(\x0b\x32\x15.openapi.v3.Operation\x12#\n\x07servers\x18\x0c \x03(\x0b\x32\x12.openapi.v3.Server\x12\x34\n\nparameters\x18\r \x03(\x0b\x32 .openapi.v3.ParameterOrReference\x12\x35\n\x17specification_extension\x18\x0e \x03(\x0b\x32\x14.openapi.v3.NamedAny\"g\n\x05Paths\x12\'\n\x04path\x18\x01 \x03(\x0b\x32\x19.openapi.v3.NamedPathItem\x12\x35\n\x17specification_extension\x18\x02 \x03(\x0b\x32\x14.openapi.v3.NamedAny\"O\n\nProperties\x12\x41\n\x15\x61\x64\x64itional_properties\x18\x01 \x03(\x0b\x32\".openapi.v3.NamedSchemaOrReference\"?\n\tReference\x12\x0c\n\x04_ref\x18\x01 \x01(\t\x12\x0f\n\x07summary\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\"c\n\x19RequestBodiesOrReferences\x12\x46\n\x15\x61\x64\x64itional_properties\x18\x01 \x03(\x0b\x32\'.openapi.v3.NamedRequestBodyOrReference\"\x94\x01\n\x0bRequestBody\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\'\n\x07\x63ontent\x18\x02 \x01(\x0b\x32\x16.openapi.v3.MediaTypes\x12\x10\n\x08required\x18\x03 \x01(\x08\x12\x35\n\x17specification_extension\x18\x04 \x03(\x0b\x32\x14.openapi.v3.NamedAny\"~\n\x16RequestBodyOrReference\x12/\n\x0crequest_body\x18\x01 \x01(\x0b\x32\x17.openapi.v3.RequestBodyH\x00\x12*\n\treference\x18\x02 \x01(\x0b\x32\x15.openapi.v3.ReferenceH\x00\x42\x07\n\x05oneof\"\xdf\x01\n\x08Response\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x30\n\x07headers\x18\x02 \x01(\x0b\x32\x1f.openapi.v3.HeadersOrReferences\x12\'\n\x07\x63ontent\x18\x03 \x01(\x0b\x32\x16.openapi.v3.MediaTypes\x12,\n\x05links\x18\x04 \x01(\x0b\x32\x1d.openapi.v3.LinksOrReferences\x12\x35\n\x17specification_extension\x18\x05 \x03(\x0b\x32\x14.openapi.v3.NamedAny\"t\n\x13ResponseOrReference\x12(\n\x08response\x18\x01 \x01(\x0b\x32\x14.openapi.v3.ResponseH\x00\x12*\n\treference\x18\x02 \x01(\x0b\x32\x15.openapi.v3.ReferenceH\x00\x42\x07\n\x05oneof\"\xb9\x01\n\tResponses\x12\x30\n\x07\x64\x65\x66\x61ult\x18\x01 \x01(\x0b\x32\x1f.openapi.v3.ResponseOrReference\x12\x43\n\x15response_or_reference\x18\x02 \x03(\x0b\x32$.openapi.v3.NamedResponseOrReference\x12\x35\n\x17specification_extension\x18\x03 \x03(\x0b\x32\x14.openapi.v3.NamedAny\"\\\n\x15ResponsesOrReferences\x12\x43\n\x15\x61\x64\x64itional_properties\x18\x01 \x03(\x0b\x32$.openapi.v3.NamedResponseOrReference\"\xa3\x08\n\x06Schema\x12\x10\n\x08nullable\x18\x01 \x01(\x08\x12\x30\n\rdiscriminator\x18\x02 \x01(\x0b\x32\x19.openapi.v3.Discriminator\x12\x11\n\tread_only\x18\x03 \x01(\x08\x12\x12\n\nwrite_only\x18\x04 \x01(\x08\x12\x1c\n\x03xml\x18\x05 \x01(\x0b\x32\x0f.openapi.v3.Xml\x12/\n\rexternal_docs\x18\x06 \x01(\x0b\x32\x18.openapi.v3.ExternalDocs\x12 \n\x07\x65xample\x18\x07 \x01(\x0b\x32\x0f.openapi.v3.Any\x12\x12\n\ndeprecated\x18\x08 \x01(\x08\x12\r\n\x05title\x18\t \x01(\t\x12\x13\n\x0bmultiple_of\x18\n \x01(\x01\x12\x0f\n\x07maximum\x18\x0b \x01(\x01\x12\x19\n\x11\x65xclusive_maximum\x18\x0c \x01(\x08\x12\x0f\n\x07minimum\x18\r \x01(\x01\x12\x19\n\x11\x65xclusive_minimum\x18\x0e \x01(\x08\x12\x12\n\nmax_length\x18\x0f \x01(\x03\x12\x12\n\nmin_length\x18\x10 \x01(\x03\x12\x0f\n\x07pattern\x18\x11 \x01(\t\x12\x11\n\tmax_items\x18\x12 \x01(\x03\x12\x11\n\tmin_items\x18\x13 \x01(\x03\x12\x14\n\x0cunique_items\x18\x14 \x01(\x08\x12\x16\n\x0emax_properties\x18\x15 \x01(\x03\x12\x16\n\x0emin_properties\x18\x16 \x01(\x03\x12\x10\n\x08required\x18\x17 \x03(\t\x12\x1d\n\x04\x65num\x18\x18 \x03(\x0b\x32\x0f.openapi.v3.Any\x12\x0c\n\x04type\x18\x19 \x01(\t\x12-\n\x06\x61ll_of\x18\x1a \x03(\x0b\x32\x1d.openapi.v3.SchemaOrReference\x12-\n\x06one_of\x18\x1b \x03(\x0b\x32\x1d.openapi.v3.SchemaOrReference\x12-\n\x06\x61ny_of\x18\x1c \x03(\x0b\x32\x1d.openapi.v3.SchemaOrReference\x12\x1f\n\x03not\x18\x1d \x01(\x0b\x32\x12.openapi.v3.Schema\x12$\n\x05items\x18\x1e \x01(\x0b\x32\x15.openapi.v3.ItemsItem\x12*\n\nproperties\x18\x1f \x01(\x0b\x32\x16.openapi.v3.Properties\x12\x43\n\x15\x61\x64\x64itional_properties\x18  \x01(\x0b\x32$.openapi.v3.AdditionalPropertiesItem\x12(\n\x07\x64\x65\x66\x61ult\x18! \x01(\x0b\x32\x17.openapi.v3.DefaultType\x12\x13\n\x0b\x64\x65scription\x18\" \x01(\t\x12\x0e\n\x06\x66ormat\x18# \x01(\t\x12\x35\n\x17specification_extension\x18$ \x03(\x0b\x32\x14.openapi.v3.NamedAny\"n\n\x11SchemaOrReference\x12$\n\x06schema\x18\x01 \x01(\x0b\x32\x12.openapi.v3.SchemaH\x00\x12*\n\treference\x18\x02 \x01(\x0b\x32\x15.openapi.v3.ReferenceH\x00\x42\x07\n\x05oneof\"X\n\x13SchemasOrReferences\x12\x41\n\x15\x61\x64\x64itional_properties\x18\x01 \x03(\x0b\x32\".openapi.v3.NamedSchemaOrReference\"R\n\x13SecurityRequirement\x12;\n\x15\x61\x64\x64itional_properties\x18\x01 \x03(\x0b\x32\x1c.openapi.v3.NamedStringArray\"\xef\x01\n\x0eSecurityScheme\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\n\n\x02in\x18\x04 \x01(\t\x12\x0e\n\x06scheme\x18\x05 \x01(\t\x12\x15\n\rbearer_format\x18\x06 \x01(\t\x12%\n\x05\x66lows\x18\x07 \x01(\x0b\x32\x16.openapi.v3.OauthFlows\x12\x1b\n\x13open_id_connect_url\x18\x08 \x01(\t\x12\x35\n\x17specification_extension\x18\t \x03(\x0b\x32\x14.openapi.v3.NamedAny\"\x87\x01\n\x19SecuritySchemeOrReference\x12\x35\n\x0fsecurity_scheme\x18\x01 \x01(\x0b\x32\x1a.openapi.v3.SecuritySchemeH\x00\x12*\n\treference\x18\x02 \x01(\x0b\x32\x15.openapi.v3.ReferenceH\x00\x42\x07\n\x05oneof\"h\n\x1bSecuritySchemesOrReferences\x12I\n\x15\x61\x64\x64itional_properties\x18\x01 \x03(\x0b\x32*.openapi.v3.NamedSecuritySchemeOrReference\"\x91\x01\n\x06Server\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12.\n\tvariables\x18\x03 \x01(\x0b\x32\x1b.openapi.v3.ServerVariables\x12\x35\n\x17specification_extension\x18\x04 \x03(\x0b\x32\x14.openapi.v3.NamedAny\"{\n\x0eServerVariable\x12\x0c\n\x04\x65num\x18\x01 \x03(\t\x12\x0f\n\x07\x64\x65\x66\x61ult\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x35\n\x17specification_extension\x18\x04 \x03(\x0b\x32\x14.openapi.v3.NamedAny\"Q\n\x0fServerVariables\x12>\n\x15\x61\x64\x64itional_properties\x18\x01 \x03(\x0b\x32\x1f.openapi.v3.NamedServerVariable\"X\n\x16SpecificationExtension\x12\x10\n\x06number\x18\x01 \x01(\x01H\x00\x12\x11\n\x07\x62oolean\x18\x02 \x01(\x08H\x00\x12\x10\n\x06string\x18\x03 \x01(\tH\x00\x42\x07\n\x05oneof\"\x1c\n\x0bStringArray\x12\r\n\x05value\x18\x01 \x03(\t\"A\n\x07Strings\x12\x36\n\x15\x61\x64\x64itional_properties\x18\x01 \x03(\x0b\x32\x17.openapi.v3.NamedString\"\x90\x01\n\x03Tag\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12/\n\rexternal_docs\x18\x03 \x01(\x0b\x32\x18.openapi.v3.ExternalDocs\x12\x35\n\x17specification_extension\x18\x04 \x03(\x0b\x32\x14.openapi.v3.NamedAny\"\x91\x01\n\x03Xml\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tnamespace\x18\x02 \x01(\t\x12\x0e\n\x06prefix\x18\x03 \x01(\t\x12\x11\n\tattribute\x18\x04 \x01(\x08\x12\x0f\n\x07wrapped\x18\x05 \x01(\x08\x12\x35\n\x17specification_extension\x18\x06 \x03(\x0b\x32\x14.openapi.v3.NamedAnyBc\n\x0eorg.openapi_v3B\x0cOpenAPIProtoP\x01Z.github.com/google/gnostic/openapiv3;openapi_v3\xa2\x02\x03OAS\xaa\x02\nopenapi.v3b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'openapiv3.OpenAPIv3_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\016org.openapi_v3B\014OpenAPIProtoP\001Z.github.com/google/gnostic/openapiv3;openapi_v3\242\002\003OAS\252\002\nopenapi.v3'
  _globals['_ADDITIONALPROPERTIESITEM']._serialized_start=68
  _globals['_ADDITIONALPROPERTIESITEM']._serialized_end=184
  _globals['_ANY']._serialized_start=186
  _globals['_ANY']._serialized_end=242
  _globals['_ANYOREXPRESSION']._serialized_start=244
  _globals['_ANYOREXPRESSION']._serialized_end=348
  _globals['_CALLBACK']._serialized_start=350
  _globals['_CALLBACK']._serialized_end=456
  _globals['_CALLBACKORREFERENCE']._serialized_start=458
  _globals['_CALLBACKORREFERENCE']._serialized_end=574
  _globals['_CALLBACKSORREFERENCES']._serialized_start=576
  _globals['_CALLBACKSORREFERENCES']._serialized_end=668
  _globals['_COMPONENTS']._serialized_start=671
  _globals['_COMPONENTS']._serialized_end=1230
  _globals['_CONTACT']._serialized_start=1232
  _globals['_CONTACT']._serialized_end=1338
  _globals['_DEFAULTTYPE']._serialized_start=1340
  _globals['_DEFAULTTYPE']._serialized_end=1417
  _globals['_DISCRIMINATOR']._serialized_start=1420
  _globals['_DISCRIMINATOR']._serialized_end=1551
  _globals['_DOCUMENT']._serialized_start=1554
  _globals['_DOCUMENT']._serialized_end=1914
  _globals['_ENCODING']._serialized_start=1917
  _globals['_ENCODING']._serialized_end=2110
  _globals['_ENCODINGS']._serialized_start=2112
  _globals['_ENCODINGS']._serialized_end=2181
  _globals['_EXAMPLE']._serialized_start=2184
  _globals['_EXAMPLE']._serialized_end=2342
  _globals['_EXAMPLEORREFERENCE']._serialized_start=2344
  _globals['_EXAMPLEORREFERENCE']._serialized_end=2457
  _globals['_EXAMPLESORREFERENCES']._serialized_start=2459
  _globals['_EXAMPLESORREFERENCES']._serialized_end=2549
  _globals['_EXPRESSION']._serialized_start=2551
  _globals['_EXPRESSION']._serialized_end=2616
  _globals['_EXTERNALDOCS']._serialized_start=2618
  _globals['_EXTERNALDOCS']._serialized_end=2721
  _globals['_HEADER']._serialized_start=2724
  _globals['_HEADER']._serialized_end=3103
  _globals['_HEADERORREFERENCE']._serialized_start=3105
  _globals['_HEADERORREFERENCE']._serialized_end=3215
  _globals['_HEADERSORREFERENCES']._serialized_start=3217
  _globals['_HEADERSORREFERENCES']._serialized_end=3305
  _globals['_INFO']._serialized_start=3308
  _globals['_INFO']._serialized_end=3541
  _globals['_ITEMSITEM']._serialized_start=3543
  _globals['_ITEMSITEM']._serialized_end=3614
  _globals['_LICENSE']._serialized_start=3616
  _globals['_LICENSE']._serialized_end=3707
  _globals['_LINK']._serialized_start=3710
  _globals['_LINK']._serialized_end=3973
  _globals['_LINKORREFERENCE']._serialized_start=3975
  _globals['_LINKORREFERENCE']._serialized_end=4079
  _globals['_LINKSORREFERENCES']._serialized_start=4081
  _globals['_LINKSORREFERENCES']._serialized_end=4165
  _globals['_MEDIATYPE']._serialized_start=4168
  _globals['_MEDIATYPE']._serialized_end=4408
  _globals['_MEDIATYPES']._serialized_start=4410
  _globals['_MEDIATYPES']._serialized_end=4481
  _globals['_NAMEDANY']._serialized_start=4483
  _globals['_NAMEDANY']._serialized_end=4539
  _globals['_NAMEDCALLBACKORREFERENCE']._serialized_start=4541
  _globals['_NAMEDCALLBACKORREFERENCE']._serialized_end=4629
  _globals['_NAMEDENCODING']._serialized_start=4631
  _globals['_NAMEDENCODING']._serialized_end=4697
  _globals['_NAMEDEXAMPLEORREFERENCE']._serialized_start=4699
  _globals['_NAMEDEXAMPLEORREFERENCE']._serialized_end=4785
  _globals['_NAMEDHEADERORREFERENCE']._serialized_start=4787
  _globals['_NAMEDHEADERORREFERENCE']._serialized_end=4871
  _globals['_NAMEDLINKORREFERENCE']._serialized_start=4873
  _globals['_NAMEDLINKORREFERENCE']._serialized_end=4953
  _globals['_NAMEDMEDIATYPE']._serialized_start=4955
  _globals['_NAMEDMEDIATYPE']._serialized_end=5023
  _globals['_NAMEDPARAMETERORREFERENCE']._serialized_start=5025
  _globals['_NAMEDPARAMETERORREFERENCE']._serialized_end=5115
  _globals['_NAMEDPATHITEM']._serialized_start=5117
  _globals['_NAMEDPATHITEM']._serialized_end=5183
  _globals['_NAMEDREQUESTBODYORREFERENCE']._serialized_start=5185
  _globals['_NAMEDREQUESTBODYORREFERENCE']._serialized_end=5279
  _globals['_NAMEDRESPONSEORREFERENCE']._serialized_start=5281
  _globals['_NAMEDRESPONSEORREFERENCE']._serialized_end=5369
  _globals['_NAMEDSCHEMAORREFERENCE']._serialized_start=5371
  _globals['_NAMEDSCHEMAORREFERENCE']._serialized_end=5455
  _globals['_NAMEDSECURITYSCHEMEORREFERENCE']._serialized_start=5457
  _globals['_NAMEDSECURITYSCHEMEORREFERENCE']._serialized_end=5557
  _globals['_NAMEDSERVERVARIABLE']._serialized_start=5559
  _globals['_NAMEDSERVERVARIABLE']._serialized_end=5637
  _globals['_NAMEDSTRING']._serialized_start=5639
  _globals['_NAMEDSTRING']._serialized_end=5681
  _globals['_NAMEDSTRINGARRAY']._serialized_start=5683
  _globals['_NAMEDSTRINGARRAY']._serialized_end=5755
  _globals['_OAUTHFLOW']._serialized_start=5758
  _globals['_OAUTHFLOW']._serialized_end=5928
  _globals['_OAUTHFLOWS']._serialized_start=5931
  _globals['_OAUTHFLOWS']._serialized_end=6182
  _globals['_OBJECT']._serialized_start=6184
  _globals['_OBJECT']._serialized_end=6245
  _globals['_OPERATION']._serialized_start=6248
  _globals['_OPERATION']._serialized_end=6753
  _globals['_PARAMETER']._serialized_start=6756
  _globals['_PARAMETER']._serialized_end=7164
  _globals['_PARAMETERORREFERENCE']._serialized_start=7166
  _globals['_PARAMETERORREFERENCE']._serialized_end=7285
  _globals['_PARAMETERSORREFERENCES']._serialized_start=7287
  _globals['_PARAMETERSORREFERENCES']._serialized_end=7381
  _globals['_PATHITEM']._serialized_start=7384
  _globals['_PATHITEM']._serialized_end=7893
  _globals['_PATHS']._serialized_start=7895
  _globals['_PATHS']._serialized_end=7998
  _globals['_PROPERTIES']._serialized_start=8000
  _globals['_PROPERTIES']._serialized_end=8079
  _globals['_REFERENCE']._serialized_start=8081
  _globals['_REFERENCE']._serialized_end=8144
  _globals['_REQUESTBODIESORREFERENCES']._serialized_start=8146
  _globals['_REQUESTBODIESORREFERENCES']._serialized_end=8245
  _globals['_REQUESTBODY']._serialized_start=8248
  _globals['_REQUESTBODY']._serialized_end=8396
  _globals['_REQUESTBODYORREFERENCE']._serialized_start=8398
  _globals['_REQUESTBODYORREFERENCE']._serialized_end=8524
  _globals['_RESPONSE']._serialized_start=8527
  _globals['_RESPONSE']._serialized_end=8750
  _globals['_RESPONSEORREFERENCE']._serialized_start=8752
  _globals['_RESPONSEORREFERENCE']._serialized_end=8868
  _globals['_RESPONSES']._serialized_start=8871
  _globals['_RESPONSES']._serialized_end=9056
  _globals['_RESPONSESORREFERENCES']._serialized_start=9058
  _globals['_RESPONSESORREFERENCES']._serialized_end=9150
  _globals['_SCHEMA']._serialized_start=9153
  _globals['_SCHEMA']._serialized_end=10212
  _globals['_SCHEMAORREFERENCE']._serialized_start=10214
  _globals['_SCHEMAORREFERENCE']._serialized_end=10324
  _globals['_SCHEMASORREFERENCES']._serialized_start=10326
  _globals['_SCHEMASORREFERENCES']._serialized_end=10414
  _globals['_SECURITYREQUIREMENT']._serialized_start=10416
  _globals['_SECURITYREQUIREMENT']._serialized_end=10498
  _globals['_SECURITYSCHEME']._serialized_start=10501
  _globals['_SECURITYSCHEME']._serialized_end=10740
  _globals['_SECURITYSCHEMEORREFERENCE']._serialized_start=10743
  _globals['_SECURITYSCHEMEORREFERENCE']._serialized_end=10878
  _globals['_SECURITYSCHEMESORREFERENCES']._serialized_start=10880
  _globals['_SECURITYSCHEMESORREFERENCES']._serialized_end=10984
  _globals['_SERVER']._serialized_start=10987
  _globals['_SERVER']._serialized_end=11132
  _globals['_SERVERVARIABLE']._serialized_start=11134
  _globals['_SERVERVARIABLE']._serialized_end=11257
  _globals['_SERVERVARIABLES']._serialized_start=11259
  _globals['_SERVERVARIABLES']._serialized_end=11340
  _globals['_SPECIFICATIONEXTENSION']._serialized_start=11342
  _globals['_SPECIFICATIONEXTENSION']._serialized_end=11430
  _globals['_STRINGARRAY']._serialized_start=11432
  _globals['_STRINGARRAY']._serialized_end=11460
  _globals['_STRINGS']._serialized_start=11462
  _globals['_STRINGS']._serialized_end=11527
  _globals['_TAG']._serialized_start=11530
  _globals['_TAG']._serialized_end=11674
  _globals['_XML']._serialized_start=11677
  _globals['_XML']._serialized_end=11822
# @@protoc_insertion_point(module_scope)
