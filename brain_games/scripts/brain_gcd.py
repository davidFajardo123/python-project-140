from brain_games.cli import welcome_user
from brain_games.cli import next_q
import random
import math


# JUEGO GCD : CONDITION
def generate_numbers():
    
    # Rnd num 1
    num1 = random.randint(1, 100)
    # Rnd num 2
    num2 = random.randint(1, 100)
    # Calcula el MCD con la funcion gcd
    gcd_result = math.gcd(num1, num2)
    # Retorna los numeros y el mcd
    return num1, num2, gcd_result
    
    
# JUEGO GCD : GAME
def game_gcd(name):
    
    # Game message
    print("Find the greatest common divisor of given numbers.")
    
    correct_answers = 0
    while correct_answers < 3:
        
        # Game variables + question
        num1, num2, answer = generate_numbers()
        print(f"Question: {num1} {num2}")
        
        # user input
        user_answer = input("Your answer: ").strip()
        
        # Verify
        correct_answers = next_q(answer, user_answer, name, correct_answers)
        
        
        
def main():
    
    name = welcome_user()
    game_gcd(name)
    

if __name__ == "__main__":
    main()
