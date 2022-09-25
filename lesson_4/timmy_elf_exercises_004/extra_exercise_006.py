first_list = [3, 7, 9, 2, 6]
second_list = [2, 3, 6, 7, 9]

result = [(x, first_list.index(x)) for x in second_list]
print(result)