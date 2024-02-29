import os,platform
import pandas as pd
import matplotlib.pyplot as plt


if platform.system() == 'Windows':
        os.system('cls')
else:
        os.system('clear')

        
excel_file = r'C:\Users\leeji\OneDrive\Desktop\(3) SQIT3073 (A) Business Analytic Programming\Python Programme\A231 SQIT3073 GA 1\GA1_Chart_4.1_Data.xlsx'

# Read extracted table from xlsx file
data = pd.read_excel(excel_file, sheet_name="Sheet1")
df = pd.DataFrame(data)

# Convert 'Period' to string and concatenate with 'Quarter'
df['PeriodQuarter'] = df['Period'].astype(str) + ' ' + df['Quarter']

# Plotting the GDP growth rate over time
plt.figure(figsize=(16, 6))
plt.plot(df['PeriodQuarter'], df['Gross Domestic Product (GDP)'], marker='o', linestyle='-')

# Adding a red line at y=0
plt.axhline(y=0, color='red', linestyle='--')


# Loop through the data points and plot, marking negative values in red
for i, value in enumerate(df['Gross Domestic Product (GDP)']):
    if value < 0:
        plt.plot(df['PeriodQuarter'][i], value, marker='o', linestyle='-', color='red')
    else:
        plt.plot(df['PeriodQuarter'][i], value, marker='o', linestyle='-', color='blue')


# Adjust the data labels
    plt.annotate(f'{value:.2f}', (df['PeriodQuarter'][i], value),
                 textcoords="offset points", xytext=(1, 5 if value > 0 else -15), ha='center')



# Customize the plot
plt.title('Quarterly YoY GDP Growth Rate')
plt.xlabel('Period')
plt.ylabel('GDP Growth Rate (%)')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.grid(True)

# Display the plot
plt.tight_layout()
plt.show()