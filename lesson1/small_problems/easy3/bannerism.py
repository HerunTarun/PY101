def print_in_box(string):
    length = len(string)
    dash = "-" * length
    space =  " " * length
    print(f'+-{dash}-+')
    print(f'| {space} |')
    print(f'| {string} |')
    print(f'| {space} |')
    print(f'+-{dash}-+')
    
# print_in_box('To boldly go where no one has gone before.')
# print_in_box('')

# # Further Exploration - Truncation

def truncated_print_in_box(string, limit):
    length = len(string)
    if length > limit:
        string = string[:limit + 1]
        length = limit + 1
    dash = "-" * length
    space =  " " * length
    print(f'+-{dash}-+')
    print(f'| {space} |')
    print(f'| {string} |')
    print(f'| {space} |')
    print(f'+-{dash}-+')
    
truncated_print_in_box('To boldly go where no one has gone before.', 10)

# Further Exploration - Word Wrap

def wordwrap_print_in_box(string):
    length = len(string)
    width = 75
    if length > width:
        counter = length // width
        slicer = width
        dash = "-" * width
        space = " " * width
        print(f'+-{dash}-+')
        print(f'| {space} |')
        while counter != 0:
            print(f'| {string[slicer - width:slicer]} |')
            counter -= 1
            slicer += width
        final_slice_start = (length // width) * width
        additional_space = " " * (width - (length - final_slice_start))
        print(f'| {string[final_slice_start:]}{additional_space} |')
        print(f'| {space} |')
        print(f'+-{dash}-+')
    else:
        dash = "-" * length
        space =  " " * length
        print(f'+-{dash}-+')
        print(f'| {space} |')
        print(f'| {string} |')
        print(f'| {space} |')
        print(f'+-{dash}-+')
    
wordwrap_print_in_box('You should work through the exercise groups from the PY101-PY109 Small Problems while making your way through PY101. You can do them all at once, or spread them out over the rest of this course. Either way, complete those exercise groups before taking the PY109 assessments.')

