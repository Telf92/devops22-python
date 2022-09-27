a = "first"
b = "second"

#a 
c = a
a = b
b = c

print (a)
print(b)
# b
a, b = b, a
print(a)
print(b)