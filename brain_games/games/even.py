from random import randint


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def set_exercise():
    start_border_of_random = 0
    end_border_of_random = 100
    radius = (start_border_of_random, end_border_of_random)
    num = randint(radius[0], radius[1])

    return num


def is_even(num):
    answer = 'no'

    if (num % 2) == 0:
        answer = 'yes'

    return answer


def set_exercise_and_answer():
    exercise = set_exercise()
    answer = is_even(exercise)

    return exercise, answer
