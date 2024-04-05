a function that returns the sum of two numbers

START

PRINT num1 + num2

END

a function that takes a list of strings, and returns a string that is all 
those strings concatenated together

START

SET new_string = ""

FOR string in string_list
    new_string + string
    
PRINT new_string

END


a function that takes a list of integers and returns a new list with every 
other element from the original list, starting with the first element

START

SET new_list = []
SET index = 0

WHILE index < len(integer_list)
    new_list = new_list + integer_list[index]
    index = index + 2

PRINT new_list

END

a function that determines the index of the 3rd occurence of a given character
in a string. If the given character doesn't occur at least 3 times, return None

START

IF string.count(substring) < 3
    RETURN None
    
SET count = 0

FOR index, char in ENUMERATE(string)
    if char == substring
        count = count + 1
        if count == 3
            RETURN index

END

a function that takes two lists of numbers and returns the result of merging 
the lists. The elements of the first list should become the elements at the 
even indexes of the returned list, while elements of the second list should
become the elements at the odd indexes. You may assume both list arguments 
have the same number of elements

START

SET merge_list = []

FOR n in range(len(list_1)-1)
    merge_list = merge_list + list1[n]
    merge_list = merge_list + list2[n]

END