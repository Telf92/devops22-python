# Sum

start = int(input("Enter a starting integer: ")) #User start input

stop = int(input("Enter a stopping integer: ")) #User stop input

total = 0

for i in range(start, stop):
    print(i)
    total += i

print(f"Sum: {total}") #Sum of integers