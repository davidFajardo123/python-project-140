from brain_games.cli import welcome_user
from brain_games.cli import game_gcd


def main():
    
    name = welcome_user()
    game_gcd(name)
    

if __name__ == "__main__":
    main()
