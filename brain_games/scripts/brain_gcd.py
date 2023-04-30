#!/usr/bin/env python3
import brain_games.game_engine
from brain_games.games.gcd import set_expression_and_answer

task = 'Find the greatest common divisor of given numbers.'


def main():
    brain_games.game_engine.main(task, set_expression_and_answer)


if __name__ == '__main__':
    main()
