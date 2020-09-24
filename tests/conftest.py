import pytest
from .resources import *


@pytest.fixture()
def resource():
    create_base_scene()
