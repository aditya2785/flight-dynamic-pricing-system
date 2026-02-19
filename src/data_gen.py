import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

def clean_flight_data(df):

    df['Airline-Name'] = df['Airline-Class'].str.split('\n').str[0].str.strip()
    df['Class'] = df['Airline-Class'].str.split('\n').str[-1].str.strip()

    df['Date of Journey'] = pd.to_datetime(df['Date of Journey'], format='%d/%m/%Y')
    df['Date of Booking'] = pd.to_datetime(df['Date of Booking'], format='%d/%m/%Y')

    df['days_before_flight'] = (df['Date of Journey'] - df['Date of Booking']).dt.days
    df['journey_day'] = df['Date of Journey'].dt.day
    df['journey_day_name'] = df['Date of Journey'].dt.day_name()

    df['Departure City'] = df['Departure Time'].str.split('\n').str[1].str.strip()
    df['Arrival City'] = df['Arrival Time'].str.split('\n').str[1].str.strip()

    df['Total Stops'] = df['Total Stops'].str.replace(r'\n\s*\t*', '', regex=True)
    df['Total Stops'] = df['Total Stops'].str.replace(r'(stop).*', r'\1', regex=True)

    df['Departure_Time'] = df['Departure Time'].str.split('\n').str[0].str.strip()
    df['Arrival_Time'] = df['Arrival Time'].str.split('\n').str[0].str.strip()

    df['Duration'] = df['Duration'].str.extract(r'(\d+)h (\d+)m') \
        .astype(float) \
        .apply(lambda x: round(x[0] + x[1] / 60, 4), axis=1)

    df['arrival_time'] = pd.to_datetime(df['Arrival_Time'], format='%H:%M').dt.hour
    df['arrival_category'] = df['arrival_time'].apply(lambda x: 0 if x < 19 else 1)

    df['Price'] = df['Price'].replace(',', '', regex=True).astype(int)

    df.drop(['Date of Booking','Date of Journey','Airline-Class',
             'Departure Time','Arrival Time','arrival_time'], axis=1, inplace=True)

    return df


def feature_engineering(df):

    df['Route'] = df['Departure City'] + ' -> ' + df['Arrival City']
    df.drop(['Departure City','Arrival City'], axis=1, inplace=True)

    df['Departure_Time_hr'] = pd.to_datetime(df['Departure_Time'], format='%H:%M').dt.hour
    df['Arrival_Time_hr'] = pd.to_datetime(df['Arrival_Time'], format='%H:%M').dt.hour

    df.drop(['Departure_Time','Arrival_Time'], axis=1, inplace=True)

    return df


def encode_data(df):

    df = pd.get_dummies(df, columns=['Total Stops'], prefix='Stops', dtype=int)

    frequency_map = df['journey_day_name'].value_counts(normalize=True).to_dict()
    df['journey_day_name_FreqEnc'] = df['journey_day_name'].map(frequency_map)
    df.drop(['journey_day_name'], axis=1, inplace=True)

    return df


def preprocess_pipeline(filepath):

    df = pd.read_csv(filepath)
    df = clean_flight_data(df)
    df = feature_engineering(df)

    # filter specific route (optional)
    df = df[(df['Airline-Name']=='Air India') &
            (df['Class']=='ECONOMY') &
            (df['Route']=='Delhi -> Mumbai')]

    df.drop(['Airline-Name','Class','Route'], axis=1, inplace=True)

    df = encode_data(df)

    return df
