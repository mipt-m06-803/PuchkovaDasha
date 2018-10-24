#умножение списков
A = [int(elem) for elem in input().split()]
B = [int(elem) for elem in input().split()]
C = [int(elem) for elem in input().split()]

D = [A[i] * B[i] * C[i] for i in range(len(A))]
s = ' '.join(map(str, D))
print(s)

D2 = [a*b*c for a, b, c in zip(A, B, C)]
s2 = ' '.join(map(str, D2))
print(s2)
