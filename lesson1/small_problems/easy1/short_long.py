def short_long_short(string1, string2):
    if len(string1) > len(string2):
        longer = string1
        shorter = string2
    else:
        longer = string2
        shorter = string1
    
    return shorter + longer + shorter

print(short_long_short('abc', 'defg'))
print(short_long_short('', 'defg'))

# # another way
# if len(string1) > len(string2):
#     return string2 + string1 + string2
# else:
#     return string1 + string2 + string1

# ternary
# shorter, longer = (string1, string2) if len(string1) < len(string2) else (string2, string1)
# return shorter + longer + shorter