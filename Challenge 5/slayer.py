print("Guess a six-digit number SLAYER so that following equation is true, where letter stands for the digit in the position shown: SLAYER + SLAYER + SLAYER = LAYERS")

def calculate(slayer):
    total = int(slayer+slayer+slayer)
    slayer=str(slayer)
    layers = int(slayer[1:]+slayer[0])
    return layers, total



def run():
    guess = int(input("Enter guess for SLAYER: "))
    layers,total = calculate(guess)
    if total != layers:
        print(f"Your guess is incorrect:")
    else:
        print(f"Your guess is correct:")
    print("SLAYER + SLAYER + SLAYER = {layers}")
    print(f"LAYERS = {layers}")
    print("Thanks for playing")
    
if __name__ == "__main__":
    run()
