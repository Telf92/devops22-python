fruits = ['apple', 'orange', 'pear', 'banana', 'grapes']
basket = []
amount = int(input("How many fruits?"))

for i in range(amount):
    basket.append(fruits[i % len(fruits)])
print(basket)

basket_2 = []
while amount:
    for fruit in fruits:
        if not amount:
            break
        basket_2.append(fruit)
        amount -= 1
print(basket_2)