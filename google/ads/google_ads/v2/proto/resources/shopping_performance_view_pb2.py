# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v2/proto/resources/shopping_performance_view.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v2/proto/resources/shopping_performance_view.proto',
  package='google.ads.googleads.v2.resources',
  syntax='proto3',
  serialized_options=_b('\n%com.google.ads.googleads.v2.resourcesB\034ShoppingPerformanceViewProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v2/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V2.Resources\312\002!Google\\Ads\\GoogleAds\\V2\\Resources\352\002%Google::Ads::GoogleAds::V2::Resources'),
  serialized_pb=_b('\nGgoogle/ads/googleads_v2/proto/resources/shopping_performance_view.proto\x12!google.ads.googleads.v2.resources\x1a\x1cgoogle/api/annotations.proto\"0\n\x17ShoppingPerformanceView\x12\x15\n\rresource_name\x18\x01 \x01(\tB\x89\x02\n%com.google.ads.googleads.v2.resourcesB\x1cShoppingPerformanceViewProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v2/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V2.Resources\xca\x02!Google\\Ads\\GoogleAds\\V2\\Resources\xea\x02%Google::Ads::GoogleAds::V2::Resourcesb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_SHOPPINGPERFORMANCEVIEW = _descriptor.Descriptor(
  name='ShoppingPerformanceView',
  full_name='google.ads.googleads.v2.resources.ShoppingPerformanceView',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v2.resources.ShoppingPerformanceView.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=140,
  serialized_end=188,
)

DESCRIPTOR.message_types_by_name['ShoppingPerformanceView'] = _SHOPPINGPERFORMANCEVIEW
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ShoppingPerformanceView = _reflection.GeneratedProtocolMessageType('ShoppingPerformanceView', (_message.Message,), dict(
  DESCRIPTOR = _SHOPPINGPERFORMANCEVIEW,
  __module__ = 'google.ads.googleads_v2.proto.resources.shopping_performance_view_pb2'
  ,
  __doc__ = """Shopping performance view. Provides Shopping campaign statistics
  aggregated at several product dimension levels. Product dimension values
  from Merchant Center such as brand, category, custom attributes, product
  condition and product type will reflect the state of each dimension as
  of the date and time when the corresponding event was recorded.
  
  
  Attributes:
      resource_name:
          The resource name of the Shopping performance view. Shopping
          performance view resource names have the form:
          ``customers/{customer_id}/shoppingPerformanceView``
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.resources.ShoppingPerformanceView)
  ))
_sym_db.RegisterMessage(ShoppingPerformanceView)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)