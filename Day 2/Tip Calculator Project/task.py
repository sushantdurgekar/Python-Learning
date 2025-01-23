

####### Data Types

print(len("Hello"))

# error about data type int
# print(len(1234))

"Hello" # this is string data type

# Subscripting
print("Hello"[0]) #H
print("Hello"[4]) #o
print("Hello"[-1]) #o

# String

print("123"+"456") # Concatenation

# Integers = Whole number
print(123+456)

# Large Integers
print(123_456_789)

# Float = Floating Point Number
print(3.14159)

# Boolean
print(True,0)
print(False,1)



######## Type Error, Checking and Conversion

# PAUSE 1. Fix the len() function so it has no more warnings or errors.
print(len("Hello"))
print("type('Hello')",type("Hello"))

# PAUSE 2. Write out 4 type checks to print all 4 data types
print("type('12345')",type("12345"))
print("type(12345)",type(12345))
print("type(123.45)",type(123.45))
print("type(True)",type(True))


# Type Conversion
# float()
# int()
# str()
# bool()

print(int("123")+int("456"))
print(str(123)+str(456))
print(str(12.3)+str(45.6))
print(float("12.3")+float("45.6"))
print(float(123)+float(456))
print(bool("true"),bool(""),bool("abc"),bool(0),bool(1),bool(0.0),
      bool(0.1),bool([]),bool([1]))


# PAUSE 3. Make this line of code run without errors

# print("Number of letters in your name: " + str(len(input("Enter your name"))))

name=input("Enter your name\n")
length_of_name=len(name)
print("type of 'Number of letters in your name: '",type("Number of letters in your name: "))
print("type of 'length_of_name'",type(length_of_name))
print("Number of letters in your name: " + str(length_of_name))





###### Mathematical Operations

print("My age: " + str(12))

print(123 + 456)
print(7 - 3)
print(3 * 2)
print(6 / 3)
print(6 // 3)
print(5 / 3)
print(5 // 3)
print(2 ** 14)

# PEMDAS LR - Parentheses, Exponents, Multiplication/Division,
# Addition/Subtraction  (Left to Right)
# ()
# **
# * OR /
# + OR -


# PAUSE 1. What is the output of this code?

print(3*3+3/3-3) #7.0

# PAUSE 2. Change the code so it outputs 3?
# print(3 * 3 + 3 / 3 - 3)

print(3 * (3 + 3) / 3 - 3) #3.0
print(3+3*3/3-3) #3.0


###### Number Manipulation

bmi = 84 / 1.65 ** 2

print(bmi)
# Flooring a Number
print(int(bmi))

# Rounding a Number
print(round(3.738492)) # Becomes 4

print(round(3.14159)) # Becomes 3

print(round(3.14159, 2)) # Becomes 3.14)

print(round(bmi))
print(round(bmi,2))

# Assignment Operators
# +=
# -=
# *=
# /=

score=100

# User scores a point
score+=1
print(score)

# User lost a point
score-=1
print(score)


# Similar cases for multiplication and division
score*=2
print(score)
score/=4
print(score)

# f-Strings

score=10
height=1.7
is_winning=True

print(f"Your score is {score}, your height is {height}, "
      f"your winning is {is_winning}")







##### Tip Calculator Project

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 "
                "15 "))
people = int(input("How many people to split the bill? "))

bill_per_person=round(bill/people*(1+tip/100),2)

print(f"Each person should pay: ${bill_per_person}")