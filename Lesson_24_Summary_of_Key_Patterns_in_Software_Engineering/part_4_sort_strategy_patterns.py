class SortStrategy:
    def sort(self, data):
        raise NotImplementedError

class QuickSort(SortStrategy):
    def sort(self, data):
        return sorted(data)  # Placeholder for quicksort logic

class BubbleSort(SortStrategy):
    def sort(self, data):
        for i in range(len(data)):
            for j in range(0, len(data)-i-1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
        return data

class Sorter:
    def __init__(self, strategy: SortStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: SortStrategy):
        self.strategy = strategy

    def sort(self, data):
        return self.strategy.sort(data)

# Example usage
data = [5, 3, 8, 6, 2]

sorter = Sorter(QuickSort())
print("QuickSort:", sorter.sort(data))

sorter.set_strategy(BubbleSort())
print("BubbleSort:", sorter.sort(data))
