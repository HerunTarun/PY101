def clean_up(string):
    new_string = ''
    for char in string:
        if char.isalpha():
            new_string += char
        else:
            new_string += ' '
    return new_string.replace("  ", " ")
    
    
    
print(clean_up("---what's my +*& line?") == " what s my line ")
# True