#Return the max between two values
def max(num1,num2):
    if num1 > num2:
        result = num1
    else:
        result = num2
    
    return result #Return resuft

def main():
    i=5
    j=2
    k= max(i,j)
    print("The maximum between",i,"and",j,"is",k)

main()       #Call the main function