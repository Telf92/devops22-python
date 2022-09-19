my_list = [1, 2, 3]
my_tuple = (3, 3, 3)

# You can add a tuple to a list.
my_list.append(my_tuple)
print(f'[1] append tuple to list {my_list}')

# Notice the difference with extend.
my_list.extend(my_tuple)
print(f'[2] extend tuple to list {my_list}')

# Lists are mutable, you can add, delete, change elements.
# Tuples are immutable, you can't add, delete, or change elements.

# If you store a mutable type in a tuple, you can still modify the type.
mutable_list = ["I have a Volvo"]
immutable_tuple = ("A value", mutable_list)

# Immutable_tuple [0] = "This is not possible"
my_list_in_tuple = immutable_tuple[1]

# You can get a reference to the inner list and change it's value.
print(f'[3] print tuple {immutable_tuple}')
my_list_in_tuple[0] = "I have a SAAB"

# Then when you print the tuple, the value has changed.
print(f'[4] print tuple after change of list element {immutable_tuple}')