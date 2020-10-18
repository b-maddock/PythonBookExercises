user_0 = {
	'uname': 'OccupyTheWeb',
	'fname': 'Ben', 
	'lname': 'Maddock'
}

# Items() returns list of key value pairs 
for key, value in user_0.items(): #create two values to store the key and value for the loop
	print("\nKey:", key) #prints each key and value in dictionary 
	print("value:", value)

print("\n==============================================================")

#favourite languages 

favourite_languages = {
	'Ben': 'Python',
	'Jack': 'Java',
	'Patrick': 'MatLab',
	'Ellyn': 'C',
	'Gill': 'Javascript', 
	'Steve': 'Python'
}

for key, value in favourite_languages.items():
	print("\n", key + "'s favourite language is", value)

print("\n==============================================================")

# .keys() returns just the keys from the dictonary
for key in favourite_languages.keys():
	print(key, "took the poll")

if 'erin' not in favourite_languages.keys():
	print("Erin please take our poll")

print("\n==============================================================")

# Sorting dictionary using sorted()
print(favourite_languages)
for name in sorted(favourite_languages.keys()):
	print(name)   

print("\n==============================================================")

# looping through dictionary by value 

print("The following languages have been mentioned:")
for language in favourite_languages.values():
	print(language.title())

print()

#to stop repeats, we can use sets. Similar to a list, however each item must be unique 
print("None repeat:")
for language in set(favourite_languages.values()):
	print(language.title())




