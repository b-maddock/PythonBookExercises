#using multpiple lists 

toppings_available = ["Cheese", "Mushrooms", "Bacon", "Meatballs", "Onion", "Tuna", "Peppers"]

requested_toppings = ["Cheese", "Onion", "Ham"]

for requested_topping in requested_toppings:
	if requested_topping in toppings_available:
		print("Adding", requested_topping, "to pizza!")
	else:
		print("Sorry,", requested_topping, "is not available at the moment!")
print("Pizza is finshed")