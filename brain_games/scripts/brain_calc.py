#!/usr/bin/env python3
from brain_games.game_engine import main as engine_main
from brain_games.games import set_expression_for_calc

task = 'What is the result of the expression?'


def main():
    engine_main(task, set_expression_for_calc)


if __name__ == '__main__':
    main()
