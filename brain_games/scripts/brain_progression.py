#!/usr/bin/env python3
from brain_games.game_engine import run_game
from brain_games.games.progression import set_progression_and_answer
from brain_games.games.progression import TASK


def main():
    run_game(TASK, set_progression_and_answer)


if __name__ == '__main__':
    main()
