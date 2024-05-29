s = "hello"
len(s)
l = len(s)
l
print(l)

s = ''
len(s)


s = "Dimik's"
print(s)
s = 'Dimik\'s'
print(s)

country = "Bangladesh"
country[0] 

for c in country:
    print(c)


c = ['A','b','c']
print(c)

c[0] = 'a'
print(c)

country = "Bangladesh"
country[0] = 'b'


country = "Bangla" + "desh"
print(country)

x = "50" + "5"
print(x)

country = "Bangladesh"
country.find("Ban")


country = "North Korea"
new_country = country.replace("North", "South")
print(new_country)
print(country)

text = "this is a test.this is another test. this is final test."
new_text = text.replace("this", "This")
print(new_text)
print(text)

text = " this is a string. "
text
text.lstrip()
text.rstrip()
text


text = " this is a string. "
new_text = text.rstrip()
new_text
text

s1 = "Bangladesh"
s_up = s1.upper()
s_up
s_lo = s1.lower()
s_lo
s = "hello"
s_cap = s.capitalize()
s_cap

str = " I am a programmer ."
words = str.split()
print(words)
words
for word in words:
    print(word)


str = "This is "
str.count("is")

s = "Bangladesh"
s.startswith("Ban")
s.startswith("ban")
text = 'hello'
text = text.replace('hello', 'Hello')
print(text)


name = "Mr. Anderson"
if name.startswith("Mr. "):
   print("Dear Sir")

import turtle

name = turtle.textinput("name", "What is your name?")
name = name.lower()
if name.startswith("mr"):
    print("Hello Sir, how are you?")
elif name.startswith("mrs") or name.startswith("miss") or name.startswith("ms"):
    print("Hello Madam, how are you?")
else:
    name = name.capitalize()
    str = "Hi" + name + "! How are you?"
    print(str)

turtle.exitonclick()

str = "a quick brown fox jumps over the lazy dog"
for c in "abcdefghijklmnopqrstuvwxyz":
    print(c, str.count(c))