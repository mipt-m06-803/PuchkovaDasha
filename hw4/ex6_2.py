L1 = [elem for elem in input().split()]
L2 = [elem for elem in input().split()]
L2_reverse = L2[::-1]
s2_reverse = ' '.join(L2_reverse)

s1 = ' '.join(L1)
s2 = ' '.join(L2)


if s2 in s1:
    s1 = s1.replace(s2, s2_reverse, 1)


print(s1)