#Считывание данных из файла

with open('hw5.9.txt', 'r') as f:
    f.seek(0)
    lines = f.readlines()

list = [lines[i].rstrip('\n') for i in range(len(lines))]
N = []
X = []
Y = []
l = [list[i].split() for i in range(len(lines))]
for n, x, y in l:
    N.append(int(n))
    X.append(float(x))
    Y.append(float(y))

print(N)
print(X)
print(Y)