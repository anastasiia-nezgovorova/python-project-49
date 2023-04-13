from random import randint
from math import gcd


def generate_rand_num():
    radius_of_random = (1, 30)
    rand_num = randint(radius_of_random[0], radius_of_random[1])
    return rand_num


def set_expression():
    first_numb = generate_rand_num()
    second_numb = generate_rand_num()
    answer = str(gcd(first_numb, second_numb))
    question = f'Question: {first_numb} {second_numb}'

    return question, answer
