import turtle

class babyturtle(turtle.Turtle):
    def __init__(self,color):
        super().__init__()
        self.shape("turtle")
        self.color(color)
        self.speed('fastest')
    def make_circle(self):
        self.circle(100)
    def make_square(self):
        for i in range(4):
            self.forward(100)
            self.right(90)
    def make_triangle(self):
        for i in range(3):
            self.forward(100)
            self.right(120)
        
import random
for i in range(20):
    b = babyturtle(['green','red','blue'][i%3])
    b.left(random.randint(0,360))
    b.make_square()
    b.penup()
    b.forward(50)
    b.pendown()
    b.make_triangle()
    b.penup()
    b.forward(20)
    b.pendown()
    b.make_circle()



turtle.mainloop()


