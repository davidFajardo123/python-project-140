import random
from brain_games.cli import welcome_user
import prompt

# Funcion para saber el numero es primos
def is_prime(n):
    
    # Mirar si es divisible por 2
    if n < 2:
        return False
    # Evaluar cantidad de divisores
    for i in range(2, int(n ** 0.5) + 1):
        # Verificar si la division es exacta
        if n % i == 0:
            return False
    return True


def main():
    
    # Mensaje de inicio
    print("Welcome to the Brain Games!")
    # Guarda el nombre del jugador
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    # Mensaje del juego
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    correct_answers = 0
    # Ciclo de preguntas
    while correct_answers < 3:
        # Generar número aleatorio
        number = random.randint(1, 100)
        print(f"Question: {number}")
        # Esperar respuesta
        user_answer = input("Your answer: ").strip().lower()
        # Sacar respuesta correcta llamando a la funcion
        correct_answer = "yes" if is_prime(number) else "no"
        # Comparar respuesta
        if user_answer == correct_answer:
            print("Correct!")
            # Contador respuestas correctas
            correct_answers += 1
        else:
            print((
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            ))
            print(f"Let's try again, {name}!")
            # Termina el juego si hay un error
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
