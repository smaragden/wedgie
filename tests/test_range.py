from wedgie import (
    FrameRange,
    RangeRGB,
    RangeRGBA,
    RangeFLOAT,
    RangeUINT,
    RangeVECTOR2,
    RangeVECTOR,
    RangeMATRIX,
)
import pytest


def test_range_parsing_basic():
    r = FrameRange.from_string("0-100")
    assert r.start == 0
    assert r.end == 100


def test_range_parsing_reverse():
    r = FrameRange.from_string("100-0")
    assert r.start == 100
    assert r.end == 0


def test_range_parsing_invalid():
    with pytest.raises(SyntaxError):
        FrameRange.from_string("100")


def test_range_parsing_invalid_type():
    with pytest.raises(TypeError):
        FrameRange.from_string(65436534)


def test_range_parsing_zeros():
    r = FrameRange.from_string("000-000")
    assert r.start == 0
    assert r.end == 0


def test_range_parsing_multi_delimiter():
    with pytest.raises(SyntaxError):
        FrameRange.from_string("0----0")


def test_vec2range_basic():
    r = RangeVECTOR2((0.5, 1.0), (0.2, 0.3))
    assert r.start.x == pytest.approx(0.5)
    assert r.start.y == pytest.approx(1.0)

    assert r.end.x == pytest.approx(0.2)
    assert r.end.y == pytest.approx(0.3)


def test_vecrange_basic():
    r = RangeVECTOR((0.5, 1.0, 9.8), (0.2, 0.3, 3.5))
    assert r.start.x == pytest.approx(0.5)
    assert r.start.y == pytest.approx(1.0)
    assert r.start.z == pytest.approx(9.8)

    assert r.end.x == pytest.approx(0.2)
    assert r.end.y == pytest.approx(0.3)
    assert r.end.z == pytest.approx(3.5)


def test_rgbrange_basic():
    r = RangeRGB((0.1, 0.5, 1.0), (1.0, 0.2, 0.2))
    assert r.start.r == pytest.approx(0.1)
    assert r.start.g == pytest.approx(0.5)
    assert r.start.b == pytest.approx(1.0)

    assert r.end.r == pytest.approx(1.0)
    assert r.end.g == pytest.approx(0.2)
    assert r.end.b == pytest.approx(0.2)


def test_rgbarange_basic():
    r = RangeRGBA((0.1, 0.5, 1.0, 1.0), (1.0, 0.2, 0.2, 0.2))
    assert r.start.r == pytest.approx(0.1)
    assert r.start.g == pytest.approx(0.5)
    assert r.start.b == pytest.approx(1.0)
    assert r.start.a == pytest.approx(1.0)

    assert r.end.r == pytest.approx(1.0)
    assert r.end.g == pytest.approx(0.2)
    assert r.end.b == pytest.approx(0.2)
    assert r.end.a == pytest.approx(0.2)


def test_uintrange_basic():
    r = RangeUINT(0.1, 1.9)
    assert r.start == 0
    assert r.end == 1


def test_intrange_basic():
    r = RangeUINT(-154, 64532)
    assert r.start == -154
    assert r.end == 64532


def test_floatrange_basic():
    r = RangeFLOAT(0.1, 0.9)
    assert r.start == pytest.approx(0.1)
    assert r.end == pytest.approx(0.9)


def test_matrixrange_basic():
    r = RangeMATRIX(
        (
            1.0,
            0.0,
            0.0,
            0.0,
            0.0,
            1.0,
            0.0,
            0.0,
            0.0,
            0.0,
            1.0,
            0.0,
            0.0,
            0.0,
            0.0,
            1.0,
        ),
        (
            1.0,
            0.0,
            0.0,
            0.0,
            0.0,
            1.0,
            0.0,
            0.0,
            0.0,
            0.0,
            1.0,
            0.0,
            0.0,
            0.0,
            1.0,
            1.0,
        ),
    )
    assert r.start.data[0][0] == pytest.approx(1.0)
    assert r.end.data[3][3] == pytest.approx(1.0)