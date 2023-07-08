import random
from colorama import Fore

computer_number = random.randint(1, 100)

while True:
    player_input = input(Fore.BLUE + "Guess the number (1, 100): ")
    if not player_input.isdigit():
        print(Fore.RED + "Invalid input. Try again...")
        continue
    player_input = int(player_input)
    if player_input == computer_number:
        print(Fore.GREEN + "You guess it!")
        break
    elif player_input > computer_number:
        print(Fore.LIGHTYELLOW_EX + "Too High!")
    else:
        print(Fore.LIGHTYELLOW_EX + "Too Low!")