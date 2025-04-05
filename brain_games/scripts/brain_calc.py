from brain_games.cli import welcome_user
from brain_games.cli import next_q
import random


# JUEGO CALC : CONDITION
def generate_expression():

    # Rnd de num 1
    num1 = random.randint(1, 50)
    # Rnd de num 2
    num2 = random.randint(1, 50)
    # Rnd operador entre opciones
    operator = random.choice(["+", "-", "*"])
    # Set expression
    expression = f"{num1} {operator} {num2}"
    # Evalúa la expresión matemática
    result = eval(expression)
    # Retorna expresion y resultado
    return expression, result


# JUEGO CALC : GAME
def game_calc(name):
    
    # Game message
    print("What is the result of the expression?")
    
    correct_answers = 0
    while correct_answers < 3:
        
        # Game variables + question
        expression, answer = generate_expression()
        print(f"Question: {expression}")
        
        # User input
        user_answer = input("Your answer: ").strip().lower()
        
        # Verify
        correct_answers = next_q(answer, user_answer, name, correct_answers)
  

def main():

    name = welcome_user()
    game_calc(name)
    

if __name__ == "__main__":
    main()