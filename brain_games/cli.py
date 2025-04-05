import prompt


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