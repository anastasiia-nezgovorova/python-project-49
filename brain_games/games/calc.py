from random import randint


def generate_rand_num():
    radius_of_random = (-100, 100)
    rand_num = randint(radius_of_random[0], radius_of_random[1])
    return rand_num


def choose_oper():
    operators_set = ("*", "+", "-")
    index_radius = (0, len(operators_set) - 1)
    rand_oper = operators_set[randint(index_radius[0], index_radius[1])]
    return rand_oper


def set_expression():
    answer = 0
    first_numb = generate_rand_num()
    second_numb = generate_rand_num()
    oper = choose_oper()

    if oper == '*':
        answer = str(first_numb * second_numb)
    if oper == '+':
        answer = str(first_numb + second_numb)
    if oper == '-':
        answer = str(first_numb - second_numb)

    expression = f'Question: {first_numb} {oper} {second_numb}'

    return expression, answer
