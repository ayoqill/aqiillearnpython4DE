# can handle individual value and perform operation on each of them in a list or any iterable.

my_list = [1, 2, 3, 4, 5]

def square(item):
    return item*item

result = list(map(square, my_list)) # map(function, iterable)
print(result)