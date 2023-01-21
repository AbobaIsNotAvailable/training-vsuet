# Вариант 2

"""
    Дан одномерный массив, состоящий из N целочисленных элементов. Ввести
    массив с клавиатуры. Найти минимальный элемент. Вывести индекс
    минимального элемента на экран.
"""

numbers = list(map(int, input("Введите числа через пробел: ").split(" ")))

print(numbers.index(min(numbers)))


"""
    Дан массив целых чисел. Переписать все положительные элементы во второй
    массив, а остальные - в третий.
"""

list_numbers_pos = []
list_numbers = []

for i in numbers:
    if i > 0:
        list_numbers_pos.append(i)
    else:
        list_numbers.append(i)

print(list_numbers_pos)
print(list_numbers)

