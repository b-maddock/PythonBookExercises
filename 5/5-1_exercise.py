car = 'BMW'

print(car == 'BMW')

if car == 'BMW':
	print("1.", car)
else:
	print("1. Not correct\n")

if car == "VW":
	print("2.",car)
else:
	print("2. Not correct\n")

car = "VW" 

if car.lower() == "vw":
	print("2.",car)
else:
	print("2. Not correct\n")

numbers = [1,3,5,7,9,11]

if 1 and 4 in numbers:
	print(True)
else: 
	print(False)

if 1 or 4 in numbers:
	print(True)
else: 
	print(False)