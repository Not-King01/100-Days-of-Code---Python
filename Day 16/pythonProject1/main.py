# from turtle import Turtle, Screen
# king = Turtle()
# print(king)
#
# my_screen = Screen()
# king.color('aquamarine')
# king.shape('turtle')
# print(my_screen.canvheight)
# king.forward(100)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)