# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.


lst = [1, 3, 16, 5, 9, 16, 8, 4, 5]
print(lst)
new_lst = []
# print(len(lst))
for i in lst:
    if i not in new_lst:
        new_lst.append(i)
print(new_lst)
