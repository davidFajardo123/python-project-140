from brain_games.cli import welcome_user


def main():

    import random
    correct_answers = 0
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    while correct_answers < 3:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        user_answer = input("Your answer: ").strip().lower()
        if (number%2==0):
            answer = "yes"
        else:
            answer = "no"

        if answer == user_answer:
            correct_answers+=1
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{answer}'.")
            print(f"Let's try again, {name}!")
            exit()
        
        if correct_answers == 3:
            print(f"Congratulations, {name}!")
            exit()


if __name__ == "__main__":
    main()