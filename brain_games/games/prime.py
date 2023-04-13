from random import randint


def generate_rand_num():
    radius_of_random = (0, 100)
    rand_num = randint(radius_of_random[0], radius_of_random[1])
    return rand_num


def set_exercise():
    num = generate_rand_num()
    answer = 'yes'

    if num <= 1:
        answer = 'no'
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                answer = 'no'

    question = f'Question: {num}'

    return question, answer
