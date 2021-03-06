# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: models.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='models.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0cmodels.proto\"(\n\x06UserPB\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"c\n\nUserListPB\x12)\n\x05items\x18\x01 \x03(\x0b\x32\x1a.UserListPB.UserListItemPB\x1a*\n\x0eUserListItemPB\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x1b\n\x0bTestModelPB\x12\x0c\n\x04name\x18\x02 \x01(\t\"w\n\x0fTestModelListPB\x12\x33\n\x05items\x18\x01 \x03(\x0b\x32$.TestModelListPB.TestModelListItemPB\x1a/\n\x13TestModelListItemPB\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\tb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_USERPB = _descriptor.Descriptor(
  name='UserPB',
  full_name='UserPB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='UserPB.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='password', full_name='UserPB.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=16,
  serialized_end=56,
)


_USERLISTPB_USERLISTITEMPB = _descriptor.Descriptor(
  name='UserListItemPB',
  full_name='UserListPB.UserListItemPB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='UserListPB.UserListItemPB.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='UserListPB.UserListItemPB.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=115,
  serialized_end=157,
)

_USERLISTPB = _descriptor.Descriptor(
  name='UserListPB',
  full_name='UserListPB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='UserListPB.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_USERLISTPB_USERLISTITEMPB, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=58,
  serialized_end=157,
)


_TESTMODELPB = _descriptor.Descriptor(
  name='TestModelPB',
  full_name='TestModelPB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='TestModelPB.name', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=159,
  serialized_end=186,
)


_TESTMODELLISTPB_TESTMODELLISTITEMPB = _descriptor.Descriptor(
  name='TestModelListItemPB',
  full_name='TestModelListPB.TestModelListItemPB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='TestModelListPB.TestModelListItemPB.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='TestModelListPB.TestModelListItemPB.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=260,
  serialized_end=307,
)

_TESTMODELLISTPB = _descriptor.Descriptor(
  name='TestModelListPB',
  full_name='TestModelListPB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='TestModelListPB.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_TESTMODELLISTPB_TESTMODELLISTITEMPB, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=188,
  serialized_end=307,
)

_USERLISTPB_USERLISTITEMPB.containing_type = _USERLISTPB
_USERLISTPB.fields_by_name['items'].message_type = _USERLISTPB_USERLISTITEMPB
_TESTMODELLISTPB_TESTMODELLISTITEMPB.containing_type = _TESTMODELLISTPB
_TESTMODELLISTPB.fields_by_name['items'].message_type = _TESTMODELLISTPB_TESTMODELLISTITEMPB
DESCRIPTOR.message_types_by_name['UserPB'] = _USERPB
DESCRIPTOR.message_types_by_name['UserListPB'] = _USERLISTPB
DESCRIPTOR.message_types_by_name['TestModelPB'] = _TESTMODELPB
DESCRIPTOR.message_types_by_name['TestModelListPB'] = _TESTMODELLISTPB

UserPB = _reflection.GeneratedProtocolMessageType('UserPB', (_message.Message,), dict(
  DESCRIPTOR = _USERPB,
  __module__ = 'models_pb2'
  # @@protoc_insertion_point(class_scope:UserPB)
  ))
_sym_db.RegisterMessage(UserPB)

UserListPB = _reflection.GeneratedProtocolMessageType('UserListPB', (_message.Message,), dict(

  UserListItemPB = _reflection.GeneratedProtocolMessageType('UserListItemPB', (_message.Message,), dict(
    DESCRIPTOR = _USERLISTPB_USERLISTITEMPB,
    __module__ = 'models_pb2'
    # @@protoc_insertion_point(class_scope:UserListPB.UserListItemPB)
    ))
  ,
  DESCRIPTOR = _USERLISTPB,
  __module__ = 'models_pb2'
  # @@protoc_insertion_point(class_scope:UserListPB)
  ))
_sym_db.RegisterMessage(UserListPB)
_sym_db.RegisterMessage(UserListPB.UserListItemPB)

TestModelPB = _reflection.GeneratedProtocolMessageType('TestModelPB', (_message.Message,), dict(
  DESCRIPTOR = _TESTMODELPB,
  __module__ = 'models_pb2'
  # @@protoc_insertion_point(class_scope:TestModelPB)
  ))
_sym_db.RegisterMessage(TestModelPB)

TestModelListPB = _reflection.GeneratedProtocolMessageType('TestModelListPB', (_message.Message,), dict(

  TestModelListItemPB = _reflection.GeneratedProtocolMessageType('TestModelListItemPB', (_message.Message,), dict(
    DESCRIPTOR = _TESTMODELLISTPB_TESTMODELLISTITEMPB,
    __module__ = 'models_pb2'
    # @@protoc_insertion_point(class_scope:TestModelListPB.TestModelListItemPB)
    ))
  ,
  DESCRIPTOR = _TESTMODELLISTPB,
  __module__ = 'models_pb2'
  # @@protoc_insertion_point(class_scope:TestModelListPB)
  ))
_sym_db.RegisterMessage(TestModelListPB)
_sym_db.RegisterMessage(TestModelListPB.TestModelListItemPB)


# @@protoc_insertion_point(module_scope)
