import turtle, random, math

class Game:
    '''
    Purpose: sets up game screen 
    Instance variables: __init__(self) defines the start game screen 
    Methods: gameloop(loops game)
    '''

    def __init__(self):
        #Bottom left corner of screen is (0, 0)
        #Top right corner is (500, 500)
        turtle.setworldcoordinates(0, 0, 500, 500)
        cv = turtle.getcanvas()
        cv.adjustScrolls()

        #Ensure turtle is running as fast as possible
        turtle.delay(0)      
        self.player = SpaceCraft(random.uniform(100,400), random.uniform(250,450), random.uniform(-4,4), random.uniform(-2,0))
        self.gameloop()

        turtle.onkeypress(self.player.thrust, 'Up')
        #These two lines must always be at the BOTTOM of __init__
        turtle.listen()
        turtle.mainloop()

    def gameloop(self):
        self.player.move()
        turtle.ontimer(self.gameloop, 30)
        if self.player.ycor() < 20:
            if -3<=self.player.yvel<=3 and -3<=self.player.xvel<=3:
                print("Successful landing!")
            else: 
                print("You crashed!")



  



class SpaceCraft(turtle.Turtle):
    '''
    Purpose: represents an object falling towards the moon's surface 
    Instance variables: self.vel is the velocity of the object, self.fuel is the fuel remaining
    Methods: move(moves spacecraft), thrust(usues up arrow to move craft), left/right_turn(turns the spacecraft)
    '''
    def __init__(self, x, y, xvel, yvel):
            turtle.Turtle.__init__(self)
            self.xvel = xvel
            self.yvel = yvel
            self.fuel = 40
            self.left(90)

            self.penup()
            self.speed = 0
            self.goto(x,y)
    def move(self):
         self.yvel = self.yvel - 0.0486
         new_x = self.xcor() + self.xvel
         new_y = self.ycor() + self.yvel
         self.goto(new_x,new_y)
    def thrust(self): 
        #  print("Up button pressed")
        if self.fuel > 0 :
             self.fuel = self.fuel - 1
             angle = math.radians(self.heading())
             cos_angle = math.cos(angle)
             self.xvel = self.xvel + cos_angle
             sin_angle = math.sin(angle)
             self.yvel = self.yvel + sin_angle
             print("Fuel:", self.fuel)
        else: 
             print("Out of fuel")
    def left_turn(self):
        if self.fuel > 0 :
            self.fuel = self.fuel - 1
            self.left(15)
            print("Fuel:", self.fuel)
        else: 
            print("Out of fuel")
    def right_turn(self):
        if self.fuel > 0 :
            self.fuel = self.fuel - 1
            self.right(15)
            print("Fuel:", self.fuel)
        else: 
            print("Out of fuel")

         



if __name__ == '__main__':
    Game()
