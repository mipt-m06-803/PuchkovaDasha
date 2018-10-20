from random import randint as rnt
L = [''.join(['a']*rnt(0, 20)) for _ in range(rnt(0, 100))]
print(L)
a = len(L)

for i in range (a):
    L2 = len(L[i])
    #print (L2)
d = dict(zip(L, L2))
print (d)