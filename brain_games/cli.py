# ----------------- DEP ------------------
import prompt
import random
import math


# WELCOME USER
def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


# JUEGO DE PARES 
def game_even(name):
    
    correct_answers = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    
    while correct_answers < 3:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        user_answer = input("Your answer: ").strip().lower()
        if (number % 2 == 0):
            answer = "yes"
        else:
            answer = "no"

        if answer == user_answer:
            correct_answers += 1
            print("Correct!")
        else:
            print((
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{answer}'."
            ))
            print(f"Let's try again, {name}!")
            exit()
        
        if correct_answers == 3:
            print(f"Congratulations, {name}!")
            exit()


# JUEGO CALC
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


def game_calc(name):
    
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
    

# JUEGO MCD 
def generate_numbers():
    
    # Rnd num 1
    num1 = random.randint(1, 100)
    # Rnd num 2
    num2 = random.randint(1, 100)
    # Calcula el MCD con la funcion gcd
    gcd_result = math.gcd(num1, num2)
    # Retorna los numeros y el mcd
    return num1, num2, gcd_result
    

def game_gcd(name):
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
    
    
# JUEGO PROGRESION
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


def game_progresion(name):
    
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
            print((
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            ))
            print(f"Let's try again, {name}!")
            # Termina el juego si hay un error
            return

    print(f"Congratulations, {name}!")

# JUEGO PRIMO 
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


def game_prime(name):
    
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