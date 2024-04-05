def twice(number):
    if is_double(number):
        return number
    else:
        return number * 2
        
def is_double(number):
    string = str(number)
    length = len(string)
    if length % 2 == 0:
        return string[:(length // 2)] == string[length // 2:]
    else:
        return False
        
        
print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True