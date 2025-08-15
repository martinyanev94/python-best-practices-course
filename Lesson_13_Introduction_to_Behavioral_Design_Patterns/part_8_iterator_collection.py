class Iterator:
    def __init__(self, collection):
        self._collection = collection
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._collection):
            result = self._collection[self._index]
            self._index += 1
            return result
        raise StopIteration


class Collection:
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def __iter__(self):
        return Iterator(self._items)


# Using the Iterator pattern
collection = Collection()
collection.add_item("Item 1")
collection.add_item("Item 2")
collection.add_item("Item 3")

for item in collection:
    print(item)
