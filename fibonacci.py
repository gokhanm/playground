# Fibonacci examples

class Fibonacci:
    def gen(self, n):
        """Print a Fibonacci series up to n."""
        a, b = 0, 1
        while b < n:
            print(b)
            a, b = b, a + b

f = Fibonacci()
f.gen(1145)

# Difference Usage

from time import sleep

def fibonacci():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b

for f in fibonacci():
    print(f,)
    sleep(1)
