import pandas as pd
import os
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import numpy as np

# Clear the console
os.system("cls")

# Replace the directory with the correct path to your Excel file
data = pd.read_excel(r"C:\Users\leeji\OneDrive\Desktop\(3) SQIT3073 (A) Business Analytic Programming\Python Programme\A231 SQIT3073 GA 1\GA1_Chart_4.2_Data.xlsx",sheet_name="Sheet1")

# Read the Excel file into a DataFrame
df = pd.DataFrame(data)

# Extract data for x and y axes
col_names = list(df['Period'])
y1_data = list(df['Agriculture'])
y2_data = list(df['Mining and Quarrying'])
y3_data = list(df['Manufacturing'])
y4_data = list(df['Construction'])
y5_data = list(df['Services'])
y6_data = list(df['Import Duties'])

# Create a stacked area chart
fig, ax = plt.subplots(figsize=(14, 6))
ax.stackplot(col_names, y1_data, y2_data, y3_data, y4_data, y5_data, y6_data, labels = ['Agriculture', 'Mining and Quarrying', 'Manufacturing', 'Construction', 'Services', 'Import Duties'])

# Update axis labels and title
ax.set_xlabel('Period', fontsize=16)
ax.set_ylabel('RM million', fontsize=16)
ax.set_title('Gross Domestic Product by Kind of Economic Activity')

# Set y-axis limits
plt.yticks(range(0, 1700000, 200000))

# Use ScalarFormatter to force integer formatting for y-axis ticks
ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax.ticklabel_format(style='plain', axis='y')

# Add total labels for each year
for year, y1, y2, y3, y4, y5, y6, total_value in zip(col_names, y1_data, y2_data, y3_data, y4_data, y5_data, y6_data, df['SUM']):
    plt.text(year, total_value + 1, f"{int(total_value)}", ha='center', va='bottom', color='black')

# Add dotted lines after each year
for year in col_names[0:]:
    plt.axvline(x=year, color='black', linestyle='dashed', linewidth=1, dashes=(10, 15))

# Display legend
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=12).set_draggable(True)

# Adjust layout to prevent clipping
plt.tight_layout()

# Show the chart
plt.show()