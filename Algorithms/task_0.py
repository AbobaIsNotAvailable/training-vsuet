def task_1():
    numbers_list = input("Ввод чисел через пробел: ")
    numbers_list = numbers_list.split(" ")

    number_list_map_object = list(map(int, numbers_list))
    min_number = min(number_list_map_object)

    print(f"Минимальное число: {min_number}")
    print(f"Индекс числа: {number_list_map_object.index(min_number)}")
    
 
task_1()


def task_2():
    numbers_list = [1, 5, -10, 3, 5, -32]
    empty_numbers_list_pos = []
    empty_numbers_list_negative = []
    
    for i in numbers_list:
        if i > 0:
            empty_numbers_list_pos.append(i)
        else:
            empty_numbers_list_negative.append(i)
            
    print(f"Положительные числа: {empty_numbers_list_pos}")
    print(f"Отрицательные числа: {empty_numbers_list_negative}")
    
task_2()
