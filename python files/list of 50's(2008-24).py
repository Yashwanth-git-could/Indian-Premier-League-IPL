import pandas as pd
import requests
from bs4 import BeautifulSoup

# Define the range of years for the IPL seasons
years = [i for i in range(2008, 2025)]

# Initialize an empty list to store data for each year
dataofyears = []

# Loop over the years to extract data for each year
for year in years:
    # Construct the URL for the specific IPL year
    url = f'https://t20cricstats.com/ipl-{year}/stats/total-fifties'
    
    # Send a request to fetch the page content
    page = requests.get(url=url)
    
    # Parse the page content using BeautifulSoup
    soup = BeautifulSoup(page.text, 'html.parser')
    
    # Find the table body in the parsed HTML
    tbody = soup.find('tbody')
    
    # Find the first row in the table body
    tr = tbody.find('tr')
    
    # Extract all the data (td) cells from the row
    td = tr.find_all('td')
    
    # Initialize a DataFrame with the appropriate column names
    df = pd.DataFrame(columns=['Year', 'Total fifties'])
    
    # Extract text from each cell in the row and strip any leading/trailing spaces
    data = [i.text.strip() for i in td]
    
    # Append the data for the current year to the DataFrame
    length = len(df)
    df.loc[length] = data
    
    # Add the DataFrame for the current year to the list
    dataofyears.append(df)

# Concatenate the data for all years into a single DataFrame
data = pd.concat(dataofyears)

# Convert the 'Total fifties' column to integer type
data['Total fifties'] = data['Total fifties'].astype(int)

# Save the final DataFrame to a CSV file
data.to_csv(r"ipl\list of 50's(2008-24).csv", index=False)

# Print the final DataFrame to verify
print(data)
