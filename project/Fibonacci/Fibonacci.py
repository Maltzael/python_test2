from timeit import timeit
class Fibonacci:
    def __init__(self, numb=5):
        self.counter = 1
        self.numb = numb
        self.Fib_list = [0,1]
        self.Fib_list2 = [0,1]

    def increm(self):
        for x in range(0, self.numb - 2):
            yield self.Fib_list.append(self.Fib_list[x] + self.Fib_list[x + 1])
            #chyba nie czaje xD
        print(self.Fib_list)

    def requr(self):
        if self.counter != self.numb-1:
            self.Fib_list2.append(self.Fib_list2[self.counter - 1] + self.Fib_list2[self.counter])
            self.counter += 1
            return self.requr()
        else:
            return self.Fib_list2


timeIncr = timeit(lambda : Fibonacci(100).increm())
print(timeIncr)
timeRecur = timeit(lambda : Fibonacci(100).requr())
print(timeRecur)