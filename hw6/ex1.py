l1 = str(input()).split( )
l2 = str(input()).split( )
s = ','.join(l1) + '\n' + ','.join(l2)
print(s)
with open('hw6_ex1.txt', 'w') as f:
    f.write(s)

