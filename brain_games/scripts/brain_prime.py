from brain_games.cli import *


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


def main():
    
    name = welcome_user()
    game_prime(name)
    

if __name__ == "__main__":
    main()
