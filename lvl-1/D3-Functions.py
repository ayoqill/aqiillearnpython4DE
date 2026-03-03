# Use function to make the code reuseable and organize. jimat ruang code

"""
def my_function(x):

    if (x > 10):
        print("x is greater than 10")
    elif (x == 10):
        print("x is equal to 10")
    else:
        print("x is less than 10")
    return x*2

returned_val = my_function(20)
print(returned_val)
"""

# Function with multiple parameters

""""
def greet(name, age):

    return(name, age)

greeting = greet("aqil", 22)

print(greeting)
"""

# What if the input/data is so many? make it into tuple

"""
def biodata(*bio):

    return bio

my_bio = biodata("aqil", 22, "coding", "gaming", "traveling")
print(my_bio)
"""

# Function with keyword arguments, change it to dictionary
def biodata(**bio):

    return bio

my_bio = biodata(name="aqil", age=22, hobby="coding", hobby2="gaming", hobby3="traveling")
print(my_bio)