'''
This is where I will create code to evaluate the data I have scrapped
from the web. 
'''
def analyzing_data():
    df = pd.read_csv('Data/Lebron_Stat.csv')


    results.to_csv('Data/Analytical_results.csv', index=False)

if __name__ == "__main__":
    analyzing_data()
 # At the moment this code will not work, as I have to find out more about the kind of coding I need 
 # To do in order to follow the analytical model I chose for this business problem and data.
 # What I want to evaluate here is Lebrons stats for the first 5 years of his career to study
 # The Trend of an upcoming player and the impact he can have on a game.
 