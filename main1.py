#enter the frist point with two double values
x1=float(input("Enter x-coordinate for pioint 1:"))
y1=float(input("Enter y-coordinate for pioint 1:"))
#enter the second point with two double values
x2=float(input("Enter x-coordinate for pioint 2:"))
y2=float(input("Enter y-coordinate for pioint 2:"))
#compute the distance
distance=((x2+x1)**2+(y2+y1)**2)**0.5

print("The distance between the two points is",distance)