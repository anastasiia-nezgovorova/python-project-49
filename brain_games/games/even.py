from random import randint


def set_exercise():
    start_border_of_random = 0
    end_border_of_random = 100
    radius = (start_border_of_random, end_border_of_random)
    num = randint(radius[0], radius[1])

    question = f'Question: {num}'
    answer = 'no'

    if (num % 2) == 0:
        answer = 'yes'

    return question, answer
