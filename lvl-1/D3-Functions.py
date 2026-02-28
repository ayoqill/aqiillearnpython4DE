# Use function to make the code reuseable and organize. jimat ruang code

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
