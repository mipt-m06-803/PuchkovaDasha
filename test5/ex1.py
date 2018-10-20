import math
list_ = [math.factorial(i) for i in range (1,101)]
print(list_)


import math
l2 = [math.factorial(i) for i in range(1, 101) if str(math.factorial(i))[0] == 2]
print(l2)