## 1.Title: Dominating the Runs: Orange Cap Champions of IPL

## Steps:

### 1. Import Libraries
- Import `pandas` for data manipulation.
- Import `matplotlib.pyplot` for plotting.

### 2. Load Data
- Read the CSV file `orangecap.csv` using `pd.read_csv`.

### 3. Group Data
- Group the data by the 'Winners' column and count the number of occurrences using `groupby` and `count`.
- Reset the index to format the data into a DataFrame with columns 'Winners' and 'Times Won'.

### 4. Extract Data
- Extract the unique winners (teams) and their respective win counts into variables `x` and `y`.

### 5. Generate Colors for Pie Chart
- Generate a color palette using `plt.cm.tab20c` based on the number of unique winners.
- Create a dictionary `color_map` to associate each winner with a color.

### 6. Create Subplots
- Create a figure with two subplots: `ax1` for a table and `ax2` for a pie chart.

### 7. Create Pie Chart
- Plot a donut-style pie chart using `ax2.pie` with `autopct` to display percentage, and custom wedge properties.
- Add a white circle in the center to create a donut chart effect.

### 8. Add Legend
- Add a legend to the pie chart showing the names of the winners.

### 9. Create Table
- Use `ax1.table` to create a table displaying the winners and their corresponding win counts.
- Customize the table's font size and scale.

### 10. Color Table Rows
- Apply color to each row of the table based on the winner’s color from the `color_map`.

### 11. Remove Table Axis
- Turn off the axis for the table subplot to clean up the view.

### 12. Set Title
- Add a title to the entire figure using `fig.suptitle`.

### 13. Adjust Layout and Show Plot
- Use `plt.tight_layout()` to ensure proper spacing between subplots.
- Display the plot using `plt.show()`.
## Result
This visualization will showcase a donut-style pie chart and a table displaying the IPL Orange Cap winners and the number of times they have won the award. Each wedge of the pie chart will represent a different team, with the percentage of wins displayed for each. The chart will include customized wedge properties such as edge color and a white center circle to create a donut effect. A legend will be added to indicate which team corresponds to each color in the pie chart. The table will show the teams (winners) and their respective win counts, with rows colored according to the team’s associated color for easy interpretation. The overall figure will have a clear title and be well-organized for a clean presentation.

## 2.Title: Winning Leadership: Exploring Captains' Win Percentages & Loss Percentages

## Steps:

### 1. Import Libraries
- Import `pandas` for handling data manipulation.
- Import `matplotlib.pyplot` for plotting the pie charts.
- Import `numpy` (though it's not used in this script, it's often useful for numerical operations).

### 2. Read Data
- Load the IPL captains' data from a CSV file (`captains.csv`) using `pd.read_csv`.

### 3. Filter and Sort Data
- Filter the DataFrame to include only players who have played more than 45 matches using `df[df['Mat'] > 45]`.
- Sort the data by 'Mat' (matches played) in descending order using `sort_values`.

### 4. Extract Relevant Columns
- Extract the 'Player' column as the x-axis data (`x`).
- Extract the 'Won%' and 'Lost%' columns as the y-axis data (`y` and `w` respectively).

### 5. Set Pie Chart Parameters
- Create an `explode` list to highlight the top player in the pie chart (set to 0.07 for the top player).
- Format the 'Won%' and 'Lost%' columns as labels with percentages (`label1` and `label2`).

### 6. Create Subplots
- Create a figure with two subplots (`ax1` for win percentages and `ax2` for loss percentages).

### 7. Plot Win Percentage Pie Chart
- Plot the pie chart for 'Won%' using `ax1.pie`, with rotated labels, label distance, and exploded slices.
- Add a legend to the pie chart that lists the players' names using `ax1.legend`.

### 8. Plot Loss Percentage Pie Chart
- Plot the pie chart for 'Lost%' using `ax2.pie`, with the same label rotation and exploded slices.

### 9. Add Title
- Add a title to the figure using `plt.suptitle` to describe the content ("Winning Leadership: Exploring Captains' Win Percentages & Loss Percentages").

### 10. Display Plot
- Display the final plot with `plt.show()`.
## Result
This visualization will showcase two pie charts displaying the win and loss percentages of IPL captains who have played more than 45 matches. The first pie chart will represent the 'Won%' values, with the top player’s slice highlighted to draw attention. The second pie chart will represent the 'Lost%' values, allowing comparison between captains' performances. Both pie charts will include labeled slices showing the percentage of wins and losses, with a legend listing the players' names. The entire figure will have a clear title to explain the analysis, and the layout will be clean and well-organized for easy interpretation of the captains' leadership performance.


## 3.Title: Leading from the Front: Performance of IPL Captains in Matches Won and Lost

## Steps:

### 1. Import Libraries
- Import `pandas` for reading and manipulating data.
- Import `matplotlib.pyplot` for plotting the bar chart.
- Import `numpy` for handling numerical operations (to define the positions of bars).

### 2. Read Data
- Load the IPL captains' data from a CSV file (`captains.csv`) using `pd.read_csv`.

### 3. Filter and Sort Data
- Filter the data to include players who have played more than 45 matches using `df[df['Mat'] > 45]`.
- Sort the data by the number of matches played (`'Mat'`) in ascending order using `sort_values`.

### 4. Extract Relevant Columns
- Extract the 'Player' names, the number of matches played ('Mat'), the number of matches won ('Won'), and the number of matches lost ('Lost') from the DataFrame.

### 5. Set Bar Chart Parameters
- Define the width of the bars (`barwidth = 0.3`).
- Use `np.arange(len(x))` to create the positions for each player on the y-axis.

### 6. Plot Horizontal Bars
- Use `plt.barh()` to create horizontal bars for each category: Matches played (`y`), Matches won (`z`), and Matches lost (`w`).

### 7. Add Text Labels to Bars
- For each of the categories ('Mat', 'Won', 'Lost'), add the corresponding values as text labels inside the bars using `plt.text`.

### 8. Set Labels and Title
- Set the x-axis label to 'No. of Matches, Won, Lost' with a custom font style.
- Set the y-axis label to 'Players' with a custom font style.
- Set the title of the plot as 'Leading from the Front: Performance of IPL Captains in Matches Won and Lost'.

### 9. Add Legend
- Add a legend to distinguish between the different bars: Matches, Won, and Lost.

### 10. Adjust Layout
- Use `plt.subplots_adjust()` to fine-tune the layout and ensure everything fits properly.

### 11. Display Plot
- Use `plt.show()` to display the final plot.

### 12. Save Plot (Optional)
- Optionally, you can save the plot as an image using `plt.savefig('output_image.png')` if needed.
## Result
This visualization will display a horizontal bar chart comparing the IPL captains' performance in terms of the number of matches played, won, and lost. Each player will have three bars representing these values: one for total matches played, one for matches won, and one for matches lost. The bars will be labeled with their respective values, making it easy to interpret each captain's performance. The x-axis will show the number of matches, wins, and losses, while the y-axis will display the players' names. A legend will help distinguish between the different categories, and the chart will have a title for clarity. The layout will be adjusted to ensure proper spacing, making the plot visually clean and informative.


## 4.Title: Total Fifties Scored in IPL Matches by Year (2008-2024)

## Steps:

### 1. Import Libraries
- Import `pandas` to load and manipulate the data.
- Import `matplotlib.pyplot` for plotting the data.

### 2. Load the Data
- Load the IPL dataset of total fifties scored for each year from a CSV file (`list of 50's.csv`).

### 3. Create the Plot
- Create a figure and axis using `plt.subplots()` for better control over plot size and layout.
  
### 4. Define Data
- Set `x` to represent the years (from the 'Year' column) and `y` to represent the total fifties scored (from the 'Total fifties' column).

### 5. Create the Stackplot
- Use `ax1.stackplot()` to plot the data as a stacked area chart, with only one layer for the total fifties.

### 6. Add Title and Labels
- Add a descriptive title to the plot with custom font properties.
- Set the x-axis label to 'Year' and the y-axis label to 'Total Fifties', with custom font properties for clarity.

### 7. Annotate Points
- Annotate each data point with its corresponding total fifties value for easy reference.

### 8. Display the Legend
- Add a legend to the upper left corner of the plot, even though we only have one data series.

### 9. Adjust Layout
- Use `plt.tight_layout()` to automatically adjust the spacing for a clean look.

### 10. Show the Plot
- Display the plot using `plt.show()`, which renders the graph on the screen.
## Result
This visualization will showcase a stacked area chart displaying the total fifties scored in IPL matches from 2008 to 2024. The x-axis will represent the years, while the y-axis will show the total number of fifties scored in each respective year. Even though the chart will consist of a single layer, it will still provide a clear view of the trends over time. Data points will be annotated to highlight the exact number of fifties for each year, making it easy to interpret the values. A legend will be placed in the upper left corner, and the layout will be adjusted for a visually clean appearance. The plot will have a descriptive title and labels for clarity, and will be displayed with plt.show() for final visualization.

## 5.Title: Dominating the Field by Runs in Hundreds: A Player-Wise Breakdown

## Steps:

### 1. Import Libraries
- Import the `pandas` library to work with the data.
- Import `matplotlib.pyplot` for plotting the bar chart.

### 2. Load and Clean Data
- Load the dataset containing IPL player's hundreds data using `pd.read_csv()`.
- Select the relevant columns: 'Player', 'total hundreds', and 'total runs by 100s'.
- Remove duplicate entries to ensure data consistency.
- Filter the dataset to include only players who have scored more than 1 hundred.

### 3. Data Sorting
- Sort the dataset in descending order based on the 'total runs by 100s' column to highlight players with the most runs scored from hundreds.

### 4. Data Preparation for Plotting
- Prepare the `x`, `y`, and `z` variables for plotting:
  - `x` contains the player names.
  - `y` contains the number of hundreds each player has scored.
  - `z` contains the total runs scored by each player from their hundreds.

### 5. Create Bar Chart
- Use `plt.bar()` to create a bar plot where the x-axis represents the players and the y-axis represents the number of hundreds scored.
- Customize the colors of the bars by creating a color list using `plt.cm.BrBG`.
- Set the color of each bar by iterating over the bars and applying a color from the list.

### 6. Annotate the Bars
- Annotate each bar with the total runs scored from hundreds using `plt.text()`.

### 7. Customize the Plot
- Rotate the x-axis labels by 45 degrees to ensure they are readable.
- Add a title to the plot and customize the font size and family.
- Set labels for both the x-axis and y-axis with customized font size and color.

### 8. Adjust Layout
- Adjust the layout of the plot using `plt.subplots_adjust()` to ensure everything fits neatly.

### 9. Display the Plot
- Finally, display the plot using `plt.show()`.
## Result
This visualization will present a bar chart displaying a player-wise breakdown of hundreds scored in IPL matches. Each bar represents a player, with the x-axis showing the players' names and the y-axis representing the number of hundreds they have scored. The bars will be colored using a custom palette, and each bar will be annotated with the total number of runs scored from those hundreds, offering a clear understanding of the players' performances. The x-axis labels will be rotated for better readability. A title and axis labels will be included with customized font properties to enhance the clarity and aesthetics. Finally, the layout will be adjusted for a neat appearance and the plot will be shown with plt.show() for the final display.

## 6.Title: Historical Performance: Total Fours & Sixes by Year

## Steps:

### 1. Import Libraries
- Import the `pandas` library to work with the data.
- Import `matplotlib.pyplot` for plotting the graph.

### 2. Load the Datasets
- Load the dataset for total fours and total sixes by year using `pd.read_csv()`.

### 3. Create the Plot
- Use `plt.subplots()` to create a figure and axis for plotting the data.
- Define `x` (Year), `y` (Total Fours), and `z` (Total Sixes) for the respective plots.

### 4. Plot Total Fours
- Use `ax1.plot()` to plot total fours by year on the first y-axis (`ax1`).
- Customize the color, marker style, and line width for the plot.
- Set the x-axis label, y-axis label, and add a legend for the total fours data.

### 5. Plot Total Sixes on a Secondary y-Axis
- Use `ax1.twinx()` to create a second y-axis (`ax2`) for plotting total sixes by year.
- Use `ax2.plot()` to plot total sixes with custom styling.
- Set the secondary y-axis label and add a legend for the total sixes data.

### 6. Adjust Layout and Title
- Adjust the plot layout for better spacing using `plt.subplots_adjust()`.
- Add a title to the plot using `plt.title()`.

### 7. Display the Plot
- Finally, display the plot using `plt.show()`.
## Result
This visualization will feature a line chart showing the historical performance of total fours and sixes by IPL teams across different years. The x-axis will represent the years, while the left y-axis will show the total fours hit, and the right y-axis will display the total sixes hit. Two distinct lines will be plotted: one for total fours and another for total sixes, each with unique colors and markers for clarity. Legends will be added to differentiate between the two data series. The plot will be adjusted for optimal spacing, and a title will be added to give context to the data. Finally, the plot will be displayed with plt.show().

## 7.Title: Historical Performance: Total Runs & Wickets by Year

## Steps:

### 1. Import Libraries
- Import the `pandas` library to handle the data.
- Import `matplotlib.pyplot` to create the plot.

### 2. Load the Datasets
- Load the dataset for total runs and total wickets by year using `pd.read_csv()`.

### 3. Create the Plot
- Use `plt.subplots()` to create a figure and axis for plotting the data.
- Define `x` (Year), `y` (Total Runs), and `z` (Total Wickets) for the respective plots.

### 4. Plot Total Runs
- Use `ax1.plot()` to plot total runs by year on the first y-axis (`ax1`).
- Customize the color, marker style, and line width for the plot.
- Set the x-axis label, y-axis label, and add a legend for the total runs data.

### 5. Plot Total Wickets on a Secondary y-Axis
- Use `ax1.twinx()` to create a second y-axis (`ax2`) for plotting total wickets by year.
- Use `ax2.plot()` to plot total wickets with custom styling.
- Set the secondary y-axis label and add a legend for the total wickets data.

### 6. Adjust Layout and Title
- Adjust the plot layout for better spacing using `plt.subplots_adjust()`.
- Add a title to the plot using `plt.title()`.

### 7. Display the Plot
- Finally, display the plot using `plt.show()`.
## Result
This visualization will feature a dual-line chart displaying the historical performance of total runs and total wickets by IPL teams across various years. The x-axis will represent the years, while the left y-axis will indicate the total runs scored, and the right y-axis will show the total wickets taken. Two separate lines will be plotted: one for total runs and another for total wickets, each with distinct colors and markers for clarity. Legends will be added to differentiate between the two data series. The layout will be adjusted to ensure the plot is well-spaced, and a title will be included to provide context. The plot will be displayed with plt.show() for easy interpretation.



## 8.Title: Top Umpires with 50+ Matches in IPL

## Steps to Create the Visualization:

### 1. Import Libraries
- Import `pandas` for data manipulation, `matplotlib.pyplot` for plotting, and `numpy` for handling arrays and color generation.

### 2. Load and Process Data
- Load the data from the CSV file (`list of umpires.csv`) using `pandas.read_csv()`.
- Filter out umpires who have officiated in fewer than 50 matches using `df[df['Matches'] >= 50]`.
- Sort the remaining umpires by the number of matches (`sort_values(by='Matches')`).

### 3. Extract Data
- Extract the umpire names (`UmpireName`) and the number of matches (`Matches`) into variables `x` and `y`, respectively.

### 4. Generate Colors for Bars
- Use `plt.cm.tab20` to generate a color map for the bars. The color map will dynamically assign a unique color to each umpire based on their order in the list.

### 5. Create Horizontal Bar Plot
- Use `plt.barh()` to create a horizontal bar plot where `x` represents umpire names and `y` represents the number of matches.
- Set the bar colors using the `colors` array created in the previous step.

### 6. Customize the Plot
- Add a title, axis labels, and a grid to make the plot more readable and aesthetically pleasing.
- Adjust the labels to display the number of matches on the right side of each bar using `plt.text()`.

### 7. Display the Plot
- Finally, adjust the layout to prevent overlapping text and show the plot with `plt.tight_layout()` and `plt.show()`.

### Result
This visualization shows the top umpires who have officiated in 50 or more IPL matches, sorted by the number of matches they have officiated. The bars are color-coded, and each bar is labeled with the exact number of matches.


## 9.Title: Visualizing IPL Purple Cap Winners: Pie Chart and Table Analysis

## Steps:

### 1. Load the Data  
Load the CSV file containing data on IPL Purple Cap winners into a pandas DataFrame for analysis.

### 2. Group Data by Winner  
Group the data by the 'Winner' column and count occurrences, representing the number of times each player has won the Purple Cap.

### 3. Prepare Data for Plotting  
Extract player names and their respective win counts for use in visualization.

### 4. Generate Colors for Visualization  
Use a colormap to assign unique colors to each player, creating a color map to differentiate players in the visualization.

### 5. Create Figure and Subplots  
Set up a figure with two subplots: one for the pie chart and one for the table, displaying the data in complementary formats.

### 6. Plot the Pie Chart  
Draw a pie chart to show the distribution of Purple Cap wins among players, formatting labels to show percentages and customizing the chart to appear as a donut.

### 7. Create the Data Table  
Create a table on the second subplot to show player names and their win counts. Customize cell colors to match the pie chart for visual consistency.

### 8. Customize and Display Plot  
Adjust the layout, hide unnecessary axes, and add a title to the figure for clarity.

### 9. Show the Plot  
Display the final plot, including both the pie chart and table, to provide a clear visualization of Purple Cap win distributions across players.
## Result
This visualization will feature a combination of a pie chart and a table to analyze IPL Purple Cap winners. The pie chart will display the distribution of Purple Cap wins among players, with each slice representing a player and their respective win count, formatted as a donut chart. Each player will have a distinct color assigned, making the chart visually appealing and easy to interpret.

Below the pie chart, a table will list the players and the number of times they’ve won the Purple Cap, with rows color-coded to match the pie chart for consistency. The layout will be adjusted to ensure both the pie chart and table fit well together, and the plot will be titled for clarity. The plot will be displayed using plt.show(), presenting both the pie chart and table for a comprehensive understanding of the Purple Cap winners.

## 10.Title: Total Sixes by Team and Year in IPL (2018-2024)

## Steps:

### 1. Load the Data  
Read the CSV file containing IPL team sixes data into a pandas DataFrame for analysis.

### 2. Pivot the Data for Plotting  
Pivot the data so that the 'Year' becomes columns, 'Team' becomes the index, and '6s' becomes the values for each year.

### 3. Plot the Bar Chart  
Plot the pivoted data as a bar chart to visualize total sixes hit by each team over the years.

### 4. Adding Labels and Title  
Add a title to the chart, and labels for the x-axis (Team) and y-axis (Total 6's).

### 5. Customize x-axis and Legend  
Rotate the x-axis labels for better readability, and position the legend appropriately with a title for the years.

### 6. Adjust Subplot Margins  
Make adjustments to subplot margins for better presentation.

### 7. Display the Plot  
Use `tight_layout` to ensure proper fitting of the chart and then display the plot.
## Result
This visualization will display a bar chart representing the total sixes hit by each IPL team across the years 2018-2024. The data will be organized by first pivoting the DataFrame, with 'Year' as columns, 'Team' as the index, and '6s' as the values. This pivoted data will then be plotted as a bar chart, where each bar represents the total sixes hit by a team for a given year.

The chart will include a title, and the x-axis will display the team names while the y-axis will show the total number of sixes. The x-axis labels will be rotated for better readability, and the legend will be placed appropriately with a title indicating the years.

Subplot margins will be adjusted for clarity, and the layout will be fine-tuned using tight_layout to ensure everything fits neatly. The plot will be displayed using plt.show() to provide a clear and visually informative representation of the data.


## 11.Title: Toss and Triumph: Exploring Wins and Losses of IPL Teams

## Steps:

### 1. Load the Data  
Read the CSV file containing IPL team toss and match results data into a pandas DataFrame for analysis.

### 2. Create Team Initials  
Generate a new column 'initials' by extracting the first letter of each word in the team name to make it suitable for display in the chart.

### 3. Sort the Data  
Sort the data by 'Mat' (Matches) in descending order to arrange the teams in a visually ordered manner.

### 4. Extract Data for Plotting  
Extract the relevant columns (`Team initials`, `Matches`, `Won`, `Lost`) for plotting purposes.

### 5. Create the Plot  
Create a bar chart in a single subplot to compare the matches played, wins, and losses of each IPL team.

### 6. Set Bar Width and Index  
Define the width of the bars and the index for each team, allowing the bars to be grouped together.

### 7. Plot the Data  
Plot three different bars for each team: one for the total matches played, one for wins, and one for losses.

### 8. Add Text Annotations  
Add text annotations to each bar to display the exact value for Matches, Wins, and Losses.

### 9. Customize the Plot  
Add labels for the x-axis and y-axis, rotate the x-axis labels, and set a title for the chart.

### 10. Adjust Layout and Show Plot  
Adjust the subplot margins for better spacing and display the final chart with a legend.
## Result
This visualization presents a bar chart comparing the performance of IPL teams in terms of matches played, wins, and losses. Each team is represented by three bars: one for the total matches played, one for wins, and one for losses. The teams are sorted by the number of matches played, and each bar is annotated with the exact values for clarity. The chart includes customized labels for the x-axis and y-axis, rotated x-axis labels for better readability, and a legend to distinguish between the categories. The title "Toss and Triumph: Exploring Wins and Losses of IPL Teams" is displayed, with the layout adjusted for optimal presentation, and the plot is shown using plt.show().

## 12.Title: Toss and Triumph: Exploring Wins and Losses of IPL Teams

## Steps:

### 1. Load the Data  
Read the CSV file containing IPL team toss and match results data into a pandas DataFrame for analysis.

### 2. Create Team Initials  
Generate a new column 'initials' by extracting the first letter of each word in the team name to make it suitable for display in the chart.

### 3. Sort the Data  
Sort the data by 'Mat' (Matches) in descending order to arrange the teams in a visually ordered manner.

### 4. Extract Data for Plotting  
Extract the relevant columns (`Team initials`, `Matches`, `Won`, `Lost`) for plotting purposes.

### 5. Create the Plot  
Create a bar chart in a single subplot to compare the matches played, wins, and losses of each IPL team.

### 6. Set Bar Width and Index  
Define the width of the bars and the index for each team, allowing the bars to be grouped together.

### 7. Plot the Data  
Plot three different bars for each team: one for the total matches played, one for wins, and one for losses.

### 8. Add Text Annotations  
Add text annotations to each bar to display the exact value for Matches, Wins, and Losses.

### 9. Customize the Plot  
Add labels for the x-axis and y-axis, rotate the x-axis labels, and set a title for the chart.

### 10. Adjust Layout and Show Plot  
Adjust the subplot margins for better spacing and display the final chart with a legend.
## Result
The "Toss and Triumph: Exploring Wins and Losses of IPL Teams" chart visualizes the performance of IPL teams by showing three grouped bars for each team: one for the total matches played, one for wins, and one for losses. The data is sorted by the number of matches played, with each team's initials generated for easier display. The bars are annotated with exact values for clarity, and the plot includes rotated x-axis labels for readability and a legend for better understanding. Custom labels for the x-axis and y-axis, along with a descriptive title, ensure the plot is informative. Finally, the layout is adjusted for a clean presentation and the chart is displayed using plt.show().

## 13.Title: Proportion of Total Players in IPL by Year

## Steps:

### 1. Load the Data  
Read the CSV file containing the IPL total players data into a pandas DataFrame for analysis.

### 2. Create the Figure  
Create a figure and axis for the pie chart with a specified figure size to adjust the visual appearance.

### 3. Extract Data for Plotting  
Extract the 'Year' and 'Total Players' columns from the DataFrame, which will be used as labels and values in the pie chart.

### 4. Define a Function for Label Formatting  
Define a function to format the pie chart labels. The function will display both the absolute value (total players) and the percentage for each segment.

### 5. Create the Pie Chart  
Generate the pie chart using the extracted data, applying the custom label formatting and choosing a color palette for better visualization.

### 6. Add a Title  
Add a descriptive title to the chart, specifying the font size, color, and family for consistency.

### 7. Show the Plot  
Ensure the pie chart is displayed as a circle by setting the aspect ratio to equal, and adjust the layout for better presentation. Finally, display the plot.
## Result
The "Proportion of Total Players in IPL by Year" pie chart visualizes the distribution of total players across different IPL years. The data is extracted from the 'Year' and 'Total Players' columns of the dataset, with a custom function used to format the pie chart labels to show both the absolute values and percentages for each segment. The chart is created with a specified color palette for clarity and is accompanied by a descriptive title, ensuring consistent font size, color, and family. The aspect ratio is set to equal for a circular appearance, and the layout is adjusted for optimal presentation, followed by displaying the plot using plt.show().
