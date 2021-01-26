dolgozat1 = []
dolgozat2 = []


def beker():
	dolgozat = []
	pontszam = -2

	while pontszam != -1:
		pontszam = int(input('Pontszám: '))
		if pontszam != -1:
			dolgozat.append(pontszam)
	return dolgozat
	

def atlag(dolgozat):
	darab = len(dolgozat1)
	osszeg = 0
	for pontszam in dolgozat1:
		osszeg += pontszam
	atlag= osszeg / darab
	return atlag


print("Első dolgozat jegyei: ")
dolgozat1 = beker()
atlag1 = atlag(dolgozat1)
print("Első dolgozat átlaga: ", atlag1)

def legnagyobbElteres(dolgozat, atlag): 
	legnagyobbElteres = 0
	for pontszam in dolgozat:
		aktualisElteres = abs(atlag - pontszam)
		if aktualisElteres > legnagyobbElteres:
			legnagyobbElteres = aktualisElteres
	legnagyobbElterok = []
	for pontszam in dolgozat:
		aktualisElteres = abs(atlag - pontszam)
		if aktualisElteres == legnagyobbElteres:
			legnagyobbElterok.append(pontszam)
	
	return legnagyobbElterok

print("második dolgozat jegyei: ")
dolgozat2 = beker()
atlag2 = atlag(dolgozat2)
print("Második dolgozat átlaga: ", atlag2)

leg = legnagyobbElteres(dolgozat1, atlag1)
print('lEGNAGYOBB ELTÉRÉS: ', leg)
	
