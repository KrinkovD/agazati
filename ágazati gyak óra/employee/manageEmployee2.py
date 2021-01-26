from employee2 import Employee

class Manage:
	
	def __init__(self):
		
		self.employeeList = []
		self.read()
		self.miskolciak()
		self.szegediek()
	
	def read(self):
		
		file = open("employee.txt", "r", encoding="utf-8")
		row = file.readline()
		row = file.readline()
		while(row):
			rowSplit = row.split(":")
			emp = Employee()
			emp.name = rowSplit[0]
			emp.city = rowSplit[1]
			emp.address = rowSplit[2]
			emp.salary = rowSplit[3]
			emp.bonus = rowSplit[4]
			
			self.employeeList.append(emp)
			row = file.readline()
		
		file.close()
		print("Sikeres beolvasás")
		
	def miskolciak(self):
		counter = 0
		for employee in self.employeeList:
			
			if employee.city == "Miskolc":
				counter += 1
		print("Miskolciak: ", counter)
		
	def szegediek(self):
		sum = 0
		for employee in self.employeeList: #itt az employee csak egy i 
			if employee.city == "Szeged":
				sum += int(employee.salary)
		file = open("Szöged.txt", "w", encoding="utf-8")
		file.write("Szegediek fizetése: " + str(sum))#a write csak egy objektumot fogad el szóval + jelet kell használni
		file.close()

Manage() #példányosítom/meghívom az osztályt

