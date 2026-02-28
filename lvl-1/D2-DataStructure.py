# Data Structures in .py
# means efficient way to store and organize data in Python. 

# A list
"""
my_list = [1, 2, 'aqil', [0,1,2], True]

print(my_list[3][1]) # Accessing the second element of the nested list [0,1,2] which is 1.

"""

"""
my_list.append("Ikan")

print(my_list)
"""

# list are mutabale, which means can be edited.

# no need to like my_list = my_list.append("Ikan")


#A Dictionary

"""
my_dict = {
            "name": "aqil",
            "age": 20,
            "hobbies": ["coding", "gaming", "traveling"],
    }

print(my_dict["hobbies"][0]) 
print(my_dict)
print(my_dict.keys())
print(my_dict.items())

"""

# a Tuple

my_tuple = (1, 2, 'aqil', True)

my_tuplist = list(my_tuple) # Convert the tuple to a list to make it mutable.

my_tuplist.append("Ikan") # Now we can append to the list.

my_tuple = tuple(my_tuplist) # Convert it back to a tuple.

