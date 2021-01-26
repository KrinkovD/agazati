
def multiNumber():
	list = []


	for i in range(0, 5):
		number = int(input('Szám: '))
		list.append(number)
	
	
	multipleNum = multiple(list)
	print("A szorzat: {:^10}".format(multipleNum))
	 

def multiple(list):
	
	sum = 1
	for i in list:
		sum *= i
	
	return sum
	
multiNumber()
