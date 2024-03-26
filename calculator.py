import json

def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True
    return False

def language_choice():
    language = 'en'
    prompt("Choose a language: english or francais")
    language = input().strip()

    while language not in ['english', 'francais']:
        prompt("Try either 'english' or 'francais'!\n"
           "Essayez « english » ou « francais »!")
        language = input().strip()

    match language:
        case 'english':
            language = 'en'
        case 'francais':
            language = 'fr'
    
    return language

def obtaining_numbers():
    prompt(data['first'])
    number1 = input().strip()

    while invalid_number(number1):
        prompt(data['invalid_num'])
        number1 = input().strip()

    prompt(data['second'])
    number2 = input().strip()

    while invalid_number(number2):
        prompt(data['invalid_num'])
        number2 = input().strip()
    
    return number1, number2 

def invalid_division(num1, num2):
    try:
        float(num1) / float(num2)
    except ZeroDivisionError:
        return True
    return False

def the_calculator():
    number1, number2 = obtaining_numbers()

    prompt(data['select'])
    operation = input().strip()

    while operation not in ['1', '2', '3', '4']:
        prompt(data['invalid_select'])
        operation = input().strip()

    match operation:
        case '1':     # 1 represents addition
            output = float(number1) + float(number2)
        case '2':     # 2 represents subtraction
            output = float(number1) - float(number2)
        case '3':      # 3 represents multiplication
            output = float(number1) * float(number2)
        case '4':      # 4 represents division
            while invalid_division(number1, number2):
                prompt(data['invalid_division'])
                number1, number2 = obtaining_numbers()
            
            output = float(number1) / float(number2)

    prompt(data['result'] + f'{output:.2f}')

with open ('calculator_messages.json', 'r') as file:
    data = json.load(file)[language_choice()]

prompt(data['start'])

while True:
    the_calculator()

    prompt(data['again'])
    
    retry = input()
    if retry != 'y':
        break


# Improvements
# X error response for invalid language selection rather than case _
# X divide by zero error
# X accounting for white space in input