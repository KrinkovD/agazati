'''
Az alábbi állomány egy cég dolgozóinak adatit tartalmazza. 
Az első sor tartalmazza a mezőneveket. 
Hátulról a harmadik oszlop azt a dátumot tartalmazza, 
amikor a dolgozó belépett a cégbe.

Olvassa be az alábbi állományt, 
majd írassa azon dolgozók neveit és netto fizetésüket 
akik 2005 után jöttek a céghez.
'''


def intr():
	print("Bali Dávid, 2020-11-26, esti szoft1")
	print("feladat 1607 megoldása")
	print("")
intr()

print("{:20}{:10}".format("Név", "Nettó Fizu"))
print("-------------------------------")

fp = open("dolgozok.txt", "r", encoding="utf-8")

#a mező nevek kiolvasása
fp.readline()


#az első dolgozó beolvasása, hogy tudjon mivel dolgozni a kód
line = fp.readline()
while line != "":
	#if line == "":
		#break
	lineList = line.split(";")
	
	belepesIdeje = lineList[7]
	belepesIdejeList = belepesIdeje.split('-')
	belepesEve = belepesIdejeList[0]
	
	
	belepesEve = belepesEve.replace('"', '')
	if int(belepesEve) > 2005:
		#print(belepesEve)
		
		print('{:20}{:10}'.format(lineList[1], lineList[5]))
	line = fp.readline()
fp.close()
