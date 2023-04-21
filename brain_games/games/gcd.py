from random import randint
from math import gcd


def set_expression():
    start_border_of_random = 1
    end_border_of_random = 30
    radius = (start_border_of_random, end_border_of_random)
    first_numb = randint(radius[0], radius[1])
    second_numb = randint(radius[0], radius[1])

    answer = str(gcd(first_numb, second_numb))
    question = f'Question: {first_numb} {second_numb}'

    return question, answer
