#!/usr/bin/env python3
from random import randint
import brain_games.game_engine


def choose_oper():
    operators_set = ("*", "+", "-")
    index_radius = (0, len(operators_set) - 1)
    rand_oper = randint(index_radius[0], index_radius[1])
    return rand_oper


def set_expression(string_request=0):
    expression = None
    first_numb = brain_games.game_engine.generate_rand_num()
    second_numb = brain_games.game_engine.generate_rand_num()
    oper = choose_oper()

    if oper == '*':
        expression = first_numb * second_numb
    if oper == '+':
        expression = first_numb + second_numb
    if oper == '-':
        expression = first_numb - second_numb

    if string_request == 1:
        expression == f'Question: {first_numb} {oper} {second_numb}'
    return expression


task = 'What is the result of the expression?'


def main():
    brain_games.game_engine.main(task, set_expression(1), set_expression())
