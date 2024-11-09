import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset for total fours and total sixes by year
df = pd.read_csv(r'ipl\list of fours(2008-24).csv')
df1 = pd.read_csv(r'ipl\list of sixes(2008-24).csv')

# Create the figure and axis for plotting
fig, ax1 = plt.subplots()

# Data for the plot
x = df['Year']  # Years (x-axis)
y = df['Total fours']  # Total fours by year (y-axis for ax1)
z = df1['Total Sixes']  # Total sixes by year (y-axis for ax2)

# Plot the data for total fours
ax1.plot(x, y, color='yellow', marker='o', markersize=8, linewidth=2.0, label='Total Fours')
ax1.set_xlabel('Year', fontdict={'fontsize': 15, 'color': 'Blue', 'family': 'Times new Roman'}, labelpad=10)
ax1.set_ylabel('Fours By Each Year', fontdict={'fontsize': 15, 'color': 'Blue', 'family': 'Times new Roman'}, labelpad=10)
ax1.legend(loc='upper left')

# Create a secondary y-axis for plotting total sixes
ax2 = ax1.twinx()
ax2.plot(x, z, color='red', marker='o', markersize=8, linewidth=2.0, label='Total Sixes')
ax2.set_xlabel('Year', fontdict={'fontsize': 15, 'color': 'Blue', 'family': 'Times new Roman'}, labelpad=10)
ax2.set_ylabel('Sixes By Each Year', fontdict={'fontsize': 15, 'color': 'Blue', 'family': 'Times new Roman'}, labelpad=10)
ax2.legend(loc='upper center')

# Adjust layout for better spacing
plt.subplots_adjust(bottom=0.15)

# Set the plot title
plt.title('Historical Performance: Total Fours & Sixes by Year', fontdict={'fontsize': 20, 'family': 'Times new Roman'}, pad=10)

# Show the plot
plt.show()
