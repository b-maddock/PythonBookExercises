
while(1):
	num = input("input a number to find out if it is odd or even. ")

	if int(num) % 2 == 0:
		print(num, "is even")
	else:
		print(num, "is odd")



"""
=====================================================
Code bank

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your name? "
name = input(prompt)
print("\nHello, " + name + "!\n")

age = input("Please input your age. ")
new_age = int(age)
print("You are", int(age), "years old.")

if new_age > 17:
	print("You are old enough to vote!")
else:
	print("Not old enough yet! Still", 18 - new_age, "years left\n")
=====================================================
"""
