# length = input('Please enter the length of the room in meters: ')
# width = input('Please enter the width of the room in meters: ')

# while length == '' or width == '':
#     print('Please enter a value when you run the program!')
#     length = input('Please enter the length of the room in meters: ')
#     width = input('Please enter the width of the room in meters: ')

# area_m = float(length) * float(width)
# area_f = area_m * 10.7639

# print(f'Your area in square meters is {area_m}.') 
# print(f'Your area in square feet is {area_f}.')

# remember that you can add {:.2f} to correct to two decimal places

# Further Exploration
while True:
    unit = input("Type 'feet' or 'meters' to specify what unit you would like to use: ").lower()
    if unit == 'feet' or unit == 'meters':
        break
    else:
        print("Please check your units. I need either 'feet' or 'meters'!")
    
while True:
    length = float(input('Please enter the length of the room: '))
    width = float(input('Please enter the width of the room: '))
    if length == '' or width == '':
        print('Please enter a value!')
    elif length > 0 and width > 0:
        break
    else:
        print('Please enter a valid value!')

area = length * width

if unit == 'meters':
    convert_tof = area * 10.7639
    print(f'Your area in square meters is {area:.2f}.')
    print(f'Your area in square feet is {convert_tof:.2f}.')
elif unit == 'feet':
    convert_tom = area / 10.7639
    print(f'Your area in square feet is {area:.2f}.')
    print(f'Your area in square meters is {convert_tom:.2f}.')