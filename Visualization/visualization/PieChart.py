'''
Pie Chart(Distribution of Total Points by Team's Lebron played on): The reason I chose to make this visualization is because I feel like it can help athletes and coachs see the longivity of players
such as Lebron and how different teams and the age of the player can possibly enhance or worse the performance of a player. This can help Coaches better position their players to do better.
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



# Group data by team and sum the points
team_points = data.groupby('Team')['PTS'].sum()

# Plot the pie chart
plt.figure(figsize=(10, 6))
team_points.plot.pie(autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Total Points by Teams that Lebron Played on')
plt.ylabel('')
plt.show()