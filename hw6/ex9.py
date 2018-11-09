l = str(input()).split()
n = len(l)

k = 0
l2 = []
while k <= n-1:
    l2.append(l[k])
    if k < n-1:
        l2.append(l[n-1])
    k += 1
    n -= 1
s = ' '.join(l2)
print(s)
