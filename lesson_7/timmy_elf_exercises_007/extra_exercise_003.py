# Flow charts

def input_number_list():
    return list(map(int, input("Enter list of numbers").split(",")))

def get_next_pair(the_list, i):
    return the_list[i], the_list[i+1]

def bigger_than(a, b):
    return a > b

def swap_elements(the_list, pos1, pos2):
    the_list[pos2], the_list[pos1] = the_list[pos1], the_list[pos2]

def at_end_of_list(the_list, i):
    return i >= len(the_list)-2

list_to_sort = input_number_list()
while True:
    swapped = False
    i = 0
    while True:
        a, b = get_next_pair(list_to_sort, i)
        if bigger_than(a,b):
            swapped = True
            swap_elements(list_to_sort, i, i+1)
        if at_end_of_list(list_to_sort, i):
            break
        else:
            i +=1
    if not swapped:
        break
print(list_to_sort)