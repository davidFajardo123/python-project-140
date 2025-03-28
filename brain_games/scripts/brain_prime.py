import random
from brain_games.cli import welcome_user

# Funcion para saber el numero es primos
def is_prime(n):
    if n < 2:                               # Mirar si es divisible por 2
        return False
    for i in range(2, int(n ** 0.5) + 1):   # Evaluar cantidad de divisores
        if n % i == 0:                      # Verificar si la division es exacta
            return False
    return True


def main():
    print("Welcome to the Brain Games!")                            # Mensaje de inicio
    name = welcome_user()                                           # Guarda el nombre del jugador
    print('Answer "yes" if given number is prime. Otherwise answer "no".') # Mensaje del juego

    correct_answers = 0

    while correct_answers < 3:                                      # Ciclo de preguntas
        number = random.randint(1, 100)                             # Generar número aleatorio
        print(f"Question: {number}")
        user_answer = input("Your answer: ").strip().lower()        # Esperar respuesta

        correct_answer = "yes" if is_prime(number) else "no"        # Sacar respuesta correcta llamando a la funcion

        if user_answer == correct_answer:                           # Comparar respuesta
            print("Correct!")
            correct_answers += 1                                    # Contador respuestas correctas
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return                                                  # Termina el juego si hay un error

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
