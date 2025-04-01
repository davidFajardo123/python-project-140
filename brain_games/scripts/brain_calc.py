import random
import prompt


# Funcion genera expresión math rand y su resultado
def generate_expression():

    # Rnd de num 1
    num1 = random.randint(1, 50)
    # Rnd de num 2
    num2 = random.randint(1, 50)
    operator = random.choice(["+", "-", "*"])

    expression = f"{num1} {operator} {num2}"
    # Evalúa la expresión matemática
    result = eval(expression)
    # Retorna expresion y resultado
    return expression, result


def main():

    print("Welcome to the Brain Games!")
    # Guarda el nombre del jugador
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print("What is the result of the expression?")
    # Cont de preguntas
    correct_answers = 0
    
    # Ciclo de preguntas
    while correct_answers < 3:
        # Llamado a la funcion para generar expresion
        expression, correct_result = generate_expression()
        print(f"Question: {expression}")
        # Esperando respuesta del usuario
        user_answer = input("Your answer: ").strip()
        # Evalua si es la misma respuesta
        if user_answer == str(correct_result):
            print("Correct!")
            # Aumenta el contador
            correct_answers += 1
        else:
            print((
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_result}'."
            ))
            print(f"Let's try again, {name}!")
            # Termina el juego si hay un error
            return

    # Mensaje final
    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()