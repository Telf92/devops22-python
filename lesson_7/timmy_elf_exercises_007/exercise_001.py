# Functions

# 1.
def do_nothing():
    pass # i.

do_nothing() # ii.

# 2.
def hello(): # i.
    print("Hello world")

def ones(): # ii.
    print(1 == 1.0)

import string
def rev_alpha(): # iii.
    print(string.ascii_lowercase[::-1])

var_1 = hello()
var_2 = ones()
var_3 = rev_alpha()

print(f"{var_1} {var_2} {var_3}") # iv.

# 3.
def hello(name): # i.
    print(f"hello {name}")

def cap(word): # ii.
   print(word.upper())

def number_printer(stop): # iii.
    print(list(range(1, stop)))