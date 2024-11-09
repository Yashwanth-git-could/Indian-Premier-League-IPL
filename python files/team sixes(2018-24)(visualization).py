import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv(r'ipl\team sixes(2018-24).csv')
df_fixed = pd.DataFrame(data)

# Pivot the data for plotting (Year as columns, Team as index)
df_pivot_fixed = df_fixed.pivot(index='Team', columns='Year', values='6s')

# Plotting the corrected bar chart
df_pivot_fixed.plot(kind='bar')

# Adding labels and title
plt.title('Total Sixes by Team and Year')
plt.xlabel('Team')
plt.ylabel('Total 6\'s')
plt.xticks(rotation=45)
plt.legend(title='Year', bbox_to_anchor=(0.5, 1.0), loc='upper center', ncol=7,frameon=False)
plt.subplots_adjust(left=0.1,right=0.97,top=0.87,bottom=0.2)

# Show the plot
plt.tight_layout()
plt.show()