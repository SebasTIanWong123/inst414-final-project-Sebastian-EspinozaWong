''' In This section I will be transforming and loading the data I have.'''
import os
import csv
#Loading data
def loading_data(file_path):
    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        headers = next(reader)  
        data = [row for row in reader]
    return data
#Making sure file gets sabed in right folder and writing csv
def saved_data(data, output_folder):
    file_path = os.path.join(output_folder, 'player_stats_corrected.csv')
    
    os.makedirs(output_folder, exist_ok=True)
    
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Age', 'Team', 'League', 'G', 'AST', 'STL', 'REB', 'BLK', 'PTS'])
        writer.writerows(data)
    
    print(f"\nExtracted Data saved to: {file_path}")

if __name__ == "__main__":
    extracted_file_path = 'extracted_data.csv'
    
    # Defining the file pathway
    output_folder = r'C:\Users\sebas\OneDrive\Desktop\INST 327\inst414-final-project-Sebastian-EspinozaWong\Data'
    data = loading_data(extracted_file_path)
    # Saving the data in the proper folder.
    saved_data(data, output_folder)
