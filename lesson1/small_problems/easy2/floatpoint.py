def operation(num1, num2):
    add = num1 + num2
    sub = num2 - num2
    prod = num1 * num2
    quo = num1 / num2
    floquo = num1 // num2
    modu = num1 % num2
    expo = num1 ** num2
    
    print(f'{num1} + {num2} = {add}')
    print(f'{num1} - {num2} = {sub}')
    print(f'{num1} * {num2} = {prod}')
    print(f'{num1} / {num2} = {quo}')
    print(f'{num1} // {num2} = {floquo}')
    print(f'{num1} % {num2} = {modu}')
    print(f'{num1} ** {num2} = {expo}')

float1 = float(input('==> Enter the first number: '))
float2 = float(input('==> Enter the second number: '))

# while True:
#     float1 = input('==> Enter the first number: ')
#     if float1.isdecimal() == True:
#         float(float1)
#         break
#     else:
#         print('Please enter a valid input!')
# while True:
#     float2 = input('==> Enter the second number: ')
#     if float2.isdecimal() == True:
#         float(float2)
#         break
#     else:
#         print('Please enter a valid input!')
        
operation(float1, float2)