import time
import pandas as pd
import numpy as np
import calendar

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

MONTHS = ['all'] + [month.lower() for month in calendar.month_name[1:7]]
DAYS = ['all'] + [day.lower() for day in calendar.day_name]


def search_by():
        # Prompts user to specify a city, month, and day to analyze
    while True:
        city = input("Enter city (Chicago, New York City, Washington): ").casefold()
        if city in CITY_DATA:
            break
        print("Invalid city. Please try again.")

    while True:
        month = input("Enter month (January to June) or 'all': ").strip().lower()
        if month in MONTHS:
            break
        print("Invalid month. Please try again.")

    while True:
        day = input("Enter day of week or 'all': ").strip().lower()
        if day in DAYS:
            break
        print("Invalid day. Please try again.")

    print("-" * 50)
    return city, month, day


def load_data(city, month, day):
        # Loads data for the specified city and filters by month and day if applicable
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()

    if month != 'all':
        month_index = MONTHS.index(month)
        df = df[df['month'] == month_index]

    if day != 'all':
        df = df[df['day_of_week'] == day]

    return df


def times_of_travel(df):
        # Displays the most frequent month, day, and hour of travel
    print("\n📅 Most Frequent Times of Travel")

    popular_month = int(df['month'].mode()[0])
    print(f"  Most Popular Month: {calendar.month_name[popular_month]}")

    popular_day = df['day_of_week'].mode()[0].title()
    print(f"  Most Popular Day: {popular_day}")

    df['hour'] = df['Start Time'].dt.hour
    popular_hour = int(df['hour'].mode()[0])
    print(f"  Most Popular Start Hour: {popular_hour}:00")

    print("-" * 50)


def popular_stations(df):
        # Identifies the most commonly used start station, end station, and trip combination
    print("\n🚏 Most Popular Stations and Trip")

    print(f"  Most Popular Start Station: {df['Start Station'].mode()[0]}")
    print(f"  Most Popular End Station: {df['End Station'].mode()[0]}")

    combo = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print(f"  Most Frequent Trip: {combo[0]} → {combo[1]}")

    print("-" * 50)


def trip_duration(df):
              # Calculates and displays total and average trip durations
    print("\n🛣️ Trip Duration Stats")

    total_duration = int(np.sum(df['Trip Duration']))
    avg_duration = int(np.mean(df['Trip Duration']))

    print(f"  Total Trip Duration: {total_duration // 3600} hours, {(total_duration % 3600) // 60} minutes")
    print(f"  Average Trip Duration: {avg_duration // 60} minutes")


    print("-" * 50)


def user_info(df):
              # Displays counts of user types, gender distribution, and birth year statistics (if available)
    print("\n👥 User Stats")

    print("  User Types:")
    for user_type, count in df['User Type'].value_counts().items():
        print(f"    {user_type}: {count}")

    if 'Gender' in df.columns:
        print("\n  Gender Distribution:")
        for gender, count in df['Gender'].value_counts().items():
            print(f"    {gender}: {count}")

    if 'Birth Year' in df.columns:
        print("\n  Birth Year Statistics:")
        print(f"    Earliest: {int(df['Birth Year'].min())}")
        print(f"    Most Recent: {int(df['Birth Year'].max())}")
        print(f"    Most Common: {int(df['Birth Year'].mode()[0])}")

    print("-" * 50)

def display_raw_data(df):
    #Displays raw data 5 rows at a time upon user request
    index = 0
    while True:
        show_data = input("Would you like to see 5 lines of raw data? Enter yes or no: ").strip().lower()
        if show_data == 'yes':
            print(df.iloc[index:index+5])
            index += 5
            if index >= len(df):
                print("No more data to display.")
                break
        elif show_data == 'no':
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")



def main():
    while True:
        city, month, day = search_by()
        df = load_data(city, month, day)

        times_of_travel(df)
        trip_duration(df)
        popular_stations(df)
        user_info(df)
        display_raw_data(df)


if __name__ == "__main__":
    main()
