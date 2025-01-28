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


# ###### For Loops with Range
print(range(1, 10)) ##needs to be used with conjunction to a function

for num in range(1,11):
    print(num)
for num in range(1,11,2):
    print(num)


sum_num=0
for num in range(1,101):
    sum_num+=num
print(sum_num)

for num in range(1,101):
    if num%3==0 and num%5==0:
        print("FizzBuzz")
    elif num%3==0:
        print("Fizz")
    elif num%5==0:
        print("Buzz")
    else:
        print(num)













