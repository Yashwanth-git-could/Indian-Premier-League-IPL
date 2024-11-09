# Import necessary libraries
import requests  # For making HTTP requests
from bs4 import BeautifulSoup  # For parsing HTML content
import pandas as pd  # For handling data in DataFrame format

# List of IPL teams for which we want to scrape data
teams = [
    "chennai-super-kings",
    "mumbai-indians",
    "royal-challengers-bangalore",
    "delhi-capitals",
    "kolkata-knight-riders",
    "kings-xi-punjab",
    "rajasthan-royals",
    "sun-risers",
    "lucknow-super-giants",
    "gujarat-titans"
]

# Initialize an empty list to store dataframes for each team
all = []

# Loop through each team in the list
for team in teams:
    # Construct the URL for each team's page on cricketwa
    uri = f"https://www.cricketwa.com/records/tournament/indian-premier-league/{team}"
    
    # Send a GET request to the URL and fetch the page content
    page = requests.get(url=uri)
    
    # Parse the page content using BeautifulSoup
    soup = BeautifulSoup(page.text, 'html.parser')
    
    # Find the second table in the parsed HTML (the one with team records)
    table = soup.find_all('table')[1]
    
    # Get all rows in the table
    rows = table.find_all('tr')
    
    # Initialize a DataFrame with the required columns
    df = pd.DataFrame(columns=["oppisition", "M", "W", "L", "Tie-W", "Tie-L", "NR", "recent matches"])
    
    # Loop through each row in the table
    for row in rows:
        # Extract all the <td> elements from the row (these contain the data)
        row_data = row.find_all('td')
        
        # Clean and extract the text from each <td> element
        data = [cell.text.strip() for cell in row_data]
        
        # If there is data in the row, append it to the DataFrame
        if len(data) > 0:
            df.loc[len(df)] = data
    
    # Add the team name as a new column to the DataFrame
    df['Team'] = f"{team}"
    
    # Append the DataFrame for the current team to the 'all' list
    all.append(df)

# Concatenate all the individual team dataframes into one large dataframe
data1 = pd.concat(all, ignore_index=True)

# Replace 'kings-xi-punjab' with 'punjab-kings' and 'sun-risers' with 'Sunrisers Hyderabad'
# Also, capitalize team names and replace dashes with spaces
data1["Team"] = data1['Team'].str.replace('kings-xi-punjab', 'punjab-kings', regex=True).str.replace('sun-risers', 'Sunrisers Hyderabad', regex=True)

# Clean the 'oppisition' column by removing unwanted 'vs' text
data1['oppisition'] = data1["oppisition"].str.replace("vs \n", "", regex=True)

# Capitalize the team names in the 'Team' column
data1['Team'] = data1['Team'].str.replace("-", " ", regex=True).str.title()

# Reorganize the columns to have 'Team', 'oppisition', 'M', 'W', 'L', 'Tie-W', 'Tie-L', 'NR' in the final dataframe
data1 = data1[['Team', "oppisition", "M", "W", "L", "Tie-W", "Tie-L", "NR"]]

# Save the final DataFrame to a CSV file
data1.to_csv(r'ipl\teams-vs-teams-records.csv', index=False)
