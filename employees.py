#!/usr/bin/python3
import re

def display_count(self):
    print("Total Employee %d" % Employee.empCount)


class Employee:
    """Common base class for all employees"""
    empCount = 0  # class variable

    def __init__(self, name, empid, salary):
        self.name = name
        self.empid = empid
        self.salary = salary
        Employee.empCount += 1

    def __del__(self):
        class_name = self.__class__.__name__
        print (self.name, "destroyed")

    def display_employee(self):
        print("Name : ", self.name, ", Id: ", self.empid, ", Salary: ", self.salary)
   
   
emplist = []

for i in range(3):
    emplist.append(Employee("Employee" + str(i), i, 200000))


print("Total Employees ", Employee.empCount)
print(emplist)
print(emplist[0].name)

for employee in emplist:
    employee.display_employee()
    
phone = "2004-959-559 # This is Phone Number"
print("phone : ", phone)

# Delete Python-style comments
num = re.sub(r'T.*$', "", phone)
print("Phone Num : ", num)

# Remove anything other than digits
num = re.sub(r'\D', "", phone)    
print("Phone Num : ", num)

dict1 = {'Name': 'Zara', 'Age': 7}
print("dict1['Name']: ", dict1['Name'])


for item in dict1.keys():
    print(item)
for item in dict1.values():
    print(item)
for item in dict1:
    print(item),
    print(dict1[item])
    print("{}: {}".format(item, dict1[item]))
