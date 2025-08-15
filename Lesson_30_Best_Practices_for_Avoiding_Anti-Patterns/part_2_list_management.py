global_list = []

def add_item(item):
    global_list.append(item)
    return global_list
def add_item(item, item_list):
    new_list = item_list + [item]
    return new_list
