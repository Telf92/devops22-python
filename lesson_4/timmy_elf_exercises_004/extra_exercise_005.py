first_list = [3, 7, 9, 2, 6]
second_list = [2, 3, 6, 7, 9]

result = []
for tal in second_list:
    result.append((tal, first_list.index(tal)))
print(result)