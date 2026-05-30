#conditional statement:

#Q.1
age=int(input("Enter your age:"))

if age >=18:
    print("You are Eligible for voting")
else:
    print("Not Eligible")

# Q.2

num1=int(input("Enter the number:"))
num2=int(input("Enter the number:"))
if num1>num2:
    print(num1,"is greater number")
else:
    print(num2, "is greater number")

# Q.3

Number=int(input("Enter the number:"))
if Number %2==0:
    print("Even Number")
else:
    print("Odd number")

#Q.4 Take a number from the user:
# if marks are greater than 35 -> print "Pass"
# Otherwise print "Fail"

marks=int(input("Enter the Score:"))

if marks >=35:
    print("Pass")
else:
    print("Fail")

# Q.5 TAke temperature from the user:
# If temperature is greater than 30_> print "HOT"
# Otherwise "Cool"

temp=int(input("Enter the current Temperature:"))

if temp >=30:
    print("Temperature -> HOT")
else:
    print("Temperature -> Cool")

# Q.5 Take a password from the user:
# If the password is "python123" -> print "Access Granted"
# Otherwise -> print "Wrong Password"

password =(input("Please enter the password:"))

if password == "python123":
    print("Access Granted")
else:
    print("Wrong Password")

# Q.6 Take marks of 3 subjects from the user:
# print the total marks.
# print the average marks.
Subject1= int(input("Enter the marks of Subject1:"))
Subject2= int(input("Enter the marks of Subject2:"))
Subject3= int(input("Enter the marks of Subject3:"))

total= Subject1+ Subject2+ Subject3
average = total/3

print("Total Marks", total)
print("average Marks", average)

# Q.7 Take a number from the user and check whether it is:
# Positive
# Negative
# or Zero

Number=int(input("Enter the Value:"))

if Number > 0:
    print("Positive number")
elif Number <0:
    print("Negative number")
else:
    print("Zero")