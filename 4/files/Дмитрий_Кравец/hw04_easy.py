# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
# Разделитель
print(40*'=','\nЗадание-1:\n')

# 2016.12.08 21:48:46 checked. P.Rusanov
# Отлично!
ls = [1, 2, 4, 0]
print ([i ** 2 for i in ls])


# Задание-2:
# Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.
# Разделитель
print(40*'=','\nЗадание-2:\n')

# 2016.12.08 21:48:53 checked. P.Rusanov
# Отлично!
fructs1 = ['apple', 'banan', 'peach', 'orange']
fructs2 = ['pineapple','apple', 'kiwi', 'grapefruit', 'peach']

print([x for x in fructs1 if x in fructs2])


# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих след. условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
# Разделитель
print(40*'=','\nЗадание-3:\n')

# 2016.12.08 21:49:05 checked. P.Rusanov
# Отлично!
nums = [x for x in range(-10, 100)]

print([x for x in nums if x % 3 == 0 and x > 0 and x % 4 != 0])