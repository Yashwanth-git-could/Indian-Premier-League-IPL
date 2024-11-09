import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL to scrape the data from
url = 'https://www.espncricinfo.com/records/trophy/individual-most-matches-umpire/indian-premier-league-117'

# Send a GET request to fetch the page content
page = requests.get(url=url)
soap = BeautifulSoup(page.text, 'html.parser')

# Initialize an empty DataFrame with specific columns
df = pd.DataFrame(columns=['Umpire', 'Span', 'Matches'])

# Extract the data from the HTML table
tbody = soap.find('tbody')
tr = tbody.find_all('tr')

# Loop through each row of the table to extract data
for i in tr:
    row_data = i.find_all('td')
    data = [i.text.strip() for i in row_data]
    length = len(df)
    df.loc[length] = data

# Extract Umpire's name and country from the 'Umpire' column
df['Umpire'] = df['Umpire'].astype(str)
df[['UmpireName', 'Country']] = df['Umpire'].str.extract(r'(.+?)\s+\((.+?)\)')

# Split the 'Span' column into 'Start Year' and 'End Year'
df[['Start Year', 'End Year']] = df['Span'].str.split('-', expand=True)

# Convert the relevant columns to integer type
df[['Start Year', 'End Year', 'Matches']] = df[['Start Year', 'End Year', 'Matches']].astype(int)

# Final selection of relevant columns
df = df[['UmpireName', 'Country', 'Start Year', 'End Year', 'Matches']]

# Save the DataFrame to a CSV file
df.to_csv('ipl/list of umpires.csv', index=False)
