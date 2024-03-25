def prompt(message):            # abstracts prompts
    print(f'==> {message}')

def invalid_number(number_str): # checks for invalid operand input
    try:
        int(number_str)
    except ValueError:
        return True
    return False

prompt("Welcome to the Calculator Program!")

while True:
    prompt("What's the first number? ")
    number1 = input()
    
    while invalid_number(number1):
        prompt("Hmm, that doesn't look like a valid number")
        number1 = input()

    prompt("What's the second number? ")
    number2 = input()

    while invalid_number(number2):
        prompt("Hmm, that doesn't look like a valid number")
        number2 = input()

    prompt("Select a number for the operation you would like to perform\n"
           "1) Add 2) Subtract 3) Multiply 4) Divide")
    operation = input()

    while operation not in ['1', '2', '3', '4']:
        prompt('Please choose 1, 2, 3, or 4!')
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

    prompt(f'The result is: {output}')
    
    prompt(f'Do you want to perform more calculations?\n'
            'Please select "y" or "n".')
    retry = input()
    if retry != "y":
        break