# --------------------- DEP -----------------------------------------------
import random
from brain_games.cli import welcome_user

# Funcion que genera una expresión matemática aleatoria y su resultado -------------
def generate_expression():
    
    num1 = random.randint(1, 50)                # Rnd de num 1
    num2 = random.randint(1, 50)                # Rnd de num 2
    operator = random.choice(["+", "-", "*"])

    expression = f"{num1} {operator} {num2}"
    result = eval(expression)                   # Evalúa la expresión matemática

    return expression, result                   # Retorna expresion y resultado

# Main ---------------------------------------------------------------------------------
def main():
    
    print("Welcome to the Brain Games!")             
    name = welcome_user()                                    # Guarda el nombre del jugador
    print("What is the result of the expression?")  

    correct_answers = 0                                      # Cont de preguntas

    while correct_answers < 3:                               # Ciclo de preguntas
        expression, correct_result = generate_expression()   # Llamado a la funcion para generar expresion
        print(f"Question: {expression}")
        user_answer = input("Your answer: ").strip()         # Esperando respuesta del usuario

        if user_answer == str(correct_result):               # Evalua si es la misma respuesta
            print("Correct!")
            correct_answers += 1                             # Aumenta el contador
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_result}'.")
            print(f"Let's try again, {name}!")
            return                                          # Termina el juego si hay un error

    print(f"Congratulations, {name}!")                      # Mensaje final 

# ------------------------- MAIN ---------------------------------------------
if __name__ == "__main__":
    main()
