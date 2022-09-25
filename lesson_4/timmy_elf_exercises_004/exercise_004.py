#Sum

start = int(input("Enter start: "))
stop = int(input("Enter stop: "))

total = 0
for i in range(start, stop):
    print(i)
    total += i

print(f"sum: {total}")