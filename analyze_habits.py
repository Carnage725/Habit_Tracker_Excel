import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import os

# Define months and corresponding file names
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

# Input and output folder paths
input_folder = "templates_output"
output_folder = "charts_output"
os.makedirs(output_folder, exist_ok=True)

# Loop through each month and process its file
for month in months:
    file_path = os.path.join(input_folder, f"{month}.xlsx")
    try:
        xl = pd.ExcelFile(file_path)

        # Initialize a dictionary to store completion counts for the month
        daily_habit_data = {}

        # Process each daily sheet
        for sheet_name in xl.sheet_names:
            if sheet_name.startswith("Day"):
                df = xl.parse(sheet_name)

                # Convert the 'Completed? (Y/N)' column to string to avoid errors
                if 'Completed? (Y/N)' in df.columns:
                    df['Completed? (Y/N)'] = df['Completed? (Y/N)'].astype(str)
                    completed_count = df['Completed? (Y/N)'].str.upper().value_counts().get('Y', 0)
                else:
                    completed_count = 0  # Handle missing column case

                day = int(sheet_name.split()[1])
                daily_habit_data[day] = completed_count

        # Convert to DataFrame for easy plotting
        daily_data_df = pd.DataFrame(list(daily_habit_data.items()), columns=['Day', 'Completed Habits'])
        daily_data_df.sort_values(by="Day", inplace=True)

        # Plot the data for the current month
        plt.figure(figsize=(10, 6))
        plt.bar(daily_data_df['Day'], daily_data_df['Completed Habits'], color='skyblue', edgecolor='black')
        plt.title(f"{month} Habit Completion", fontsize=16)
        plt.xlabel("Day", fontsize=14)
        plt.ylabel("Completed Habits", fontsize=14)
        plt.xticks(range(1, len(daily_data_df) + 1))  # Ensure x-axis shows all days
        plt.gca().yaxis.set_major_locator(mticker.MaxNLocator(integer=True))  # Force y-axis to use integer ticks
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()

        # Save the chart as an image in the output folder
        chart_filename = os.path.join(output_folder, f"{month}_Habits_Graph.png")
        plt.savefig(chart_filename)
        plt.close()
        print(f"Chart saved as {chart_filename}")

    except FileNotFoundError:
        print(f"File {file_path} not found. Skipping {month}.")
    except Exception as e:
        print(f"An error occurred while processing {month}: {e}")
