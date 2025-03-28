# ----------------------- DEP -----------------------------
from brain_games.cli import welcome_user


# Main -------------------------------------------------------
def main():
    
    # import
    import random
    
    # Contador de respuestas correctas
    correct_answers = 0                                                     
    # Welcome message
    print("Welcome to the Brain Games!")                                    
    name = welcome_user()
    # message only 1 time
    print('Answer "yes" if the number is even, otherwise answer "no".')     

    # Se requieren 3 respuestas correctas seguidas
    while correct_answers < 3:
        # Genera un número aleatorio entre 1 y 100                              
        number = random.randint(1, 100)
        # Nostrar el numero a verificar                      
        print(f"Question: {number}")
        # Esperar respuesta del usuario
        user_answer = input("Your answer: ").strip().lower()
        # Condicional para saber si el numero es par o no
        if number%2==0:
            # Si es par respuesta "yes"                                   
            answer = "yes"                                   
        else:
            # Si es impar respuesta "no"
            answer = "no"                                    

        # Condicional para saber si estan bien las respuestas
        if answer == user_answer:
            # Se aumenta en 1 el numero de preguntas acertadas                            
            correct_answers+=1
            # Se muestra el mensaje de correcto                               
            print("Correct!")                                
        else:
            # Devuelve mensaje de mala respuesta
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{answer}'.") 
            print(f"Let's try again, {name}!")
            
            exit()
            
        if correct_answers == 3:
            print(f"Congratulations, {name}!")
            
            exit()
             
# ----------------------------- MAIN ----------------------------|
if __name__ == "__main__":
    
    main()
    