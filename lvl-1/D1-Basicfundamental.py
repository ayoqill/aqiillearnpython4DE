"""
print("Hi there! Welcome to Level 1 of the education. Let's get started!")
print('Hello Aqil')

Use triple quotes to write a multi-line string comments. This is useful for writing long messages.
Use # to write comments.
"""
#print ("Hello Aqil", 260) - can combine string and number in print statement, but it will convert number to string.

# Python is interpreter language, it executes code line by line.
# Python is dynamically typed language, we don't need to declare variable type.

# Being Data Engineer must always use python environment, because python has many libraries for data engineering such as pandas, numpy, etc.

# Delimiters (sep) - use to separete code into blocks

#print("Hello Aqil", 260, "is your username", sep='*')

#print('Hello \'AQIL AIMAN\'. This is a test for pyspark, as we need to master the string manipulation in python for data engineering.')

"""
total_sum = 1+2 (\)
            +3+4+5

print(total_sum) # The backslash (\) allow us to write code in multiple lines without breaking the code.
"""


# Variables

"""
Variables in Python:
- Variables are used to store data in Python.
- Variables can be of different types such as string, integer, float, etc.
- Variables can be assigned values using the assignment operator (=).
- Variable names should be descriptive and should follow the naming conventions (e.g., snake_case).

"""

"""

my_var = "Aqil"
my_lasname = "Aiman"

x = 60 # integer variable so must use str() to convert it to string when concatenating with other strings.

print(my_var + " " + my_lasname + " is " + str(x + 200)) ---- (this is type casting, converting integer to string) to concatenate with other strings.

"""

# Indentation in Python is very important

"""
x = 10

if x > 5:
    print("x is greater than 5") #true

if x < 5:
print("x is less than 5") #false

"""
"""
# Array

y = "Aqilaiman"

print(y[0:4])

"""

# explore python string methods, there are so many function of them.

#Loop

"""
tbl_list = ["User", "Order", "Product", "Category"]

for i in tbl_list:
    print(i)
    for j in i:
        print(j)
        
"""