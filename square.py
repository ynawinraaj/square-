import turtle

#create canvas
turtle.Screen().bgcolor("blue")
sc=turtle.Screen()
sc.setup(400,300)

turtle.title("welcom to the turtle windo")

# turtle object creation
board=turtle.Turtle()

#creating a square
for i in range(4):
    board.forward(100)
    board.left(90)
    i=i+1