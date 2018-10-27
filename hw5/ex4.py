#Общие элементы 2 списков

list_1 = [int(i) for i in input().split()]
list_2 = [int(i) for i in input().split()]

set_1 = set(list_1)
set_2 = set(list_2)
intersection_ = set_1 & set_2
l = list(intersection_)

print(' '.join(str(v) for v in l))