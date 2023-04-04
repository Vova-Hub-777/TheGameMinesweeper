import pytest
from MineSweeper.settings import *


def getLevel(level):  # Get the level (need to fix it later)
    if level == 'Beginner':
        return BEGINNER
    elif level == 'Intermediate':
        return INTERMEDIATE
    elif level == 'Expert':
        return ADVANCED
def getScreenSize(level):
    if level == 'Beginner':
        return SCREEN_SIZE_BEGINNER
    elif level == 'Intermediate':
        return SCREEN_SIZE_INTERMEDIATE
    elif level == 'Expert':
        return SCREEN_SIZE_ADVANCED


@pytest.mark.parametrize("level, expected",
                         [("Beginner", (5, 5, 5)), ("Intermediate", (10, 10, 10)), ("Expert", (20, 10, 20))])
def test_getLevel(level, expected):
    assert getLevel(level) == expected


@pytest.mark.parametrize("level, expected",
                         [("Beginner", (250, 250)), ("Intermediate", (500, 500)), ("Expert", (1000, 500))])
def test_getScreenSize(level, expected):
    assert getScreenSize(level) == expected