import re


class FrameRange(object):
    range_re = re.compile(r"(?P<start>[0-9]+)-(?P<end>[0-9]+)")

    def __init__(self, start, end):
        self.start = int(start)
        self.end = int(end)

    @classmethod
    def from_string(cls, string):
        try:
            r = cls.range_re.search(string)
        except TypeError:
            raise TypeError('range need to be a string like: "0-100"')
        if not r:
            raise SyntaxError("Failed to parse range: {}".format(string))
        rd = r.groupdict()
        return cls(int(rd["start"]), int(rd["end"]))

    @classmethod
    def is_range(cls, string):
        return cls.range_re.mat
