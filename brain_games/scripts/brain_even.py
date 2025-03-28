# ----------------------- DEP -----------------------------
from brain_games.cli import welcome_user


# Main -------------------------------------------------------
def main():
    
    # import
    import random
    
    # variables
    correct_answers = 0                                                     # Contador de respuestas correctas
    
    print("Welcome to the Brain Games!")                                    # Welcome message
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')     # message only 1 time

    # main loop
    while correct_answers < 3:                               # Se requieren 3 respuestas correctas seguidas
        number = random.randint(1, 100)                      # Genera un número aleatorio entre 1 y 100
        print(f"Question: {number}")                         # Nostrar el numero a verificar 
        user_answer = input("Your answer: ").strip().lower() # Esperar respuesta del usuario
        
        if number%2==0:                                      # Condicional para saber si el numero es par o no
            answer = "yes"                                   # Si es par respuesta "yes"
        else:
            answer = "no"                                    # Si es impar respuesta "no"
            
        if answer == user_answer:                            # Condicional para saber si estan bien las respuestas
            correct_answers+=1                               # Se aumenta en 1 el numero de preguntas acertadas 
            print("Correct!")                                # Se muestra el mensaje de correcto
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{answer}'.") # Devuelve mensaje de mala respuesta
            print(f"Let's try again, {name}!")
            return False                                                                 # Se sale
        
        if correct_answers == 3:
            print(f"Congratulations, {name}!")
            
    return True                                              # Devuelve "True" si contesta las 3 seguidas y salio del ciclo
        

# ----------------------------- MAIN ----------------------------|
if __name__ == "__main__":
    main()