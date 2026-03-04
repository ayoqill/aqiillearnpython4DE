# pydantic is use for data validation and settings management using Python type annotations.
# It allows us to define data models with type hints, 
# and it automatically validates the data against those types when you create instances of the models. 
# Pydantic is often used in web development, APIs, and any situation where you need to ensure that the data being processed conforms to a specific structure.


from pydantic import BaseModel

# Define a Pydantic model for a user
class User(BaseModel):
    id: int
    name: str
    email: str = None  # Optional field with a default value of None

# Create an instance of the User model
user1 = User(id=1, name="Alice", email="alice@example.com")
print(user1)  # Output: id=1 name='Alice'

# Create an instance of the User model without the optional email field
user2 = User(id=2, name="Bob")
print(user2)  # Output: id=2 name='Bob' email=None

# Attempting to create an instance with invalid data will raise a validation error
try:
    user3 = User(id="not an integer", name="Charlie")
except Exception as e:
    print(f"Validation error: {e}")

