s = str (input())
N = len(s)
#print(N)
a1 = ord(s[0])
for i in range (N):
    a_i = ord(s[i])
    if a_i> a1:
        f = 'false'
        break
    else:
        a1 = a_i
        f = 'true'
print (f)



