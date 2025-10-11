# from turtle import Turtle,Screen

# timmy=Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("teal")
# timmy.forward(150)

# myScreen=Screen()
# print(myScreen.canvheight)
# myScreen.exitonclick()


from prettytable import PrettyTable
table=PrettyTable()
table.field_names=["Name","Age","Country"]
table.add_row(["John", 30, "USA"])
table.add_row(["Anna", 25, "UK"])
table.add_row(["Peter", 35, "Australia"])
print(table)  