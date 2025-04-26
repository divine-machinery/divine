import pytest
from divine import Screen

@pytest.fixture
def screen() -> Screen:
    return Screen(
        coordinate = (1, 1),
        height = 20,
        width = 100,
    )

# -----


def test_name(screen):
    assert screen.name == 'Screen'

# -----


def test_coordinate(screen):
    assert screen.coordinate == (1, 1)

def test_height(screen):
    assert screen.height == 20

def test_width(screen):
    assert screen.width == 100

# -----


def test_border(screen):
    assert not screen.border.ACTIVATED

# -----


def test_begy(screen):
    assert screen.begy == 0

def test_begx(screen):
    assert screen.begx == 0

# -----


def test_endy(screen):
    assert screen.endy == 19

def test_endx(screen):
    assert screen.endx == 99

# -----
