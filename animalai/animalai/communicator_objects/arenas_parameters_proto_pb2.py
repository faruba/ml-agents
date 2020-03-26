# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: animalai/communicator_objects/arenas_parameters_proto.proto

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
  name='animalai/communicator_objects/arenas_parameters_proto.proto',
  package='communicator_objects',
  syntax='proto3',
  serialized_pb=_b('\n;animalai/communicator_objects/arenas_parameters_proto.proto\x12\x14\x63ommunicator_objects\"\x89\x06\n\x15\x41renasParametersProto\x12G\n\x06\x61renas\x18\x01 \x03(\x0b\x32\x37.communicator_objects.ArenasParametersProto.ArenasEntry\x12\x0c\n\x04seed\x18\x02 \x01(\x05\x1a\xa7\x04\n\x14\x41renaParametersProto\x12\t\n\x01t\x18\x01 \x01(\x05\x12\\\n\x05items\x18\x02 \x03(\x0b\x32M.communicator_objects.ArenasParametersProto.ArenaParametersProto.ItemsToSpawn\x12\x11\n\tblackouts\x18\x03 \x03(\x05\x1a\x92\x03\n\x0cItemsToSpawn\x12\x0c\n\x04name\x18\x01 \x01(\t\x12h\n\tpositions\x18\x03 \x03(\x0b\x32U.communicator_objects.ArenasParametersProto.ArenaParametersProto.ItemsToSpawn.Vector3\x12\x11\n\trotations\x18\x04 \x03(\x02\x12\x64\n\x05sizes\x18\x05 \x03(\x0b\x32U.communicator_objects.ArenasParametersProto.ArenaParametersProto.ItemsToSpawn.Vector3\x12\x65\n\x06\x63olors\x18\x06 \x03(\x0b\x32U.communicator_objects.ArenasParametersProto.ArenaParametersProto.ItemsToSpawn.Vector3\x1a*\n\x07Vector3\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\x1ao\n\x0b\x41renasEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12O\n\x05value\x18\x02 \x01(\x0b\x32@.communicator_objects.ArenasParametersProto.ArenaParametersProto:\x02\x38\x01\x42\x1b\xaa\x02\x18\x41\x41IO.CommunicatorObjectsb\x06proto3')
)




_ARENASPARAMETERSPROTO_ARENAPARAMETERSPROTO_ITEMSTOSPAWN_VECTOR3 = _descriptor.Descriptor(
  name='Vector3',
  full_name='communicator_objects.ArenasParametersProto.ArenaParametersProto.ItemsToSpawn.Vector3',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='communicator_objects.ArenasParametersProto.ArenaParametersProto.ItemsToSpawn.Vector3.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='communicator_objects.ArenasParametersProto.ArenaParametersProto.ItemsToSpawn.Vector3.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='z', full_name='communicator_objects.ArenasParametersProto.ArenaParametersProto.ItemsToSpawn.Vector3.z', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=708,
  serialized_end=750,
)

_ARENASPARAMETERSPROTO_ARENAPARAMETERSPROTO_ITEMSTOSPAWN = _descriptor.Descriptor(
  name='ItemsToSpawn',
  full_name='communicator_objects.ArenasParametersProto.ArenaParametersProto.ItemsToSpawn',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='communicator_objects.ArenasParametersProto.ArenaParametersProto.ItemsToSpawn.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='positions', full_name='communicator_objects.ArenasParametersProto.ArenaParametersProto.ItemsToSpawn.positions', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rotations', full_name='communicator_objects.ArenasParametersProto.ArenaParametersProto.ItemsToSpawn.rotations', index=2,
      number=4, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sizes', full_name='communicator_objects.ArenasParametersProto.ArenaParametersProto.ItemsToSpawn.sizes', index=3,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='colors', full_name='communicator_objects.ArenasParametersProto.ArenaParametersProto.ItemsToSpawn.colors', index=4,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ARENASPARAMETERSPROTO_ARENAPARAMETERSPROTO_ITEMSTOSPAWN_VECTOR3, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=348,
  serialized_end=750,
)

_ARENASPARAMETERSPROTO_ARENAPARAMETERSPROTO = _descriptor.Descriptor(
  name='ArenaParametersProto',
  full_name='communicator_objects.ArenasParametersProto.ArenaParametersProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='t', full_name='communicator_objects.ArenasParametersProto.ArenaParametersProto.t', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='items', full_name='communicator_objects.ArenasParametersProto.ArenaParametersProto.items', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='blackouts', full_name='communicator_objects.ArenasParametersProto.ArenaParametersProto.blackouts', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ARENASPARAMETERSPROTO_ARENAPARAMETERSPROTO_ITEMSTOSPAWN, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=199,
  serialized_end=750,
)

_ARENASPARAMETERSPROTO_ARENASENTRY = _descriptor.Descriptor(
  name='ArenasEntry',
  full_name='communicator_objects.ArenasParametersProto.ArenasEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='communicator_objects.ArenasParametersProto.ArenasEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='communicator_objects.ArenasParametersProto.ArenasEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=752,
  serialized_end=863,
)

_ARENASPARAMETERSPROTO = _descriptor.Descriptor(
  name='ArenasParametersProto',
  full_name='communicator_objects.ArenasParametersProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='arenas', full_name='communicator_objects.ArenasParametersProto.arenas', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seed', full_name='communicator_objects.ArenasParametersProto.seed', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ARENASPARAMETERSPROTO_ARENAPARAMETERSPROTO, _ARENASPARAMETERSPROTO_ARENASENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=86,
  serialized_end=863,
)

_ARENASPARAMETERSPROTO_ARENAPARAMETERSPROTO_ITEMSTOSPAWN_VECTOR3.containing_type = _ARENASPARAMETERSPROTO_ARENAPARAMETERSPROTO_ITEMSTOSPAWN
_ARENASPARAMETERSPROTO_ARENAPARAMETERSPROTO_ITEMSTOSPAWN.fields_by_name['positions'].message_type = _ARENASPARAMETERSPROTO_ARENAPARAMETERSPROTO_ITEMSTOSPAWN_VECTOR3
_ARENASPARAMETERSPROTO_ARENAPARAMETERSPROTO_ITEMSTOSPAWN.fields_by_name['sizes'].message_type = _ARENASPARAMETERSPROTO_ARENAPARAMETERSPROTO_ITEMSTOSPAWN_VECTOR3
_ARENASPARAMETERSPROTO_ARENAPARAMETERSPROTO_ITEMSTOSPAWN.fields_by_name['colors'].message_type = _ARENASPARAMETERSPROTO_ARENAPARAMETERSPROTO_ITEMSTOSPAWN_VECTOR3
_ARENASPARAMETERSPROTO_ARENAPARAMETERSPROTO_ITEMSTOSPAWN.containing_type = _ARENASPARAMETERSPROTO_ARENAPARAMETERSPROTO
_ARENASPARAMETERSPROTO_ARENAPARAMETERSPROTO.fields_by_name['items'].message_type = _ARENASPARAMETERSPROTO_ARENAPARAMETERSPROTO_ITEMSTOSPAWN
_ARENASPARAMETERSPROTO_ARENAPARAMETERSPROTO.containing_type = _ARENASPARAMETERSPROTO
_ARENASPARAMETERSPROTO_ARENASENTRY.fields_by_name['value'].message_type = _ARENASPARAMETERSPROTO_ARENAPARAMETERSPROTO
_ARENASPARAMETERSPROTO_ARENASENTRY.containing_type = _ARENASPARAMETERSPROTO
_ARENASPARAMETERSPROTO.fields_by_name['arenas'].message_type = _ARENASPARAMETERSPROTO_ARENASENTRY
DESCRIPTOR.message_types_by_name['ArenasParametersProto'] = _ARENASPARAMETERSPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ArenasParametersProto = _reflection.GeneratedProtocolMessageType('ArenasParametersProto', (_message.Message,), dict(

  ArenaParametersProto = _reflection.GeneratedProtocolMessageType('ArenaParametersProto', (_message.Message,), dict(

    ItemsToSpawn = _reflection.GeneratedProtocolMessageType('ItemsToSpawn', (_message.Message,), dict(

      Vector3 = _reflection.GeneratedProtocolMessageType('Vector3', (_message.Message,), dict(
        DESCRIPTOR = _ARENASPARAMETERSPROTO_ARENAPARAMETERSPROTO_ITEMSTOSPAWN_VECTOR3,
        __module__ = 'animalai.communicator_objects.arenas_parameters_proto_pb2'
        # @@protoc_insertion_point(class_scope:communicator_objects.ArenasParametersProto.ArenaParametersProto.ItemsToSpawn.Vector3)
        ))
      ,
      DESCRIPTOR = _ARENASPARAMETERSPROTO_ARENAPARAMETERSPROTO_ITEMSTOSPAWN,
      __module__ = 'animalai.communicator_objects.arenas_parameters_proto_pb2'
      # @@protoc_insertion_point(class_scope:communicator_objects.ArenasParametersProto.ArenaParametersProto.ItemsToSpawn)
      ))
    ,
    DESCRIPTOR = _ARENASPARAMETERSPROTO_ARENAPARAMETERSPROTO,
    __module__ = 'animalai.communicator_objects.arenas_parameters_proto_pb2'
    # @@protoc_insertion_point(class_scope:communicator_objects.ArenasParametersProto.ArenaParametersProto)
    ))
  ,

  ArenasEntry = _reflection.GeneratedProtocolMessageType('ArenasEntry', (_message.Message,), dict(
    DESCRIPTOR = _ARENASPARAMETERSPROTO_ARENASENTRY,
    __module__ = 'animalai.communicator_objects.arenas_parameters_proto_pb2'
    # @@protoc_insertion_point(class_scope:communicator_objects.ArenasParametersProto.ArenasEntry)
    ))
  ,
  DESCRIPTOR = _ARENASPARAMETERSPROTO,
  __module__ = 'animalai.communicator_objects.arenas_parameters_proto_pb2'
  # @@protoc_insertion_point(class_scope:communicator_objects.ArenasParametersProto)
  ))
_sym_db.RegisterMessage(ArenasParametersProto)
_sym_db.RegisterMessage(ArenasParametersProto.ArenaParametersProto)
_sym_db.RegisterMessage(ArenasParametersProto.ArenaParametersProto.ItemsToSpawn)
_sym_db.RegisterMessage(ArenasParametersProto.ArenaParametersProto.ItemsToSpawn.Vector3)
_sym_db.RegisterMessage(ArenasParametersProto.ArenasEntry)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\252\002\030AAIO.CommunicatorObjects'))
_ARENASPARAMETERSPROTO_ARENASENTRY.has_options = True
_ARENASPARAMETERSPROTO_ARENASENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
