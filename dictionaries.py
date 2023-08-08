employees = [{'Name': 'Zara', 'Age': 7},
             {'Name': 'Tom', 'Age': 8},
             {'Name': 'Dick', 'Age': 9},
             {'Name': 'Harry', 'Age': 10}
             ]

# last_key = list(employees.keys())[-1]
# last_value = employees[last_key]

print('Name:     Age:')
#print('keys:')

# Display the employees
for employee in employees:
    print(f"{employee['Name']:<10}{employee['Age']:>3}")
    # for item in employee.keys():
    #     if item != last_key:
    #         print(item, end=", ")
    #     else:
    #         print(item)
    # 
    # #print('values:')
    # for item in employees.values():
    #     if item != last_value:
    #         print(item, end=", ")
    #     else:
    #         print(item)
    