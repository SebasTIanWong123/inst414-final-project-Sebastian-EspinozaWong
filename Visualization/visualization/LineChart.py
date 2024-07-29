'''
Line Chart(Blocks Over the Span of Lebrons career(by age)):
If a coach wants to determine a defenders performance, one of the biggest metrics used to measure this is blocks. So with this visualization
I was able to create how many blocks lebron has had over the span of his career, of course this code can be switched to evaluate any players performance.

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

# Plot the line chart
plt.figure(figsize=(10, 6))
plt.plot(data['Age'], data['BLK'], marker='o', color='skyblue')
plt.xlabel('Age')
plt.ylabel('Blocks')
plt.title('Blocks Over the Span of Lebrons career(by age)')
plt.show()
