# keyword arguments
def describe_person(person_name, person_age, place_of_birth='Swansea'):
	print("Hello", person_name, "you are", person_age, "years old and were born in", place_of_birth)

# positional arguments, in order 
def describe_pet(animal_type, pet_name):
	print("Your pet is a", animal_type, "and it's name is", pet_name)

describe_pet('dog', 'Barry')
describe_person(person_age=23, person_name='Ellie')

"""
Exercises

8-1 & 8-2

def display_message():
	print('I am learning about functions in Python')

def favourite_book(title):
	print('One of my favourite books is ', title.title())

display_message()

favourite_book('lion king')
"""
