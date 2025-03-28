import random
from brain_games.cli import welcome_user

# Funcion para generar progresion aritmetica
def generate_progression():
    # Número inicial
    start = random.randint(1, 20)
    # Paso de la progresión
    step = random.randint(2, 10)
    # Longitud de la progresión
    length = random.randint(5, 10)
    # Calcular progresion correcta
    progression = [start + step * i for i in range(length)]
    # Poner un num random de la secuencia
    hidden_index = random.randint(0, length - 1)
    # Sacar correcta
    correct_answer = progression[hidden_index]
    # Reemplaza el número oculto con '..'
    progression[hidden_index] = ".."
    # Progresion final
    progression_str = " ".join(map(str, progression))
    # Devolver progresion con caracter oculto
    return progression_str, str(correct_answer)


def main():
    # Mensaje de inicio
    print("Welcome to the Brain Games!")
    # Guarda el nombre del jugador
    name = welcome_user()
    # Mensaje de juego
    print("What number is missing in the progression?")
    
    # Cont de preguntas
    correct_answers = 0
    
    # Ciclo preguntas
    while correct_answers < 3:
        # Llama a la funcion de progresion aritmetica
        progression_str, correct_answer = generate_progression()
        # Mostrar regresion
        print(f"Question: {progression_str}")
        # Esperar respuyesta usuario
        user_answer = input("Your answer: ").strip()

        if user_answer == correct_answer:
            print("Correct!")
            # Contador de respuestas correctas
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            # Termina el juego si hay un error
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()