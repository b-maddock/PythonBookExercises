players = ["Ben", "Ellie", "Tom", "Lucy", "Terry"]

print(players[0:3]) #slicing 
print(players[3:5])
print(players[-3:])

print("\n") 

print("Here are the players in my team:")
for player in players[:3]:
	print(player.upper())

print("\n")

#Creating a cp of list 
my_food = ["pizza", "pie", "chips", "cake", "chocolate"]
friends_food = my_food[:]
print(my_food)

print("My friends favourite food is:")
print(friends_food)

my_food.append("apples")
friends_food.append("pears")