from random import randint
from math import gcd


def set_expression():
    start_border_of_random = 1
    end_border_of_random = 30
    radius = (start_border_of_random, end_border_of_random)
    first_numb = randint(radius[0], radius[1])
    second_numb = randint(radius[0], radius[1])

    expression = [first_numb, second_numb]

    return expression


def set_answer(expr):
    [first_numb, second_numb] = expr
    answer = str(gcd(first_numb, second_numb))

    return answer


def set_expression_and_answer():
    expression = set_expression()
    answer = set_answer(expression)

    expression = str(expression)
    expression = expression.replace('[', '')
    expression = expression.replace(']', '')
    expression = expression.replace(',', '')
    expression = expression.replace("'", '')

    return expression, answer
