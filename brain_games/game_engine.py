import prompt

ROUNDS_AMOUNT = 3


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def run_game(task_text, get_round_data):
    print('Welcome to the Brain Games!')
    user_name = welcome_user()
    print(task_text)
    i = 1
    answer = ''
    correct_answer = ''

    while i <= ROUNDS_AMOUNT:
        question, correct_answer = get_round_data()
        question = f'Question: {question}'
        print(question)
        answer = prompt.string('Your answer: ')

        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")  # noqa: E501
            print(f"Let's try again, {user_name}!")
            break

        if i == ROUNDS_AMOUNT:
            print(f'Congratulations, {user_name}!')
            break

        if i < ROUNDS_AMOUNT:
            i += 1
            print('Correct!')
