#!/usr/bin/env python3
import brain_games.game_engine

task = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def set_exercise():
    num = brain_games.game_engine.generate_rand_num()
    marker = False

    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                marker = True

    if marker:
        answer = 'no'
    else:
        answer = 'yes'

    question = f'Question: {num}'

    return question, answer


def main():
    brain_games.game_engine.main(task, set_exercise)
