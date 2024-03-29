import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']
WINNING_COMBINATIONS = {'rock': ['scissors', 'lizard'],
                        'scissors': ['paper', 'lizard'],
                        'paper': ['rock', 'spock'],
                        'lizard': ['spock', 'paper'],
                        'spock': ['scissors', 'rock']
}
def prompt(message):
    print(f'==> {message}')

def display_winner(choice, computer_choice):
    prompt(calculate_winner(choice, computer_choice))

def calculate_winner(choice, computer_choice):
    if choice == computer_choice:
        return "It's a tie!"

    if computer_choice in WINNING_COMBINATIONS[choice]:
        return 'winner'
        
    return 'loser'

while True:
    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    choice = input()
    while choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        choice = input()

    computer_choice = random.choice(VALID_CHOICES)

    prompt(f'You chose {choice}, computer chose {computer_choice}')

    display_winner(choice, computer_choice)

    prompt("Do you want to play again (y/n)?")
    answer = input().lower()
    while True:
        if answer.startswith('n') or answer.startswith('y'):
            break

        prompt("Please enter 'y' or 'n'.")
        answer = input().lower()

    if answer[0] == 'n':
        break