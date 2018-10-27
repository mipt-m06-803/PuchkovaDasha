N = int(input())
D = []
for i in range(N):
    T = [int(elem) for elem in input().split()]
    D.append(T)

time = int(input())
k = 0
for a, b in D:
    if a <= time and time <= b:
        k = k+1

print(k)