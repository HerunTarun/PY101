# What will the following code print and why? 

def my_func():
    x = 15

    def inner_func1():
        x = 25
        print("Inner 1:", x)

    def inner_func2():
        print("Inner 2:", x)

    inner_func1()
    inner_func2()

my_func()

# so this will print Inner1:25, and then Inner2:15.
# inner_func1 has a variable x with a value of 25 in its scope
# so it will use that to print
# while inner_func2 will look in the outer scope of my_func for x
# where it will find x with a value of 15, which it will use to print
