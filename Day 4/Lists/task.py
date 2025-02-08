# #### Random Module
# import random
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
fruits = ["Cherry", "Apple", "Pear"]

print(fruits[0])
print(fruits[2])

states_of_america = ["Delaware", "Pennsylvania", "New Jersey",
                     "Georgia", "Connecticut", "Massachusetts",
                     "Maryland", "South Carolina", "New Hampshire",
                     "Virginia", "New York", "North Carolina",
                     "Rhode Island", "Vermont", "Kentucky",
                     "Tennessee", "Ohio", "Louisiana", "Indiana",
                     "Mississippi", "Illinois", "Alabama", "Maine",
                     "Missouri", "Arkansas", "Michigan", "Florida",
                     "Texas", "Iowa", "Wisconsin", "California",
                     "Minnesota", "Oregon", "Kansas",
                     "West Virginia", "Nevada", "Nebraska",
                     "Colorado", "North Dakota", "South Dakota",
                     "Montana", "Washington", "Idaho", "Wyoming",
                     "Utah", "Oklahoma", "New Mexico", "Arizona",
                     "Alaska", "Hawaii"]

print(states_of_america[-1])
print(states_of_america[-2])
print(states_of_america[-3])

#states_of_america[1]="Pencilvania"
states_of_america.append("SelfLand")
states_of_america.extend(["abcdLand","efghLand"])

print(states_of_america)

























