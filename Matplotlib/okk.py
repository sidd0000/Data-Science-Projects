import csv

# Function to load data from a CSV file
def load_data(file_path):
    data = {}
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data[row['name'].lower()] = row
    return data

# Function to get player data by name
def get_player_data(name, data):
    name = name.lower()
    return data.get(name, "Player not found")

# Load the player data
player_data = load_data('./gas_prices.csv')

# Example usage
name_to_search = input("Enter player name: ")
player_info = get_player_data(name_to_search, player_data)
print(player_info)
