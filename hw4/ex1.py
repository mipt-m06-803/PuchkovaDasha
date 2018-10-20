#Найдите наибольший элемент в списке. Выведите значение элемента и его индекс.
#Выведите список в обратном порядке
list_ = [int(elem) for elem in input().split()]

print(max(list_), list_.index(max(list_)))
print(list_[ : :-1])