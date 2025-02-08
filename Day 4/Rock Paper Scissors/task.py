# #### Random Module
import random
# # # import my_module
#
# random_integer=random.randint(1,10)
# print(random_integer)
# # # print(my_module.my_favourite_number)
#
# random_number_0_to_1=random.random()
# print("random_number_0_to_1",random_number_0_to_1)
# print("random_number_0_to_10",random.random()*10)
#
# random_float=random.uniform(1,10)
#
# print("random_number_1_to_10",random_float)
#
#
#
# random_coin_toss=random.randint(0,1)
# if random_coin_toss==0:
#     print("Heads")
# else:
#     print("Tails")
#
#
# # #### Lists
#
# fruits = ["Cherry", "Apple", "Pear"]
#
# print(fruits[0])
# print(fruits[2])
#
# states_of_america = ["Delaware", "Pennsylvania", "New Jersey",
#                      "Georgia", "Connecticut", "Massachusetts",
#                      "Maryland", "South Carolina", "New Hampshire",
#                      "Virginia", "New York", "North Carolina",
#                      "Rhode Island", "Vermont", "Kentucky",
#                      "Tennessee", "Ohio", "Louisiana", "Indiana",
#                      "Mississippi", "Illinois", "Alabama", "Maine",
#                      "Missouri", "Arkansas", "Michigan", "Florida",
#                      "Texas", "Iowa", "Wisconsin", "California",
#                      "Minnesota", "Oregon", "Kansas",
#                      "West Virginia", "Nevada", "Nebraska",
#                      "Colorado", "North Dakota", "South Dakota",
#                      "Montana", "Washington", "Idaho", "Wyoming",
#                      "Utah", "Oklahoma", "New Mexico", "Arizona",
#                      "Alaska", "Hawaii"]
#
# print(states_of_america[-1])
# print(states_of_america[-2])
# print(states_of_america[-3])
#
# #states_of_america[1]="Pencilvania"
# states_of_america.append("SelfLand")
# states_of_america.extend(["abcdLand","efghLand"])
#
# print(states_of_america)

# ###### Banker Roulette


# friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
#
# print(random.choice(friends))
# print(friends[random.randint(0,4)])


# ### IndexError

# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
#                      "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
#                      "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
#                      "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
#                      "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
#                      "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
#                      "New Mexico", "Arizona", "Alaska", "Hawaii"]
#
# print(states_of_america)
# print(states_of_america[len(states_of_america)-1],
#       len(states_of_america),len(states_of_america)-1)
#
#
# # # dirty_dozen=['Strawberries', 'Spinach', 'Nectarines', 'Apples', 'Potatoes', 'Grapes',
# # 'Peaches', 'Pear', 'Kale', 'Tomatoes',
# # 'Celery', 'Cherries']
#
# fruits=["Strawberries","Nectarines","Apples","Grapes","Peaches",
#         "Cherries","Pear"]
# vegetables=["Spinach","Kale","Tomatoes","Celery","Potatoes"]
#
# dirty_dozen=[fruits,vegetables]
#
# print(dirty_dozen)
#




rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rock_paper_scissor_alliance=[rock,paper,scissors]
user_choice=int(input("What do you choose? Type 0 for Rock, 1 for "
                    "Paper or 2 for "
      "Scissor\n"))

print(rock_paper_scissor_alliance[user_choice])

computer_choice=random.randint(0,2)

print("Computer chose:\n",rock_paper_scissor_alliance[computer_choice])

if user_choice==computer_choice:
    print("You Draw")
elif ((user_choice==0 and computer_choice==2) or
      (user_choice==1 and computer_choice==0) or
      (user_choice==2 and computer_choice==1)):
    print("You Win")
else:
    print("You Lose")











