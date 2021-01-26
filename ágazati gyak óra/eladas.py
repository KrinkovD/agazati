# Bali Dávid 2021.01.07 Szoft/I/E.
from jarmu import Jarmu

print("Bali Dávid 2021.01.07 Szoft. I/1/E")
print("Az ágazati vizsga 3. példafeladatának megoldása")

class Eladas:
	def olvas_file(self):
		print('beolvasás...\n')
		self.jarmuvek = []
		fp = open('jarmu.txt', 'r', encoding='utf-8')
		lines = fp.readlines()
		for line in lines[1:]: #a [1:] kihagyja az első sort a beolvasásból
			line = line.rstrip()
			(az, rendszam, szin, marka, ar) = line.split(':') #így a zárójelben megadott változónevekhez rendeli az adott indexen álló értékeket
		
			jarmu = Jarmu(az, rendszam, szin, marka, ar)
			self.jarmuvek.append(jarmu) 
		fp.close()
	
	def feher(self):
		count = 0
		for jarmu in self.jarmuvek:
			if jarmu.szin =='fehér':
				count += 1
		print('Fehér járművek: ', count, '\n')
	
	def olcso(self):
		print('Olcsó járművek: ')
		for jarmu in self.jarmuvek:
			
			if int(jarmu.ar) < 1000000:
				print(jarmu.rendszam, jarmu.szin, jarmu.marka)
	
	def feherOlcso(self):
		print('olcsó fehér járművek fájlba: ')
		fp = open('feherOlcso.txt', 'w')
		for jarmu in self.jarmuvek:
			if int(jarmu.ar) < 1000000 and jarmu.szin =='fehér':
				fp.write(
				jarmu.az +
				":" + jarmu.rendszam +
				":" + jarmu.szin +
				":" + jarmu.marka +
				":" + jarmu.ar + "\n"
				)
		fp.close()
				
		
	
			
		
eladas = Eladas()
eladas.olvas_file()
eladas.feher()
eladas.olcso()
eladas.feherOlcso()

