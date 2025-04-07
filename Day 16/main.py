# from turtle import Turtle, Screen
# timmy=Turtle()
# timmy2=Turtle()
#
# print(timmy)
# timmy.shape('turtle')
# timmy.color('coral')
# timmy.left(100)
# timmy.forward(100)
# timmy2.shape('turtle')
# timmy2.color('coral')
# timmy2.forward(100)
#
# my_screen=Screen()
#
#
# print(my_screen.canvheight)
#
# my_screen.exitonclick()

from prettytable import PrettyTable
table=PrettyTable()

print(table)

table.add_column("Pokemon Name",["Pikachu","Squirtle",
                                 "Charmandar"])
table.add_column("Type",["Electric","Water","Fire"])
table.align='l'


print(table)













