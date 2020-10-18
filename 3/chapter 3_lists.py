bands = ["crystal fighters", "Foals", "Arctic Monkeys", "ThunderCat"]

print(bands)

print(bands[1])

print(bands[0].title())

print(bands[-1]) #last item in list. -2 would be second last 

msg = "My favourite band is " + bands[1] #message 

print(msg)

bands[3] = "Jamie T" #change item 3 in list

print(bands)

bands.append("Sundara Karma") #add element 

print(bands) 

bands.insert(1, "Slaves") # index, value 

print(bands)

del bands[4] #delete value at index 

print(bands)

popped_band = bands.pop() #popping last item 

print(bands)
print(popped_band)
print("The most recent band I saw is " + bands.pop())
print(bands)

bands.insert(3, "IDLES")
print("The first band I saw is " + bands.pop(0).title()) #pop by index 

not_touring = bands[0]

bands.remove(not_touring) #remove by value 
bands.remove("IDLES")
print(bands)