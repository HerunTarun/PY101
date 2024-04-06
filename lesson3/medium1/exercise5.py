# What do you think the following code will output?
nan_value = float("nan")

print(nan_value == float("nan"))

# **True, because there's a float value of Nan, which is Not A Number
# False because nan is a value that indicates an operation intending to return a number failed
# Python doesn't allow you to use == to determin whether a value is nan

# Bonus: How can you reliably test if a value is nan?
# add 'nan' to a list and check whether the value is in the list
# or use the math.isnan() method
