from random import randint
from math import gcd


def generate_rand_num_for_even():
    radius_of_random = (0, 100)
    rand_num = randint(radius_of_random[0], radius_of_random[1])
    return rand_num


def set_exercise_for_even():
    num = generate_rand_num_for_even()
    question = f'Question: {num}'
    answer = 'no'

    if (num % 2) == 0:
        answer = 'yes'

    return question, answer


def generate_rand_num_for_calc():
    radius_of_random = (-100, 100)
    rand_num = randint(radius_of_random[0], radius_of_random[1])
    return rand_num


def choose_oper():
    operators_set = ("*", "+", "-")
    index_radius = (0, len(operators_set) - 1)
    rand_oper = operators_set[randint(index_radius[0], index_radius[1])]
    return rand_oper


def set_expression_for_calc():
    answer = 0
    first_numb = generate_rand_num_for_calc()
    second_numb = generate_rand_num_for_calc()
    oper = choose_oper()

    if oper == '*':
        answer = str(first_numb * second_numb)
    if oper == '+':
        answer = str(first_numb + second_numb)
    if oper == '-':
        answer = str(first_numb - second_numb)

    expression = f'Question: {first_numb} {oper} {second_numb}'

    return expression, answer


def generate_rand_num_for_gcd():
    radius_of_random = (1, 30)
    rand_num = randint(radius_of_random[0], radius_of_random[1])
    return rand_num


def set_expression_for_gcd():
    first_numb = generate_rand_num_for_gcd()
    second_numb = generate_rand_num_for_gcd()
    answer = str(gcd(first_numb, second_numb))
    question = f'Question: {first_numb} {second_numb}'

    return question, answer


def generate_rand_num_for_prime():
    radius_of_random = (0, 100)
    rand_num = randint(radius_of_random[0], radius_of_random[1])
    return rand_num


def set_exercise_for_prime():
    num = generate_rand_num_for_prime()
    answer = 'yes'

    if num <= 1:
        answer = 'no'
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                answer = 'no'

    question = f'Question: {num}'

    return question, answer


def generate_step():
    radius_of_random = (1, 10)
    step = randint(radius_of_random[0], radius_of_random[1])
    return step


def set_progression():  # noqa: C901
    step = generate_step()
    oper = choose_oper()
    while oper == '*':
        oper = choose_oper()

    first_numb = generate_rand_num_for_calc()
    second_numb = 0
    third_numb = 0

    if oper == '+':
        second_numb = first_numb + step
    if oper == '-':
        second_numb = first_numb - step

    progression = [first_numb, second_numb]
    progression_len = randint(5, 10)

    while len(progression) < progression_len:
        if oper == '+':
            third_numb = second_numb + step
        if oper == '-':
            third_numb = second_numb - step

        progression.append(third_numb)
        second_numb = third_numb

    ind_hidden_numb = randint(0, len(progression) - 1)
    answer = progression[ind_hidden_numb]
    progression[ind_hidden_numb] = '..'

    progression_text = str(progression)
    progression_text = progression_text.replace("[]',", '')
    progression_text = f'Question: {progression_text}'

    return progression_text, str(answer)
