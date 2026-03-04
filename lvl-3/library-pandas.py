# pandas is used for data manipulation and analysis.
# It provides data structures and functions needed to manipulate structured data, such as tables and time series data.

import pandas as pd

# Create a DataFrame from a dictionary
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

df = pd.DataFrame(data)
print(df)

# Read a CSV file into a DataFrame
# df = pd.read_csv("data.csv")
# print(df)

