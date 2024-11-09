# Import necessary libraries
import pandas as pd  # For data manipulation
import matplotlib.pyplot as plt  # For creating plots
import numpy as np  # For numerical operations (e.g., array manipulation)

# Read the data from the CSV file containing IPL team toss and match statistics
df = pd.read_csv(r'ipl\team toss lost.csv')

# Create a new column 'intials' by extracting the first letter of each word in the 'Team' column
df['intials'] = df['Team'].apply(lambda x: ''.join([word[0] for word in x.split()]))

# Sort the DataFrame by the 'Mat' column (matches played) in descending order
df = df.sort_values(by='Mat', ascending=False)

# Assign 'intials', 'Mat', 'Won', and 'Lost' columns to variables for ease of use
x = df['intials']  # Team initials for the x-axis
y = df['Mat']      # Total matches played for the y-axis
z = df['Won']      # Matches won for the z-axis
w = df['Lost']     # Matches lost for the w-axis

# Create a subplot for the bar chart
fig, axs = plt.subplots()

# Hide the top and right spines of the plot for a cleaner look
axs.spines['top'].set_visible(False)
axs.spines['right'].set_visible(False)

# Set the width of each bar in the grouped bar chart
barwidth = 0.2

# Generate an array of positions for each team on the x-axis
index = np.arange(len(x))

# Plot the bars for 'Matches', 'Won', and 'Lost' with different colors
plt.bar(index, y, barwidth, label='Matches', color='orange')  # Total matches
plt.bar(index + barwidth, z, barwidth, label='Won', color='Purple')  # Matches won
plt.bar(index + 2 * barwidth, w, barwidth, label='Lost', color='brown')  # Matches lost

# Add text annotations above each 'Matches' bar to display the count of matches
for i, value in enumerate(y):
    plt.text(i, value + 0.5, str(y.iloc[i]), ha='center')

# Add text annotations above each 'Won' bar to display the count of wins
for i, value in enumerate(z):
    plt.text(i + barwidth, value + 0.5, str(z.iloc[i]), ha='center')

# Add text annotations above each 'Lost' bar to display the count of losses
for i, value in enumerate(w):
    plt.text(i + 2 * barwidth, value + 0.5, str(w.iloc[i]), ha='center')

# Set the x-axis label
plt.xlabel('Teams')

# Set the y-axis label
plt.ylabel('Values')

# Set the x-axis tick labels (team initials) and rotate them for better visibility
plt.xticks(index + barwidth, x, rotation=45)

# Set the title of the plot
plt.title('Toss and Triumph: Exploring Wins and Losses of IPL Teams')

# Adjust the layout of the plot for better spacing
plt.subplots_adjust(left=0.12, right=0.9, top=0.85, bottom=0.15)

# Display the legend to label each bar
plt.legend()

# Show the plot
plt.show()