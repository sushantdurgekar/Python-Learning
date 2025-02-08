# # #### For Loops
#
# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit+" pie")


# # #### Highest Score
# student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59,
#                   68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
#
# total_score_by_bulitinfunc=sum(student_scores)
# print(total_score_by_bulitinfunc)
#
# score_sum=0
# for score in student_scores:
#     score_sum+=score
# print(score_sum)
#
# max_score_by_bulitinfunc=max(student_scores)
# print(max_score_by_bulitinfunc)
# min_score_by_bulitinfunc=min(student_scores)
# print(min_score_by_bulitinfunc)
#
# max_score=0
# for score in student_scores:
#     if score>max_score:
#         max_score=score
# print(max_score)
#
# min_score=max_score
# for score in student_scores:
#     if score<min_score:
#         min_score=score
# print(min_score)


# # ###### For Loops with Range
# print(range(1, 10)) ##needs to be used with
#                       conjunction to a function ex for loop
#
# for num in range(1,11):
#     print(num)
# for num in range(1,11,2):
#     print(num)
#
#
# sum_num=0
# for num in range(1,101):
#     sum_num+=num
# print(sum_num)
#
# for num in range(1,101):
#     if num%3==0 and num%5==0:
#         print("FizzBuzz")
#     elif num%3==0:
#         print("Fizz")
#     elif num%5==0:
#         print("Buzz")
#     else:
#         print(num)





# ######### Password Generator Project

import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
           'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your "
                       "password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


# # ## Easy
pwd=''

for letter in range(0,nr_letters):
    pwd+=letters[random.randint(0,len(letters)-1)]
for symbol in range(0,nr_symbols):
    pwd+=symbols[random.randint(0,len(symbols)-1)]
for number in range(0,nr_numbers):
    pwd+=numbers[random.randint(0,len(numbers)-1)]

print(f"Your easy to crack password is : {pwd}")
#
#
# # ## Hard
pwd_list=[]
for letter in range(0,nr_letters):
    pwd_list.append(letters[random.randint(0,len(letters)-1)])
for symbol in range(0,nr_symbols):
    pwd_list.append(symbols[random.randint(0,len(symbols)-1)])
for number in range(0,nr_numbers):
    pwd_list.append(numbers[random.randint(0,len(numbers)-1)])

random.shuffle(pwd_list)
hard_pwd=""
for char in pwd_list:
    hard_pwd+=char

print(f"Your tough to crack password is : {hard_pwd}")










