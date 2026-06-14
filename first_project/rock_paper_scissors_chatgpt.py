import random
options = ["rock", "paper", "scissors"]
rules = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

while True:
    player_choice = input("Choose rock, paper, or scissors: ").lower()
    if player_choice not in options:
        print("Invalid choice. Please try again.")
        continue
    computer_choice = random.choice(options)
    print(f"Player's choice: {player_choice}")
    print(f"Computer's choice: {computer_choice}")
    if player_choice == computer_choice:
        print("It's a tie!")
    elif rules.get(player_choice) == computer_choice:
        print("You win!")
    else:
        print("You lose!")
