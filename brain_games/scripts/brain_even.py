from brain_games.cli import welcome_user
from brain_games.cli import next_q
import random


# JUEGO DE PARES 
def game_even(name):
          
    # Game message
    print('Answer "yes" if the number is even, otherwise answer "no".')
    
    correct_answers = 0
    while correct_answers < 3:
        
        # Game variables + question
        number = random.randint(1, 100)
        print(f"Question: {number}")
        
        # User input
        user_answer = input("Your answer: ").strip().lower()
        
        # Game condition
        if (number % 2 == 0):
            answer = "yes"
        else:
            answer = "no"
        
        # Verify
        correct_answers = next_q(answer, user_answer, name, correct_answers)


def main():

    name = welcome_user()
    game_even(name)


if __name__ == "__main__":
    main()