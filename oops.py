'''Employee Class:
o Create an Employee class with attributes for name, ID, title, and department.
o Include a method to display employee details.
o Implement a string representation method that returns the employee&#39;s
name and ID.'''
import json
class Employee:
    count=0
    def __init__(self,name,id,title,department):
        self.name=name
        self.id=id
        self.title=title
        self.department=department
        Employee.count+=1
    def __str__ (self):
        return 'Employee(id=' + str(self.id) + ' ,name=' + self.name + ',title=' + str(self.title) + ',department=' +self.department +')'
class Department:
    def __init__(self,name):
        self.name=name
        self.employeeList=[]
    def addEmployee(self,employee):
        self.employeeList.append(employee)
    def removeEmployee(self,empid):
        for employee in self.employeeList:
            if employee.id == empid:
                self.employeeList.remove(employee)
        else:
            return "It is not in list"
    def list_employees(self):
        print(f"Employees in {self.name} department:")
        for employee in self.employees:
            print(employee)
    
    def __str__(self):
        return f"Department: {self.name}"

class Company:
    def __init__(self):
        self.department_dict={}
    def adddepartment(self,department):
        self.department_dict[department.name]=department
    def removeDepartment(self,departmentName):
        if departmentName in self.department_dict.keys():
            del self.department_dict[departmentName]
        else:
            print("The department Name does not exist")
    def display(self):
        for departmentName in self.department_dict.keys():
            print(departmentName)
    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.departments, file)

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            self.departments = json.load(file)

def print_menu():
    print("Employee Management System Menu:")
    print("1. Add Employee")
    print("2. Remove Employee")
    print("3. Display Department")
    print("4. Add Department")
    print("5. Remove Department")
    print("6. Display All Departments")
    print("7. Save Company Data to File")
    print("8. Load Company Data from File")
    print("9. Exit")

def main():
    company = Company()

    # Function to handle user input
    def handle_user_input(choice):
        if choice == '1':
            # Add Employee
            pass
        elif choice == '2':
            # Remove Employee
            pass
        elif choice == '3':
            # Display Department
            pass
        elif choice == '4':
            # Add Department
            pass
        elif choice == '5':
            # Remove Department
            pass
        elif choice == '6':
            # Display all the Departments
            company.display_departments()
        elif choice == '7':
            # Save the company data to file
            filename = input("Enter filename to save: ")
            company.save_to_file(filename)
            print("Data saved successfully.")
        elif choice == '8':
            # Load the company data from file
            filename = input("Enter filename to load: ")
            company.load_from_file(filename)
            print("Data loaded successfully.")
        elif choice == '9':
            exit()
        else:
            print("Invalid choice.")


    while True:
        print_menu()
        choice = input("Enter your choice: ")
        handle_user_input(choice)

if __name__ == "__main__":
    main()
        



emp1=Employee("Harsh","12","SDE","Softare")
emp2=Employee("Arjun","14","Tax Consultant","Finance")
emp3=Employee("Ram","16","xyz","sales")
dep1=Department("Software")
dep2=Department("Finance")
dep3=Department("sales")
dep1.addEmployee(emp1)
dep2.addEmployee(emp2)
dep3.addEmployee(emp3)
dep1.list_employees()
print(emp.__str__())

        