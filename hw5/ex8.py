# Дописывание в конец файла
with open ('hw5.8.1.txt', 'w') as f:
    f.write("I am the first file!")

with open ('hw5.8.2.txt', 'w') as f:
    f.write("I am the second file!")

with open('hw5.8.1.txt', 'r') as f:
    text1 = f.readline()

with open('hw5.8.2.txt', 'a') as f:
   f.write(''.join(text1[::-1]))

