def center_of(string):
    start = len(string) // 2 
    if len(string) % 2 == 0:
        return string[start - 1: start + 1]
    else:
        return string[start]
        
print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True