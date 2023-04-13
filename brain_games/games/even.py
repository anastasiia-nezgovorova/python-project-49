from random import randint


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
