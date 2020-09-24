import argparse


class ParamInterpolationArg:
    def __init__(self, node, param, start, end):
        self.node = node
        self.parameter = param
        self.start = start
        self.end = end

    @classmethod
    def from_string(cls, string):
        try:
            param, value = string.split("=")
            node, param = param.split(".")
            start, end = value.split("-")
            return cls(node, param, start, end)
        except ValueError as e:
            msg = "%r need to match the pattern: 'node.parameter=start-end'" % string
            raise argparse.ArgumentTypeError(msg)


class DefaultFrameAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, values)
        setattr(namespace, "frame", namespace.start_frame)