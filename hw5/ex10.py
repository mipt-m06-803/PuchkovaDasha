#Циклический сдвиг
l = input().split()

length = len(l[0])
res = l[0][length-int(l[1]):]+l[0][:(length-int(l[1]))]
print(res)