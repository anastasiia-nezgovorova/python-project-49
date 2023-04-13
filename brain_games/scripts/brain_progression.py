#!/usr/bin/env python3
import brain_games.game_engine
from brain_games.games.progression import set_progression

task = 'What number is missing in the progression?'


def main():
    brain_games.game_engine.main(task, set_progression)


if __name__ == '__main__':
    main()
