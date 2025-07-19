
# Bikeshare Data Analysis
This project analyzes bikeshare data for three major US cities: Chicago, New York City, and Washington. The script allows users to explore various statistics about bikeshare trips, including popular travel times, station usage, trip durations, and user demographics.

## Features
Interactive Data Filtering: Filter data by city, month (January to June), and day of the week.

## Trip Statistics:

Most frequent month, day, and hour of travel.

Most popular start and end stations.

Most frequent trip combinations (start and end stations).

Total and average trip durations.

## User Statistics:

Counts of different user types (e.g., Subscribers, Customers).

Gender distribution (if available in the dataset).

Birth year statistics (earliest, most recent, and most common birth year, if available).

Raw Data Display: Option to view raw trip data in chunks of 5 rows.

## How to Run
Prerequisites:

Python 3.x installed.

pandas, numpy, and calendar libraries. You can install pandas and numpy using pip:

Bash

pip install pandas numpy
Data Files:

Ensure you have the bikeshare data files (chicago.csv, new_york_city.csv, washington.csv) in the same directory as the script. These files are not included in this repository and need to be obtained separately.

Run the Script:

Bash

python bikeshare_analysis.py
Usage
Upon running the script, you will be prompted to:

Enter a city: Choose from 'Chicago', 'New York City', or 'Washington'.

Enter a month: Specify a month from January to June (e.g., 'january', 'february') or 'all' to include all months.

Enter a day: Specify a day of the week (e.g., 'monday', 'tuesday') or 'all' to include all days.

After your selections, the script will display the requested statistics. You will also have an option to view raw data.

## Example Interaction:
![image](https://github.com/user-attachments/assets/265bc1c2-2de9-465a-a42d-2ad46e0e594d)

 ## Project Structure
bikeshare_analysis.py: The main Python script containing all the functions for data loading, analysis, and display.

chicago.csv, new_york_city.csv, washington.csv: (Not included, assumed to be present) CSV files containing the bikeshare data for each city.

## Future Enhancements
Visualization: Integrate data visualization libraries (e.g., Matplotlib, Seaborn) to create charts and graphs for better insights into the data.

More Cities: Expand the analysis to include bikeshare data from additional cities, making the tool more versatile.

Advanced Filtering Options: Add more sophisticated filtering options, such as filtering by specific time ranges within a day, or by age groups for user demographics.

API Integration: Explore integrating with bikeshare APIs to fetch real-time data or more up-to-date datasets.

Error Handling Improvements: Enhance error handling for user inputs to provide more robust and user-friendly feedback.
