print("Bali Dávid 2020.12.10 Szoft. 1 /E")
print("Az 1601 feladat megoldása")
print("számok 0 végjelig, majd fájlba írás")

def beker():
	szamok = []
	szam = -1
	while szam != 0:
		szam = int(input("Szám: "))
		if szam != 0:
			szamok.append(szam)
	return szamok		


def fajlbair(szamok):
	fp = open("adat.txt", "w")
	for szam in szamok:
		fp.write(str(szam))
		fp.write("\n")
	fp.close()

def nagyobb_szaz(szamok):
	szamlalo = 0 
	for szam in szamok:
		if szam > 100:
			szamlalo += 1
	return szamlalo

def rendez(szamok):
	szamok.sort()
	return szamok

def kiir(szamok):
	for szam in szamok:
		print(szam, end= ' ')
	print()


szamok = beker()
kiir(szamok)
szamok = rendez(szamok)
kiir(szamok)
#fajlbair(szamok)
#nagy_szaz = nagyobb_szaz(szamok)
#print("Száznál nagyobb: ", nagy_szaz)
