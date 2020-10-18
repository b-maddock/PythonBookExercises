#Tuples are immutable lists, values can be referenced but not changed 

dimensions = (20, 100)

print(dimensions[1])

for dimension in dimensions:
	print(dimension)

#dimensions[1] = 250 - will not wrk 

#You can overwrite a tuple however

print("\nOriginal dimensions:")
for dimension in dimensions:
	print(dimension) 

print("\nModified dimensions:")
dimensions = (100,200)
for dimension in dimensions:
	print(dimension)
