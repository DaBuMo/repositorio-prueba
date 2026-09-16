from turtle import *

class Sprite(Turtle):

    def __init__(self, x, y, image, steps=10,color="orange"):
        super().__init__()
        self.penup()
        self.goto(x, y)
        self.shape(image)
        self.steps = steps
        self.color(color)

    def left(self):
        self.goto(self.xcor() - self.steps, self.ycor())
        self.setheading(180)

    def right(self):
        self.goto(self.xcor() + self.steps, self.ycor())
        self.setheading(0)

    def up(self):
        self.goto(self.xcor(), self.ycor() + self.steps)
        self.setheading(90)

    def down(self):
        self.goto(self.xcor(), self.ycor() - self.steps)
        self.setheading(270)

jugador = Sprite(-100, 0, "circle")

enemigo = Sprite(100, 0, "square", color="red")
enemigo2 = Sprite(100, 100, "square", color="blue")

meta = Sprite(200, 0, "triangle", color="green")

src = jugador.getscreen()

src.listen()

src.onkey(jugador.left, "Left")
src.onkey(jugador.right, "Right")
src.onkey(jugador.up, "Up")
src.onkey(jugador.down, "Down")

src.mainloop()