# Default arguments

def default_number_printer(start=1, stop=11):
    print(list(range(start, stop)))

def rev_string(word, reverse=False):
    if reverse:
        word = word[::-1]
    print(word)

rev_string("Hello")
rev_string("Hello", reverse=True)