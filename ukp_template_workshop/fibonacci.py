class Fibonacci:
    def __init__(self):
        self.mem = {}

    def fib(self, n: int) -> int:
        # fib(n) = fib(n-1) + fib(n-2)
        if n in (1, 2):
            return 1
        else:
            return self.fib(n-1) + self.fib(n-2)
