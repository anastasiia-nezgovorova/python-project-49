#!/usr/bin/env python3
import brain_games.game_engine
from brain_games.games import set_expression_for_gcd

task = 'Find the greatest common divisor of given numbers.'


def main():
    brain_games.game_engine.main(task, set_expression_for_gcd)


if __name__ == '__main__':
    main()
