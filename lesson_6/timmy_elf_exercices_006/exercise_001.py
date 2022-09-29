# Dataset

# 1.
list(range(1, 101))

# 2.
list(range(2, 61, 2))

# 3.
list(range(1, 78, 2))

# 4.
# i.
from random import sample
population = list(range(1, 301))
hundred_numbers = sample(population, k=100)

# ii.
from random import choices
population = list(range(1, 301))
hundred_numbers = choices(population, k=100)

# 5.
# i.
colors = ["yellow", "blue", "green", "black", "white"]
new_list = ["red"]
new_list.extend(sample(colors, k=2))

# ii.
random_colors = choices(new_list, k=50)

# iii.
unique_colors = set(colors)
#colors_string = ", ".join()
#print(f'{len(colors)} {colors_string}')
print(f'{len(new_list)} {", ".join(set(new_list))}')
print(f'{len(random_colors)} {", ".join(set(random_colors))}')