name = input("What's your name? ")

if name.endswith('!'):
    print(f'HELLO {name.upper()} WHY ARE WE YELLING?')
else:
    print(f'Hello {name}.')