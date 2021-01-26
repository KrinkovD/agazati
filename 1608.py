from employee import Employee

class ManageEmployee:
	def __init__(self): #konstruktor kötelező paramétere a self
		self.employeeList = [] 	#létrehozok egy listát a konstruktorban
		self.beolvas() #itt hívom meg a metódusokat
		#self.szazezer()
		self.nagy()
	
	def beolvas(self):	#beolvasás + self paramétere értéke minden metódusnak
		file = open("dolgozok.txt", "r", encoding="utf-8") #eltárolom egy file nevű változóban a beolvasott txt-t
		row = file.readline() #címsort kiolvasom és/vagy változóba teszem az első beolvasott sort
		while(row):	#ez addig fut, amíg a "row"-ban van bármi
			rowSplit = row.split(";") #indexelhető elemekre osztom a sort a .split paranccsal és megadom az elválasztót
			emp = Employee() #Az employe osztályt példányosítom egy változóban
			emp.number = rowSplit[0]#megadom az Employee, tehát az impoortált osztály változóinak értékét
			emp.name = rowSplit[1]
			emp.mother_name = rowSplit[2]
			emp.city = rowSplit[3]
			emp.address = rowSplit[4]
			emp.salary = rowSplit[5]
			emp.bonus = rowSplit[6]
			emp.hiredate = rowSplit[7]
			emp.borndate = rowSplit[8]
			
			self.employeeList.append(emp)	#hozzáadom az osztályban létrehozott listához az objektumot
			row = file.readline()	#beolvasom a következő sort
		file.close()	#ciklus lefut, fájl bezár
			
	def szazezer(self): #MINDEN METÓDUSNAK KÖTLEZŐ ÉRTÉKE A SELF
		bonus = []
		for employee in self.employeeList:
			if int(employee.bonus) < 5000:
				bonus.append(employee.name)
		for i in bonus:
			print(i)
	
	def nagy(self):
		van_e = False
		for employee in self.employeeList:
			if "Nagy" in employee.name:
				van_e = True
		if van_e == True:
			print("Van Nagy")
		
			
ManageEmployee()
