#1602 feladat

def intr():
	print("Bali Dávid, 2020-11-26, esti szoft1")
	print("feladat 1602 megoldása")
	print("Személyek adatait kérjük és tároljuk")
intr()

fp = open("szemely.txt", "w")
num = input("adja meg a sorszámot: ")
szemelyek = []

while num != "0":
	
	nev = input("Név: ")
	telepules = input("település: ")
	cim = input("Cím: ")
	jov = input("Havi jövedelem: ")
	
	line = num + " : " + nev + " : " + telepules + " e: " + cim + " : " + jov + "\n"
	fp.write(line)
	num = input("sorszám: ")

fp.close()
		
