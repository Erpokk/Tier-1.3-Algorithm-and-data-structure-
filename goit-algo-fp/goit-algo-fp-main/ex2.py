import turtle
import math

def draw_pythagoras_tree(t, length, level):
    if level == 0:
        t.forward(length)
        t.backward(length)
        return

  
    t.forward(length)
    t.left(45)
    draw_pythagoras_tree(t, length * math.sqrt(2) / 2, level - 1)
    t.right(90)
    draw_pythagoras_tree(t, length * math.sqrt(2) / 2, level - 1)
    t.left(45)
    t.backward(length)

screen = turtle.Screen()
screen.title("Фрактал: Дерево Піфагора")
t = turtle.Turtle()
t.speed(0)  
t.left(90)  
level = int(input("Введіть рівень рекурсії: "))

draw_pythagoras_tree(t, 100, level)
turtle.done()