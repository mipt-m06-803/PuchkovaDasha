G = 6.67408e-11

s1 = str(G)
s2 = "\n{}\n".format(G)
s3 = "{:.3}\n".format(G)
s4 = "{:.14f}\n".format(G)
s5 = "{:.4e}\n".format(G)
s = s1 + s2 + s3 + s4 + s5
with open('hw6_ex3.txt', 'w') as f:
    f.write(s)


str1 = (repr('\n{}\n'))
str2 = (repr('{:.3}\n'))
str3 = (repr('{:.14f}\n'))
str4 = (repr('{:.4e}\n'))
str_ = str1 + '\n' + str2 + '\n' + str3 + '\n' + str4
with open('hw6_ex3_formats.txt', 'w') as f:
    f.write(str_)

