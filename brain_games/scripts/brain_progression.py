import random
from brain_games.cli import welcome_user

# Funcion para generar progresion aritmetica
def generate_progression():
    start = random.randint(1, 20)                            # Número inicial
    step = random.randint(2, 10)                             # Paso de la progresión
    length = random.randint(5, 10)                           # Longitud de la progresión

    progression = [start + step * i for i in range(length)]  # Calcular progresion correcta
    hidden_index = random.randint(0, length - 1)             # Poner un num random de la secuencia
    correct_answer = progression[hidden_index]               # Sacar correcta

    progression[hidden_index] = ".."                         # Reemplaza el número oculto con '..'
    progression_str = " ".join(map(str, progression))        # Progresion final

    return progression_str, str(correct_answer)              # Devolver progresion con caracter oculto


def main():
    print("Welcome to the Brain Games!")                                # Mensaje de inicio
    name = welcome_user()                                               # Guarda el nombre del jugador
    print("What number is missing in the progression?")                 # Mensaje de juego

    correct_answers = 0                                                 # Cont de preguntas

    while correct_answers < 3:                                          # Ciclo preguntas
        progression_str, correct_answer = generate_progression()        # Llama a la funcion de progresion aritmetica
        print(f"Question: {progression_str}")                           # Mostrar regresion
        user_answer = input("Your answer: ").strip()                    # Esperar respuyesta usuario

        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1                                        # Contador de respuestas correctas
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return                                                      # Termina el juego si hay un error

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()