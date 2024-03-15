class Employee:
    emp_count = 0

    def __init__(self):
        self.employees = []

    def generate_e_id(self):
        return len(self.employees) + 1

    def add_employee(self, name, age, bod, mobile, designation, salary):
        emp_id = self.generate_e_id()
        employee = {
            'id': emp_id,
            'name': name,
            'age': age,
            'bod': bod,
            'mobile': mobile,
            'designation': designation,
            'salary': salary
        }
        self.employees.append(employee)
        print(f"Employee added successfully! With Employee ID {emp_id}")
        return employee

    def _get_employee_by_id(self, emp_id):
        for employee in self.employees:
            if employee['id'] == emp_id:
                return employee
        return None

    def show_emp_details(self, emp_id):
        employee = self._get_employee_by_id(emp_id)
        if employee:
            print("-" * 15)
            print(f"ID          : {employee['id']}")
            print(f"Name        : {employee['name']}")
            print(f"Age         : {employee['age']} years old")
            print(f"Birth of Date: {employee['bod']}")
            print(f"Mobile No   : {employee['mobile']}")
            print(f"Designation : {employee['designation']}")
            print(f"Salary      : {employee['salary']}")
            print("-" * 15)
        else:
            print(f"Employee id : {emp_id} is not found")

    def remove_employee(self, emp_id):
        employee = self._get_employee_by_id(emp_id)
        if employee is not None:
            self.employees.remove(employee)
            print(f"Employee id {emp_id} removed successfully")
        else:
            print("No such employee found.")

if __name__ == "__main__":
    emp = Employee()

    while True:
        print("-----Menu-----")
        print("1. Add Employee")
        print("2. Show Employee Details")
        print("3. Remove Employee")
        print("4. Exit")
        print("-" * 10)

        choice = input("Enter Your Choice: ")

        if choice == "1":
            name = input("Enter Employee Name: ")
            age = int(input("Enter Age: "))
            bod = input("Enter Birth of Date (dd/mm/yyyy): ")
            mobile = input("Enter Mobile Number: ")
            desi = input("Enter Designation: ")
            salary = input("Enter Salary: ")
            emp.add_employee(name, age, bod, mobile, desi, salary)

        elif choice == "2":
            emp_id = int(input("\nEnter Employee ID to see details: "))
            emp.show_emp_details(emp_id)

        elif choice == "3":
            emp_id = int(input("\nEnter Employee ID to remove: "))
            emp.remove_employee(emp_id)

        elif choice == "4":
            print("---Thank You For Visit---")
            break

        else:
            print("Invalid Input!! Please Enter (1-4).")
