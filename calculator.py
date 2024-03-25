import json

def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True
    return False

language = 'en'

prompt("Choose a language: english, francais")

case language:
    match 'english':
        language = 'en'
    match 'francais':
        language = 'fr'
    match _:
        pass


with open ('calculator_messages.json', 'r') as file:
    data = json.load(file)

prompt(data['start'])

while True:
    prompt(data['first'])
    number1 = input()
    
    while invalid_number(number1):
        prompt(data["invalid_num"])
        number1 = input()

    prompt(data['second'])
    number2 = input()

    while invalid_number(number2):
        prompt(data["invalid_num"])
        number2 = input()

    prompt(data["select"])
    operation = input()

    while operation not in ['1', '2', '3', '4']:
        prompt(data['invalid_select'])
        operation = input()

    match operation:
        case '1':     # 1 represents addition
            output = int(number1) + int(number2)
        case '2':     # 2 represents subtraction
            output = int(number1) - int(number2)
        case '3':      # 3 represents multiplication
            output = int(number1) * int(number2)
        case '4':      # 4 represents division
            output = int(number1) / int(number2)

    prompt(data['result'] + f'{output}')
    
    prompt(data['again'])
    retry = input()
    if retry != "y":
        break