print('Welcome to Calculator!')

# Ask the user for the first number
number1 = int(input("What's the first number? "))

# Ask the user for the second number
number2 = int(input("What's the second number? "))

# Ask the user for an operation to perform
operation = input("Select a number for the operation you would like\n"
                "1) Add 2) Subtract 3) Multiply 4) Divide\n")

# Perform the operation on the two numbers
if operation == '1':
    output = number1 + number2
elif operation == '2':
    output = number1 - number2
elif operation == '3':
    output = number1 * number2
elif operation == '4':
    output = number1 / number2

# Print the result to the terminal
print(f'The result is: {output}')
