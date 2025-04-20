from re import escape
import pytest
from ..test_domains import heaven # noqa: F401

# regex stands for regular expression btw
# new vocab, yay

# =============== Heaven ===============

def test_validate_heaven_y(heaven): # noqa: F811 
    heaven.layout.y = 1000
    with pytest.raises(ValueError, match=escape(f"y({heaven.layout.y}) of {heaven.name} must be less than the ending y({heaven.parent.endy}) of its parent, {heaven.parent.name}.")):
        heaven.layout.validate()

    heaven.layout.y = -1000
    with pytest.raises(ValueError, match=escape(f"y({heaven.y}) of {heaven.name} cannot less than the beginning y({heaven.parent.begy}) of its parent, {heaven.parent.name}.")):
        heaven.layout.validate()

# -----


def test_validate_heaven_x(heaven): # noqa: F811 
    heaven.layout.x = 1000
    with pytest.raises(ValueError, match=escape(f"x({heaven.layout.x}) of {heaven.name} must be less than the ending x({heaven.parent.endx}) of its parent, {heaven.parent.name}.")):
        heaven.layout.validate()

    heaven.layout.x = -1000
    with pytest.raises(ValueError, match=escape(f"x({heaven.x}) of {heaven.name} cannot less than the beginning x({heaven.parent.begx}) of its parent, {heaven.parent.name}.")):
        heaven.layout.validate()

# -----


def test_validate_heaven_width(heaven): # noqa: F811 
    heaven.layout.width = 1000
    with pytest.raises(ValueError, match=escape(f"width({heaven.width}) of {heaven.name} cannot exceed the available width({heaven.parent.width - heaven.x - (heaven.parent.border.ACTIVATED * 2)}) of its parent, {heaven.parent.name}.")):
        heaven.layout.validate()

    heaven.layout.width = -1000
    with pytest.raises(ValueError, match=escape(f"width({heaven.width}) of {heaven.name} cannot be less than the beginning x({heaven.parent.begx}) of its parent, {heaven.parent.name}.")):
        heaven.layout.validate()

# -----


def test_validate_heaven_height(heaven): # noqa: F811 
    heaven.layout.height = 1000
    with pytest.raises(ValueError, match=escape(f"height({heaven.height}) of {heaven.name} cannot exceed the available height({heaven.parent.height - heaven.y - (heaven.parent.border.ACTIVATED * 2)}) of its parent, {heaven.parent.name}.")):
        heaven.layout.validate()

    heaven.layout.height = -1000
    with pytest.raises(ValueError, match=escape(f"height({heaven.height}) of {heaven.name} cannot be less than the beginning y({heaven.parent.begy}) of its parent, {heaven.parent.name}.")):
        heaven.layout.validate()

# -----

# =============== Paradise ===============

def test_validate_paradise_y(heaven): # noqa: F811 
    heaven.paradise.layout.y = 1000
    with pytest.raises(ValueError, match=escape(f"y({heaven.paradise.layout.y}) of {heaven.paradise.name} must be less than the ending y({heaven.paradise.parent.endy}) of its parent, {heaven.paradise.parent.name}.")):
        heaven.paradise.layout.validate()

    heaven.paradise.layout.y = -1000
    with pytest.raises(ValueError, match=escape(f"y({heaven.paradise.y}) of {heaven.paradise.name} cannot less than the beginning y({heaven.paradise.parent.begy}) of its parent, {heaven.paradise.parent.name}.")):
        heaven.paradise.layout.validate()

# -----


def test_validate_paradise_x(heaven): # noqa: F811 
    heaven.paradise.layout.x = 1000
    with pytest.raises(ValueError, match=escape(f"x({heaven.paradise.layout.x}) of {heaven.paradise.name} must be less than the ending x({heaven.paradise.parent.endx}) of its parent, {heaven.paradise.parent.name}.")):
        heaven.paradise.layout.validate()

    heaven.paradise.layout.x = -1000
    with pytest.raises(ValueError, match=escape(f"x({heaven.paradise.x}) of {heaven.paradise.name} cannot less than the beginning x({heaven.paradise.parent.begx}) of its parent, {heaven.paradise.parent.name}.")):
        heaven.paradise.layout.validate()

# -----


def test_validate_paradise_width(heaven): # noqa: F811 
    heaven.paradise.layout.width = 1000
    with pytest.raises(ValueError, match=escape(f"width({heaven.paradise.width}) of {heaven.paradise.name} cannot exceed the available width({heaven.paradise.parent.width - heaven.paradise.x - (heaven.paradise.parent.border.ACTIVATED * 2)}) of its parent, {heaven.paradise.parent.name}.")):
        heaven.paradise.layout.validate()

    heaven.paradise.layout.width = -1000
    with pytest.raises(ValueError, match=escape(f"width({heaven.paradise.width}) of {heaven.paradise.name} cannot be less than the beginning x({heaven.paradise.parent.begx}) of its parent, {heaven.paradise.parent.name}.")):
        heaven.paradise.layout.validate()

# -----


def test_validate_paradise_height(heaven): # noqa: F811 
    heaven.paradise.layout.height = 1000
    with pytest.raises(ValueError, match=escape(f"height({heaven.paradise.height}) of {heaven.paradise.name} cannot exceed the available height({heaven.paradise.parent.height - heaven.paradise.y - (heaven.paradise.parent.border.ACTIVATED * 2)}) of its parent, {heaven.paradise.parent.name}.")):
        heaven.paradise.layout.validate()

    heaven.paradise.layout.height = -1000
    with pytest.raises(ValueError, match=escape(f"height({heaven.paradise.height}) of {heaven.paradise.name} cannot be less than the beginning y({heaven.paradise.parent.begy}) of its parent, {heaven.paradise.parent.name}.")):
        heaven.paradise.layout.validate()

# -----
