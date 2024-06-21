# Define a base class Employee
class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
    
    def display_info(self):
        raise NotImplementedError("Subclass must implement abstract method")
    
    def calculate_annual_salary(self):
        return self.salary * 12

# Define Manager class inheriting from Employee
class Manager(Employee):
    def __init__(self, name, employee_id, salary, department):
        super().__init__(name, employee_id, salary)
        self.department = department
        self.managed_employees = []
    
    def display_info(self):
        print(f"Name: {self.name}, Employee ID: {self.employee_id}, Salary: {self.salary}, Department: {self.department}")
    
    def display_managed_employees(self):
        print(f"Managed employees:")
        for employee in self.managed_employees:
            print(f"- {employee.name} (ID: {employee.employee_id})")
    
    def add_managed_employee(self, employee):
        self.managed_employees.append(employee)

# Define Developer class inheriting from Employee
class Developer(Employee):
    def __init__(self, name, employee_id, salary):
        super().__init__(name, employee_id, salary)
        self.programming_languages = []
    
    def display_info(self):
        print(f"Name: {self.name}, Employee ID: {self.employee_id}, Salary: {self.salary}")
    
    def add_programming_language(self, language):
        self.programming_languages.append(language)

# Define Intern class inheriting from Employee
class Intern(Employee):
    def __init__(self, name, employee_id, salary, school_name, graduation_year):
        super().__init__(name, employee_id, salary)
        self.school_name = school_name
        self.graduation_year = graduation_year
    
    def display_info(self):
        print(f"Name: {self.name}, Employee ID: {self.employee_id}, Salary: {self.salary}, School: {self.school_name}, Graduation Year: {self.graduation_year}")

# Example usage:
if __name__ == "__main__":
    # Create instances of different employees
    manager1 = Manager("Alice", 1001, 80000, "HR")
    developer1 = Developer("Bob", 2001, 70000)
    intern1 = Intern("Eve", 3001, 40000, "XYZ University", 2023)

    # Adding managed employees for a manager
    manager1.add_managed_employee(developer1)
    manager1.add_managed_employee(intern1)

    # Adding programming languages for a developer
    developer1.add_programming_language("Python")
    developer1.add_programming_language("Java")

    # Display information
    manager1.display_info()
    manager1.display_managed_employees()

    developer1.display_info()
    print(f"Programming Languages: {', '.join(developer1.programming_languages)}")

    intern1.display_info()

# Calculate and display annual salaries
print(f"Annual Salary of Manager: ${manager1.calculate_annual_salary():,.2f}")
print(f"Annual Salary of Developer: ${developer1.calculate_annual_salary():,.2f}")
print(f"Annual Salary of Intern: ${intern1.calculate_annual_salary():,.2f}")
