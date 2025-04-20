import pytest
from curses import window
from divine import Screen

@pytest.fixture
def stdscr(mocker) -> window:
    stdscr = mocker.Mock(spec=window)
    stdscr.getbegyx.return_value = (1, 1)
    stdscr.getmaxyx.return_value = (20, 100)
    return stdscr

@pytest.fixture
def screen(stdscr) -> Screen:
    return Screen(source=stdscr)

# -----


def test_name(stdscr, screen):
    assert screen.name == 'Screen'

def test_realm(stdscr, screen):
    assert screen.realm == stdscr

def test_parent(stdscr, screen):
    assert screen.parent == screen

# -----


def test_coordinate(stdscr, screen):
    assert screen.coordinate == (1, 1)

def test_height(stdscr, screen):
    assert screen.height == 20

def test_width(stdscr, screen):
    assert screen.width == 100

# -----


def test_border(stdscr, screen):
    assert not screen.border.ACTIVATED

# -----


def test_begy(stdscr, screen):
    assert screen.begy == 0

def test_begx(stdscr, screen):
    assert screen.begx == 0

# -----


def test_endy(stdscr, screen):
    assert screen.endy == 19

def test_endx(stdscr, screen):
    assert screen.endx == 99

# -----
