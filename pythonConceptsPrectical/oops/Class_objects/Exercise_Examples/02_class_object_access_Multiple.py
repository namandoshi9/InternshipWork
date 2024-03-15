#w.a.p.p create a class Employee and given two attribute Employee_name and Employee_age and access with multiple objects Employee1,Employee2 and Employee3

class Employee:
    employee_id = 0
    
employee1 = Employee()
employee2 = Employee()
employee3 = Employee()

employee1.employeeID = 1001
print(f"Employee Id : {employee1.employeeID}")

employee2.employeeID = 1002
print(f"Employee Id : {employee2.employeeID}")

employee3.employeeID = 1003
print(f"Employee Id : {employee3.employeeID}")