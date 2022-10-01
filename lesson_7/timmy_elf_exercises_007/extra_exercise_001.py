# Repeat

# Without functions
user_input = int(input("Input a integer: "))

if user_input > 5:
    print(str(user_input) * user_input)

elif 0 < user_input <= 5:
    for number in range(user_input + 1):
        print(str(number) * number)

# With functions
def get_user_input():
    return int(input("Input a integer: "))

def echo_printing(number):
    print(str(number) * number)

def incremental_echo_printing(number):
    for number in range(number + 1):
        echo_printing(number)

def main():
    user_input = get_user_input()
    if user_input > 5:
        echo_printing(user_input)
    else:
        incremental_echo_printing(user_input)

if __name__ == '__main__':
    main()