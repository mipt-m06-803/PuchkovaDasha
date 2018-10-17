l = [float(substr) for substr in input().split()]
l2 = ['b', 'y', 's', 'h']
ind = l.index(min(l))
l = l[ :ind+1] + l2 + l[ind+1: ]
print(l)