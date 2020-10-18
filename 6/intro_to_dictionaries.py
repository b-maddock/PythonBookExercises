alien_0 = {'colour': 'green', 'points': 5}

print(alien_0['colour'])
print(alien_0['points'])

point_counter = alien_0['points']
print("Your total points is: ", str(point_counter))

print('\n')

alien_0['x_position'] = 0
alien_0['y_position'] = 25 

print(alien_0)

alien_0 = {} #define empty dictionary 
print(alien_0)

alien_0 = {'colour': 'green', 'x_position': 0, 'y_position': 25, 'speed': 'medium', 'points':5}
print("original x_position: " + str(alien_0['x_position']))

if alien_0['speed'] == 'slow':
	speed_increment = 1
elif alien_0['speed'] == 'medium':
	speed_increment = 2
else:
	speed_increment = 3

# New alien position 
alien_0['x_position'] = alien_0['x_position'] + speed_increment
print('new x_position: ' + str(alien_0['x_position']))

print('\n')

# Removing a key-value pair using del funtion 

del alien_0['points']
print(alien_0)

print('\n')

# Handling different objects in a dictionary 

favourite_languages = {
	'Ben': 'Python',
	'Jack': 'Java',
	'Patrick': 'MatLab'
}

print("Bens favourite lanuage is:", favourite_languages['Ben'])