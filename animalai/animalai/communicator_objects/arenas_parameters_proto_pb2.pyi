# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from animalai.communicator_objects.arena_parameters_proto_pb2 import (
    ArenaParametersProto as animalai___communicator_objects___arena_parameters_proto_pb2___ArenaParametersProto,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Mapping as typing___Mapping,
    MutableMapping as typing___MutableMapping,
    Optional as typing___Optional,
    Union as typing___Union,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode


class ArenasParametersProto(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class ArenasEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key = ... # type: builtin___int

        @property
        def value(self) -> animalai___communicator_objects___arena_parameters_proto_pb2___ArenaParametersProto: ...

        def __init__(self,
            *,
            key : typing___Optional[builtin___int] = None,
            value : typing___Optional[animalai___communicator_objects___arena_parameters_proto_pb2___ArenaParametersProto] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> ArenasParametersProto.ArenasEntry: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ArenasParametersProto.ArenasEntry: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    seed = ... # type: builtin___int

    @property
    def arenas(self) -> typing___MutableMapping[builtin___int, animalai___communicator_objects___arena_parameters_proto_pb2___ArenaParametersProto]: ...

    def __init__(self,
        *,
        arenas : typing___Optional[typing___Mapping[builtin___int, animalai___communicator_objects___arena_parameters_proto_pb2___ArenaParametersProto]] = None,
        seed : typing___Optional[builtin___int] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ArenasParametersProto: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ArenasParametersProto: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"arenas",b"arenas",u"seed",b"seed"]) -> None: ...
