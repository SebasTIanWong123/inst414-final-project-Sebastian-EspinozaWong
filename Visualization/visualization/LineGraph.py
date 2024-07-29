'''
This is where I will create visualization from the data collect from 
the websites. The kind of visualization is EDA. I have created 4 different visualization on Python under the visualizaton folder. I made them different things I feel could
show the business problem I am trying to solve. Every file has their own explanation.

Line Graph(Lebrons Performance Over Career): I chose this visualization in order to show players or coaches the longivity of a player and how their performance can get better or worse as they age.

'''

import matplotlib.pyplot as plt 
import csv 
import pandas as pd

# Load the CSV file into a DataFrame
file_path = 'Lebron_data.csv'
data = pd.read_csv(file_path)

# Remove rows with missing values
data = data.dropna().reset_index(drop=True)

# Display the first few rows of the DataFrame to ensure it loaded correctly
print(data.head())

#Performance over years, created a graph.
plt.figure(figsize=(10, 6))
plt.plot(data['Age'], data['PTS'], marker='o', label='Points')
plt.plot(data['Age'], data['AST'], marker='o', label='Assists')
plt.plot(data['Age'], data['REB'], marker='o', label='Rebounds')
plt.xlabel('Age of Lebron')
plt.ylabel('Basketball Statistics')
plt.title('Lebrons Performance Over Career')
plt.legend()
plt.xticks(rotation=45)
plt.show()