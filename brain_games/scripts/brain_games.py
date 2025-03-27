# ----------------------- DEP -----------------------------
from brain_games.cli import welcome_user
#from brain_games.scripts.brain_even import main as brain_even


# Main -------------------------------------------------------
def main():
    
    # variables 
    name = ''
    responses = ''
    
    # --------------------- START GAME ---------------------------
    print("Welcome to the Brain Games!")        # Welcome message
    welcome_user()
    #name = welcome_user()                       # Cli.py
    #responses = brain_even()                    # brain_even.py
    
    #if responses == True:
    #    print(f"Congratulations, {name}!")       # El usuario gano el juego de pares
    #else:
    #    print(f"Let's try again, {name}!")       # El usuario perdio el juego de pares
        
    # siguiente pregunta
    

# ----------------------------- MAIN ----------------------------|
if __name__ == "__main__":
    main()
