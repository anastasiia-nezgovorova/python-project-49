#!/usr/bin/env python3
import brain_games.game_engine
from brain_games.games import set_exercise_for_prime

task = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    brain_games.game_engine.main(task, set_exercise_for_prime)


if __name__ == '__main__':
    main()
