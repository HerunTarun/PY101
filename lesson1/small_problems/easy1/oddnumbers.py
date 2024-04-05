numbers = list(range(1, 100, 2))
for number in numbers:
    print(number)
    
# # better way
# for number in range(1, 100, 2):
#     print(number)
    
# further exploration

def choose(start, end):
    if start < end:
        left = start
        right = end + 1
    else:
        left = end
        right = start -1
    for number in range(left, right):
        if number % 2 != 0:
            print(number)

choose(1, 8)
choose(4, 51)
choose(-1, -14)
choose(-14, 1)
choose(9, 1)