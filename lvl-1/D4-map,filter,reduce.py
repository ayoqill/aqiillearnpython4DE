# can handle individual value and perform operation on each of them in a list or any iterable.

my_list = [1, 2, 3, 4, 5]

def square(item):
    return item*item

result = list(map(square, my_list)) # map(function, iterable)
print(result)

#above is only map example.
#reduce and filter is not really used in real world, but it is good to know how it works.