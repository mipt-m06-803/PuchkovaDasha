def rost():
    d = {}
    while True:
        s = str(input())
        if s == 'STOP':
            break
        l = s.split()
        d[l[0]] = l[1]
    return d

d = rost()
print(d)

def zamena():
    sortirovka = sorted(list(d.items()), reverse=True)
    d2 = dict(sortirovka)
    d3 = {v: k for k, v in d2.items()}
    return d3

print(zamena())