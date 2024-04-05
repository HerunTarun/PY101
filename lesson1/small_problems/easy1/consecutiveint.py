while True:
    integer = int(input('Please enter an integer greater than 0: '))
    if integer > 0:
        break
    else:
        print('Please enter a valid number!')
        
while True:
    process = input("Enter 's' to compute the sum, or 'p' to compute the product: ")
    if process == 's' or process == 'p':
        break
    else:
        print('Please enter either "s" or "p"')
print()

if process == 's':
    total = 0  # sum(range(1, integer + 1)) would also work
    for num in range(integer + 1):
        total += num
    print(f'The sum of the integers between 1 and {integer} is {total}')
elif process == 'p':
    total = 1
    for num in range(1, integer + 1):
        total *= num
    print(f'The product of the integers betwen 1 and {integer} is {total}')
    
# Further Exploration
while True:
    integers = input('Please enter integers above zero separated by spaces: ')
    integer_list = integers.split(' ')
    for num in integer_list:
        if int(num) > 0 and num.isdigit():
            continue
        else:
            print('Please enter valid integers!')
    break

while True:
    process = input("Enter 's' to compute the sum, or 'p' to compute the product: ")
    if process == 's' or process == 'p':
        break
    else:
        print('Please enter either "s" or "p"')
print()
if process == 's':
    total = 0 
    for num in integer_list:
        total += int(num)
    print(f'The sum of the integers is {total}')
elif process == 'p':
    total = 1
    for num in integer_list:
        total *= int(num)
    print(f'The product of the integers is {total}')
    
    
