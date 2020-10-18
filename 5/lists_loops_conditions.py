requested_toppings = ["Cheese", "Ham", "Pineapple", "pepperoni", "Mushroom"]

finished_pizza = []

for requested_topping in requested_toppings:
	if(requested_topping.lower() == "ham"):
		print("I am sorry we are out of ham")
	else: 
		print(requested_topping, "added to pizza.")
		finished_pizza.append(requested_topping)
print("Your pizza is made with the following toppings:", finished_pizza)

print('\n')

second_pizza_toppings = []

if second_pizza_toppings:
	for second_pizza_topping in second_pizza_toppings:
		print(second_pizza_topping, "added")
else:
	print("Are you sure it is plain?")