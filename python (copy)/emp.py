class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}, Employee ID: {self.emp_id}, Salary: ${self.salary:.2f}")

    def calculate_annual_salary(self):
        return self.salary * 12

class Manager(Employee):
    def __init__(self, name, emp_id, salary, department, employees_managed):
        super().__init__(name, emp_id, salary)
        self.department = department
        self.employees_managed = employees_managed

    def display_managed_employees(self):
        print(f"Managed Employees: {', '.join(self.employees_managed)}")

class Developer(Employee):
    def __init__(self, name, emp_id, salary, programming_languages):
        super().__init__(name, emp_id, salary)
        self.programming_languages = programming_languages

    def add_programming_language(self, language):
        self.programming_languages.append(language)

class Intern(Employee):
    def __init__(self, name, emp_id, salary, school_name, graduation_year):
        super().__init__(name, emp_id, salary)
        self.school_name = school_name
        self.graduation_year = graduation_year

# Example usage:
manager1 = Manager("John Doe", "M001", 80000, "Engineering", ["Alice", "Bob"])
developer1 = Developer("Jane Smith", "D001", 60000, ["Python", "Java"])
intern1 = Intern("Eva Brown", "I001", 20000, "XYZ University", 2024)

manager1.display_info()
manager1.display_managed_employees()

developer1.display_info()
developer1.add_programming_language("JavaScript")
print(f"Programming Languages: {', '.join(developer1.programming_languages)}")

intern1.display_info()
print(f"School: {intern1.school_name}, Graduation Year: {intern1.graduation_year}")
