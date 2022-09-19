# Sorting

cars = ["volvo", "saab", "audi", "skoda", "volkswagen", "tesla", "kia", "toyota", "lexus", "bmw"]
# 1.
sorted_cars = sorted(cars)
print(sorted_cars)

# 2.
cars.sort()
print(cars)

# 3.
sorted_cars = sorted(cars, reverse=True)
print(sorted_cars)

cars.sort(reverse=True)
print(cars)

# 4.
cars = [("volvo", "xc90"), ("saab", "900"), ("audi", "r8"), ("skoda", "yeti"), ("volkswagen", "passat"), ("tesla", "model s"), ("kia", "niro"), ("toyota", "rav4"), ("lexus", "rx 350"), ("bmw", "m3")]
cars.sort()
print(cars)

# Custom order is possible with itemgetter, but this is not needed in this case
# From operator import itemgetter
# sorted(cars, key=itemgetter(0,1))