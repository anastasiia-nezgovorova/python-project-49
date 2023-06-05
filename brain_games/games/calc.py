from random import randint


TASK = 'What is the result of the expression?'
START_BORDER_OF_RANDOM = -100
END_BORDER_OF_RANDOM = 100


def choose_operator():
    operators_set = ("*", "+", "-")
    index_radius = (0, len(operators_set) - 1)
    rand_oper = operators_set[randint(index_radius[0], index_radius[1])]
    return rand_oper


def set_expression():
    radius = (START_BORDER_OF_RANDOM, END_BORDER_OF_RANDOM)
    first_numb = randint(radius[0], radius[1])
    second_numb = randint(radius[0], radius[1])

    oper = choose_operator()

    expression = [first_numb, oper, second_numb]

    return expression


def set_answer(first_numb, oper, second_numb):
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
    answer = str(set_answer(first_num, oper, second_num))

    return expression, answer
