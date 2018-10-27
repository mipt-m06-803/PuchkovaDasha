#вычисляется среднее арифметическое всех оценок в журнале
marks = [int(elem) for elem in input().split()]

N = len(marks)
sum = marks[0]
n = 1
for i in range(1, N):
    sum = sum + marks[i]
    n = n+1
    if marks[i - 1] == 2 and marks[i] != 2:
        sum = sum - marks[i - 1]
        n = n - 1
mark = sum//n
print(mark)

