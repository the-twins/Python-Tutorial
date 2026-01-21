class FibonacciIterator:
    
    def __init__(self, n):
        self._numb = n
        self._x = 0
        self._y = 1
    
    def __iter__(self):
        return self
        
    def __next__(self):
        if not self._numb:
            raise StopIteration
        temp_x = self._x
        self._x, self._y = self._y, self._x + self._y
        self._numb -= 1
        return temp_x


def fibonacci_generator(n: int):
    x = 0
    y = 1
    for i in range(n):
        yield x
        x, y = y, x + y
        
        
def square_generator(n: int):
    for i in range(n):
        yield i * i


if __name__ == '__main__':
    numb_fib = FibonacciIterator(3)
    for i in numb_fib:
        print(i)
    print()
    
    numb_fib = fibonacci_generator(3)
    print(numb_fib)
    for i in numb_fib:
        print(i)
    print()
    
    numb_square = square_generator(10)
    for i in numb_square:
        print(i)
    print()
        
    numb_square = [i * i for i in range(10)]
    print(numb_square)
    
    numb_square = (i * i for i in range(10))
    print(numb_square)
    for i in numb_square:
        print(i)
 