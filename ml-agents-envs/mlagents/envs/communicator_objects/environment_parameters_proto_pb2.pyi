# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from mlagents.envs.communicator_objects.custom_reset_parameters_pb2 import (
    CustomResetParameters as mlagents___envs___communicator_objects___custom_reset_parameters_pb2___CustomResetParameters,
)

from typing import (
    Mapping as typing___Mapping,
    MutableMapping as typing___MutableMapping,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class EnvironmentParametersProto(google___protobuf___message___Message):
    class FloatParametersEntry(google___protobuf___message___Message):
        key = ... # type: typing___Text
        value = ... # type: float

        def __init__(self,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[float] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> EnvironmentParametersProto.FloatParametersEntry: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"key",u"value"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[b"key",b"value"]) -> None: ...


    @property
    def float_parameters(self) -> typing___MutableMapping[typing___Text, float]: ...

    @property
    def custom_reset_parameters(self) -> mlagents___envs___communicator_objects___custom_reset_parameters_pb2___CustomResetParameters: ...

    def __init__(self,
        float_parameters : typing___Optional[typing___Mapping[typing___Text, float]] = None,
        custom_reset_parameters : typing___Optional[mlagents___envs___communicator_objects___custom_reset_parameters_pb2___CustomResetParameters] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> EnvironmentParametersProto: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"custom_reset_parameters"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"custom_reset_parameters",u"float_parameters"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"custom_reset_parameters",b"custom_reset_parameters"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"custom_reset_parameters",b"float_parameters"]) -> None: ...
