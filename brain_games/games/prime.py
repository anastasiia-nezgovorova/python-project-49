from random import randint


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
START_BORDER_OF_RANDOM = 0
END_BORDER_OF_RANDOM = 100


def set_exercise():
    radius = (START_BORDER_OF_RANDOM, END_BORDER_OF_RANDOM)
    num = randint(radius[0], radius[1])

    return num


def get_answer(num):
    answer = 'yes'

    if num <= 1:
        answer = 'no'
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                answer = 'no'

    return answer


def set_exercise_and_answer():
    exercise = set_exercise()
    answer = get_answer(exercise)
    return exercise, answer
