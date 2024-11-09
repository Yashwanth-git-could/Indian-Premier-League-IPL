# Import necessary libraries
import requests  # For making HTTP requests
from bs4 import BeautifulSoup  # For parsing HTML
import pandas as pd  # For data manipulation

# Define the URL to scrape data from
url = 'https://www.crictracker.com/ipl-winners-and-runners-list/'

# Send a GET request to the URL
page = requests.get(url=url)

# Parse the page content with BeautifulSoup
soap = BeautifulSoup(page.text, 'html.parser')

# Create an empty DataFrame with the desired column names
df = pd.DataFrame(columns=['Year', 'Winner', 'Won By', 'Runner Up', 'Venue'])

# Find the table body (tbody) and extract all rows
tbody = soap.find('tbody')
tr = tbody.find_all('tr')[2:19]  # Extract rows from index 2 to 19 (since first 2 rows may be headers or unwanted data)

# Loop through each row in the table body
for i in tr:
    row_data = i.find_all('td')  # Extract all table data (td) from the row
    data = [i.text.strip() for i in row_data]  # Clean the data by stripping extra spaces
    length = len(df)
    df.loc[length] = data  # Add the row to the DataFrame

# Save the DataFrame to a CSV file
df.to_csv(r'ipl\teamstitles.csv', index=False)
