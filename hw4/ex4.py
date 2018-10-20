#Фибоначчи через мн. присваивание
def fib(n):
    prev, next_ = 1, 1
    for _ in range(n - 2):
        prev, next_ = next_, prev + next_
    return next_

for i in range(20):
    print(fib(i))