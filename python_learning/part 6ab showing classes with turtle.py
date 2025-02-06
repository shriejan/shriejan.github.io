import turtle 


class shriejanturtle(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        
        self.goto(0,0)
        self.setheading(90)

    def move_forward(self):
        self.forward(100)

    def turn_left(self):
        self.left(90)

    def turn_right(self):
        self.right(90)
    def change_angle_slightly(self,a):
        self.left(a)
    
    def make_sqaure(self):
        for i in range(4):
            self.move_forward()
            self.turn_right()


sht = shriejanturtle()

for i in range(20):
    sht.make_sqaure()
    sht.change_angle_slightly(10)


turtle.mainloop()



