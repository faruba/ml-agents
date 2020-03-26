# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: animalai/communicator_objects/space_type_proto.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from animalai.communicator_objects import (
    resolution_proto_pb2 as animalai_dot_communicator__objects_dot_resolution__proto__pb2,
)


DESCRIPTOR = _descriptor.FileDescriptor(
    name="animalai/communicator_objects/space_type_proto.proto",
    package="communicator_objects",
    syntax="proto3",
    serialized_options=_b("\252\002\034MLAgents.CommunicatorObjects"),
    serialized_pb=_b(
        "\n4animalai/communicator_objects/space_type_proto.proto\x12\x14\x63ommunicator_objects\x1a\x34\x61nimalai/communicator_objects/resolution_proto.proto*.\n\x0eSpaceTypeProto\x12\x0c\n\x08\x64iscrete\x10\x00\x12\x0e\n\ncontinuous\x10\x01\x42\x1f\xaa\x02\x1cMLAgents.CommunicatorObjectsb\x06proto3"
    ),
    dependencies=[
        animalai_dot_communicator__objects_dot_resolution__proto__pb2.DESCRIPTOR,
    ],
)

_SPACETYPEPROTO = _descriptor.EnumDescriptor(
    name="SpaceTypeProto",
    full_name="communicator_objects.SpaceTypeProto",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="discrete", index=0, number=0, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="continuous", index=1, number=1, serialized_options=None, type=None
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=132,
    serialized_end=178,
)
_sym_db.RegisterEnumDescriptor(_SPACETYPEPROTO)

SpaceTypeProto = enum_type_wrapper.EnumTypeWrapper(_SPACETYPEPROTO)
discrete = 0
continuous = 1


DESCRIPTOR.enum_types_by_name["SpaceTypeProto"] = _SPACETYPEPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
