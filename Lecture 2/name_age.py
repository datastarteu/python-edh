ages = {'Pablo':34, 'Eva':23}

name = input("What is your name? ")
if name in ages.keys():
	print(name)
	print("Your age is "+str(ages[name]))
else:
	print("Wrong name")

	
#EXERCISE:
# Write a program that gives you the bill in a restaurant:
# - User enters the food items (separated by comma)
# - You program looks in a dictionary of prices the cost of each food item
# - The costs are added and are shown to the user.