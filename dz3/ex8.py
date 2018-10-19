d = {}
while True:
    s = str(input())
    if s == 'STOP':
        break
    l = s.split()
    d[l[0]] = l[1]
print(d)