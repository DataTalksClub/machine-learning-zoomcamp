import sys
import types

import numpy as np


class Message:
    def __init__(self, **fields):
        self.__dict__.update(fields)


class TensorShapeProto(Message):
    Dim = Message


def load_proto(monkeypatch):
    # tensorflow is too heavy for a unit test, so replace the protobuf classes
    framework = types.ModuleType("tensorflow.core.framework")
    framework.tensor_pb2 = types.SimpleNamespace(TensorProto=Message)
    framework.tensor_shape_pb2 = types.SimpleNamespace(TensorShapeProto=TensorShapeProto)
    framework.types_pb2 = types.SimpleNamespace(DT_FLOAT=1)
    for name in ("tensorflow", "tensorflow.core"):
        monkeypatch.setitem(sys.modules, name, types.ModuleType(name))
    monkeypatch.setitem(sys.modules, "tensorflow.core.framework", framework)
    monkeypatch.delitem(sys.modules, "proto", raising=False)
    import proto

    monkeypatch.delitem(sys.modules, "proto")
    return proto


def test_np_to_protobuf_serialises_tensor_bytes(monkeypatch):
    proto = load_proto(monkeypatch)
    data = np.array([[1.0, 2.0], [3.0, 4.0]], dtype="float32")

    tensor = proto.np_to_protobuf(data)

    assert tensor.tensor_content == data.tobytes()
    assert [d.size for d in tensor.tensor_shape.dim] == [2, 2]
