__author__ = 'Дмитрий Кравец'
# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
# Ряд 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946
# Разделитель
print(40*'=','\nЗадание-1:\n')

# Простое решение
def fibonacci(n, m):
    if n > m: return
    if m < 4 and n < 3: return [1, 1, 2]
    num1 = num2 = 1
    num_sum = 0
    num_lst = list()

    i = 2
    while n <= m:
        while i < n:
            num_sum = num1 + num2
            num1 = num2
            num2 = num_sum
            i += 1
        num_lst.append(num_sum)
        n += 1

    return num_lst


print(fibonacci(5, 18))

# Математическое решение
from math import sqrt

def fibonacci2(n, m):
    if n > m: return
    if m < 4 and n < 3: return [1, 1, 2]

    fib = list()
    while n <= m:
        phi = (sqrt(5) + 1) / 2
        fib.append(int(phi ** n / sqrt(5) + 0.5))
        n += 1

    return fib


print(fibonacci2(5, 18))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()
# Разделитель
print(40*'=','\nЗадание-2:\n')

def sort_to_max(origin_list):
    result = list()
    while origin_list:
        result.append(min(origin_list))
        origin_list.remove(min(origin_list))

    return result

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
# Разделитель
print(40*'=','\nЗадание-3:\n')

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
# Разделитель
print(40*'=','\nЗадание-4:\n')
