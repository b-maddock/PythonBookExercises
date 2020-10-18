glossary = {
	'C': 'a high-level programming language that was developed in the mid-1970s.', 
	'DBMS': 'Stands for "Database Management System." In short, a DBMS is a database program.',
	'Firewall': 'A computer firewall limits the data that can pass through it and protects a networked server or client machine from damage by unauthorized users.',
	'Gateway': 'A gateway is either hardware or software that acts as a bridge between two networks so that data can be transferred between a number of computers.',
	'abs': 'Return the absolute value of a number.',
	'argument': 'Extra information which the computer uses to perform commands.'
}


#6-4 looping glossary 
for key, value in glossary.items():
	print(key+":", value + '\n')

#6-5 rivers 

rivers ={
	'Nile': 'Egypt',
	'Sepik': 'New Guinea',
	'Amazon': 'Brazil', 
	'Yangtze': 'China',
	'Danube': 'Germany'
}

for key, value in rivers.items():
	print("The", key, "flows through ", value)

print()

for river in rivers.keys():
	print(river)

print()

for location in rivers.values():
	print(location)

print()

#6-6 polling

favourite_languages = {
	'Ben': 'Python',
	'Jack': 'Java',
	'Patrick': 'MatLab',
	'Ellyn': 'C',
	'Gill': 'Javascript', 
	'Steve': 'Python'
} 

people_to_take_poll = {
	'Jo': 'Javascript',
	'ben': 'Python',
	'Steve': 'Python',
	'Luke': 'PHP'
}

user_lower = [user.lower() for user in favourite_languages.keys()] #lower all characters for comparison 

for people_to_take in people_to_take_poll.keys(): #loop users to take poll and check if they have 
	if people_to_take.lower() in user_lower:
		print(people_to_take.title() + ", thank you for your response")
	else: 
		print(people_to_take.title() + ", please take the poll")








