#!/usr/bin/env python3
from random import randint
from brain_games.game_engine import main as engine_main


task = 'What is the result of the expression?'


def generate_rand_num():
    radius_of_random = (-100, 100)
    rand_num = randint(radius_of_random[0], radius_of_random[1])
    return rand_num


def choose_oper():
    operators_set = ("*", "+", "-")
    index_radius = (0, len(operators_set) - 1)
    rand_oper = operators_set[randint(index_radius[0], index_radius[1])]
    return rand_oper


def set_expression():
    answer = 0
    first_numb = generate_rand_num()
    second_numb = generate_rand_num()
    oper = choose_oper()

    if oper == '*':
        answer = str(first_numb * second_numb)
    if oper == '+':
        answer = str(first_numb + second_numb)
    if oper == '-':
        answer = str(first_numb - second_numb)

    expression = f'Question: {first_numb} {oper} {second_numb}'

    return expression, answer


def main():
    engine_main(task, set_expression)


if __name__ == '__main__':
    main()
