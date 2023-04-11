#!/usr/bin/env python3
from random import randint
from brain_games.game_engine import main as engine_main

task = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_rand_num():
    radius_of_random = (0, 100)
    rand_num = randint(radius_of_random[0], radius_of_random[1])
    return rand_num


def set_exercise():
    num = generate_rand_num()
    question = f'Question: {num}'
    answer = 'no'

    if (num % 2) == 0:
        answer = 'yes'

    return question, answer


def main():
    engine_main(task, set_exercise)


if __name__ == '__main__':
    main()
