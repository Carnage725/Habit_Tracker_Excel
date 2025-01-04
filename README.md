# Habit Tracker Project

## Overview
This project provides a habit-tracking system using Excel templates and Python scripts to analyze and visualize daily habit completion. Users can customize their habits, generate monthly templates, and review their progress with automated visualizations.

---

## Features
1. **Customizable Habit Templates**:
   - Define the number of habits and their names.
   - Automatically generate monthly Excel files with daily tracking sheets.

2. **Data Analysis and Visualization**:
   - Analyze daily habit completion data.
   - Generate bar charts for each month showing habit completion trends.

3. **Organized Directory Structure**:
   - `templates_output/` contains all generated Excel templates.
   - `charts_output/` contains all generated monthly bar charts.

---

## Project Structure

```plaintext
Habit_Tracker/
|-- create_templates.py       # Script to generate Excel templates
|-- analyze_habits.py         # Script to process and visualize data
|-- README.md                 # Project documentation
|-- templates_output/         # Directory for generated Excel templates
|-- charts_output/            # Directory for generated monthly charts
```

---

## Requirements

### **Python Libraries**
Install the required libraries using `pip`:
```bash
pip install openpyxl pandas matplotlib
```

---

## Usage

### 1. Generate Habit Tracking Templates
Run the `create_templates.py` script to create monthly habit-tracking templates:
```bash
python create_templates.py
```
- The script prompts you to:
  - Enter the number of habits.
  - Define habit names.
- Templates are saved in the `templates_output/` folder.

### 2. Fill in the Templates
- Open the Excel files in the `templates_output/` folder (e.g., `January.xlsx`).
- For each day, mark habits as "Y" (Yes) or "N" (No) in the `Completed? (Y/N)` column.

### 3. Analyze and Visualize Habits
Run the `analyze_habits.py` script to process the templates and generate charts:
```bash
python analyze_habits.py
```
- The script reads data from `templates_output/` and saves charts in the `charts_output/` folder.

---

## Outputs

### **Excel Templates** (`templates_output/`)
- Monthly Excel files for tracking habits (e.g., `January.xlsx`, `February.xlsx`, ...).

### **Monthly Charts** (`charts_output/`)
- Bar charts visualizing daily habit completion for each month (e.g., `January_Habits_Graph.png`).

---

## Example Workflow

1. **Create Templates**:
   - Input: Number of habits and their names.
   - Output: Excel templates for all 12 months.

2. **Fill Templates**:
   - Record daily habit completion in the generated Excel files.

3. **Analyze and Generate Charts**:
   - Input: Completed Excel templates.
   - Output: Bar charts for habit completion trends.

---

## Future Improvements
- Add support for multiple years.
- Include percentage-based analysis for overall habit adherence.
- Implement a web-based interface for better usability.


