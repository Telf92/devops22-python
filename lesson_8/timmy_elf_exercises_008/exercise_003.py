# try/except

def div(x, y):
    not_a_string(y)
    try:
        return x/y
    except ZeroDivisionError:
        print('Division by zero is not allowed')

def not_a_string(y):
    if isinstance(y, str):
        raise TypeError("string is not allowed")

div(1, 1)
# div(1, 0)
# div (1, "1")

# Alternative move error handling to calling loop
