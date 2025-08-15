def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
class Memoizer:
    def __init__(self):
        self.memo = {}

    def fib(self, n):
        if n in self.memo:
            print(f"Fetching fib({n}) from memo.")
            return self.memo[n]
        if n <= 1:
            return n
        print(f"Calculating fib({n})")
        self.memo[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.memo[n]

memoizer = Memoizer()
for i in range(10):
    print(memoizer.fib(i))
