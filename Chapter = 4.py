numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers)
print(numbers[0])
print(numbers[1])
print(numbers[5])
saarc = ["Bangladesh","Afganistan","Bhutan","Nepal","India","Pakistan","Srilanka"]
country = input("Enter the name of the country: ")

if country in saarc:
    print(country,"is a member of SAARC")
else:
    print(country,"is not a member of SAARC")
    print("Program terminated")


marks = input("Please enter your marks: ")
marks = int(marks)

if marks >= 80:
    grade = "A+"
elif marks >= 70:
        grade = "A"
elif marks >= 60:
            grade = "A-"
elif marks >= 50:
                grade = "B"
else:
                    grade= "F"
print("Your grade is",grade)


n1 = 50
n2 = 60
n3 = 65

if n1 > n2:
    max_n = n1
else:
    max_n = n2

if n3 > max_n:
    max_n = n3

print("Maximum  : ",max_n)

#LEAP YEAR
year = input("Enter the year : ")
year = int(year)
if year % 4 == 0:
    print(year,"is a Leap Year")
else:
    print(year,"is not a Leap Year")

    