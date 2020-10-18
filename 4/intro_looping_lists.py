magician = ["alice", "David", "Michael"]

for magician in magician:
	print(magician.title() + " that was a great trick")

print("Wow that was amazing!")

pizza_toppings = ["Cheese", "olives", "onion", "Meatballs"]

for pizza_toppings in pizza_toppings:
	print("I like " + pizza_toppings + " on my pizza")

print("WOW JUST LOVE PIZZA")

print('\n\n\n\n')

for value in range(0,4):
	print(value)

list_of_nums = list(range(0,6))
print(list_of_nums)

print('\n\n\n')

#even numbers 

even_nums = list(range(2,11,2))

print(even_nums)

print('\n\n\n')

#Loops

squares = []
"""
for value in range(1,11): #loop from 1 to 11 calulating square and adding to list 
	square = value**2
	squares.append(square)
print(squares)
"""
for value in range(1,11):
	squares.append(value**2)
print(squares)

print('\n\n\n')

#MAX, MIN, SUM

digits = list(range(1,11))

print(min(digits))
print(max(digits))
print(sum(digits))

print('\n\n\n')

#Comprehension list 

squares = [value**2 for value in range(1,11)] 
print(squares)