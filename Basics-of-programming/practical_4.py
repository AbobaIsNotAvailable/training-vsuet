
# Задание 1

"""

Каждое задание вставлять в отдельный файл, при запуске этого файла
будут ошибки

"""

a, b = int(input("Введите число A: ")), int(input("Введите второе число B: "))

if a < b:
    for i in range(a, b + 1):
        print(i)
else:
    print("Число A должно быть меньше числа B")


# Задание 2

a, b = int(input("Введите число A: ")), int(input("Введите второе число B: "))

if a < b:
    for i in range(a, b + 1):
        print(i)
else:
    for i in reversed(range(b, a + 1)):
        print(i)

# Задание 3

a, b = int(input("Введите число A: ")), int(input("Введите второе число B: "))

if a > b:
    for i in reversed(range(b, a + 1)):
        if (i % 2) != 0:
            print(i)


# Задание 4

list_numbers = []
for i in range(int(input("Введите количество чисел: "))):
    list_numbers.append(int(input("Введите число: ")))

print(sum(list_numbers))

# Задание 5

n = int(input("Введите число: "))
m = 0
for i in range(1, n+1):
    m += i ** 3
print(m)

# Задание 6

default = 1
n = int(input("Введите число: "))
for i in range(1, n + 1):
    default *= i
print(default)

# Задание 7

default = 1
n = int(input("Введите число: "))
for i in range(1, n + 1):
    default += i
print(default)


# Задание 8

def func_fib(n):
   if n == 1 or n == 2:
       return 1
   else:
       return func_fib(n - 2) + func_fib( n - 1 )
 
n = int(input("Введите число:"))
print(func_fib( n + 2) - 1)


# Задание 9
fib1 = fib2 = 1
 
n = int(input("Количество чисел из ряда Фибоначчи: "))
k = int(input("порядковый номер в ряду, с которого нужно начать: "))
 
print(fib1, fib2, end=' ')
 
for i in range(k, n):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')