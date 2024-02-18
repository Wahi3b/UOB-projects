# class Movie:
    
#     id_counter = 0 
#     def __init__(self,title,rating):
#         self.title = title
#         self.rating = rating
#         Movie.id_counter += 1
#         self.id = Movie.id_counter

#     def info(self):
#         print(f"ID:{self.id}, Title:{self.title}, Rating:{self.rating}  ")

# instance1 = Movie("Inception",8.8)
# instance2 = Movie('The Matrix', 8.7)
# instance1.info()
# instance2.info()

# Classes ==================================================================

class HRManager:
    
    # Add the class attributes

    def __init__(self, name, age, department, phone, annual_salary):
        self.name = name
        self.age = age
        self.department = department
        self.phone = phone
        self.annual_salary= annual_salary

class Employee:
    
    # Add the class attributes

    def __init__(self, name, age, address, phone, department,annual_salary):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
        self.department = department
        self.annual_salary= annual_salary

# Program ==================================================================

# Function that prints the monthly salary of each employee
# and the total payroll expense for the company
def process_payroll(employees):

    total_payroll_expense = 0
    print("\n========= Welcome to the HR Payroll System =========\n")

    # Iterate over the list of instances to calculate
    # and display the monthly salary for each employee,
    # and add the total payroll expense
    for emp in employees:
        monthly_salary = emp.annual_salary / 12
        print(f"{emp.name.capitalize()}'s monthly salary is: ${monthly_salary:.2f}")
        total_payroll_expense += monthly_salary

    # Print the total payroll expense for the month
    print("\nThe total payroll expense for the month is: $", total_payroll_expense)

# Instances (employees)
jack = HRManager("jack", 50, "Human Resources", "555-321-4567", 50000)
isabel = Employee("isabel", 28, "123 Maple St", "555-654-1234", "Marketing", 44000)

# List of employee instances
employees = [jack, isabel]

# Call the function, passing in the list of employee instances
process_payroll(employees)