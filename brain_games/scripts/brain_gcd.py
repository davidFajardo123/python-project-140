import random
import math
from brain_games.cli import welcome_user


# Funcion para generar numeros aleatorios y mcd 
def generate_numbers():
    
    # Rnd num 1
    num1 = random.randint(1, 100)
    # Rnd num 2
    num2 = random.randint(1, 100)
    # Calcula el MCD con la funcion gcd
    gcd_result = math.gcd(num1, num2)
    # Retorna los numeros y el mcd
    return num1, num2, gcd_result


def main():
    
    # Mensaje inicio
    print("Welcome to the Brain Games!")
    # Func welcome
    name = welcome_user()
    # Mensaje de juego
    print("Find the greatest common divisor of given numbers.")
    # Contador preguntas
    correct_answers = 0
    # ciclo preguntas
    while correct_answers < 3:
        # Llamado a funcion de mcd
        num1, num2, correct_gcd = generate_numbers()
        # Mostrar los numeros random
        print(f"Question: {num1} {num2}")
        # Esperar respuesta del usuario
        user_answer = input("Your answer: ").strip()
        # Verificar respuesta
        if user_answer == str(correct_gcd):
            print("Correct!")
            # Contador de pregunta correcta
            correct_answers += 1
        else:
            print((
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_gcd}'."
            ))
            print(f"Let's try again, {name}!")
            # Termina el juego si hay un error
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
