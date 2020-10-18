# Lists of dictionaries

"""
alien_0 = {'color': 'green', 'points': 5} 
alien_1 = {'color': 'yellow', 'points': 10} 
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
	print(alien)
"""

aliens = []

for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5}
	aliens.append(new_alien)

for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow' 
		alien['speed'] = 'medium' 
		alien['points'] = 10

for alien in aliens[:5]:
	print(alien)

print()

print(len(aliens), "aliens have been created")

print()

# List inside a dictionary 

pizza = {
	'crust': 'Thick',
	'toppings': ['mushrooms', 'cheese']
}

print("Your pizza has", pizza['crust'], "crust with the toppings:")
for topping in pizza['toppings']:
	print('\t', topping.title())

print()

# Listings 

favourite_languages = {
	'Ben': ['Python', 'Perl'],
	'Jack': ['Java'],
	'Patrick': ['MatLab', 'C'],
	'Ellyn': ['C'],
	'Gill': ['Javascript'], 
	'Steve': ['Python']
} 

for person, languages in favourite_languages.items():
	print("\nHello", person, "your favourite languages are:")
	for language in languages:
		print('\t', language)

print()

# Dictionary inside a dictionary 

users = { 
	'aeinstein': {
		'first': 'albert', 
		'last': 'einstein', 
		'location': 'princeton', 
		},
	'mcurie': {
		'first': 'marie', 
		'last': 'curie', 
		'location': 'paris', 
		},
}

for username, user_info in users.items():
	print("\nUsername: " + username)
	full_name = user_info['first'] + " " + user_info['last']
	location = user_info['location']
	
	print("\tFull name: " + full_name.title()) 
	print("\tLocation: " + location.title())


