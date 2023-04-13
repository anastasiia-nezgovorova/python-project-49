from random import randint


def generate_rand_num():
    radius_of_random = (-100, 100)
    rand_num = randint(radius_of_random[0], radius_of_random[1])
    return rand_num


def choose_oper():
    operators_set = ("+", "-")
    index_radius = (0, len(operators_set) - 1)
    rand_oper = operators_set[randint(index_radius[0], index_radius[1])]
    return rand_oper


def generate_step():
    radius_of_random = (1, 10)
    step = randint(radius_of_random[0], radius_of_random[1])
    return step


def set_progression():  # noqa: C901
    step = generate_step()
    oper = choose_oper()
    first_numb = generate_rand_num()
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
