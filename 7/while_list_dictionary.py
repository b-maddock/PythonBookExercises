responses = {}

status = True 

while(status):

	name = input("Please enter your name\n")
	vote_response = input("How do you vote? \n")

	responses[name] = vote_response

	print("Thank you for your response", name)

	terminate = input("Is another person voting? Y/N \n")

	if terminate == 'N':
		status = False 
	
print("--- Polling responses ---")

for name, response in responses.items():
	print(name, "responed with a ", response)

"""
unconfirmed_users = ['Ben', 'Ellyn', 'Tom', 'Joe']

confirmed_users = []

#verify users 
while(unconfirmed_users):
	current_user = unconfirmed_users.pop()
	print("verifying user:", current_user)

	confirmed_users.append(current_user)
print()

for confirmed_user in confirmed_users:
	print(confirmed_user.title(), "is now verified")

========================================================

pets = ['Cat', 'Dog', 'frog', 'Goat', 'Dog', 'cat', 'Hampster', 'snake']
print(pets)

pets = [pet.lower() for pet in pets]
print(pets)


while 'cat' in pets:
	pets.remove('cat')
print(pets) 

"""


