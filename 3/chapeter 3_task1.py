guest_list = ["Barry", "George", "Freddie", "Luke"]

print("Guest list: \n\t", guest_list)

print("Unfortuanatly " + guest_list.pop(0) + " can not longer make it.")

guest_list.insert(0, "Gil")

print(guest_list[0] + " will take their place")

print(guest_list)

print("We have found a bigger table!")

guest_list.insert(0, "Tom")
guest_list.insert(2, "Ben")
guest_list.append("Steve")

print(guest_list)

#task 3.8 

print(len(guest_list),"people are invited")

print("only two people are allowed now.")

print(guest_list.pop(0) + " is no longer invited")
print(guest_list.pop(5) + " is no longer invited")
print(guest_list.pop(4) + " is no longer invited")
print(guest_list.pop(3) + " is no longer invited")
print(guest_list.pop(2) + " is no longer invited")

print(guest_list, "are still invited.")

del guest_list[0]
del guest_list[0]
print(guest_list)


