from __future__ import print_function
from arnold import *


def test_env(resource):
    api, _, _, _ = AiGetVersion()
    assert int(api) > 5
