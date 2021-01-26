def base():
	
	ageList = []
	for i in range(0, 3):
		age = int(input("Kor: "))
		ageList.append(age)
	
	average = ageAverage( ageList )
	print("Az átlagéletkor: {:>10.2f}".format(average)) 

def ageAverage( ageList ):
	#average = ( ageList[0] + ageList[1] + ageList[2] ) / len(ageList)
	sumAge = 0
	for i in range(len(ageList)):
		sumAge += ageList[i]
	
	average = sumAge / len(ageList)
	return average
	
base()
