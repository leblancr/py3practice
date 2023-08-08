#!/usr/bin/python3
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
        # class_name = self.__class__.__name__
        print(self.name, "destroyed")

    def display_employee(self):
        print("Name : ", self.name, ", Id: ", self.empid, ", Salary: ", self.salary)
   
   
emplist = []

# Create employee objects, add to list
for i in range(3):
    emplist.append(Employee("Employee" + str(i), i, 200000))


print("Total Employees ", Employee.empCount)
print(emplist)
print(emplist[0].name)

for employee in emplist:
    employee.display_employee()
    