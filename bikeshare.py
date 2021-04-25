import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # take choosen city from user 
    while True:
        city = input("Which city from those three cities chicago, new york city and washington, you want to see its data?\n").lower()
        if city == "chicago" or city == "new york city" or city == "washington" :
            break
    # asking for specified filter of month or no filter
    while True:
        month = input("Which month would you want to filter the data? please choose january, february, march, april, may, june or all\n")
        if month == "january" or month == "february" or month == "march" or month == "april" or month == "may" or month == "june" or month == "all" :
            break
    # asking for specified filter of day or no filter
    while True:
        day = input("Which day would you want to filter the data? please choose monday, tuesday, wednesday, thursday, friday, saturday, sunday or all\n")
        if day == "sunday" or day == "saturday" or day == "friday" or day == "thursday" or day == "wednesday" or day == "tuesday" or day == "monday" or day == "all" :
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all' :
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all' :
        df = df[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    mc_month = df['month'].value_counts().idxmax()
    print("The most commen month is {}".format(mc_month))

    # Display the most common day of week
    mc_day = df['day'].value_counts().idxmax()
    print("The most commen day is {}".format(mc_day))
    
    # Display the most common start hour
    mc_hour = df['hour'].value_counts().idxmax()
    print("The most commen hour is {}".format(mc_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    mc_start_station = df['Start Station'].value_counts().idxmax()
    print("The most commen start station is {}".format(mc_start_station))

    # Display most commonly used end station
    mc_end_station = df['End Station'].value_counts().idxmax()
    print("The most commen end station is {}".format(mc_end_station))

    # Display most frequent combination of start station and end station trip
    mc_com_station = df[['Start Station','End Station']].mode().loc[0]
    print("The most commen combination of start station and end station are {}, {}".format(mc_com_station[0], mc_com_station[1] ))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_time = df['Trip Duration'].sum()
    print("Total travel time is {}".format(total_time))
    # Display mean travel time
    mean_time = df['Trip Duration'].mean()
    print("Mean travel time is {}".format(mean_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_count = df["User Type"].value_counts()
    print("Counts of user types are \n")
    for index, value in enumerate(user_count) :
        print("{} : {}".format(user_count.index[index], user_count))


    # Display counts of gender
    if 'Gender' in df.columns :
        gender_count = df["Gender"].value_counts()
        print("Counts of genders are \n")
        for index, value in enumerate(gender_count) :
            print("{} : {}".format(gender_count.index[index], gender_count))
    else :
        print("Gender column does not exist")
        

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns : 
        birth_year = df['Birth Year']
    
        earliest = birth_year.min()
        print("The earliest birth year is {}".format(earliest))

        recently = birth_year.max()
        print("The most recent birth year is {}".format(recently))

        mc_year = birth_year.value_counts().idxmax()
        print("The most common birth year is {}".format(mc_year))
    else :
        print("Birth Year column does not exist")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_row_data(df) :
    
    display_data = input("Would you like to see the raw data? Type 'Yes' or 'No'.\n")
    start_row = 0
    if display_data == 'Yes' :
        while True :
            print(df.iloc[start_row : start_row + 5])
            start_row += 5
            view_more_five = input("Would you like to see more five lines? Type 'Yes' or 'No' :)\n")
            if view_more_five == 'No' :
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        display_row_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
