# Raise

# 1.
def is_float(value):
    if not isinstance(value, float):
        raise TypeError("Value is not a float")

my_var = 0
is_float(my_var)