import prompt

ROUNDS_AMOUNT = 3


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def main(task_text, game_func):
    print('Welcome to the Brain Games!')
    u_name = welcome_user()
    print(task_text)
    i = 1

    while i <= ROUNDS_AMOUNT:
        question_text, correct_answer = game_func()
        print(question_text)
        answer = prompt.string('Your answer: ')

        if answer == correct_answer:
            if i == ROUNDS_AMOUNT:
                print(f'Congratulations, {u_name}!')
            else:
                print('Correct!')
            i += 1
        else:
            i += 3
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")  # noqa: E501
            print(f"Let's try again, {u_name}!")
