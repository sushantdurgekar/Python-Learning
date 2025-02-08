# # # ###### Dictionaries
#
# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from "
#            "running as expected.",
#     "Function": "A piece of code that you can easily call over and "
#                 "over again.",
#     "Loop" : "The action of doing something over and over again.",
#     123:"Just integer 123"
# }
#
# # print(programming_dictionary["Bug"])
# # print(programming_dictionary["Function"])
# # print(programming_dictionary[123])
# #
# # programming_dictionary["Dictionaries"]=("A dictionary in Python "
# #                                         "functions similarly to a "
# #                                         "dictionary in real life. "
# #                                         "It's a data structure that allows us to associate a key to a value and pair the two pieces of data together.")
# #
# # print(programming_dictionary)
#
# # programming_dictionary["Bug"]="A moth in your computer"
#
# print(programming_dictionary)
#
# for thing in programming_dictionary:
#     print(thing)
#     print(programming_dictionary[thing])
#
#
#
# ###### # Nested Lists and Dictionaries
#
# capitals={
#     "France":"Paris",
#     "Germany":"Berlin"
# }
#
# # # #### nested list in dictionary
# travel_log={
#     "France":["Paris","Lille","Dijon"],
#     "Germany":["Stuttgart","Berlin"],
# }
#
# print(travel_log["France"][1])
#
# # # ### nested list
# nested_list=["A","B",["C","D"]]
#
# print(nested_list[2][1])

# # #### nested dictionary in dictionary

travel_log={
    "France": {
        "total_visited":8,
        "cities_visited":["Paris", "Lille", "Dijon"]
    },
    "Germany": {
        "total_visited":8,
        "cities_visited":["Berlin", "Hamburg", "Stuttgart"]
    },
}

print(travel_log["Germany"]["cities_visited"][2])






