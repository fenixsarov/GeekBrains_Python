__author__ = 'Дмитрий Кравец'
# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом)
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math
# Разделитель
print(40*'=','\nЗадание-1:\n')

# решение, что называется, "в лоб"
def my_round(number, ndigits):
    return round(number, ndigits)

# решение поинтереснее через "старое" и "новое" форматирование
def my_round2(number, ndigits):
    return "%.{}f".format(ndigits) % number


print(my_round(2.1234567, 5))
print(my_round2(2.1234567, 3))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

# Разделитель
print(40*'=','\nЗадание-2:\n')

def lucky_ticket(ticket_number):
    lst_numbers = tuple(str(ticket_number))

    if len(lst_numbers) != 6:
        return

    left_part = rigth_part = 0

    for i in range(len(lst_numbers)):
        if int(i) < 3:
            left_part += int(lst_numbers[i])
        else:
            rigth_part += int(lst_numbers[i])

    return 'У Вас счастливый билетик!' if left_part == rigth_part else 'Повезёт в следующий раз'


print(lucky_ticket(656557))