# Alyssa was asked to write an implementation of a rolling buffer. 
# You can add and remove elements from a rolling buffer. 
# However, once the buffer becomes full, any new elements will 
# displace the oldest elements in the buffer.

# # She wrote two implementations of the code for 
# adding elements to the buffer:
def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
    buffer.append(new_element)
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
    buffer = buffer + [new_element]
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

# Is there a difference between these implementations, 
# other than the way she is adding an element to the buffer?

# # add_to_rolling_buffer2 allows you to add multiple new elements at a time
# while add_to_rolling_buffer1() only allows you to add one new element at a time
# using the .extend() method might fix it for the first function

# Answer - yes, the first function mutates the original list, while the second 
# creates a new list and returns that