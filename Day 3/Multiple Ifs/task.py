# # ####### IF ELSE
#
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
#
# ## Comparator Operators
# ##   >     -    Greater than
# ##   <     -    Less than
# ##   >=    -    Greater than or equal to
# ##   <=    -    Less than or equal to
# ##   ==    -    Equal to
# ##   !=    -    Not equal to
#
#
# if height>120:
#     print("Yoy can ride the rollercoaster")
# else:
#     print("Sorry you have to grow taller before you can ride.")


# # ######## Modulo
#
# ## PAUSE 1 - What is 10 % 3?
#
# print(10%3)
#
# # ## PAUSE 2 - Check Odd or Even
#
# num=input("Enter a Number: ")
#
# if float(num)%2==0:
#     print("Even")
# else:
#     print("Odd")


# # ## Nesting and Elif
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
#
# if height >= 120:
#     print("You can ride the rollercoaster")
#     age = int(input("What is your age? "))
#     if age<=12:
#         print("Please pay 5$.")
#     elif age<=18:
#         print("Please pay 7$.")
#     else:
#         print("Please pay 12$.")
#
# else:
#     print("Sorry you have to grow taller before you can ride.")



# # ## Multiple Ifs

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    ticket_price=0
    if age <= 12:
        print("Child tickets are $5.")
        ticket_price=5
    elif age <= 18:
        print("Youth tickets are $7.")
        ticket_price=7
    else:
        print("Adult tickets are $12.")
        ticket_price=12
    photo_required=input("Do you want to have a photo take? Type y "
                         "for Yes and n for No")
    if photo_required=='y':
        ticket_price+=3
    print(f"Your total bill is ${ticket_price}")
else:
    print("Sorry you have to grow taller before you can ride.")



