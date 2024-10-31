import time
from datetime import timedelta
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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city=input('What city would you like to see data from ? Chicago, New york City or Washington\n\n').lower()
    while city not in CITY_DATA :
        print('Please enter a valid city\n')
        city=input('What city would you like to see data from ? Chicago, New york City or Washington\n\n').lower()

    # get user input for month (all, january, february, ... , june)

    months = ['january', 'february', 'march', 'april', 'may', 'june','all']
    month=input('Which month ? Type any month from the following or type all for no filter: January, February, March, April, May, June\n').lower()
    while month not in months :
        print('Please enter a valid month \n')
        month=input('Which month ? Type any month from the following or type all for no filter: January, February, March, April, May, June\n').lower()
        
    

    # get user input for day of week (all, monday, tuesday, ... sunday)

    days=['satuday','sunday','monday','tuesday','wednesday','thursday','friday','all']
    day=input('Which day ? type all for no filter\n').lower()
    while day not in days :
        print('Please enter a valid day')
        day=input('Which day ? type all for no filter\n').lower()



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
        df - pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int

        """ I cleared this two lines and found that there is a function
        that could do what i want easily here and thank you for your advice but i couldn't do it
        it kept getting me an error"""

        #months = ['january', 'february', 'march', 'april', 'may', 'june']
        #month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month.title()]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df
    


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    #months = ['january', 'february', 'march', 'april', 'may', 'june']

    month=df['month'].mode()[0]
    print('The most common month is {} . '.format(month))

    # display the most common day of week

    common_day=df['day_of_week'].mode()[0]
    print('The most common day of week is {} .'.format(common_day))

    # display the most common start hour

    common_hour=df['Start Time'].dt.hour.mode()[0]
    if common_hour<13 :
        print('The most common start hour is {} Am . '.format(common_hour))
    else :
        common_hour-=12
        print('The most common start hour is {} Pm . '.format(common_hour))

    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    common_start_station=df['Start Station'].mode()[0]
    print('The most commonly used start station is {} . '.format(common_start_station))
    common_start_count=df['Start Station'].value_counts().head(1)[0]
    print('and happened {} of times'.format(common_start_count))


    # display most commonly used end station

    common_end_station=df['End Station'].mode()[0]
    print('The most commonly used end station is {} . '.format(common_end_station))
    common_end_count=df['End Station'].value_counts().head(1)[0]
    print('and happened {} of times'.format(common_end_count))

    # display most frequent combination of start station and end station trip

    start_end=(df['Start Station']+','+df['End Station']).mode()[0]
    print('The most frequent combination of start station and end station trip is {} . '.format(start_end))
    common_combine_count=(df['Start Station']+','+df['End Station']).value_counts().head(1)[0]
    print('and happened {} of times'.format(common_combine_count))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    total_travel=int(df['Trip Duration'].sum())
    total_travel_intime=timedelta(seconds=total_travel)
    print('Total travel time is {} . '.format(total_travel_intime))

    # display mean travel time

    mean_travel=round(float(df['Trip Duration'].mean()))
    mean_travel_intime=timedelta(seconds=mean_travel)
    print('Average travel time is {} . '.format(mean_travel_intime))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    user_count=df['User Type'].value_counts().to_frame()
    print('Number of \n{} . '.format(user_count))

    # Display counts of gender

    # Display earliest, most recent, and most common year of birth

    if city!='washington' :

        gender_count=df['Gender'].value_counts().to_frame()
        print('Total number of \n{} . '.format(gender_count))

        earlist_year=int(df['Birth Year'].min())
        print('Earliest year of birth is {} . '.format(earlist_year))

        most_recent_year=int(df['Birth Year'].max())
        print('Most recent year of birth is {} . '.format(most_recent_year))

        most_common_year=int(df['Birth Year'].mode()[0])
        print('Most common year is {} . '.format(most_common_year))

    else :
        print('\nThere is no gender or birth year data for Washington')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Displays data of bikeshare users."""

    print('\nDisplaying Data...\n')
    start_time = time.time()

    #take input answer from the user to display first 5 rows of the data

    user_answer=input('Do you want to see first 5 rows of data ?   type yes or no \n').lower()
    while user_answer not in ('yes','no') :
        print('Please type invalid answer')
        user_answer=input('Do you want to see first 5 rows of data ?   type yes or no \n').lower()

    #use a while loop to keep displaying next 5 five row when the answer is yes

    count=0

    while user_answer=='yes' :
            print(df.iloc[count:count+5])
            count+=5
            user_answer=input('Do you want to see another 5 rows of data ?   type yes or no\n').lower()
            
        
    if user_answer=='no' :
        print('Thank you')

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
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
