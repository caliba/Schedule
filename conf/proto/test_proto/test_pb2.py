# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='test.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\ntest.proto\"2\n\tTimestamp\x12\x0f\n\x07seconds\x18\x01 \x01(\x03\x12\x14\n\x0cmicroseconds\x18\x02 \x01(\x05\"\xac\x01\n\x0b\x43\x32\x46_Request\x12\x12\n\nrequest_id\x18\x01 \x01(\x05\x12!\n\x05image\x18\x02 \x01(\x0b\x32\x12.C2F_Request.Image\x12\x1d\n\ttimestamp\x18\x03 \x01(\x0b\x32\n.Timestamp\x12\x0b\n\x03log\x18\x04 \x01(\t\x1a:\n\x05Image\x12\x0e\n\x06height\x18\x01 \x01(\x05\x12\r\n\x05width\x18\x02 \x01(\x05\x12\x12\n\nbyte_image\x18\x03 \x01(\x0c\"\x1c\n\x0c\x43\x32\x46_Response\x12\x0c\n\x04\x66lag\x18\x01 \x01(\x08\"\xbf\x01\n\x0b\x46\x32S_Request\x12\x12\n\nrequest_id\x18\x01 \x01(\x05\x12\x0c\n\x04size\x18\x02 \x01(\x05\x12\x35\n\x0f\x66rontendmessage\x18\x03 \x03(\x0b\x32\x1c.F2S_Request.FrontendMessage\x1aW\n\x0f\x46rontendMessage\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\n\n\x02id\x18\x02 \x01(\x05\x12\x0b\n\x03log\x18\x03 \x01(\t\x12\x1d\n\ttimestamp\x18\x04 \x03(\x0b\x32\n.Timestamp\"\x1c\n\x0c\x46\x32S_Response\x12\x0c\n\x04\x66lag\x18\x01 \x01(\x08\"\xad\x01\n\x0bS2C_Request\x12\x12\n\nrequest_id\x18\x01 \x01(\x05\x12\x31\n\rservermessage\x18\x02 \x03(\x0b\x32\x1a.S2C_Request.ServerMessage\x1aW\n\rServerMessage\x12\r\n\x05index\x18\x01 \x01(\x05\x12\x0b\n\x03res\x18\x02 \x01(\t\x12\x0b\n\x03log\x18\x03 \x01(\t\x12\x1d\n\ttimestamp\x18\x04 \x03(\x0b\x32\n.Timestamp\"\x1c\n\x0cS2C_Response\x12\x0c\n\x04\x66lag\x18\x01 \x01(\x08\",\n\rSetup_Request\x12\x0c\n\x04port\x18\x01 \x01(\t\x12\r\n\x05\x62\x61tch\x18\x02 \x01(\x05\"+\n\x0eSetup_Response\x12\x0c\n\x04\x66lag\x18\x01 \x01(\x08\x12\x0b\n\x03slo\x18\x02 \x01(\x05\"!\n\x0b\x46\x32\x44_Request\x12\x12\n\nthroughput\x18\x01 \x01(\x05\"\x1c\n\x0c\x46\x32\x44_Response\x12\x0c\n\x04\x66lag\x18\x01 \x01(\x08\"G\n\x0bS2D_Request\x12\x12\n\nthroughput\x18\x01 \x01(\x05\x12\x16\n\x0emax_throughput\x18\x02 \x01(\x05\x12\x0c\n\x04port\x18\x03 \x01(\t\"\x1c\n\x0cS2D_Response\x12\x0c\n\x04\x66lag\x18\x01 \x01(\x08\x32\x32\n\x03\x43\x32\x46\x12+\n\nC2F_getmsg\x12\x0c.C2F_Request\x1a\r.C2F_Response\"\x00\x32\x32\n\x03\x46\x32S\x12+\n\nF2S_getmsg\x12\x0c.F2S_Request\x1a\r.F2S_Response\"\x00\x32\x32\n\x03S2C\x12+\n\nS2C_getmsg\x12\x0c.S2C_Request\x1a\r.S2C_Response\"\x00\x32:\n\x05Setup\x12\x31\n\x0cSetup_getmsg\x12\x0e.Setup_Request\x1a\x0f.Setup_Response\"\x00\x32\x32\n\x03\x46\x32\x44\x12+\n\nF2D_getmsg\x12\x0c.F2D_Request\x1a\r.F2D_Response\"\x00\x32\x32\n\x03S2D\x12+\n\nS2D_getmsg\x12\x0c.S2D_Request\x1a\r.S2D_Response\"\x00\x62\x06proto3'
)




_TIMESTAMP = _descriptor.Descriptor(
  name='Timestamp',
  full_name='Timestamp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='seconds', full_name='Timestamp.seconds', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='microseconds', full_name='Timestamp.microseconds', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=14,
  serialized_end=64,
)


_C2F_REQUEST_IMAGE = _descriptor.Descriptor(
  name='Image',
  full_name='C2F_Request.Image',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='height', full_name='C2F_Request.Image.height', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='width', full_name='C2F_Request.Image.width', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='byte_image', full_name='C2F_Request.Image.byte_image', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=181,
  serialized_end=239,
)

_C2F_REQUEST = _descriptor.Descriptor(
  name='C2F_Request',
  full_name='C2F_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_id', full_name='C2F_Request.request_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='image', full_name='C2F_Request.image', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='C2F_Request.timestamp', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='log', full_name='C2F_Request.log', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_C2F_REQUEST_IMAGE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=67,
  serialized_end=239,
)


_C2F_RESPONSE = _descriptor.Descriptor(
  name='C2F_Response',
  full_name='C2F_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='flag', full_name='C2F_Response.flag', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=241,
  serialized_end=269,
)


_F2S_REQUEST_FRONTENDMESSAGE = _descriptor.Descriptor(
  name='FrontendMessage',
  full_name='F2S_Request.FrontendMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='F2S_Request.FrontendMessage.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='F2S_Request.FrontendMessage.id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='log', full_name='F2S_Request.FrontendMessage.log', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='F2S_Request.FrontendMessage.timestamp', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=376,
  serialized_end=463,
)

_F2S_REQUEST = _descriptor.Descriptor(
  name='F2S_Request',
  full_name='F2S_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_id', full_name='F2S_Request.request_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='size', full_name='F2S_Request.size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='frontendmessage', full_name='F2S_Request.frontendmessage', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_F2S_REQUEST_FRONTENDMESSAGE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=272,
  serialized_end=463,
)


_F2S_RESPONSE = _descriptor.Descriptor(
  name='F2S_Response',
  full_name='F2S_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='flag', full_name='F2S_Response.flag', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=465,
  serialized_end=493,
)


_S2C_REQUEST_SERVERMESSAGE = _descriptor.Descriptor(
  name='ServerMessage',
  full_name='S2C_Request.ServerMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='index', full_name='S2C_Request.ServerMessage.index', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='res', full_name='S2C_Request.ServerMessage.res', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='log', full_name='S2C_Request.ServerMessage.log', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='S2C_Request.ServerMessage.timestamp', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=582,
  serialized_end=669,
)

_S2C_REQUEST = _descriptor.Descriptor(
  name='S2C_Request',
  full_name='S2C_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_id', full_name='S2C_Request.request_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='servermessage', full_name='S2C_Request.servermessage', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_S2C_REQUEST_SERVERMESSAGE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=496,
  serialized_end=669,
)


_S2C_RESPONSE = _descriptor.Descriptor(
  name='S2C_Response',
  full_name='S2C_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='flag', full_name='S2C_Response.flag', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=671,
  serialized_end=699,
)


_SETUP_REQUEST = _descriptor.Descriptor(
  name='Setup_Request',
  full_name='Setup_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='port', full_name='Setup_Request.port', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='batch', full_name='Setup_Request.batch', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=701,
  serialized_end=745,
)


_SETUP_RESPONSE = _descriptor.Descriptor(
  name='Setup_Response',
  full_name='Setup_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='flag', full_name='Setup_Response.flag', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='slo', full_name='Setup_Response.slo', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=747,
  serialized_end=790,
)


_F2D_REQUEST = _descriptor.Descriptor(
  name='F2D_Request',
  full_name='F2D_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='throughput', full_name='F2D_Request.throughput', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=792,
  serialized_end=825,
)


_F2D_RESPONSE = _descriptor.Descriptor(
  name='F2D_Response',
  full_name='F2D_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='flag', full_name='F2D_Response.flag', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=827,
  serialized_end=855,
)


_S2D_REQUEST = _descriptor.Descriptor(
  name='S2D_Request',
  full_name='S2D_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='throughput', full_name='S2D_Request.throughput', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_throughput', full_name='S2D_Request.max_throughput', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='port', full_name='S2D_Request.port', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=857,
  serialized_end=928,
)


_S2D_RESPONSE = _descriptor.Descriptor(
  name='S2D_Response',
  full_name='S2D_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='flag', full_name='S2D_Response.flag', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=930,
  serialized_end=958,
)

_C2F_REQUEST_IMAGE.containing_type = _C2F_REQUEST
_C2F_REQUEST.fields_by_name['image'].message_type = _C2F_REQUEST_IMAGE
_C2F_REQUEST.fields_by_name['timestamp'].message_type = _TIMESTAMP
_F2S_REQUEST_FRONTENDMESSAGE.fields_by_name['timestamp'].message_type = _TIMESTAMP
_F2S_REQUEST_FRONTENDMESSAGE.containing_type = _F2S_REQUEST
_F2S_REQUEST.fields_by_name['frontendmessage'].message_type = _F2S_REQUEST_FRONTENDMESSAGE
_S2C_REQUEST_SERVERMESSAGE.fields_by_name['timestamp'].message_type = _TIMESTAMP
_S2C_REQUEST_SERVERMESSAGE.containing_type = _S2C_REQUEST
_S2C_REQUEST.fields_by_name['servermessage'].message_type = _S2C_REQUEST_SERVERMESSAGE
DESCRIPTOR.message_types_by_name['Timestamp'] = _TIMESTAMP
DESCRIPTOR.message_types_by_name['C2F_Request'] = _C2F_REQUEST
DESCRIPTOR.message_types_by_name['C2F_Response'] = _C2F_RESPONSE
DESCRIPTOR.message_types_by_name['F2S_Request'] = _F2S_REQUEST
DESCRIPTOR.message_types_by_name['F2S_Response'] = _F2S_RESPONSE
DESCRIPTOR.message_types_by_name['S2C_Request'] = _S2C_REQUEST
DESCRIPTOR.message_types_by_name['S2C_Response'] = _S2C_RESPONSE
DESCRIPTOR.message_types_by_name['Setup_Request'] = _SETUP_REQUEST
DESCRIPTOR.message_types_by_name['Setup_Response'] = _SETUP_RESPONSE
DESCRIPTOR.message_types_by_name['F2D_Request'] = _F2D_REQUEST
DESCRIPTOR.message_types_by_name['F2D_Response'] = _F2D_RESPONSE
DESCRIPTOR.message_types_by_name['S2D_Request'] = _S2D_REQUEST
DESCRIPTOR.message_types_by_name['S2D_Response'] = _S2D_RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Timestamp = _reflection.GeneratedProtocolMessageType('Timestamp', (_message.Message,), {
  'DESCRIPTOR' : _TIMESTAMP,
  '__module__' : 'test_pb2'
  # @@protoc_insertion_point(class_scope:Timestamp)
  })
_sym_db.RegisterMessage(Timestamp)

C2F_Request = _reflection.GeneratedProtocolMessageType('C2F_Request', (_message.Message,), {

  'Image' : _reflection.GeneratedProtocolMessageType('Image', (_message.Message,), {
    'DESCRIPTOR' : _C2F_REQUEST_IMAGE,
    '__module__' : 'test_pb2'
    # @@protoc_insertion_point(class_scope:C2F_Request.Image)
    })
  ,
  'DESCRIPTOR' : _C2F_REQUEST,
  '__module__' : 'test_pb2'
  # @@protoc_insertion_point(class_scope:C2F_Request)
  })
_sym_db.RegisterMessage(C2F_Request)
_sym_db.RegisterMessage(C2F_Request.Image)

C2F_Response = _reflection.GeneratedProtocolMessageType('C2F_Response', (_message.Message,), {
  'DESCRIPTOR' : _C2F_RESPONSE,
  '__module__' : 'test_pb2'
  # @@protoc_insertion_point(class_scope:C2F_Response)
  })
_sym_db.RegisterMessage(C2F_Response)

F2S_Request = _reflection.GeneratedProtocolMessageType('F2S_Request', (_message.Message,), {

  'FrontendMessage' : _reflection.GeneratedProtocolMessageType('FrontendMessage', (_message.Message,), {
    'DESCRIPTOR' : _F2S_REQUEST_FRONTENDMESSAGE,
    '__module__' : 'test_pb2'
    # @@protoc_insertion_point(class_scope:F2S_Request.FrontendMessage)
    })
  ,
  'DESCRIPTOR' : _F2S_REQUEST,
  '__module__' : 'test_pb2'
  # @@protoc_insertion_point(class_scope:F2S_Request)
  })
_sym_db.RegisterMessage(F2S_Request)
_sym_db.RegisterMessage(F2S_Request.FrontendMessage)

F2S_Response = _reflection.GeneratedProtocolMessageType('F2S_Response', (_message.Message,), {
  'DESCRIPTOR' : _F2S_RESPONSE,
  '__module__' : 'test_pb2'
  # @@protoc_insertion_point(class_scope:F2S_Response)
  })
_sym_db.RegisterMessage(F2S_Response)

S2C_Request = _reflection.GeneratedProtocolMessageType('S2C_Request', (_message.Message,), {

  'ServerMessage' : _reflection.GeneratedProtocolMessageType('ServerMessage', (_message.Message,), {
    'DESCRIPTOR' : _S2C_REQUEST_SERVERMESSAGE,
    '__module__' : 'test_pb2'
    # @@protoc_insertion_point(class_scope:S2C_Request.ServerMessage)
    })
  ,
  'DESCRIPTOR' : _S2C_REQUEST,
  '__module__' : 'test_pb2'
  # @@protoc_insertion_point(class_scope:S2C_Request)
  })
_sym_db.RegisterMessage(S2C_Request)
_sym_db.RegisterMessage(S2C_Request.ServerMessage)

S2C_Response = _reflection.GeneratedProtocolMessageType('S2C_Response', (_message.Message,), {
  'DESCRIPTOR' : _S2C_RESPONSE,
  '__module__' : 'test_pb2'
  # @@protoc_insertion_point(class_scope:S2C_Response)
  })
_sym_db.RegisterMessage(S2C_Response)

Setup_Request = _reflection.GeneratedProtocolMessageType('Setup_Request', (_message.Message,), {
  'DESCRIPTOR' : _SETUP_REQUEST,
  '__module__' : 'test_pb2'
  # @@protoc_insertion_point(class_scope:Setup_Request)
  })
_sym_db.RegisterMessage(Setup_Request)

Setup_Response = _reflection.GeneratedProtocolMessageType('Setup_Response', (_message.Message,), {
  'DESCRIPTOR' : _SETUP_RESPONSE,
  '__module__' : 'test_pb2'
  # @@protoc_insertion_point(class_scope:Setup_Response)
  })
_sym_db.RegisterMessage(Setup_Response)

F2D_Request = _reflection.GeneratedProtocolMessageType('F2D_Request', (_message.Message,), {
  'DESCRIPTOR' : _F2D_REQUEST,
  '__module__' : 'test_pb2'
  # @@protoc_insertion_point(class_scope:F2D_Request)
  })
_sym_db.RegisterMessage(F2D_Request)

F2D_Response = _reflection.GeneratedProtocolMessageType('F2D_Response', (_message.Message,), {
  'DESCRIPTOR' : _F2D_RESPONSE,
  '__module__' : 'test_pb2'
  # @@protoc_insertion_point(class_scope:F2D_Response)
  })
_sym_db.RegisterMessage(F2D_Response)

S2D_Request = _reflection.GeneratedProtocolMessageType('S2D_Request', (_message.Message,), {
  'DESCRIPTOR' : _S2D_REQUEST,
  '__module__' : 'test_pb2'
  # @@protoc_insertion_point(class_scope:S2D_Request)
  })
_sym_db.RegisterMessage(S2D_Request)

S2D_Response = _reflection.GeneratedProtocolMessageType('S2D_Response', (_message.Message,), {
  'DESCRIPTOR' : _S2D_RESPONSE,
  '__module__' : 'test_pb2'
  # @@protoc_insertion_point(class_scope:S2D_Response)
  })
_sym_db.RegisterMessage(S2D_Response)



_C2F = _descriptor.ServiceDescriptor(
  name='C2F',
  full_name='C2F',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=960,
  serialized_end=1010,
  methods=[
  _descriptor.MethodDescriptor(
    name='C2F_getmsg',
    full_name='C2F.C2F_getmsg',
    index=0,
    containing_service=None,
    input_type=_C2F_REQUEST,
    output_type=_C2F_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_C2F)

DESCRIPTOR.services_by_name['C2F'] = _C2F


_F2S = _descriptor.ServiceDescriptor(
  name='F2S',
  full_name='F2S',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1012,
  serialized_end=1062,
  methods=[
  _descriptor.MethodDescriptor(
    name='F2S_getmsg',
    full_name='F2S.F2S_getmsg',
    index=0,
    containing_service=None,
    input_type=_F2S_REQUEST,
    output_type=_F2S_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_F2S)

DESCRIPTOR.services_by_name['F2S'] = _F2S


_S2C = _descriptor.ServiceDescriptor(
  name='S2C',
  full_name='S2C',
  file=DESCRIPTOR,
  index=2,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1064,
  serialized_end=1114,
  methods=[
  _descriptor.MethodDescriptor(
    name='S2C_getmsg',
    full_name='S2C.S2C_getmsg',
    index=0,
    containing_service=None,
    input_type=_S2C_REQUEST,
    output_type=_S2C_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_S2C)

DESCRIPTOR.services_by_name['S2C'] = _S2C


_SETUP = _descriptor.ServiceDescriptor(
  name='Setup',
  full_name='Setup',
  file=DESCRIPTOR,
  index=3,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1116,
  serialized_end=1174,
  methods=[
  _descriptor.MethodDescriptor(
    name='Setup_getmsg',
    full_name='Setup.Setup_getmsg',
    index=0,
    containing_service=None,
    input_type=_SETUP_REQUEST,
    output_type=_SETUP_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SETUP)

DESCRIPTOR.services_by_name['Setup'] = _SETUP


_F2D = _descriptor.ServiceDescriptor(
  name='F2D',
  full_name='F2D',
  file=DESCRIPTOR,
  index=4,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1176,
  serialized_end=1226,
  methods=[
  _descriptor.MethodDescriptor(
    name='F2D_getmsg',
    full_name='F2D.F2D_getmsg',
    index=0,
    containing_service=None,
    input_type=_F2D_REQUEST,
    output_type=_F2D_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_F2D)

DESCRIPTOR.services_by_name['F2D'] = _F2D


_S2D = _descriptor.ServiceDescriptor(
  name='S2D',
  full_name='S2D',
  file=DESCRIPTOR,
  index=5,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1228,
  serialized_end=1278,
  methods=[
  _descriptor.MethodDescriptor(
    name='S2D_getmsg',
    full_name='S2D.S2D_getmsg',
    index=0,
    containing_service=None,
    input_type=_S2D_REQUEST,
    output_type=_S2D_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_S2D)

DESCRIPTOR.services_by_name['S2D'] = _S2D

# @@protoc_insertion_point(module_scope)
