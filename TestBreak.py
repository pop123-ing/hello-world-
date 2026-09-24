sum=0
number=0
while number < 20:
    number += 1
    sum += number
    if number >= 100:
        break

print("Sum is", sum)
print("Number is", number)