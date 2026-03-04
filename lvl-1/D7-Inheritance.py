# Inheritance 

class company:
    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"Company Name: {self.name}")


class employee(company):
    def __init__(self, name, emp_name):
        super().__init__(name) # Call the constructor of the parent class to initialize the name attribute.
        self.emp_name = emp_name

    def info(self):
        super().info() # Call the info method of the parent class to print the company name.
        print(f"Employee Name: {self.emp_name}") # Print the employee name.


# create an object of the employee class
emp1 = employee("Tech Company", "Aqil")
emp1.info() # Call the info method of the employee class, which will also call the info method of the company class due to inheritance.

print(isinstance(emp1, employee)) # Check if emp1 is an instance of the employee class, which should return True.
print(isinstance(emp1, company)) # Check if emp1 is an instance of the company

