# Import necessary libraries
import pandas as pd  # For data manipulation
import requests  # For making HTTP requests
from bs4 import BeautifulSoup  # For parsing HTML

# Define the list of years from 2008 to 2024
years = [i for i in range(2008, 2025)]

# Initialize an empty list to store data for each year
dataofyears = []

# Loop through each year to scrape the data for that year
for year in years:
    # Construct the URL for the current year
    url = f'https://t20cricstats.com/ipl-{year}-standings'
    
    # Send a GET request to the URL
    page = requests.get(url=url)
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page.text, 'html.parser')
    
    # Find the table header (thead) and extract the headers
    thead = soup.find('thead')
    tr = thead.find('tr')
    headers = [i.text for i in tr.find_all('th')]
    
    # Create an empty DataFrame with the extracted headers
    df = pd.DataFrame(columns=headers)
    
    # Find the table body (tbody) and extract the rows
    tbody = soup.find('tbody')
    tr = tbody.find_all('tr')
    
    # Loop through each row and extract the data
    for i in tr:
        td = i.find_all('td')
        data = [i.text.strip() for i in td]  # Clean the data by stripping extra spaces
        
        # Add the data to the DataFrame
        length = len(df)
        df.loc[length] = data
    
    # Add the year as a new column to the DataFrame
    df['Year'] = f'{year}'
    
    # Append the DataFrame for this year to the list of all years
    dataofyears.append(df)

# Concatenate the DataFrames for all years into a single DataFrame
data = pd.concat(dataofyears)

# Convert the columns 'M', 'W', 'L', 'Pts' to integers
data[['M', 'W', 'L', 'Pts']] = data[['M', 'W', 'L', 'Pts']].astype(int)

# Convert the 'NRR' column to float
data['NRR'] = data['NRR'].astype(float)

# Drop the 'For' and 'Against' columns as they are not needed
data = data.drop(['For', 'Against'], axis=1)

# Reorganize the columns to the desired order
data = data[['Year', 'Team', 'M', 'W', 'L', 'Pts', 'NRR']]

# Save the final DataFrame to a CSV file
data.to_csv(r'ipl\2008-24pointstable.csv', index=False)
