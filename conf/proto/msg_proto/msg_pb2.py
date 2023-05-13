# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: msg.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='msg.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\tmsg.proto\"\xa0\x01\n\x0b\x43\x32\x46_Request\x12\x12\n\nrequest_id\x18\x01 \x01(\x05\x12\x0b\n\x03img\x18\x04 \x01(\x0c\x12!\n\x05image\x18\x02 \x01(\x0b\x32\x12.C2F_Request.Image\x12\x11\n\tsend_time\x18\x03 \x01(\x02\x1a:\n\x05Image\x12\x0e\n\x06height\x18\x01 \x01(\x05\x12\r\n\x05width\x18\x02 \x01(\x05\x12\x12\n\nbyte_image\x18\x03 \x01(\x0c\"\x1c\n\x0c\x43\x32\x46_Response\x12\x0c\n\x04\x66lag\x18\x01 \x01(\x08\"`\n\x0b\x46\x32S_Request\x12\x12\n\nrequest_id\x18\x01 \x01(\x05\x12\x0c\n\x04size\x18\x02 \x01(\x05\x12\r\n\x05index\x18\x04 \x03(\x05\x12\r\n\x05image\x18\x03 \x03(\x0c\x12\x11\n\tsend_time\x18\x05 \x01(\x02\"\x1c\n\x0c\x46\x32S_Response\x12\x0c\n\x04\x66lag\x18\x01 \x01(\x08\")\n\x0bS2C_Request\x12\x0b\n\x03res\x18\x01 \x03(\t\x12\r\n\x05index\x18\x02 \x03(\x05\"\x1c\n\x0cS2C_Response\x12\x0c\n\x04\x66lag\x18\x01 \x01(\x08\",\n\rSetup_Request\x12\x0c\n\x04port\x18\x01 \x01(\t\x12\r\n\x05\x62\x61tch\x18\x02 \x01(\x05\"\x1e\n\x0eSetup_Response\x12\x0c\n\x04\x66lag\x18\x01 \x01(\x08\"(\n\x0cTest_Request\x12\x0b\n\x03msg\x18\x01 \x01(\x05\x12\x0b\n\x03img\x18\x02 \x01(\x0c\"\x1d\n\rTest_Response\x12\x0c\n\x04\x66lag\x18\x01 \x01(\x08\x32\x32\n\x03\x43\x32\x46\x12+\n\nC2F_getmsg\x12\x0c.C2F_Request\x1a\r.C2F_Response\"\x00\x32\x32\n\x03\x46\x32S\x12+\n\nF2S_getmsg\x12\x0c.F2S_Request\x1a\r.F2S_Response\"\x00\x32\x32\n\x03S2C\x12+\n\nS2C_getmsg\x12\x0c.S2C_Request\x1a\r.S2C_Response\"\x00\x32:\n\x05Setup\x12\x31\n\x0cSetup_getmsg\x12\x0e.Setup_Request\x1a\x0f.Setup_Response\"\x00\x32\x36\n\x04Test\x12.\n\x0bTest_getmsg\x12\r.Test_Request\x1a\x0e.Test_Response\"\x00\x62\x06proto3'
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
  serialized_start=116,
  serialized_end=174,
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
      name='img', full_name='C2F_Request.img', index=1,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='image', full_name='C2F_Request.image', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='send_time', full_name='C2F_Request.send_time', index=3,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=14,
  serialized_end=174,
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
  serialized_start=176,
  serialized_end=204,
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
      name='index', full_name='F2S_Request.index', index=2,
      number=4, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='image', full_name='F2S_Request.image', index=3,
      number=3, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='send_time', full_name='F2S_Request.send_time', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=206,
  serialized_end=302,
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
  serialized_start=304,
  serialized_end=332,
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
      name='res', full_name='S2C_Request.res', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='index', full_name='S2C_Request.index', index=1,
      number=2, type=5, cpp_type=1, label=3,
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
  serialized_start=334,
  serialized_end=375,
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
  serialized_start=377,
  serialized_end=405,
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
  serialized_start=407,
  serialized_end=451,
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
  serialized_start=453,
  serialized_end=483,
)


_TEST_REQUEST = _descriptor.Descriptor(
  name='Test_Request',
  full_name='Test_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg', full_name='Test_Request.msg', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='img', full_name='Test_Request.img', index=1,
      number=2, type=12, cpp_type=9, label=1,
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
  serialized_start=485,
  serialized_end=525,
)


_TEST_RESPONSE = _descriptor.Descriptor(
  name='Test_Response',
  full_name='Test_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='flag', full_name='Test_Response.flag', index=0,
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
  serialized_start=527,
  serialized_end=556,
)

_C2F_REQUEST_IMAGE.containing_type = _C2F_REQUEST
_C2F_REQUEST.fields_by_name['image'].message_type = _C2F_REQUEST_IMAGE
DESCRIPTOR.message_types_by_name['C2F_Request'] = _C2F_REQUEST
DESCRIPTOR.message_types_by_name['C2F_Response'] = _C2F_RESPONSE
DESCRIPTOR.message_types_by_name['F2S_Request'] = _F2S_REQUEST
DESCRIPTOR.message_types_by_name['F2S_Response'] = _F2S_RESPONSE
DESCRIPTOR.message_types_by_name['S2C_Request'] = _S2C_REQUEST
DESCRIPTOR.message_types_by_name['S2C_Response'] = _S2C_RESPONSE
DESCRIPTOR.message_types_by_name['Setup_Request'] = _SETUP_REQUEST
DESCRIPTOR.message_types_by_name['Setup_Response'] = _SETUP_RESPONSE
DESCRIPTOR.message_types_by_name['Test_Request'] = _TEST_REQUEST
DESCRIPTOR.message_types_by_name['Test_Response'] = _TEST_RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

C2F_Request = _reflection.GeneratedProtocolMessageType('C2F_Request', (_message.Message,), {

  'Image' : _reflection.GeneratedProtocolMessageType('Image', (_message.Message,), {
    'DESCRIPTOR' : _C2F_REQUEST_IMAGE,
    '__module__' : 'msg_pb2'
    # @@protoc_insertion_point(class_scope:C2F_Request.Image)
    })
  ,
  'DESCRIPTOR' : _C2F_REQUEST,
  '__module__' : 'msg_pb2'
  # @@protoc_insertion_point(class_scope:C2F_Request)
  })
_sym_db.RegisterMessage(C2F_Request)
_sym_db.RegisterMessage(C2F_Request.Image)

C2F_Response = _reflection.GeneratedProtocolMessageType('C2F_Response', (_message.Message,), {
  'DESCRIPTOR' : _C2F_RESPONSE,
  '__module__' : 'msg_pb2'
  # @@protoc_insertion_point(class_scope:C2F_Response)
  })
_sym_db.RegisterMessage(C2F_Response)

F2S_Request = _reflection.GeneratedProtocolMessageType('F2S_Request', (_message.Message,), {
  'DESCRIPTOR' : _F2S_REQUEST,
  '__module__' : 'msg_pb2'
  # @@protoc_insertion_point(class_scope:F2S_Request)
  })
_sym_db.RegisterMessage(F2S_Request)

F2S_Response = _reflection.GeneratedProtocolMessageType('F2S_Response', (_message.Message,), {
  'DESCRIPTOR' : _F2S_RESPONSE,
  '__module__' : 'msg_pb2'
  # @@protoc_insertion_point(class_scope:F2S_Response)
  })
_sym_db.RegisterMessage(F2S_Response)

S2C_Request = _reflection.GeneratedProtocolMessageType('S2C_Request', (_message.Message,), {
  'DESCRIPTOR' : _S2C_REQUEST,
  '__module__' : 'msg_pb2'
  # @@protoc_insertion_point(class_scope:S2C_Request)
  })
_sym_db.RegisterMessage(S2C_Request)

S2C_Response = _reflection.GeneratedProtocolMessageType('S2C_Response', (_message.Message,), {
  'DESCRIPTOR' : _S2C_RESPONSE,
  '__module__' : 'msg_pb2'
  # @@protoc_insertion_point(class_scope:S2C_Response)
  })
_sym_db.RegisterMessage(S2C_Response)

Setup_Request = _reflection.GeneratedProtocolMessageType('Setup_Request', (_message.Message,), {
  'DESCRIPTOR' : _SETUP_REQUEST,
  '__module__' : 'msg_pb2'
  # @@protoc_insertion_point(class_scope:Setup_Request)
  })
_sym_db.RegisterMessage(Setup_Request)

Setup_Response = _reflection.GeneratedProtocolMessageType('Setup_Response', (_message.Message,), {
  'DESCRIPTOR' : _SETUP_RESPONSE,
  '__module__' : 'msg_pb2'
  # @@protoc_insertion_point(class_scope:Setup_Response)
  })
_sym_db.RegisterMessage(Setup_Response)

Test_Request = _reflection.GeneratedProtocolMessageType('Test_Request', (_message.Message,), {
  'DESCRIPTOR' : _TEST_REQUEST,
  '__module__' : 'msg_pb2'
  # @@protoc_insertion_point(class_scope:Test_Request)
  })
_sym_db.RegisterMessage(Test_Request)

Test_Response = _reflection.GeneratedProtocolMessageType('Test_Response', (_message.Message,), {
  'DESCRIPTOR' : _TEST_RESPONSE,
  '__module__' : 'msg_pb2'
  # @@protoc_insertion_point(class_scope:Test_Response)
  })
_sym_db.RegisterMessage(Test_Response)



_C2F = _descriptor.ServiceDescriptor(
  name='C2F',
  full_name='C2F',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=558,
  serialized_end=608,
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
  serialized_start=610,
  serialized_end=660,
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
  serialized_start=662,
  serialized_end=712,
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
  serialized_start=714,
  serialized_end=772,
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


_TEST = _descriptor.ServiceDescriptor(
  name='Test',
  full_name='Test',
  file=DESCRIPTOR,
  index=4,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=774,
  serialized_end=828,
  methods=[
  _descriptor.MethodDescriptor(
    name='Test_getmsg',
    full_name='Test.Test_getmsg',
    index=0,
    containing_service=None,
    input_type=_TEST_REQUEST,
    output_type=_TEST_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TEST)

DESCRIPTOR.services_by_name['Test'] = _TEST

# @@protoc_insertion_point(module_scope)
