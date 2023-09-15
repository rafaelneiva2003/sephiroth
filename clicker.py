# a clicker game where you kill Sephiroith :D
import turtle

wn = turtle.Screen()
wn.title("Kill Sephiroth by Rafael Neiva")
wn.bgcolor("black")

wn.register_shape("seph.gif")

cookie = turtle.Turtle()
cookie.shape("seph.gif")
cookie.speed(0)

clicks = 100

pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0, 250)
pen.write(f"Damage: {clicks}", align="center", font=("Courier New", 32, "normal"))

def clicked(x, y):
    global clicks
    clicks -= 1
    pen.clear()
    pen.write(f"Damage: {clicks}", align="center", font=("Courier New", 32, "normal"))
    
cookie.onclick(clicked)

wn.mainloop()