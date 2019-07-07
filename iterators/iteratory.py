class MySimpleIterator:

    def __init__(self, n):
        self.iteration = 0
        self.n = n
        self.current = 0
        self.next = 1

    def __next__(self):
        if self. iteration >= self.n:
            raise StopIteration # rzuca wyjątek
        self.iteration += 1
        return self.iteration

    def __iter__(self):
        return self


if __name__ == '__main__':

    for i in MySimpleIterator(10):
        print(i)

    """ Inny sposób na pętle:
    while True:
        try:
            print(next(fib))
        except StopIteration
            break
    """