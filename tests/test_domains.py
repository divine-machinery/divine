import pytest
from divine import Heaven, Paradise

# =============== SETUP ===============

@pytest.fixture
def heaven() -> Heaven:
    heaven = Heaven(
        coordinate=(2, 2),
        height = 30,
        width = 100,
        border = False,
    )
    heaven.summon()
    heaven.__setattr__('paradise', Paradise(
        parent = heaven,
        coordinate = (3, 5),
        height = 23,
        width = 95,
    ))

    return heaven

# =============== Heaven ===============

def test_heaven_y(heaven):
    assert heaven.y == 2

def test_heaven_x(heaven):
    assert heaven.x == 2

# -----

def test_heaven_height(heaven):
    assert heaven.height == 30

def test_heaven_width(heaven):
    assert heaven.width == 100

# -----


def test_heaven_begy(heaven):
    assert heaven.begy == 0

def test_heaven_begx(heaven):
    assert heaven.begx == 0

def test_heaven_endy(heaven):
    assert heaven.endy == 29

def test_heaven_endx(heaven):
    assert heaven.endx == 99

def test_heaven_orgy(heaven):
    assert heaven.orgy == 2

def test_heaven_orgx(heaven):
    assert heaven.orgx == 2

# -----

# =============== Paradise ===============

def test_paradise_y(heaven):
    assert heaven.paradise.y == 3

def test_paradise_x(heaven):
    assert heaven.paradise.x == 5

# -----

def test_paradise_height(heaven):
    assert heaven.paradise.height == 23

def test_paradise_width(heaven):
    assert heaven.paradise.width == 95

# -----


def test_paradise_begy(heaven):
    assert heaven.paradise.begy == 0

def test_paradise_begx(heaven):
    assert heaven.paradise.begx == 0

def test_paradise_endy(heaven):
    assert heaven.paradise.endy == 22

def test_paradise_endx(heaven):
    assert heaven.paradise.endx == 94

def test_paradise_orgy(heaven):
    heaven.paradise.summon()
    assert heaven.paradise.orgy == 5

def test_paradise_orgx(heaven):
    heaven.paradise.summon()
    assert heaven.paradise.orgx == 7

# -----
