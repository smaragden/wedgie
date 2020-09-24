from arnold import *
from collections.abc import Iterable


def parameter_to_range_type(param):
    if param.type == AI_TYPE_BYTE:
        return RangeINT
    elif param.type == AI_TYPE_INT:
        return RangeINT
    elif param.type == AI_TYPE_UINT:
        return RangeUINT
    elif param.type == AI_TYPE_FLOAT:
        return RangeFLOAT
    elif param.type == AI_TYPE_RGB:
        return RangeRGB
    elif param.type == AI_TYPE_RGBA:
        return RangeRGBA
    elif param.type == AI_TYPE_VECTOR:
        return RangeVECTOR
    elif param.type == AI_TYPE_VECTOR2:
        return RangeVECTOR2
    elif param.type == AI_TYPE_MATRIX:
        return RangeMATRIX
    elif param.type == AI_TYPE_USHORT:
        return RangeUINT
    elif param.type == AI_TYPE_HALF:
        return RangeFLOAT

    raise TypeError("Unsupported param type: {}", AiParamGetTypeName(param.type))


class ParamRange(object):
    def __init__(self, start, end):
        if isinstance(start, Iterable):
            self.start = self._inner_type(*start)
        else:
            self.start = self._inner_type(start)

        if isinstance(end, Iterable):
            self.end = self._inner_type(*end)
        else:
            self.end = self._inner_type(end)

    def __call__(self, t):
        return self.interpolate(t)

    def interpolate(self, t):
        return (self.end - self.start) * t + self.start

    def set_value(self, param, value):
        raise NotImplementedError

    @classmethod
    def from_string_values(cls, start, end):
        start = cls.parse(start)
        end = cls.parse(end)
        return cls(start, end)

    @staticmethod
    def parse(string):
        raise NotImplementedError

    def __repr__(self):
        return "<{} start={} end={}>".format(
            self.__class__.__name__, self.start, self.end
        )


class RangeVECTOR2(ParamRange):
    _inner_type = AtVector2


class RangeVECTOR(ParamRange):
    _inner_type = AtVector


class RangeRGB(ParamRange):
    _inner_type = AtRGB

    def set_value(self, param, value):
        AiNodeSetRGB(param.node, param.name, value.r, value.g, value.b)

    @staticmethod
    def parse(string):
        return eval(string)


class RangeRGBA(ParamRange):
    _inner_type = AtRGBA


class RangeINT(ParamRange):
    _inner_type = int


# FIXME: This one one might bite back
RangeUINT = RangeINT


class RangeFLOAT(ParamRange):
    _inner_type = float

    def interpolate(self, t):
        return (self.end - self.start) * t + self.start

    def set_value(self, param, value):
        AiNodeSetFlt(param.node, param.name, value)

    @staticmethod
    def parse(string):
        return float(string)


class RangeMATRIX(ParamRange):
    _inner_type = AtMatrix
