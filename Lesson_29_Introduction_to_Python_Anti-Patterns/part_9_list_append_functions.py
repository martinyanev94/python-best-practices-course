def append_to_list(mylist=[]):
    mylist.append("default")
    return mylist
def better_append_to_list(mylist=None):
    if mylist is None:
        mylist = []
    mylist.append("default")
    return mylist
