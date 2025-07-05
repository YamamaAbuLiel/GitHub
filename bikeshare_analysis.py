import time
import pandas as pd
import numpy as np
import calendar

# Global constants for data and filter options
CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

MONTHS = ['all'] + [month.lower() for month in calendar.month_name[1:7]]
DAYS = ['all'] + [day.lower() for day in calendar.day_name]


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str, str, str): city, month, and day filters.
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # Get user input for city (chicago, new york city, washington).
    while True:
        city = input("Enter city (Chicago, New York City, Washington): ").casefold()
        if city in CITY_DATA:
            break
        print("Invalid city. Please try again.")

    # Get user input for month (all, january, february, ... , june)
    while True:
        month = input("Enter month (January to June) or 'all': ").strip().lower()
        if month in MONTHS:
            break
        print("Invalid month. Please try again.")

    # Get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Enter day of week or 'all': ").strip().lower()
        if day in DAYS:
            break
        print("Invalid day. Please try again.")

    print('-'*50)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        city (str): Name of the city to analyze.
        month (str): Name of the month to filter by, or "all" to apply no month filter.
        day (str): Name of the day of week to filter by, or "all" to apply no day filter.

    Returns:
        pandas.DataFrame: Filtered bikeshare data.
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month, day of week, and hour from Start Time
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()
    df['hour'] = df['Start Time'].dt.hour

    # Filter by month if applicable
    if month != 'all':
        # Use the index of the month name to get the corresponding integer month
        month_index = MONTHS.index(month)
        df = df[df['month'] == month_index]

    # Filter by day of week if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """
    Displays statistics on the most frequent times of travel.

    Args:
        df (pandas.DataFrame): Filtered bikeshare data.
    """
    print('\n📅 Most Frequent Times of Travel:\n')
    start_time = time.time()

    if df.empty:
        print("No data available for the selected filters to calculate time statistics.")
        return

    popular_month = int(df['month'].mode()[0])
    popular_day = df['day_of_week'].mode()[0].title()
    popular_hour = int(df['hour'].mode()[0])

    data = {
        "Statistic": ["Most Popular Month", "Most Popular Day", "Most Popular Start Hour"],
        "Value": [calendar.month_name[popular_month], popular_day, f"{popular_hour}:00"]
    }
    print(pd.DataFrame(data).to_markdown(index=False))
    print(f"\n(Calculated in {time.time() - start_time:.2f} seconds)")
    print('-'*50)


def station_stats(df):
    """
    Displays statistics on the most popular stations and trip.

    Args:
        df (pandas.DataFrame): Filtered bikeshare data.
    """
    print('\n🚏 Most Popular Stations and Trip:\n')
    start_time = time.time()

    if df.empty:
        print("No data available for the selected filters to calculate station statistics.")
        return

    popular_start_station = df['Start Station'].mode()[0]
    popular_end_station = df['End Station'].mode()[0]

    # Check for empty dataframe before attempting to group for combined trips
    if not df.empty:
        combo = df.groupby(['Start Station', 'End Station']).size().idxmax()
        most_frequent_trip = f"{combo[0]} → {combo[1]}"
    else:
        most_frequent_trip = "N/A (No data for this filter combination)"


    data = {
        "Statistic": ["Most Popular Start Station", "Most Popular End Station", "Most Frequent Trip"],
        "Value": [popular_start_station, popular_end_station, most_frequent_trip]
    }
    print(pd.DataFrame(data).to_markdown(index=False))
    print(f"\n(Calculated in {time.time() - start_time:.2f} seconds)")
    print('-'*50)


def trip_duration_stats(df):
    """
    Displays statistics on the total and average trip duration.

    Args:
        df (pandas.DataFrame): Filtered bikeshare data.
    """
    print('\n🛣️ Trip Duration Stats:\n')
    start_time = time.time()

    if df.empty:
        print("No data available for the selected filters to calculate trip duration statistics.")
        return

    total_duration = int(np.sum(df['Trip Duration']))
    avg_duration = int(np.mean(df['Trip Duration']))

    # Convert total_duration to hours, minutes, seconds for better readability
    total_hours = total_duration // 3600
    total_minutes = (total_duration % 3600) // 60
    total_seconds = total_duration % 60

    # Convert average_duration to minutes, seconds for better readability
    avg_minutes = avg_duration // 60
    avg_seconds = avg_duration % 60

    data = {
        "Statistic": ["Total Trip Duration", "Average Trip Duration"],
        "Value": [
            f"{total_hours} hours, {total_minutes} minutes, {total_seconds} seconds",
            f"{avg_minutes} minutes, {avg_seconds} seconds"
        ]
    }
    print(pd.DataFrame(data).to_markdown(index=False))
    print(f"\n(Calculated in {time.time() - start_time:.2f} seconds)")
    print('-'*50)


def user_stats(df):
    """
    Displays statistics on bikeshare users.

    Args:
        df (pandas.DataFrame): Filtered bikeshare data.
    """
    print('\n👥 User Stats:\n')
    start_time = time.time()

    if df.empty:
        print("No data available for the selected filters to calculate user statistics.")
        return

    # Display counts of user types
    user_type_counts = df['User Type'].value_counts()
    user_type_data = [{"User Type": user_type, "Count": count} for user_type, count in user_type_counts.items()]
    print("User Types:")
    print(pd.DataFrame(user_type_data).to_markdown(index=False))
    print("\n")

    # Display gender distribution (if 'Gender' column exists)
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        gender_data = [{"Gender": gender, "Count": count} for gender, count in gender_counts.items()]
        print("Gender Distribution:")
        print(pd.DataFrame(gender_data).to_markdown(index=False))
        print("\n")
    else:
        print("Gender data not available for this city.\n")

    # Display birth year statistics (if 'Birth Year' column exists and has non-null values)
    if 'Birth Year' in df.columns and not df['Birth Year'].isnull().all():
        birth_year_data = {
            "Statistic": ["Earliest Birth Year", "Most Recent Birth Year", "Most Common Birth Year"],
            "Value": [
                int(df['Birth Year'].min()),
                int(df['Birth Year'].max()),
                int(df['Birth Year'].mode()[0])
            ]
        }
        print("Birth Year Statistics:")
        print(pd.DataFrame(birth_year_data).to_markdown(index=False))
    else:
        print("Birth Year data not available for this city.\n")

    print(f"\n(Calculated in {time.time() - start_time:.2f} seconds)")
    print('-'*50)

def display_raw_data(df):
    """
    Displays raw data 5 rows at a time upon user request.

    Args:
        df (pandas.DataFrame): Filtered bikeshare data.
    """
    if df.empty:
        print("No raw data to display for the selected filters.")
        print('-'*50)
        return

    index = 0
    while True:
        show_data = input("Would you like to see 5 lines of raw data? Enter yes or no: ").strip().lower()
        if show_data == 'yes':
            if index < len(df):
                # Using .to_markdown(index=False) for consistent table formatting
                print(df.iloc[index:index+5].to_markdown(index=False))
                index += 5
            else:
                print("No more data to display.")
                break
        elif show_data == 'no':
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
    print('-'*50)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        # Offer to save the filtered data for external analysis (e.g., Tableau)
        save_data_prompt = input("Do you want to save the filtered data to a CSV file for external analysis (e.g., Tableau)? (yes/no): ").strip().lower()
        if save_data_prompt == 'yes':
            output_filename = f"{city.replace(' ', '_')}_{month}_{day}_bikeshare_data.csv"
            df.to_csv(output_filename, index=False)
            print(f"\nFiltered data saved to '{output_filename}'. You can now use this file in Tableau or other tools.")
            print('-'*50)
        elif save_data_prompt != 'no':
            print("Invalid input. Skipping saving data.")
            print('-'*50)

        # Proceed with displaying statistics
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart the analysis? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()