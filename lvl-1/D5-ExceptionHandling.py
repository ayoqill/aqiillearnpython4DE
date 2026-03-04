# the logic is that if there's an error it will catch it and continue run the next line of code, even if there's an error.

x = "10"

try:
    if (x > 10):
        print("x is greater than 10")
    
    else:
        print("x is less than or equal to 10")

except Exception as e:
    print(f"An error occurred: {e}") 

    # e is the error
    # we can print the variable in string using f-string, which is a way to format string in Python.
    # It allows us to embed expressions inside string literals, using curly braces {}.


print("This line will still be executed even if there's an error in the try block.")

