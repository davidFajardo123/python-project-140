from brain_games.cli import welcome_user
from brain_games.cli import game_progresion


def main():
    
    name = welcome_user()
    game_progresion(name)
    

if __name__ == "__main__":
    main()