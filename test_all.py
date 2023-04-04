import pytest
from MineSweeper.settings import *
from MineSweeper.gameLogic import GameLogic


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


def test_createMap_beginner():
    game_logic = GameLogic()
    beginner_map = game_logic.createMap((5, 5, 5))
    assert len(beginner_map) == 5
    assert len(beginner_map[0]) == 5


def test_createMap_intermediate():
    game_logic = GameLogic()
    intermediate_map = game_logic.createMap((10, 10, 10))
    assert len(intermediate_map) == 10
    assert len(intermediate_map[0]) == 10


def test_createMap_advanced():
    game_logic = GameLogic()
    advanced_map = game_logic.createMap((20, 10, 20))
    assert len(advanced_map) == 10
    assert len(advanced_map[0]) == 20
