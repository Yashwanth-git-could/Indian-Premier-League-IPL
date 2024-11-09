import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv(r"ipl\list of 50's.csv")

# Create the figure and axis
fig, ax1 = plt.subplots(figsize=(10, 6))  # Adjust figure size if needed

# Data for the plot
x = df['Year']
y = df['Total fifties']

# Create the stackplot (only one layer here)
ax1.stackplot(x, y, color='skyblue', alpha=0.6)

# Add a title
plt.title('Total Fifties Scored in IPL Matches by Year',
          fontdict={'fontsize': 18, 'color': 'darkcyan', 'family': 'Times New Roman'}, pad=20)

# Add x and y labels
ax1.set_xlabel('Year', fontdict={'fontsize': 15, 'color': 'blue', 'family': 'Times New Roman'}, labelpad=10)
ax1.set_ylabel('Total Fifties', fontdict={'fontsize': 15, 'color': 'blue', 'family': 'Times New Roman'}, labelpad=10)

# Annotate each point with the total fifties achieved
for i in range(len(x)):
    ax1.text(x[i], y[i] + 1, str(y[i]), ha='center', va='bottom', color='black', fontsize=10)

# Show legend
ax1.legend(loc='upper left')

# Customize layout for better spacing
plt.tight_layout()

# Show the plot
plt.show()
