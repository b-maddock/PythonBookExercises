# 7-5/7-6 - Movie Tickets 

prompt = "Please enter age for ticket price.\n"
prompt += "Please enter 'quit' to exit the program.\n"


ticket_price = 0 
status = True 

while(status):
	age = input(prompt)

	if age == 'quit':
		#status = False
		break
	else:
		age = int(age)

		if age < 3:
			ticket_price = "Free"
		elif age >= 3 and age < 12:
			ticket_price = 10 
		else:
			ticket_price = 15 

	print("Cost of ticket:", ticket_price)


"""
7-4 - Pizza toppings

prompt = "Please input what toppings you would like on your pizza\n"
prompt += "To finish please type 'finish' in the prompt\n"

usr_input = ""
status = True
toppings = []

while(status):
	usr_input = input(prompt)

	if usr_input == 'finish':
		status = False
	else:
		toppings.append(usr_input)

print("\nYour toppings are: ")
for topping in toppings:
	print(topping)

===========================================================

"""



