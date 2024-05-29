saarc = ["Bangladesh", "India", "Srilanka", "Pakistan", "Nepal", "Bhutan"]
print(saarc)
saarc.append("Afhanistan")
print(saarc)
saarc.sort()
print(saarc)
li = [1, 3, 7, 2, 4, 6, 1]
li.sort()
print(li)

li = [1, 2, 3, 4 ]
li.reverse()
print(li)

li =["Mango","Banana","Orange"]
li.reverse()
print(li)


fruits = ["Mango","Banana","Orange"]
fruits.insert(0, "Apple")
print(fruits)
fruits.insert(2, "Coconut")
print(fruits)


fruits = ['apple', 'mango', 'coconut', 'banana', 'orange']
fruits.remove("coconut")
print(fruits)
fruits.remove("pineapple")
print(fruits)

fruits = ['apple', 'mango', 'coconut', 'banana', 'orange']
item = "pineapple"
if item in fruits:
    remove(item)
else:
    print(item, "not in list")

fruits = ['apple', 'mango', 'coconut', 'banana', 'orange']
item = fruits.pop()
item
fruits


fruits = ['apple', 'mango', 'coconut', 'banana', 'orange']
item = fruits.pop(1)
item
fruits

li = [1, 2, 3]
li2 = [3, 4, 5, 6]
li.extend(li2)
li

li = [1, 2, 3, 3, 4, 5, 6]
li.count(3)
li.count(5)
li.count(10)
 
li = [1, 2, 3, 3, 4, 5, 6]
del(li[1])

li = []
for x in range(10):
    li.append(x)

print(li)



li1 = [1,2,3]
li2 = [4,5,6]
li = li1 + li2
print(li)

li1 = [1,2,3]
li2 = li1 * 3
print(li2)


li = ["a","b","c"]
print(li)

str = "".join(li)
print(str)

str = "-".join(li)
print(str)


# list comprehensions
li = [1,2,3,4]
new_li = []
for x in li:
    new_li.append(2*x)

print(new_li)

new_li = [2 * x for x in li]
new_li

li = [1,2,3,4,5,6,7,8,9,10]
even_numbers = []
for x in li:
    if x % 2 == 0:
        even_numbers.append(x)

print(even_numbers)

# using list comprehensions
even_numbers = [x for x in range(1,11) if x % 2 == 0]