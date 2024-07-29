import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
all_months=['january','february','march','april','may','june','july','august','september','october','november','december']
all_cities=['chicago','new york city','washington']
all_days=['saturday','sunday','monday','tuesday','wednesday','thursday','friday']
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
        city = input('Would your like to see data for Chicago, New York, or Washington?\n')
        if city not in all_cities:
            print('please enter chicago or new york city or washington\n')
        else:
            break


    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('which month? January, February, March, April, May, or June')
        if month not in all_months:
            print('enter a right month\n')
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Which day? Please type your response as an integer (e.g., 1=sunday).')
        if day not in all_days:
            print('enter a right day\n')
        else:
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

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    df['time'] = pd.to_datetime(df['time'])
    df['month']= df['time'].dt.month
    df['day']= df['time'].dt.day

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('the most common month is {}' .format(df['month'].mode()[0]))

    # display the most common day of week
    print('the most common day is {}' .format(df['day'].mode()[0]))

    # display the most common start hour
    df['hour']=df['time'].dt.hour
    print('the most common hour is {}' .format(df['hour'].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station\
    print('the most common start station {}' .format(df['start station'].mode()[0]))

    # display most commonly used end station
    print('the most common end station {}' .format(df['end station'].mode()[0]))


    # display most frequent combination of start station and end station trip
    combination = df['start station'].map(str) + df['end station'].map(str)
    print('the most common combination between start and end stations is {}' .format(combination.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('user types count is {}'.format(df['user types'].value_counts()))

    # Display counts of gender
    print('gender counts {}' .format(df['gender'].value_counts()))

    # Display earliest, most recent, and most common year of birth
    print('earliest year of birth {}'.format(df['birth year'].min()))
    print('most recent year of birth {}'.format(df['birth year'].max()))
    print('common year of birth {}'.format(df['birth year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
