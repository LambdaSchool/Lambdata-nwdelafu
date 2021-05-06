"""Basic Unit testing for example.py"""
from random import randint
from example import increment, COLORS


def test_increment_int():
    """Testing positive ints for increment function"""

    assert increment(3) == 4
    assert increment(100) == 101

    for i in range(10000):
        test_value = randint(100, 1000)
        assert increment(test_value) == test_value + 1


def test_increment_neg_int():
    """Testing negative ints for increment function"""
    assert increment(-5) == -4


def test_increment_floats():
    """Testing positive floats for increment function"""

    assert increment(10.8) == 11.8
    assert increment(2.8) == 3.8


def test_increment_neg_floats():
    """Testing negative floats for increment function"""
    # TODO: STRETCH GOAL - How can I test negative floats?
    pass


def test_number_colors():
    """Testing colors contents"""
    assert len(COLORS) == 4


def test_color_contents():
    assert "blue" in COLORS
    assert "mauve" in COLORS
    assert "brown" not in COLORS
