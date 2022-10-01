# Return

def get_number():
    return 1

def get_tip(x, y):
    return x, y

def get_bool():
    return True

def get_float():
    return 1.0

def fullname(firstname, lastname):
    return f'{firstname} {lastname}'

def area(l, b):
    return l*b

def sum_list(values):
    return (sum(values))

def echo(word, repeat):
    for r in range(repeat):
        print(word)

echo("Hello", 3)