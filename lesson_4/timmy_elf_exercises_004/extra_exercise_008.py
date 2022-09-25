from math import sqrt

test_number = 1
prime_number = []

while test_number <100:
    # print(f'Testing number: {test_number}')
    previous_numbers = test_number - 1
    while previous_numbers > 1:
        # print f'{test_number} % {previous_numbers}')
        if not test_number % previous_numbers:
            # print("Not a prime")
            break
        previous_numbers -= 1
    if previous_numbers == 1:
        prime_number.append(test_number)
    test_number += 1

print(prime_number)

test_number = 3
prime_numbers = [2]
while test_number < 100:
    square = sqrt(test_number)
    isPrime = False
    for prime in prime_numbers:
        if prime > square:
            isPrime = True
            break
        isPrime = test_number % prime
        if not isPrime:
            break
    if isPrime:
        prime_numbers.append(test_number)
    test_number += 1

print(prime_numbers)