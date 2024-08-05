'''
This is where I will create code to extract the data from the websites
I will be using. I will also be adding Basketball Reference 2023 NBA Team statistics.
'''
import requests
from bs4 import BeautifulSoup
import csv
#Extracting data on Lebron James from 
def extracted_data(URL):
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table', {'id': 'per_game'})

    headers = [th.get_text() for th in table.find_all('tr')[0].find_all('th')]

    basketball_data = []
    for row in table.find_all('tr')[1:]:  # Added this in order to skip the inital header row.
        cols = row.find_all('td')
        if cols:
            age = cols[0].get_text()     # Age
            team = cols[1].get_text()        # Team
            league = cols[2].get_text()      # League
            games = cols[4].get_text()        # Games(G)
            ast = cols[23].get_text()        # Assists (AST)
            stl = cols[24].get_text()        # Steals (STL)
            reb = cols[22].get_text()        # Rebounds (REB)
            blk = cols[25].get_text()        # Blocks (BLK)
            pts = cols[28].get_text()        # Points (PTS)
            basketball_data.append([
                age,
                team,
                league,
                games,
                ast,
                stl,
                reb,
                blk,
                pts
            ])
    return basketball_data

if __name__ == "__main__":
    URL = 'https://www.basketball-reference.com/players/j/jamesle01.html'
    basketball_data = extracted_data(URL)
    #I have done this last part to make it easier to keep track of what the code is doing, after this final code it should populate
    # A "Lebron_data.csv" file which is what I will use in the transform/load.py to load it into the Data folder.
    with open('Lebron_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Age', 'Team', 'League', 'G', 'AST', 'STL', 'REB', 'BLK', 'PTS'])
        writer.writerows(basketball_data)
