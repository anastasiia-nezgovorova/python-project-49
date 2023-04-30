#!/usr/bin/env python3
from brain_games.game_engine import main as engine_main
from brain_games.games.even import set_exercise_and_answer

task = 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    engine_main(task, set_exercise_and_answer)


if __name__ == '__main__':
    main()
