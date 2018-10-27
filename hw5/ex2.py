#координаты точек
import math
PI = 3.14
N = int(input())
T = [10 / N * i for i in range(N)]
X = [1 + math.cos(2 * PI / N * i) for i in range(N)]
Y = [math.sin(2 * PI / N * i) for i in range(N)]
Z = [1 / N * i for i in range(N)]


D = []
for T, X, Y, Z in zip(T,X,Y,Z):
    s = 't = {0}, x = {1}, y = {2}, z = {3}'.format(T, X, Y, Z)
    D.append(s)

print(D)


