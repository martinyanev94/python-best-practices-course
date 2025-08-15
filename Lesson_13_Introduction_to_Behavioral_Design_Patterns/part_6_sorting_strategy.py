class SortStrategy:
    def sort(self, data):
        pass


class QuickSort(SortStrategy):
    def sort(self, data):
        print("Sorting using QuickSort")
        return sorted(data)


class BubbleSort(SortStrategy):
    def sort(self, data):
        print("Sorting using BubbleSort")
        for i in range(len(data)):
            for j in range(0, len(data) - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
        return data


class SortedList:
    def __init__(self, sorting_strategy):
        self.strategy = sorting_strategy
        self.data = []

    def set_strategy(self, sorting_strategy):
        self.strategy = sorting_strategy

    def add(self, value):
        self.data.append(value)

    def sort(self):
        return self.strategy.sort(self.data)


# Using the Strategy pattern
sorted_list = SortedList(QuickSort())
sorted_list.add(5)
sorted_list.add(2)
sorted_list.add(8)
print(sorted_list.sort())

# Switching sorting strategy
sorted_list.set_strategy(BubbleSort())
sorted_list.add(1)
print(sorted_list.sort())
