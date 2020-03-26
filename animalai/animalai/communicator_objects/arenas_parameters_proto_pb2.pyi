# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Iterable as typing___Iterable,
    Mapping as typing___Mapping,
    MutableMapping as typing___MutableMapping,
    Optional as typing___Optional,
    Text as typing___Text,
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
    class ArenaParametersProto(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        class ItemsToSpawn(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            class Vector3(google___protobuf___message___Message):
                DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
                x = ... # type: builtin___float
                y = ... # type: builtin___float
                z = ... # type: builtin___float

                def __init__(self,
                    *,
                    x : typing___Optional[builtin___float] = None,
                    y : typing___Optional[builtin___float] = None,
                    z : typing___Optional[builtin___float] = None,
                    ) -> None: ...
                if sys.version_info >= (3,):
                    @classmethod
                    def FromString(cls, s: builtin___bytes) -> ArenasParametersProto.ArenaParametersProto.ItemsToSpawn.Vector3: ...
                else:
                    @classmethod
                    def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ArenasParametersProto.ArenaParametersProto.ItemsToSpawn.Vector3: ...
                def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
                def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
                def ClearField(self, field_name: typing_extensions___Literal[u"x",b"x",u"y",b"y",u"z",b"z"]) -> None: ...

            name = ... # type: typing___Text
            rotations = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___float]

            @property
            def positions(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ArenasParametersProto.ArenaParametersProto.ItemsToSpawn.Vector3]: ...

            @property
            def sizes(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ArenasParametersProto.ArenaParametersProto.ItemsToSpawn.Vector3]: ...

            @property
            def colors(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ArenasParametersProto.ArenaParametersProto.ItemsToSpawn.Vector3]: ...

            def __init__(self,
                *,
                name : typing___Optional[typing___Text] = None,
                positions : typing___Optional[typing___Iterable[ArenasParametersProto.ArenaParametersProto.ItemsToSpawn.Vector3]] = None,
                rotations : typing___Optional[typing___Iterable[builtin___float]] = None,
                sizes : typing___Optional[typing___Iterable[ArenasParametersProto.ArenaParametersProto.ItemsToSpawn.Vector3]] = None,
                colors : typing___Optional[typing___Iterable[ArenasParametersProto.ArenaParametersProto.ItemsToSpawn.Vector3]] = None,
                ) -> None: ...
            if sys.version_info >= (3,):
                @classmethod
                def FromString(cls, s: builtin___bytes) -> ArenasParametersProto.ArenaParametersProto.ItemsToSpawn: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ArenasParametersProto.ArenaParametersProto.ItemsToSpawn: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"colors",b"colors",u"name",b"name",u"positions",b"positions",u"rotations",b"rotations",u"sizes",b"sizes"]) -> None: ...

        t = ... # type: builtin___int
        blackouts = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int]

        @property
        def items(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ArenasParametersProto.ArenaParametersProto.ItemsToSpawn]: ...

        def __init__(self,
            *,
            t : typing___Optional[builtin___int] = None,
            items : typing___Optional[typing___Iterable[ArenasParametersProto.ArenaParametersProto.ItemsToSpawn]] = None,
            blackouts : typing___Optional[typing___Iterable[builtin___int]] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> ArenasParametersProto.ArenaParametersProto: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ArenasParametersProto.ArenaParametersProto: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"blackouts",b"blackouts",u"items",b"items",u"t",b"t"]) -> None: ...

    class ArenasEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key = ... # type: builtin___int

        @property
        def value(self) -> ArenasParametersProto.ArenaParametersProto: ...

        def __init__(self,
            *,
            key : typing___Optional[builtin___int] = None,
            value : typing___Optional[ArenasParametersProto.ArenaParametersProto] = None,
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
    def arenas(self) -> typing___MutableMapping[builtin___int, ArenasParametersProto.ArenaParametersProto]: ...

    def __init__(self,
        *,
        arenas : typing___Optional[typing___Mapping[builtin___int, ArenasParametersProto.ArenaParametersProto]] = None,
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
