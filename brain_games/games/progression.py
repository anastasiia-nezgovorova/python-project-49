from random import randint, choice


RULE = 'What number is missing in the progression?'
FIRST_BORDER_OF_LEN = 5
SECOND_BORDER_OF_LEN = 10
START_BORDER_OF_RANDOM = -100
END_BORDER_OF_RANDOM = 100


def choose_operator():
    operators_set = ("+", "-")
    random_operator = choice(operators_set)
    return random_operator


def generate_step():
    step = randint(1, 10)
    return step


def generate_random_kit_for_progression():
    first_number = randint(START_BORDER_OF_RANDOM, END_BORDER_OF_RANDOM)
    step = generate_step()
    progression_length = randint(FIRST_BORDER_OF_LEN, SECOND_BORDER_OF_LEN)
    operator = choose_operator()
    return [first_number, step, progression_length, operator]


def set_progression(random_kit):
    first_number, step, progression_length, operator = random_kit
    progression = [first_number]

    for _ in range(1, progression_length):
        if operator == '+':
            next_number = first_number + step
        else:
            next_number = first_number - step

        progression.append(next_number)
        first_number = next_number

    return progression


def set_answer_and_stub(progression):
    ind_hidden_num = randint(0, len(progression) - 1)
    answer = str(progression[ind_hidden_num])
    return [answer, ind_hidden_num]


def set_progression_and_answer():
    progression = set_progression(generate_random_kit_for_progression())
    [answer, hidden_number_index] = set_answer_and_stub(progression)
    progression[hidden_number_index] = '..'

    progression_text = ' '.join(map(str, progression))

    return progression_text, answer
