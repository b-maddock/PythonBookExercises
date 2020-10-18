players = ["Ben", "Ellie", "Tom", "Lucy", "Terry", "OccupyTheWeb"]

print("Team 1:", players[:3])
print("Team 2:", players[-3:])

print("Three items from the middle of the list are:", players[2:5])

pizza_toppings = ["Cheese", "olives", "onion", "meatballs", "bacon", "pineapple"]

friends_pizza = pizza_toppings[:]

pizza_toppings.append("tuna")
friends_pizza.append("beans")

print("\nMy favourite pizza is: ")

for pizza in pizza_toppings:
	print(pizza)

print("\nMy friends favourite pizza is: ")

for pizza in friends_pizza:
	print(pizza)


