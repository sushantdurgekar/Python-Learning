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































