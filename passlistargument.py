def main():
    x=1 #x represents an int value
    y=[1,2,3]  #y represents a list

    m(x,y) #Invoke m with arguments x and y

    print("x is",x) 
    print("y[0] is",y[0])

def m(number,numbers):
    number=1001 #number is a local variable
    numbers[0]=5555 #numbers is a reference to the list y

main()