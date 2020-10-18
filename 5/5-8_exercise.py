#5-8 greeting messages 
uname = ["Admin", "User", "Guest", "Benny", "EDoe"]

for user in uname:
	if user == 'Admin':
		print("Hello admin, would you like to see a status report?")
	else:
		print("Hello", user, "thank you for logging in again.")

print ('\n')

#5-9 empty list test 
uname = []

if uname: #if true 
	for user in uname:
		if user == 'Admin':
			print("Hello admin, would you like to see a status report?")
		else:
			print("Hello", user, "thank you for logging in again.")
else:
	print("We need to find some users!")
print ('\n')

#5-10 Checking usernames 

current_users = ["Benny", "EDoe", "Big G", "JoeP", "StevenMads", "John"]

new_users = ["GillMads", "Tommy", "PWilson", "Grey", "Hank", "Benny", "JoeP", "JOHN"]

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
	if new_user.lower() in current_users_lower:
		print(new_user, "is taken, please enter new user name")
	else:
		print(new_user, "is available.")

print ('\n')

#5-11 Ordinal numbers 

numbers = list(range(1,10)) #create list 1 to 9 
numbers_to_sting = [str(num) for num in numbers] #convert to string

for number in numbers_to_sting: #output
	if number == '1':
		print(number + "st")
	elif number == '2':
		print(number + "nd")
	elif number == '3':
		print(number + "rd")
	else:
		print(number + "th")