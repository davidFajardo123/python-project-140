from brain_games.cli import welcome_user
from brain_games.cli import game_even


def main():

    name = welcome_user()
    game_even(name)


if __name__ == "__main__":
    main()