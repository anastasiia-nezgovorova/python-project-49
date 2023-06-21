from random import randint


RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
START_BORDER_OF_RANDOM = 0
END_BORDER_OF_RANDOM = 100


def set_exercise():
    radius = (START_BORDER_OF_RANDOM, END_BORDER_OF_RANDOM)
    num = randint(radius[0], radius[1])

    return num


def get_answer(num):
    answer = 'no'

    if (num % 2) == 0:
        answer = 'yes'

    return answer


def set_exercise_and_answer():
    exercise = set_exercise()
    answer = get_answer(exercise)

    return exercise, answer
