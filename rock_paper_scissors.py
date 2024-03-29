import json
import random
import os

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']
WINNING_COMBINATIONS = {'rock': ['scissors', 'lizard'],
                        'scissors': ['paper', 'lizard'],
                        'paper': ['rock', 'spock'],
                        'lizard': ['spock', 'paper'],
                        'spock': ['scissors', 'rock']
}

def prompt(message):
    print(f'==> {message}')

def print_welcome():
    # add welcoming message and description
    prompt(messages['welcome'])
    prompt(messages['game_rules'])

def obtain_input():
    # add input
    prompt('placeholder')

def check_input():
    # add input validation
    prompt('plcaeholder')

def calculate_winner(choice, computer_choice):
    if choice == computer_choice:
        return messages['tie']

    if computer_choice in WINNING_COMBINATIONS[choice]:
        return messages['win']
        
    return messages{'lose']

def print_winner(choice, computer_choice):
    prompt(calculate_winner(choice, computer_choice))

def play_again():
    # add play again function
    prompt('placeholder')

with open('rps_messages.json', 'r') as file:
    messages = json.load(file)

while True:
    print_welcome()
    
    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    choice = input()
    while choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        choice = input()

    computer_choice = random.choice(VALID_CHOICES)

    prompt(f'You chose {choice}, computer chose {computer_choice}')

    print_winner(choice, computer_choice)

    prompt("Do you want to play again (y/n)?")
    answer = input().lower()
    while True:
        if answer.startswith('n') or answer.startswith('y'):
            break

        prompt("Please enter 'y' or 'n'.")
        answer = input().lower()

    if answer[0] == 'n':
        break
    
# TODO
# X restructure program to use functions
# add json file for messages
# Add clear screen
# add goodbye message
# add help function
# add shortened input bonus feature
# add best of five bonus feature
# clear todo when done with code
# clean up pylint comments

