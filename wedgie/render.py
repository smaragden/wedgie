from .parameter import Parameter
from .param_range import *
from arnold import *
import uuid


class Render(object):
    def __init__(self, infile, outfile, start, end, parameter_interpolations=[]):
        self._infile = infile
        self._outfile = outfile
        self._start = start
        self._end = end
        self._param_interpolations = parameter_interpolations

    def override_output(self, frame):
        filename = "{}.{:04}.png".format(self._outfile, frame)
        prefix = str(uuid.uuid4())
        options = AiUniverseGetOptions()
        driver_name = "{}_driver".format(prefix)
        filter_name = "{}_filter".format(prefix)
        default_driver = AiNode("driver_png", driver_name)
        AiNodeSetStr(default_driver, "filename", filename)
        default_filter = AiNode("gaussian_filter", filter_name)
        AiNodeSetStr(
            options, "outputs", "RGBA RGBA {} {}".format(filter_name, driver_name)
        )

    def __call__(self, frame):
        AiMsgSetConsoleFlags(AI_LOG_ALL)
        AiBegin()
        AiASSLoad(self._infile)
        self.override_output(frame)
        options = AiUniverseGetOptions()
        AiNodeSetBool(options, "skip_license_check", True)
        for p in self._param_interpolations:
            param = Parameter(p.node, p.parameter)
            param_range_type = parameter_to_range_type(param)
            param_range = param_range_type.from_string_values(p.start, p.end)
            t = self._t(frame)
            value = param_range(t)
            param_range.set_value(param, value)
        AiRender()
        AiEnd()

    def _t(self, frame):
        num_frames = self._end - self._start
        if num_frames == 0:
            return 0.0
        offset = frame - self._start
        return float(offset) / float(num_frames)

    @classmethod
    def from_args(cls, args):
        render = cls(
            args.infile,
            args.outfile,
            args.start_frame,
            args.end_frame,
            args.parameter_interpolation,
        )
        return render
