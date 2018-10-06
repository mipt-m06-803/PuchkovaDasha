#На вход сначала подается число N, а затем по очереди N чисел. Определите наибольшее из них.
N = int(input())
max_number = int(input())
for i in range(N-1):
    number = int(input())
    if number > max_number:
        max_number = number
print(max_number)