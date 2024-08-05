''' 
I will be doing predictive and descriptive analysis, as well as EDA. I have some questions that a consumer may ask when thinking about what the business problem I am trying to solve will actually show.

What's the problem that having better statistical analysis on players solves? 
Having better statistical analysis of players is able to improve player longevity and performance, as well as solve possible consumer concerns when it comes to players and how they may perform. Having better analysis allows coaches and players alike to make more educated decisions and how they may perform and possible injury concerns, and how they perform under certain circumstance or conditions such as age, team, etc. 

Why would a business need this? 
A business such as a sports team or even possibly schools or colleges who play sport could use these models in order to better protect players from injuries but also possible improve player performance by analyzing certain metrics that coaches or player may otherwise not think about.

What kind of company has business problems wrt NBA stats?
Companies such as ESPN, Professional Sports teams, Collegiate Sports Teams, These models could even be altered to collect physical therapy data and possibly track the improvement of patients!

Why would they hire you to solve this business problem?
The reason they would want to hire a data scientist to solve this business problem is because data scientist can not only extract data, information, or even statistics. 
But they can also analyze all this information in a way that can show certain things that maybe a business may not otherwise see, in relation to this business problem, these companies hire data analysts because there is so much data on players in todays age and there seeking to create new algorithms and models that can either predict player performance or predict player injury, 
What I am doing is trying to create a safer game of basketball by creating insightful visualization from data that can be used to show such trends.


I will be using a Linear Regression Model in order to gather the analysis I need in order to solve the business problem

#NEW COMMIT: I will be now doing both regression model as well as a logistic regression, I will also be testing out trying some kind of clustering model but am not sure about its eligilibty with this data set.

''' 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
import numpy as np

# Load the Lebron_data.csv file and drop rows with any missing values
file_path = 'Lebron_data.csv'
data = pd.read_csv(file_path)

data = data.dropna().reset_index(drop=True)

# This is extracting all the relevant columns needed
X = data['Age'].values.reshape(-1, 1)
y = data['PTS'].values

# This is creating the linear regression model
model = LinearRegression()
model.fit(X, y)

# This is meant to predict the points using the model
y_pred = model.predict(X)

# This is creating the regression plot
plt.figure(figsize=(10, 6))
sns.regplot(x='Age', y='PTS', data=data, scatter_kws={'color': 'red'}, line_kws={'color': 'blue'})
plt.xlabel('Age')
plt.ylabel('Points')
plt.title("Linear Regression: Lebron James Points over his career")
plt.show()

# This is plotting the points and regression line separately
plt.figure(figsize=(10, 6))
plt.scatter(data['Age'], data['PTS'], color='red', label= 'Points')
plt.plot(data['Age'], y_pred, color='blue', label='Regression Line')
plt.xlabel('Age')
plt.ylabel('Points')
plt.title("Linear Regression: Lebron James Points over his career")
plt.legend()
plt.show()


