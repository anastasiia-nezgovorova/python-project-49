from random import randint


TASK = 'What number is missing in the progression?'


FIRST_BORDER_OF_LEN = 5
SECOND_BORDER_OF_LEN = 10


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
    start_border_of_random = -100
    end_border_of_random = 100
    radius = (start_border_of_random, end_border_of_random)
    first_numb = randint(radius[0], radius[1])
    second_numb = 0
    third_numb = 0

    step = generate_step()
    oper = choose_oper()

    if oper == '+':
        second_numb = first_numb + step
    if oper == '-':
        second_numb = first_numb - step

    progression = [first_numb, second_numb]
    progression_len = randint(FIRST_BORDER_OF_LEN, SECOND_BORDER_OF_LEN)

    while len(progression) < progression_len:
        if oper == '+':
            third_numb = second_numb + step
        if oper == '-':
            third_numb = second_numb - step

        progression.append(third_numb)
        second_numb = third_numb

    return progression


def set_answer_and_stub(progression):
    ind_hidden_num = randint(0, len(progression) - 1)
    answer = str(progression[ind_hidden_num])
    return [answer, ind_hidden_num]


def set_progression_and_answer():
    progression = set_progression()
    [answer, ind_hidden_numb] = set_answer_and_stub(progression)
    progression[ind_hidden_numb] = '..'

    progression_text = str(progression)
    progression_text = progression_text.replace("[", '')
    progression_text = progression_text.replace("]", '')
    progression_text = progression_text.replace("'", '')
    progression_text = progression_text.replace(",", '')

    return progression_text, answer
