current_num = 0 

while current_num <= 10:
	current_num += 1

	if current_num % 2 == 0:
		continue 
	else:
		print(current_num)



"""
Spare code buckets

current_num = 0 

while current_num <= 5:
	print(current_num)
	current_num += 1

===============================================================

msg = "Enter some text and I will repeat it back to you\n"
msg += "Enter 'quit' to \n"

usr_input = ""
active = True

while(active):
	usr_input = input(msg)

	if usr_input != 'quit':
		print(usr_input, '\n')
	else:
		active = False
		print()

===============================================================

prompt = "Enter countries you would like to visit\n"
prompt += "Enter 'quit' to exit\n"

usr_input = ""

while(True):
	usr_input = input(prompt)

	if usr_input == 'quit':
		break 
	else:
		print("I would like to visit", usr_input, 'as well!\n')

"""