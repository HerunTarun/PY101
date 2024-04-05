# What will the following code print and why? 

num = 5

def my_func():
    global num
    num = 10

my_func()
print(num)

# This will print 10, since the num in my_func was specifically
# identified as the global variable num using the global statement