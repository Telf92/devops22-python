# Unicode

price = int(input("your new car costs? "))
print(f"Your new car costs: {price}\u20BF")
if price < 50000:
    print("\N{grinning face}")
else:
    print("\U0001F606")