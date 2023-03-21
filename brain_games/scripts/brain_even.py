#!/usr/bin/env python3
import random
import prompt
import brain_games.scripts.brain_games
import brain_games.cli


def main():  # noqa: C901
    brain_games.scripts.brain_games.main()
    text_of_exr = 'Answer "yes" if the number is even, otherwise answer "no".'
    print(text_of_exr)

    radius_of_random = (1, 100)
    i = 1
    num_of_rounds = 3
    correct_answer = ''

    while i <= num_of_rounds:
        rand_num = random.randint(radius_of_random[0], radius_of_random[1])
        text_of_question = f'Question: {rand_num}'
        print(text_of_question)
        answer = prompt.string('Your answer: ')

        if (rand_num % 2) == 0 and answer.lower() == 'yes':
            if i == num_of_rounds:
                print(f'Congratulations, {brain_games.cli.name}!')
            else:
                print('Correct!')
            i += 1
        elif (rand_num % 2) != 0 and answer.lower() == 'no':
            if i == num_of_rounds:
                print(f'Congratulations, {brain_games.cli.name}!')
            else:
                print('Correct!')
            i += 1
        else:
            if answer == 'yes':
                correct_answer = 'no'
            if answer == 'no':
                correct_answer = 'yes'
            i += 3
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")  # noqa: E501
            print(f"Let's try again, {brain_games.cli.name}!")


if __name__ == '__main__':
    main()
