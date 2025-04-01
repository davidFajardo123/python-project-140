import prompt
import random
import math


# GEN : WELCOME USER
def welcome_user():
    
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


# GEN : CORRECT ANSWER
def ans_correct(correct_answers):
    
    correct_answers += 1
    print("Correct!")
    return correct_answers


# GEN : WRONG ANSWER
def fail(user_answer, answer, name):
    
    print((
        f"'{user_answer}' is wrong answer ;(. "
        f"Correct answer was '{answer}'."
    ))
    print(f"Let's try again, {name}!")
    exit()


# GEN : CONGRATS USER
def congrats(correct_answers, name):
    
    if correct_answers == 3:
        print(f"Congratulations, {name}!")
        exit()
    

# GEN : NEXT QUESTION CONDITION
def next_q(answer, user_answer, name, correct_answers):
    
    # Next question condition
    if str(answer) == str(user_answer):
        correct_answers = ans_correct(correct_answers)
    else:
        fail(user_answer, answer, name)
    
    congrats(correct_answers, name)
    return correct_answers
        
        
# JUEGO DE PARES 
def game_even(name):
          
    # Game message
    print('Answer "yes" if the number is even, otherwise answer "no".')
    
    correct_answers = 0
    while correct_answers < 3:
        
        # Game variables + question
        number = random.randint(1, 100)
        print(f"Question: {number}")
        
        # User input
        user_answer = input("Your answer: ").strip().lower()
        
        # Game condition
        if (number % 2 == 0):
            answer = "yes"
        else:
            answer = "no"
        
        # Verify
        correct_answers = next_q(answer, user_answer, name, correct_answers)


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
    

# JUEGO GCD : CONDITION
def generate_numbers():
    
    # Rnd num 1
    num1 = random.randint(1, 100)
    # Rnd num 2
    num2 = random.randint(1, 100)
    # Calcula el MCD con la funcion gcd
    gcd_result = math.gcd(num1, num2)
    # Retorna los numeros y el mcd
    return num1, num2, gcd_result
    

# JUEGO GCD : GAME
def game_gcd(name):
    
    # Game message
    print("Find the greatest common divisor of given numbers.")
    
    correct_answers = 0
    while correct_answers < 3:
        
        # Game variables + question
        num1, num2, answer = generate_numbers()
        print(f"Question: {num1} {num2}")
        
        # user input
        user_answer = input("Your answer: ").strip()
        
        # Verify
        correct_answers = next_q(answer, user_answer, name, correct_answers)
        
        
# JUEGO PROGRESION : CONDITION
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


# JUEGO PROGRESION : GAME
def game_progresion(name):
    
    # Game message
    print("What number is missing in the progression?")
    
    correct_answers = 0
    while correct_answers < 3:
        
        # Game variables + question
        progression_str, answer = generate_progression()
        print(f"Question: {progression_str}")
        
        # user input
        user_answer = input("Your answer: ").strip()

        # Verify
        correct_answers = next_q(answer, user_answer, name, correct_answers)


# JUEGO PRIMO : CONDITION
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


# JUEGO PRIMO : GAME
def game_prime(name):
    
    # Game message
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    correct_answers = 0
    while correct_answers < 3:
        
        # Game variables + question
        number = random.randint(1, 100)
        answer = "yes" if is_prime(number) else "no"
        print(f"Question: {number}")
        
        # user input
        user_answer = input("Your answer: ").strip().lower()
        
        # Verify
        correct_answers = next_q(answer, user_answer, name, correct_answers)