s = str(input())
res = [i for i in s if ord(i)%3 !=0]
res_string = ''.join(res)
print(res_string)