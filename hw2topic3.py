import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_curve(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()

    for _ in 3 * [None]:
        koch_curve(t, order, size)
        t.right(120)

    window.mainloop()

# Виклик функції
try:
    user_order = int(input("Введіть рівень рекурсії (наприклад 3): "))
    draw_koch_curve(user_order)
except ValueError:
    print("❗ Помилка: введіть ціле число!")
