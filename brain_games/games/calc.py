from random import randint


def choose_oper():
    operators_set = ("*", "+", "-")
    index_radius = (0, len(operators_set) - 1)
    rand_oper = operators_set[randint(index_radius[0], index_radius[1])]
    return rand_oper


def set_expression():
    start_border_of_random = -100
    end_border_of_random = 100
    radius = (start_border_of_random, end_border_of_random)
    first_numb = randint(radius[0], radius[1])
    second_numb = randint(radius[0], radius[1])

    oper = choose_oper()

    expression = [first_numb, oper, second_numb]

    return expression


def set_answer(expr):
    first_numb, oper, second_numb = expr
    answer = 0

    if oper == '*':
        answer = first_numb * second_numb
    if oper == '+':
        answer = first_numb + second_numb
    if oper == '-':
        answer = first_numb - second_numb

    return answer


def set_expression_and_answer():
    [first_num, oper, second_num] = set_expression()
    expression = f'{first_num} {oper} {second_num}'
    answer = str(set_answer([first_num, oper, second_num]))

    return expression, answer
