'''
This is where I will create code to extract the data from the websites
I will be using.
'''
import os
import requests
import pandas as pd


#Extract data from ESPN
def extract_data():
    
    URL = "https://www.espn.com/nba/stats"
    response = requests.get(URL)

    with open ('data/extracted/espn_html', 'w') as file:
        file.write(response.text)

    #Now for Basketball Reference
    URL = "https://www.basketball-reference.com/"
    response = requests.get(URL)

    with open('data/extracted/basketball_refernces.html', 'w') as file:
        file.write(response.text)

if __name__ == "__main__":
    extract_data()
        