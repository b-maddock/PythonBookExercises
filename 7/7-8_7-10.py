# 7-10 Dream vacation 

vacation_poll = {}
prompt = "If you could visit one place in the world, where would you go?\n"

status = True

while(status):
	name = input("Please input your name.\n")

	response = input(prompt)

	vacation_poll[name] = response

	terminate = input("Is another person taking the poll? Y or N\n")

	if terminate.upper() == 'N':	
		status = False

for name, place in vacation_poll.items():
	print(name, "would like to go to", place)

"""
# 7-8/7-9 Deli

sandwich_orders = ['Pastrami','Ham & Cheese', 'Pastrami', 'Just ham', 'Tuna', 'Pastrami', 'Cheese & Pickle']

finished_sandwiches =[] 

print("We are all out of Pastrami.")
print("Please select another sandwich")

while 'Pastrami' in sandwich_orders:
	sandwich_orders.remove('Pastrami')

print(sandwich_orders)

while(sandwich_orders):
	sandwich = sandwich_orders.pop()
	print("Your", sandwich, "has been made.")
	finished_sandwiches.append(sandwich)

print(finished_sandwiches)
"""








