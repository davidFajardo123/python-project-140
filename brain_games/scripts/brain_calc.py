from brain_games.cli import welcome_user
from brain_games.cli import game_calc


def main():

    name = welcome_user()
    game_calc(name)
    

if __name__ == "__main__":
    main()