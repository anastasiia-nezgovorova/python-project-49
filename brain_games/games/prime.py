from random import randint


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def set_exercise():
    start_border_of_random = 0
    end_border_of_random = 100
    radius = (start_border_of_random, end_border_of_random)
    num = randint(radius[0], radius[1])

    return num


def set_answer(num):
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
    answer = set_answer(exercise)
    return exercise, answer
