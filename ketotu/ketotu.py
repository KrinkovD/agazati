class Dolgoz:
	def __init__(self, 
			az,
			nev, 
			anyjaneve,
			telepules,
			cim,
			netto,
			juttatas,
			belepes,
			szuletes,
			szulhely
			):
		self.az = az
		self.nev = nev
		self.anyjaneve = anyjaneve
		self.telepules = telepules
		self.cim = cim
		self.netto = netto
		self.juttatas = juttatas
		self.belepes = belepes
		self.szuletes = szuletes
		self.szulhely = szulhely

def beolvas():
	dolgozo_lista = [] 		
	fp = open("dolgozok.txt", "r", encoding="utf-8")
	sorok = fp.readlines()
	for sor in sorok:#egyes sortól olvassuk be!!!
		tomb = sor.split(";")
		dolgozo_lista.append(
			Dolgoz(
			tomb[0].replace('\"',''),
			tomb[1].replace('\"',''),
			tomb[2].replace('\"',''),
			tomb[3].replace('\"',''),
			tomb[4].replace('\"',''),
			tomb[5].replace('\"',''),
			tomb[6].replace('\"',''),
			tomb[7].replace('\"',''),
			tomb[8].replace('\"',''),
			tomb[9].replace('\"','')
			)
		)
	fp.close()
	return dolgozo_lista


def tabi_fizetesek(dolgozo_lista):
	fizetes = 0
	for dolgozo in dolgozo_lista:
		if dolgozo.telepules == "Tab":
			fizetes += int(dolgozo.netto)
	print("Tabi lakosok fizetése: ", fizetes)

dolgozo_lista = beolvas()
tabi_fizetesek(dolgozo_lista)

