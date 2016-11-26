# -*- coding: utf-8 -*-
import random, turtle, sys

def gotoxy(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def draw_line(from_x, from_y, to_x, to_y):
    gotoxy(from_x, from_y)
    turtle.goto(to_x, to_y)

x = random.randint(1, 100)
print("Случайное число: ", x)

turtle.speed(110)
turtle.color("blue")



# столб
draw_line(-160, -100, -160, 80)

# горизонтальная балка
draw_line(-160, 80, -80, 80)

# косая черта - ребро жесткости
draw_line(-160, 40, -120, 80)

# веревка
draw_line(-100, 80, -100, 40)

# голова
gotoxy(-100, 0)
turtle.circle(20)

# туловище
draw_line(-100, 0, -100, -50)

# левая рука
draw_line(-100, -10, -120, -20)

# правая рука
draw_line(-100, -10, -80, -20)

# левая нога
draw_line(-100, -50, -120, -60)

# правая нога
draw_line(-100, -50, -80, -60)

gotoxy(-200, 250)

turtle.write("Я загадал число от 1 до 100. \nПопробуй угадать",
    font=("Arial", 18, "normal"))

answer = turtle.textinput("Хотите поиграть?", "(y/n)")
if answer == 'n':
    sys.exit(7) #выход из программы, что удивительно, код может быть любой

hints = False
answer = turtle.textinput('Давать ли Вам подсказки?', "(y/n)")
if answer == "y":
    hints = True

try_count = 0

while True:
    number = turtle.numinput("Попробуй угадать", "Число", 0, -10, 100 )

    if hints:
        gotoxy(170, 200 - try_count * 12)
        if number < x:
            turtle.write(str(number) + " Загаданное число больше")
        else:
            turtle.write(str(number) + "Загаданное число меньше")

    if number == x:
        gotoxy(-150, -200)
        turtle.color("green")
        turtle.write("Ура! Ты победил!", font=(
        'Arial', 20, "normal"))
        break
    elif number == -5:
        sys.exit(-5)
    else:
        gotoxy(-150, 100)
        turtle.color("red")
        turtle.write("Неверно!", font=('Arial', 20, "normal"))
        try_count += 1

        if try_count == 10:
            gotoxy(-150, 150)
            turtle.color("red")
            turtle.write("Ты проиграл! АХАХАХА!!!", font=('Arial', 20, "normal"))
            break

input("Нажмите любую клавишу")