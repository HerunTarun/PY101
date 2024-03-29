import random

VALID_CHOICES = ['rock', 'paper', 'scissors']

def prompt(message):
    print(f'==> {message}')

def display_winner():
    if ((choice == 'rock' and computer_choice == 'scissors') or
        (choice == 'scissors' and computer_choice == 'paper') or
        (choice == 'paper' and computer_choice == 'rock')):
            prompt('You win!')
    elif ((choice == 'rock' and computer_choice == 'paper') or
        (choice == 'scissors' and computer_choice == 'rock') or
        (choice == 'paper' and computer_choice == 'scissors')):
            prompt('Computer wins!')
    else:
        prompt("It's a tie!")

while True:
    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    choice = input()
    while choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        choice = input()

    computer_choice = random.choice(VALID_CHOICES)

    prompt(f'You chose {choice}, computer chose {computer_choice}')

    display_winner()

    prompt("Do you want to play again (y/n)?")
    answer = input().lower()
    while True:
        if answer.startswith('n') or answer.startswith('y'):
            break

        prompt("Please enter 'y' or 'n'.")
        answer = input().lower()

    if answer[0] == 'n':
        break