# Name counter

from random import choices

# 1.
names = choices(["johan", "lisa", "johan", "tove"], k=100)

# 2.
from collections import Counter
names_counter = Counter(names)

# 3.
print(names_counter.most_common(3))

# 4.
print(names_counter.most_common()[-1])

# 5.
# i.
unique_names = sorted(list(set(names)))
print(unique_names)

# ii.
from random import shuffle
shuffle(unique_names)
print(unique_names)

# iii.
unique_names.sort(reverse=True)
print(unique_names)