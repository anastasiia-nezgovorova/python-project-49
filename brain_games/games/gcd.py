from random import randint
from math import gcd


TASK = 'Find the greatest common divisor of given numbers.'
START_BORDER_OF_RANDOM = 1
END_BORDER_OF_RANDOM = 30


def set_expression():
    radius = (START_BORDER_OF_RANDOM, END_BORDER_OF_RANDOM)
    first_numb = randint(radius[0], radius[1])
    second_numb = randint(radius[0], radius[1])

    expression = [first_numb, second_numb]

    return expression


def set_answer(first_numb, second_numb):
    answer = gcd(first_numb, second_numb)
    return answer


def set_expression_and_answer():
    [first_num, second_num] = set_expression()
    answer = str(set_answer(first_num, second_num))
    expression = f'{first_num} {second_num}'

    return expression, answer
