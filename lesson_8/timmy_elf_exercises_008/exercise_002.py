# Input validation

def int_input():
    try:
        return int(input("Write a integer: "))
    except:
        print("Sorry, not an int")
        return int_input()

def even_input():
    number = int_input()
    if not number % 2:
        raise Exception('Even numbers is not allowed')
    return number

even_input()