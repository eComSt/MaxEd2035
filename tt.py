import turtle

# Установка параметров для черепахи
turtle.speed(3)
turtle.bgcolor("black")
turtle.pensize(3)
turtle.color("red")

# Начать рисование
turtle.begin_fill()

# Рисуем левую половину сердца
turtle.left(140)
turtle.forward(180)
turtle.circle(-90, 200)

# Рисуем правую половину сердца
turtle.setheading(60)
turtle.circle(-90, 200)
turtle.forward(180)

# Заканчиваем рисование
turtle.end_fill()

# Завершаем работу с черепахой
turtle.done()