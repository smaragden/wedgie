import os
from arnold import *

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
RESOURCE_DIR = os.path.join(CURRENT_DIR, "_data")


def resource_dir(func):
    def wrapper():
        try:
            os.makedirs(RESOURCE_DIR)
        except:
            pass
        func()

    return wrapper


@resource_dir
def create_base_scene():
    AiBegin()
    options = AiUniverseGetOptions()
    AiNodeSetInt(options, "xres", 256)
    AiNodeSetInt(options, "yres", 256)
    camera = AiNode("persp_camera", "/nodes/camera01")
    AiNodeSetVec(camera, "position", 0, 0, 1.1)
    AiNodeSetVec(camera, "look_at", 0, 0, 0)
    sphere = AiNode("sphere", "/nodes/sphere01")
    surface = AiNode("standard_surface", "/nodes/surface")
    AiNodeSetPtr(sphere, "shader", surface)
    AiASSWrite(os.path.join(RESOURCE_DIR, "base_scene.ass"), AI_NODE_ALL, False)
    AiEnd()