# Function - parameter, argument

def add(n1,n2):
    return n1 + n2

n = 100 
m = 500
result = add(n,m)
print(result)

n = 35
m = 34
print(add(n,m))

# Drawing square using turtle and function

import turtle

def draw_square(side_length):
    for i in range(4):
         turtle.forward(side_length)
         turtle.left(90)

counter = 0
while counter < 90:
    draw_square(100)
    turtle.right(4)
    counter += 1

turtle.exitonclick()


def myfnc(x):
    print("inside myfnc", x)
    x = 10
    print("inside myfnc", x)
    
x = 20
myfnc(x)
print(x)


def myfnc(y):
    print("y =", y)
    print("x", x)

x = 20
myfnc(x)


def myfnc(y):
    print("y = ", y)
    print("x = ", x)

x = 20
myfnc(x)
print("y:", y)


def myfnc(y = 10):
    print("y =", y)

x = 20
myfnc(x)
myfnc()

def myfnc(x, y=10, z):
    print("x =", x, "y =", y, "z =", z)

x = 5
y = 6 
z = 7
myfnc(x, y, z)


def myfnc(x, y=10, z=0):
    print("x =", x, "y =", y, "z =", z)

x = 5
y = 6 
z = 7
myfnc(x, y, z)
myfnc(x, y)
myfnc(x)


def myfnc(x, z, y=10):
    print("x =", x, "y =", y, "z =", z)

myfnc(x =1, y = 2, z = 5)
a = 5
b = 6
myfnc(x = a, z = b)
a = 1
b = 2
c = 3
myfnc(y = a, z = b, x = c)


def add_numbers(numbers):
    result =  0
    for number in numbers:
        result += number
    return result

result = add_numbers([1, 2, 30, 4, 5, 9])
print(result)

def test_fnc(li):
    li[0] = 10

my_list = [1, 2, 3, 4]
print("before function call", my_list)
test_fnc(my_list)
print("after function call", my_list)

list1 = [1, 2, 3, 4]
list2 = list1
print(list1)
print(list2)
list2[0] = 100
print(list2)
print(list1)


li = [1, 2, 3]
result = sum(li)
print(result)