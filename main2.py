import turtle

#prompt the user for inputing two points
x1=float(input("Enter x-coordinate for Point 1"))
y1=float(input("Enter y-coordinate for Point 1"))
x2=float(input("Enter x-coordinate for Point 2"))
y2=float(input("Enter y-coordinate for Point 2"))

#compute ths distance
distance=((x1-x2)**2+(y1-y2)**2)**0.5

#display two points and connecting line
turtle.penup()
turtle.goto(x1,y1) #move to (x1,y1)
turtle.pendown()
turtle.write("Point 1", font=("Times",12))
turtle.goto(x2,y2) #draw a line to (x2,x1)

#Move to the center point of the line
turtle.penup()
turtle.goto((x1+x2) / 2,(y1+y2) / 2)
turtle.write(distance,font=("Times",12))

turtle.done()