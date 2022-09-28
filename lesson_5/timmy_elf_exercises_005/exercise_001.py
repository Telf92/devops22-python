# Basic usage

firstname = "john"
lastname = "smith"
tele = "0046123456789"

# 1.
print(f'{firstname} {lastname} {tele}')

# 2. 3.
fullname = f'{firstname} {lastname}'

# 4.
print(len(fullname), len(firstname), len(lastname))

# 5.
print(f"{fullname}\n{tele}")

# 6.
 # i.
print(fullname + ", tel: " + tele)

# ii.
print(f"{fullname}, tel: {tele}")

# iii.
print("{}, tel: {}".format(fullname, tele))

# iv.
print("%s, tel: %s" % (fullname, tele))