from brain_games.cli import *


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


def main():
    
    name = welcome_user()
    game_progresion(name)
    

if __name__ == "__main__":
    main()