# What will the following code print and why?

num = 5

def my_func():
    num = 10

my_func()
print(num)

# This will print 5. The num inside my_func is a local variable 
# while the print(num) expression will use the num on line 3