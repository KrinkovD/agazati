from employee import Employee

class ManageEmployee:
	def __init__(self):
		
		self.rowList = []
		self.readFile()
		self.countEmployee()
		self.sumMiskolcSal()
		self.szegedWrite()

	def readFile(self):
		print("Első feladat: fájl beolvasás")
		file = open("employee.txt", "r", encoding="utf-8")
		file.readline()
		
		row = file.readline()
		while( row ):
			rowS = row.split(":")
			emp = Employee()
			emp.name = rowS[0]
			emp.city = rowS[1]
			emp.address = rowS[2]
			emp.salary = rowS[3]
			emp.bonus = rowS[4]
			emp.borndate = rowS[5]
			emp.hiredate = rowS[6]
			
			self.rowList.append(emp)
			row = file.readline()
			
		file.close()
		print("Sikeres beolvasás")
		
	def countEmployee(self):
		print("Második ferladat: Dolgozók megszámolása")
		counter = 0
		for i in self.rowList:
			counter += 1
		print("A dolgozók száma: {:10}".format(counter))

	def sumMiskolcSal(self):
		print("Harmadik feladat: Miskolci fizetések összegzése")
		sumSalary = 0
		for employee in self.rowList:
			
			if (employee.city == "Miskolc"):
				sumSalary += int(employee.salary)
		print("Miskolciak fizetése: {:10}".format(sumSalary))
	
	def szegedWrite(self):
		print("negyedik feladat: szegedi fizetések fájlbaírása")
		sumSalary = 0
		for employee in self.rowList:
			
			if (employee.city == "Szeged"):
				sumSalary += int(employee.salary)
		wFile = open("szegedi.txt", "w")
		wFile.write("Szegediek fizetése: " + str(sumSalary))
		
		wFile.close()
		print("Sikeres kiírás")
		
		
	

ManageEmployee()

