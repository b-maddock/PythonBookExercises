# 6-7 people

user_1=	{ 
		'first_name': 'Ben',
		'surname': 'Maddock', 
		'Age': 23, 
		'city': "Swansea"
		}

user_2=	{
		'first_name': 'Ellyn',
		'surname': 'Doe', 
		'Age': 22, 
		'city': "Bristol"
		}

user_3=	{
		'first_name': 'Joe',
		'surname': 'Lingard', 
		'Age': 26, 
		'city': "Newport"
		}

people = [user_1, user_2, user_3]

for people in people:
	print(people)

print()

# 6-8 pets 

Duke = {
	'type': 'Dog', 
	'owner': 'Gill'
	}
Trevor = {
	'type': 'cat',
	'owner': 'Tom'
}
Sam = {
	'type': 'turtle',
	'owner': 'Kyle'
}
Lucy = {
	'type': 'cat',
	'owner': 'jake'
}

Ben = {
	'type': 'dog',
	'owner': 'caitlin'
}

pets = [Duke, Trevor, Sam, Lucy, Ben]

for pet in pets:
	print(pet)

print()

# 6-9 favoutite places

favoutite_places = {
	'Ben': ['Beach', 'Gym'],
	'ellie': ['town'],
	'tom': ['gym', 'pub', 'coasts']
}

for people, places in favoutite_places.items():  #first store people as key and places has value 
	print(people.title() + "'s favourite places are:")
	for place in places: #loop though places for each name 
		print("\t",place.lower())
	print()

print()

# 6-10 Favourite number 

fav_colour = {
	'Ellyn': ['Green', 'Teal'], 
	'Gillian': ['Blue'], 
	'Steven': ['Red', 'Orange'], 
	'Tom': ['White', 'Black'], 
	"Joe": ['Purple']
}

for person, colours in fav_colour.items():
	print(person + "'s favourite colours are ")
	for colour in colours:
		print("\t",colour)
	print()

print()

# 6-11 Cities
cities = {
    'Swansea': {
        'country': 'Wales',
        'pop': '241,300',
        'fact': "For pretty much 300 years Swansea was an English town"
    },

    'Cardiff': {
        'country': 'Wales',
        'pop': '346,000',
        'fact': "Cardiff is the capital of Wales and the UK's 11th largest city"
    },

    'Newport':{
        'country': 'Wales',
        'pop': '145,700',
        'fact': "1314: First town charter"
    },
    
    'Bristol': {
        'country': 'England',
        'pop': '463,400',
        'fact': "THE WORLD'S FIRST BUNGEE JUMP TOOK PLACE IN BRISTOL"
    }
}

for city, city_info in cities.items():
    print(city)
    print('country: ', city_info['country'])
    print('pop: ', city_info['pop'])
    print('fact: ', city_info['fact'])
    print()











