set1 = set(input())
set2 = set(input())
set3 = set(input())
symdiff = (set1| set2 | set3)- (set1 & set2)- (set1 & set3)-(set3 & set2)
symdiff_2 = (set1 ^ set2 ^ set3) - (set1 & set2 & set3)

print(symdiff)
print(symdiff_2)