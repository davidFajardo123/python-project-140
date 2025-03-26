# ----------------- DEP ------------------
import prompt


# Funcion welcome user ---------------------------
def welcome_user():
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name