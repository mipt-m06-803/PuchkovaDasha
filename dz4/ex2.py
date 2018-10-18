s = str(input())

def names_(s):
    names = s.split(" ")
    res = []
    for idx, name in enumerate(names,1):
        res.append(f'{idx}. {name}')

    return (res)

print (names_(s))