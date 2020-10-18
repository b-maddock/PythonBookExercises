bands = ["Kings of Leon", "Foals", "TDCC", "Catfish", "Sundara Karma"]

for band in bands:
	if band.lower() == "foals":
		print(band.upper())
	else:
		print(band.lower())

print("\n\n")

favourite_band = "Sea girls"
if favourite_band not in bands:
	print(favourite_band + " should be in this!")