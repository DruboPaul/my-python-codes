for i in range(10):
    print("I want to be a great programmer")

for i in range(5):
    print(i)

import turtle 

turtle.shape("turtle")
turtle.speed(1)

turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)

turtle.exitonclick()



import turtle
turtle.shape("turtle")
turtle.speed(1)

for i in range(4):
    turtle.forward(100)
    turtle.left(90)

turtle.exitonclick() 


result = 0 
for i in range(50):
    result = result + 1
     
print(result)

result = 0 
for _ in range(50):
    result = result + 1
     
print(result)


result = 0 
num = 1 
for _ in range(50):
    result = result + num 
    num = num + 1
     
print(result)


result = 0 
num = 1 
for _ in range(50):
    result += num 
    num += 1
     
print(result)


result = 0 
for num in range(1,51):
    result += num 
     
print(result)

for i in range(1,20,5):
    print(i)




numbers = [6, 1, 3, 0, 9, 3, 2, 5]
max_n = numbers[0]

# Find the maximum value
for n in numbers:
    if n > max_n:
        max_n = n

# Print the maximum value
print(max_n)


result = 0

for num in range(100):
    if num % 5 == 0:
        print(num)
        result += num

# Print the sum after the loop has finished
print("Sum is:", result)



result = 0 
for num in range(5,101,5):
    print(num)
    result += num
print("Sum is : ",result)



import turtle 
turtle.speed(1)

for i in range(20):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(3)
    turtle.pendown()

turtle.exitonclick

# loop into the loop(Nested loop)
import turtle
turtle.shape("turtle")
turtle.speed(1)

for side_length in range(50,100,10):
    for i in range(4):
        turtle.forward(side_length)
        turtle.left(90)

turtle.exitonclick()


# loop into the list

saarc = ["Bangladesh","Afghanistan","Bhutan","Nepal","India","Pakistan","Srilanka"]
for country in saarc:
    print(country,"is a member of SAARC")


li = list(range(11))
print(li)

li = list(range(2,21,2))
print(li)


# while loop

i = 0 
while i < 5:
    print(i)
    i += 1


i = 5 
while i>= 0:
    i -= 1
    print(i)


# namta

n = int(input("Please enter a positive integer:"))

m = 1
while m<= 10:
    print(n,"x",m,"=",n*m)
    m += 1

import turtle 

turtle.color("red")
turtle.speed(5)

counter = 0
while counter < 36:
    for i in range(4):
      turtle.forward(100)
      turtle.right(90)
    turtle.right(10)
    counter += 1
     
turtle.exitonclick()


import turtle
height = 5
width = 5

turtle.speed(2)

turtle.penup()

for y in range(height):
    for x in range(width):
        turtle.dot()
        turtle.forward(20)
    turtle.backward(20*width)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)

turtle.exitonclick()

while True:
    n = int(input("Please enter a number (0 to exit): "))
    if n == 0:
        break
    print("Square of",n,"is",n*n)

while True:
    n = int(input("Please enter a positive number(0 to exit):"))
    if n < 0:
        print("We only allow positve number.Please try again.")
        continue
    if n == 0:
        break
    print("Square of",n,"is",n*n)


terminate = False

while not terminate:
    number1 = int(input("Please enter a number: "))
    number2 = int(input("Please enter another number: "))

    while True:
        operation = input("Please enter add/sub or quit to exit: ")
        if operation == "quit":
            terminate = True
            break
        if operation not in ["add", "sub"]:
            print("Unknown operation!")
            continue
        if operation == "add":
            print("Result is", number1 + number2)
            break
        if operation == "sub":
            print("Result is", number1 - number2)
            break