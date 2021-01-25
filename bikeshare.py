#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt



# In[3]:



CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


# In[4]:



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
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
   
    df['age'] = (2020-df['Birth Year'])

    return df


# In[5]:


df = load_data("chicago", "march", "friday")
df


# In[ ]:


#enter a age range to see trip duration
def age_range_trip_duration(df):
    age_range_description = '''
        0: age range 0-20
        1: age range 21-40
        2: age range 41-60
        3: age range 61-80
        4: age range 81-100
        5: age range >100

        '''
    need_valid_input = True

    while need_valid_input:
        print(age_range_description)
        age_range = int(input('Enter the number for the age range: '))
        if age_range <=5 and age_range >= 0:
            need_valid_input = False
        else:
            print('incorrect input')

    age_ranges = {0:[0,20],1:[21,40],2:[41,60],3:[61,80],4:[81,100],5:[101,120]}
    age_min, age_max = age_ranges[age_range]

    age_min, age_max = float(age_min),float(age_max)
    df1 = df[(age_min <= df['age']) & (df['age'] <= age_max)]
    df1.plot(kind='scatter' , x='age', xlim = (age_min, age_max), y= 'Trip Duration', ylim = (0,df1['Trip Duration'].max()), color= 'red')


    plt.show()
           



# In[ ]:


def general(df):
    df.plot(kind='scatter' , x='Birth Year', y= 'Trip Duration', color= 'red')
    plt.show()


# In[ ]:


def gender(df):
    df.groupby('Gender')['Trip Duration'].nunique().plot(kind='bar', y = 'Trip Duration')
    plt.show()


# In[ ]:


while True:
    city = input('Please select a city: chicago, new york city ')
    if (city.lower() == 'chicago') or (city.lower() == 'new york city' ):
        df = load_data(city, 'all', 'all')
        print('What does a graph of the Trip Duration vs Birth Year look like?')
        general(df)
        print( 'Which gender uses our bikes more?')      
        gender(df)
        print('What does the data base tell us about the riders based on age range?')      
        age_range_trip_duration(df)    
        
    answer = input('Do you want to continue: yes or no? ')
    if answer.lower().startswith("no"):
        print("Goodbye")
        break
    


# In[ ]:




