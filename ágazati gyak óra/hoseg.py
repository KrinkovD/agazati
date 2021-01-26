# Bali Dávid 2021.01.07 Szoft/I/E.
print("Bali Dávid 2021.01.07 Szoft. I/1/E")
print("Az ágazati vizsga 2. példafeladatának megoldása")

def fagy(ho):
	if int(ho) < 0:
		return True
	else:
		return False

ho = ''
while ho != 'vege':
	ho = input('Hő: ')
	if ho != 'vege':
		if fagy(int(ho)): #függvényparamétereknél is át lehet alakítani a típust
			print('Fagy volt.')
		else:
			print('Nem volt fagy')

