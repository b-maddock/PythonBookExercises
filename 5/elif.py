input = input("\nEnter your age: ")

print("Age entered: ", input)

age = int(input)

if age < 10:
	price = 0
elif age >= 10 and age < 18:
	price = 5
else:
	price = 10 

print("price of ticket is:", price, "\n")
