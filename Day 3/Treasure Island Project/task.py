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

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
#
# if height >= 120:
#     print("You can ride the rollercoaster")
#     age = int(input("What is your age? "))
#     ticket_price=0
#     if age <= 12:
#         print("Child tickets are $5.")
#         ticket_price=5
#     elif age <= 18:
#         print("Youth tickets are $7.")
#         ticket_price=7
#     else:
#         print("Adult tickets are $12.")
#         ticket_price=12
#     photo_required=input("Do you want to have a photo take? Type y "
#                          "for Yes and n for No")
#     if photo_required=='y':
#         ticket_price+=3
#     print(f"Your total bill is ${ticket_price}")
# else:
#     print("Sorry you have to grow taller before you can ride.")



# #### Python Pizza
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M or L: ")
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")
#
# final_bill=0
#
# if size=='S':
#     final_bill+=15
# elif size=='M':
#     final_bill+=20
# elif size=='L':
#     final_bill+=25
# else :
#     print("You enter the wrong input")
#
# if pepperoni=='Y':
#     if size=='S':
#         final_bill+=2
#     else:
#         final_bill+=3
#
# if extra_cheese=='Y':
#     final_bill+=1
#
# print(f"Your final bill is: ${final_bill}.")


# # #### Logical Operators
#
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0
#
# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if age < 12:
#         bill = 5
#         print("Child tickets are $5.")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets are $7.")
#     elif age>=45 and age<=55:
#         print("Everything is going to be ok.Have a free ride on us!")
#     else:
#         bill = 12
#         print("Adult tickets are $12.")
#
#     wants_photo = input("Do you want a photo taken? Y or N. ")
#     if wants_photo == "Y":
#         bill += 3
#
#     print(f"Your final bill is ${bill}")
#
# else:
#     print("Sorry, you have to grow taller before you can ride.")



print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

cross_road_direction=input("You're at a cross road. Where do you "
                           "want to go?\n   Type 'left' or 'right'\n")

if cross_road_direction.lower()=="left":
    print("You've come to a lake. "
          "There is an island in the middle of the lake.")
    swim_or_wait=input("     Type 'wait' to wait for a boat. "
              "Type 'swim' to swim across.\n")
    if swim_or_wait.lower()=='wait':
        print("You arrive at the island unharmed. "
              "There is a house with 3 doors.")
        door_color_choice=input("One red, one yellow and one blue. "
                                "Which colour do you choose?\n")
        if door_color_choice.lower()=='red':
            print("It's a room full of fire. Game Over.")
        elif door_color_choice.lower()=='blue':
            print("You enter a room of beasts. Game Over.")
        elif door_color_choice.lower()=='yellow':
            print("You found the treasure! You Win!")
        else:
            print("Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fall into a hole. Game Over.")
