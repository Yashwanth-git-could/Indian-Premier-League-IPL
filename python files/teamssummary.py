# Import necessary libraries
import requests  # For making HTTP requests
from bs4 import BeautifulSoup  # For parsing HTML
import pandas as pd  # For data manipulation

# Define the URL to scrape data from
url = 'https://www.espncricinfo.com/records/trophy/team-results-summary/indian-premier-league-117'

# Send a GET request to the URL
page = requests.get(url=url)

# Parse the page content with BeautifulSoup
soap = BeautifulSoup(page.text, 'html.parser')

# Find the table header (thead) and extract column headers
thead = soap.find('thead')
trow = thead.find('tr')
headers = [i.text.strip() for i in trow.find_all('td')]

# Create an empty DataFrame with the extracted headers
df = pd.DataFrame(columns=headers)

# Find the table body (tbody) and extract all rows
tbody = soap.find('tbody')
tr = tbody.find_all('tr')

# Loop through each row in the table body
for i in tr:
    row_data = i.find_all('td')
    data = [i.text.strip() for i in row_data]  # Clean the data by stripping extra spaces
    length = len(df)
    df.loc[length] = data  # Add the row to the DataFrame

# Split the 'Span' column into 'Start Year' and 'End Year' and convert them to integers
df[['Start Year', 'End Year']] = df['Span'].str.split('-', expand=True).astype(int)

# Convert relevant columns ('Start Year', 'End Year', 'Mat', 'Won', 'Lost') to integers
df[['Start Year', 'End Year', 'Mat', 'Won', 'Lost']] = df[['Start Year', 'End Year', 'Mat', 'Won', 'Lost']].astype(int)

# Calculate the winning percentage and losing percentage, round to 3 decimal places
df['Win%'] = round((df['Won'] / df['Mat']) * 100, 3).astype(float)
df['Lost%'] = round((df['Lost'] / df['Mat']) * 100, 3).astype(float)

# Calculate the win-loss ratio, round to 3 decimal places
df['Win-loss(ratio)'] = round((df['Won'] / df['Lost']), 3).astype(float)

# Reorganize the columns to display the relevant data
df = df[['Team', 'Start Year', 'End Year', 'Mat', 'Won', 'Lost', 'Win%', 'Lost%', 'Win-loss(ratio)']]

# Save the DataFrame to a CSV file
df.to_csv(r'ipl\teamssummary.csv', index=False)
