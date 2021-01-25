import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
DAYS = ['monday', 'tuesday', 'wednesday','thursday', 'friday','saturday','sunday']
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Choose a city out of Chicago, New York City or Washington?\n>').lower()
        if city in CITY_DATA:
            break
        else:
            print('Please select either Chicago, New York City or Washington.\n>')

        # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Choose 'all' or one of the following months: january , february, march, april, may or june.\n>").lower()
        if month in MONTHS or month == 'all':
            break
        else:
            print('Please select "all" or a month!')
       
        # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Choose 'all' or name of the day of the week\n>").lower()
        if day in DAYS or day =='all':
            break
        else:
            print('Please select "all" or a day!')

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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = MONTHS.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
   
    #df['age'] = (2020-df['Birth Year'])

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('\nThe most common month....\n')
    common_month = df["month"].mode()[0]
    print(MONTHS[common_month -1])

    # display the most common day of week
    print('\nThe most commond day of the week ....\n')
    common_day = df['day_of_week'].mode()[0]
    print(common_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    start_hour = df['hour'].mode()[0]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('Most commonly used start station ...')
    common_start_station = df['Start Station'].mode()[0]
    print(common_start_station)

    # display most commonly used end station
    print('Most commonly used end station ...')
    common_end_station = df['End Station'].mode()[0]
    print(common_end_station)
    
    # display most frequent combination of start station and end station trip
    print('Most frequent combination of start station and end station trip  ...')
    df['start_stop'] = df['Start Station'] +' to ' + df['End Station']
    combination = df['start_stop'].mode()[0]
    print(combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total travel time   ... ')
    total = df['Trip Duration'].sum()
    print(total)

    # display mean travel time
    print('Mean Travel Time ... ')
    mean = df['Trip Duration'].mean()
    print(mean)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Counts of user types ...')
    user_type = df['User Type'].value_counts()
    print(user_type)

    # Display counts of gender
    if 'Gender' in df.columns:
        print('Counts of gender ...')
        gender = df['Gender'].value_counts()
        print(gender)
    else:
        print('No Gender for this city')
    
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('Display earliest, most recent, and most common year of birth ...')
        earliest = df['Birth Year'].min()
        recent = df['Birth Year'].max()
        common = df['Birth Year'].mode()[0]
        print(earliest, recent, common)
    else:
        print('No Birth Year for this city')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    " To Show RAW DATA"
    end_line = 0
    while True:
        user_input = input('Do you want to see 5 lines of raw data? Enter yes or no. \n').lower()
        if user_input == 'yes':
            end_line += 5
            print(df.head(n = end_line).tail(n = 5))
        else:
            break
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
    print('Goodbye')


if __name__ == "__main__":
	main()
