#exercise 5-3, 5-4, 5-5, 5-6, 5-7, using elif statements

alien = 'green'

if alien == 'green':
	print("player points = 5")
else:
	print("player points has earnt no points.")

if alien == 'red':
	print("player points = 5")
else:
	print("player points has earnt no points.")

print("\n")

alien = "red"

if alien == 'green':
	print("player points = 5")
elif alien == 'red':
	print("player points = 10")
else:
	print("player points has earnt no points.")

print("\n")

#5-6 Stages of life 

age = 65

if age < 2:
	print("You are a baby")
elif age >= 2 and age < 4: 
	print("You are a Toddlar")
elif age >= 4 and age < 13: 
	print("You are a Kid")
elif age >= 13 and age < 20: 
	print("You are a Teenager")
elif age >= 20 and age < 65: 
	print("You are a Adult")
else:
	print("You are an Elder")

print("\n")

#5-7 list of fruit 

favourite_fruit = ["Apple", "Orange", "Banana", "Grapes"]

if "Banana" in favourite_fruit:
	print("ooo I like bananas")
if "Orange" in favourite_fruit:
	print("ooo I like Orange")
if "Grapes" in favourite_fruit:
	print("ooo I like Grapes")
if "Apple" in favourite_fruit:
	print("ooo I like Apples")
if "Melon" not in favourite_fruit:
	print("Thank goodness I hate melon")


