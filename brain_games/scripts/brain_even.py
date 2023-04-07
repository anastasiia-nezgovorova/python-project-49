#!/usr/bin/env python3
import brain_games.game_engine

task = 'Answer "yes" if the number is even, otherwise answer "no".'


def set_exercise():
    num = brain_games.game_engine.generate_rand_num()
    question = f'Question: {num}'
    answer = 'no'

    if (num % 2) == 0:
        answer = 'yes'

    return question, answer


def main():
    brain_games.game_engine.main(task, set_exercise)
