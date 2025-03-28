import random
import math
from brain_games.cli import welcome_user

# Funcion para generar numeros aleatorios y mcd 
def generate_numbers():
    
    num1 = random.randint(1, 100)       # Rnd num 1
    num2 = random.randint(1, 100)       # Rnd num 2
    gcd_result = math.gcd(num1, num2)   # Calcula el MCD con la funcion gcd

    return num1, num2, gcd_result       # Retorna los numeros y el mcd


def main():
    print("Welcome to the Brain Games!")                            # Mensaje inicio
    name = welcome_user()                                           # Func welcome
    print("Find the greatest common divisor of given numbers.")     # Mensaje de juego

    correct_answers = 0                                             # Contador preguntas

    while correct_answers < 3:                                      # ciclo preguntas
        num1, num2, correct_gcd = generate_numbers()                # Llamado a funcion de mcd
        print(f"Question: {num1} {num2}")                           # Mostrar los numeros random
        user_answer = input("Your answer: ").strip()                # Esperar respuesta del usuario

        if user_answer == str(correct_gcd):                         # Verificar respuesta
            print("Correct!")                                       
            correct_answers += 1                                    # Contador de pregunta correcta
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_gcd}'.")   
            print(f"Let's try again, {name}!")
            return                                                  # Termina el juego si hay un error

    print(f"Congratulations, {name}!")                              


if __name__ == "__main__":
    main()
