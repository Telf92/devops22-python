# Stack

# 1.
import string

list(string.ascii_lowercase)

# ii.
my_stack = []
for letter in string.ascii_lowercase:
    my_stack.append(letter)

# iii.
my_string = ""
while my_stack:
    my_string += my_stack.pop()

print(my_string)