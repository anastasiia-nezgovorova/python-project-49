import prompt

ROUNDS_AMOUNT = 3


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def run_game(task_text, game_func):
    print('Welcome to the Brain Games!')
    u_name = welcome_user()
    print(task_text)
    i = 1

    while i <= ROUNDS_AMOUNT:
        question, correct_answer = game_func()
        question = f'Question: {question}'
        print(question)
        answer = prompt.string('Your answer: ')

        if answer == correct_answer and i < ROUNDS_AMOUNT:
            i += 1
            print('Correct!')

        elif answer == correct_answer and i == ROUNDS_AMOUNT:
            print(f'Congratulations, {u_name}!')
            break
        else:
            i += 3
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")  # noqa: E501
            print(f"Let's try again, {u_name}!")
