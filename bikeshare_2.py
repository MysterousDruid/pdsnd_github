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
    citys = ['chicago','new york city','washington']
    months = ['january','february','march','april','may','june','all']
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday','all']
    while True:
        city = input('enter the city you want to apply (chicago, new york city, washington): ').lower()
        if city not in citys:
            print('\n please enter the city name right')
        else:
            break
    # get user input for month (all, january, february, ... , june)
    while True:
            month = input('enter the month you want to filterby(january, february, ... , june) or all to apply no filter!: ').lower()
            if month not in months:
                print('\n please enther a  vaild month')
            else:
                break
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('enter the day you want to filterby(monday, tuesday, ... sunday) or all to apply no filter!: ').lower()
        if day not in days:
            print('\n please enter a valid day')
        else:
            break

    print('-'*40)
    return city, month, day
def load_data(city, month, day):



    #took code from project practice 3#
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
<<<<<<< HEAD
        df - Pandas DataFrame containing city data filtered by month and day or no filter applys
||||||| f63b541
        df - Pandas DataFrame containing city data filtered by month and day
=======
        df - Pandas DataFrame containing city data filtered by month and day or no filtered applied 
>>>>>>> documentation
    """

    df = pd.read_csv(CITY_DATA[city])


    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['hour'] = df['Start Time'].dt.hour
    df['month'] = df['Start Time'].dt.month
    #day_name() from: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.dt.day_name.html
    df['day_of_week'] = df['Start Time'].dt.day_name()


    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # display the most common month
    common_month = df['month'].mode()[0]
    print('Most common Month: {}'.format(common_month))

    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('most common day: {}'.format(common_day))

    # display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('most common hour: {}'.format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    most_common_start_station = df['Start Station'].mode()[0]
    print('most common start station: {}'.format(most_common_start_station))

    most_common_end_station = df['End Station'].mode()[0]
    print('most common end station: {}'.format(most_common_end_station))
    most_common_combiened_station = df['Start Station'] + ' to ' + df['End Station']
    most_common_combiened_station = most_common_combiened_station.mode()[0]
    print('most common combiened station: {}'.format(most_common_combiened_station))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and mean trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = (pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])).sum()
    print('total time travel: ',total_travel_time)

    # display mean travel time
    mean_travel_time = (pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time']))
    print('mean time travel: ',mean_travel_time.mean())
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
    if city != 'washington':
        gender_types = df['Gender'].value_counts()
        print(gender_types)

    # Display earliest, most recent, and most common year of birth
    if city != 'washington':
        earliest_year = int(df['Birth Year'].min())
        print('Earliest Year: {}'.format(earliest_year))
        most_recent_year = int(df['Birth Year'].max())
        print('Most Recent Year: {}'.format(most_recent_year))
        most_common_year = int(df['Birth Year'].mode()[0])
        print('Most Common Year: {}'.format(most_common_year))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        #code belew was help from a mentor
        i = 0
        while True:
            display_more=input('do you want to see 5 more line of data? yes or no: \n').lower()
            if display_more == 'yes':
                five_rows=df.iloc[:i+5]
                print(five_rows)
                i += 5
            else:
                break
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
