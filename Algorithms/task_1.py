x = int(input("Натуральное число Х: "))
n = int(input("Натуральное число N: "))
    

def task_block_a(x, n):
    
    if x == n:
        print(x)
        return
    else:
        print(x)
        x += 1
        task_block_a(x, n)
    
task_block_a(x, n)

def task_block_b():
    num = list(input("Введите натуральное число: "))
    num = map(int, num)
    
    print(max(num))
    task_block_b()
    
task_block_b()
