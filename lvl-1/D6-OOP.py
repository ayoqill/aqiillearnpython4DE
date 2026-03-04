# oop is like a template for creating objects.

class employee:
    # class attributes
    emp_name = "aqil"
    position = "data engineer"

    def __init__(self, emp_name=None, position=None):
        if emp_name is not None:
            self.emp_name = emp_name
        if position is not None:
            self.position = position

    def info(self):
        print(f"{self.emp_name} is working as a {self.position}.")

    @classmethod
    def from_string(cls, emp_str):
        emp_name, position = emp_str.split(",")
        return cls(emp_name, position)

    @staticmethod
    def is_working():
        return "The employee is working."

# create an object of the class employee
emp1 = employee()
print(emp1.emp_name) # Accessing the class attribute emp_name
print(emp1.position) # Accessing the class attribute position
emp1.info() # Calling the class method info() to print the employee's information.

# Call static method on instance
print(emp1.is_working())
# Call classmethod to create new instance
print(employee.from_string("aqil,data engineer").emp_name)