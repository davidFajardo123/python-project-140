from brain_games.cli import welcome_user
from brain_games.cli import game_prime


def main():
    
    name = welcome_user()
    game_prime(name)
    

if __name__ == "__main__":
    main()
