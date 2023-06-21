#!/usr/bin/env python3
from brain_games.game_engine import run_game
from brain_games.games.even import set_exercise_and_answer
from brain_games.games.even import RULE


def main():
    run_game(RULE, set_exercise_and_answer)


if __name__ == '__main__':
    main()
