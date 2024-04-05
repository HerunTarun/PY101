def penultimate(string):
    return string.split(' ')[-2]
    
# These examples should print True
print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")

# Further Exploration

def middling(string):
    # string = str(string)
    lst = string.split()
    return lst[len(lst) // 2]
    # while True:
    #     if len(string) = True:
    #         break
    #     elif len(lst) > 0:
    #         break
        
print(middling('first and last'))