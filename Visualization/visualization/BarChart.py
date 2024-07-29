'''
Bar Chart(Average games played(quantified by amount of seasons of average games)):
I think this is a really good metric that most people may overlook. This Bar chart is basically showing how the average games lebron played, and the number of season he reached those games.
For example, there were 3 seasons 55-57 games, and then there is 12 seasons where he played more than 75 games! 

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

#Bar Graph I created.
plt.figure(figsize=(10, 6))
plt.hist(data['G'], bins=15, color='g', edgecolor='black')
plt.xlabel('Games Played')
plt.ylabel('Number of seasons games were played')
plt.title('Average games played(quantified by amount of seasons of average games)')
plt.show()