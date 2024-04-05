def triangle(n):
    counter = n
    white = counter - 1
    star = 1
    while counter != 0:
        print(f'{white * " "}{star * "*"}')
        counter -= 1
        white -= 1
        star += 1
        
triangle(5)

def triangular(n):
    for number in range (1, n + 1):
        white = n - number
        star = number
        print(f'{white * " "}{star * "*"}')


triangular(4)