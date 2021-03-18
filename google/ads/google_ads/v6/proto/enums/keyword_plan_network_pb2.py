# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v6/enums/keyword_plan_network.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v6/enums/keyword_plan_network.proto',
  package='google.ads.googleads.v6.enums',
  syntax='proto3',
  serialized_options=b'\n!com.google.ads.googleads.v6.enumsB\027KeywordPlanNetworkProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v6/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V6.Enums\312\002\035Google\\Ads\\GoogleAds\\V6\\Enums\352\002!Google::Ads::GoogleAds::V6::Enums',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n8google/ads/googleads/v6/enums/keyword_plan_network.proto\x12\x1dgoogle.ads.googleads.v6.enums\x1a\x1cgoogle/api/annotations.proto\"\x7f\n\x16KeywordPlanNetworkEnum\"e\n\x12KeywordPlanNetwork\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x11\n\rGOOGLE_SEARCH\x10\x02\x12\x1e\n\x1aGOOGLE_SEARCH_AND_PARTNERS\x10\x03\x42\xec\x01\n!com.google.ads.googleads.v6.enumsB\x17KeywordPlanNetworkProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v6/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V6.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V6\\Enums\xea\x02!Google::Ads::GoogleAds::V6::Enumsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_KEYWORDPLANNETWORKENUM_KEYWORDPLANNETWORK = _descriptor.EnumDescriptor(
  name='KeywordPlanNetwork',
  full_name='google.ads.googleads.v6.enums.KeywordPlanNetworkEnum.KeywordPlanNetwork',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GOOGLE_SEARCH', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GOOGLE_SEARCH_AND_PARTNERS', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=147,
  serialized_end=248,
)
_sym_db.RegisterEnumDescriptor(_KEYWORDPLANNETWORKENUM_KEYWORDPLANNETWORK)


_KEYWORDPLANNETWORKENUM = _descriptor.Descriptor(
  name='KeywordPlanNetworkEnum',
  full_name='google.ads.googleads.v6.enums.KeywordPlanNetworkEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _KEYWORDPLANNETWORKENUM_KEYWORDPLANNETWORK,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=121,
  serialized_end=248,
)

_KEYWORDPLANNETWORKENUM_KEYWORDPLANNETWORK.containing_type = _KEYWORDPLANNETWORKENUM
DESCRIPTOR.message_types_by_name['KeywordPlanNetworkEnum'] = _KEYWORDPLANNETWORKENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

KeywordPlanNetworkEnum = _reflection.GeneratedProtocolMessageType('KeywordPlanNetworkEnum', (_message.Message,), {
  'DESCRIPTOR' : _KEYWORDPLANNETWORKENUM,
  '__module__' : 'google.ads.googleads.v6.enums.keyword_plan_network_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.enums.KeywordPlanNetworkEnum)
  })
_sym_db.RegisterMessage(KeywordPlanNetworkEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)