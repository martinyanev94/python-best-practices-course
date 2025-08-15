def add_to_list(item, item_list):
    item_list.append(item)
    return item_list

a = [1, 2, 3]
add_to_list(4, a)
print(a)  # Output: [1, 2, 3, 4]
def add_to_tuple(item, item_tuple):
    return item_tuple + (item,)

b = (1, 2, 3)
new_b = add_to_tuple(4, b)
print(b)      # Output: (1, 2, 3)
print(new_b)  # Output: (1, 2, 3, 4)
