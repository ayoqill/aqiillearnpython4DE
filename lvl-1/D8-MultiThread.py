# Multi Threading is a technique that allows a program to run multiple threads of execution concurrently.
# This can be useful for improving the performance of a program by allowing it to perform multiple tasks at the same time.
# make it run faster and handy for Data Engineer, because we can run multiple tasks at the same time, which can save time and increase efficiency.

# imagine a restaurant, where there are multiple tables and customers. 
# The restaurant can serve multiple customers at the same time, which can save time and increase efficiency. 
# This is like having a multi chef
import time
import random
from concurrent.futures import ThreadPoolExecutor

tables = ["table1", "table2", "table3", "table4", "table5"]


def task(i):

    wait_time = random.randint(1, 3) 
    print(f"Task {i} is running, will take {wait_time} seconds to complete.")
    time.sleep(wait_time)
    print(f"Task {i} is completed.")

for i in tables:
    task(i)