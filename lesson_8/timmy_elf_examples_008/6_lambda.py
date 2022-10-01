# Create testdata
one_to_ten = list(range(1, 11))
print(one_to_ten)

# Print all values
print(sum(one_to_ten))

# Use lambda to filter values
# Keep value if it's 2
only_keep_twos = filter(lambda x: x == 2, one_to_ten)
print(list(only_keep_twos))

# Use lambda to filter values
# Keep values above 4
above_four = filter(lambda x: x > 4, one_to_ten)
print(list(above_four))

# Sum all odd values in a list?
# sum(1, 3, 5, 7, 8) = 25
print(sum(filter(lambda x: x % 2, one_to_ten)))