#!/usr/bin/env python3
import brain_games.game_engine
from math import gcd


def set_expression():
    first_numb = brain_games.game_engine.generate_rand_num()
    second_numb = brain_games.game_engine.generate_rand_num()
    answer = str(gcd(first_numb, second_numb))
    question = f'{first_numb} {second_numb}'

    return question, answer


task = 'Find the greatest common divisor of given numbers.'


def main():
    brain_games.game_engine.main(task, set_expression)
