#Замените все подсписки L1, равные список L2, на записанный в обратном порядке L2

L1 = [int(elem) for elem in input().split()]
L2 = [int(elem) for elem in input().split()]

n = len(L2)
L1.append(0)

for i in range(len(L1)-n):
    if L1[i:i+n] == L2:
        L3 = L2[::-1]
        L1[i:i + n] = L3
        break
del L1[len(L1)-1]
print(L1)