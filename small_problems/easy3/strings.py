def stringy(number):
    string = ""
    for n in range(number):
        if n % 2 == 0:
            string += "1"
        else:
            string += "0"
    return string
    
print(stringy(6))
print(stringy(9))
print(stringy(4))
print(stringy(7))