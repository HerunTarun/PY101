def xor(value1, value2):
    first = value1 or value2
    second = value1 and value2
    if first and not second:
        return True
    else:
        return False
# if (value1 and not value2) or (value2 and not value1):
#   return True
# return False
        
print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)