from employee import Employee

class ManageEmployee:
	def __init__(self):
		self.employeeList = []
		self.beolvas()
		#self.szazezer()
		self.nagy()
	
	def beolvas(self):
		file = open("dolgozok.txt", "r", encoding="utf-8")
		row = file.readline()
		while(row):
			rowSplit = row.split(";")
			emp = Employee()
			emp.number = rowSplit[0]
			emp.name = rowSplit[1]
			emp.mother_name = rowSplit[2]
			emp.city = rowSplit[3]
			emp.address = rowSplit[4]
			emp.salary = rowSplit[5]
			emp.bonus = rowSplit[6]
			emp.hiredate = rowSplit[7]
			emp.borndate = rowSplit[8]
			
			self.employeeList.append(emp)
			row = file.readline()
		file.close()
			
	def szazezer(self):
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
