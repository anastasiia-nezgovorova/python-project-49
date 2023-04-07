#!/usr/bin/env python3
from random import randint
import brain_games.game_engine
from brain_games.scripts.brain_calc import choose_oper

task = 'What number is missing in the progression?'


def generate_step():
    radius_of_random = (1, 10)
    step = randint(radius_of_random[0], radius_of_random[1])
    return step


def set_progression():  # noqa: C901
    step = generate_step()
    oper = choose_oper()
    while oper == '*':
        oper = choose_oper()

    first_numb = brain_games.game_engine.generate_rand_num()
    second_numb = 0
    third_numb = 0

    if oper == '+':
        second_numb = first_numb + step
    if oper == '-':
        second_numb = first_numb - step

    progression = [first_numb, second_numb]
    progression_len = randint(5, 10)

    while len(progression) < progression_len:
        if oper == '+':
            third_numb = second_numb + step
        if oper == '-':
            third_numb = second_numb - step

        progression.append(third_numb)
        second_numb = third_numb

    ind_hidden_numb = randint(0, len(progression) - 1)
    answer = progression[ind_hidden_numb]
    progression[ind_hidden_numb] = '..'

    progression_text = str(progression)
    progression_text = progression_text.replace('[', 'Question: ')
    progression_text = progression_text.replace(']', '')
    progression_text = progression_text.replace(',', '')
    progression_text = progression_text.replace("'", "")

    return progression_text, str(answer)


def main():
    brain_games.game_engine.main(task, set_progression)


if __name__ == '__main__':
    main()
