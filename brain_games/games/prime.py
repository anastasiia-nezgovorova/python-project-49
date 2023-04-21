from random import randint


def set_exercise():
    start_border_of_random = 0
    end_border_of_random = 100
    radius = (start_border_of_random, end_border_of_random)
    num = randint(radius[0], radius[1])

    answer = 'yes'

    if num <= 1:
        answer = 'no'
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                answer = 'no'

    question = f'Question: {num}'

    return question, answer
