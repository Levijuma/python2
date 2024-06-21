class Employee:
    def _init_(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: ${self.salary:,.2f}")

    def calculate_annual_salary(self):
        return self.salary * 12


class Manager(Employee):
    def _init_(self, name, employee_id, salary, department):
        super()._init_(name, employee_id, salary)
        self.department = department
        self.employees_managed = []

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")
        print("Employees Managed: ")
        for employee in self.employees_managed:
            print(f" - {employee.name} (ID: {employee.employee_id})")

    def add_employee(self, employee):
        self.employees_managed.append(employee)


class Developer(Employee):
    def _init_(self, name, employee_id, salary):
        super()._init_(name, employee_id, salary)
        self.programming_languages = []

    def display_info(self):
        super().display_info()
        print("Programming Languages: ")
        for language in self.programming_languages:
            print(f" - {language}")

    def add_programming_language(self, language):
        self.programming_languages.append(language)


class Intern(Employee):
    def _init_(self, name, employee_id, salary, school_name, graduation_year):
        super()._init_(name, employee_id, salary)
        self.school_name = school_name
        self.graduation_year = graduation_year

    def display_info(self):
        super().display_info()
        print(f"School Name: {self.school_name}")
        print(f"Graduation Year: {self.graduation_year}")


# Example data
manager= Manager("Alice Smith", 1, 80000, "Sales")
developer= Developer("Bob Johnson", 2, 60000)
intern= Intern("Charlie Brown", 3, 20000, "ABC University", 2024)

developer.add_programming_language("Python")
developer.add_programming_language("JavaScript")

manager.add_employee(developer)
manager.add_employee(intern)

# Display information
print("Manager's Information:")
manager.display_info()
print()

print("Developer's Information:")
developer.display_info()
print()

print("Intern's Information:")
intern.display_info()
print()

# Calculate and display annual salaries
print(f"Annual Salary of Manager: ${manager.calculate_annual_salary():,.2f}")
print(f"Annual Salary of Developer: ${developer.calculate_annual_salary():,.2f}")
print(f"Annual Salary of Intern: ${intern.calculate_annual_salary():,.2f}")
