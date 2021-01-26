print("Csapadék mennyiség milliméterben.")

aktualis = input("Aktuális heti csapadék: ")
elozo = input("Előzö heti csapadék: ")

if aktualis > elozo:
	print("Több csapadék")
	
elif aktualis < elozo:
	print("kevesebb csapadék")

else:
	print("Nem változott")
