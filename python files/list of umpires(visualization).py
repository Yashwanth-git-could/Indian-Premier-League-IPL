import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load and process the data
df = pd.read_csv(r'ipl\list of umpires.csv')
df = df[df['Matches'] >= 50].sort_values(by='Matches')

x = df['UmpireName']
y = df['Matches']

# Get colors based on length of x
colors = plt.cm.tab20(np.arange(len(x)))

# Create a horizontal bar plot
plt.figure(figsize=(10, 6))
bars = plt.barh(x, y, color=[colors[i] for i in range(len(x))])

# Add title and axis labels
plt.title('Top Umpires with 50+ Matches in IPL', fontsize=16)
plt.xlabel('Number of Matches', fontsize=12)
plt.ylabel('Umpire Name', fontsize=12)

# Add grid for better readability
plt.grid(axis='x', linestyle='--', alpha=0.4)

# Add value labels to the bars
for bar in bars:
    plt.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2, 
             str(int(bar.get_width())), 
             va='center', ha='left', fontsize=10, color='black')

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()
