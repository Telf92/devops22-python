salary = 10000
currency = 'SEK'

# 1.
print(f"Your current salary is {salary} {currency}")

# 2.
initial_increase = int(input("How much do you expect in salary increase? "))

# 3.
percentage = initial_increase / salary * 100
print(f"You ask for a increase of {percentage}%, the answer is NO!")

# 6.
decision = "NO"
while decision != 'YES':

# 4.
    increase = input("How much do you expect in salary increase? ")    
    if increase == 'quit':
        break

# 5.
    increase_in_proc = int(increase) / salary * 100
    if (int(increase) <  initial_increase):
        decision = 'YES'
        print(f"You ask for a increase of {percentage}%, I accept!")
    else:
        print(f"You ask for a increase of {percentage}%, the asnwer is {decision}!")