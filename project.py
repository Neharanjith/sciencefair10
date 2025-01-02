import pandas as pd
from sklearn.preprocessing import OneHotEncoder

year07 = pd.read_csv('solar_wind_data/2007_CELIAS_Proton_Monitor_5min.csv')
year08 = pd.read_csv('solar_wind_data/2008_CELIAS_Proton_Monitor_5min.csv')
year09 = pd.read_csv('solar_wind_data/2009_CELIAS_Proton_Monitor_5min.csv')
year10 = pd.read_csv('solar_wind_data/2010_CELIAS_Proton_Monitor_5min.csv')
year11 = pd.read_csv('solar_wind_data/2011_CELIAS_Proton_Monitor_5min.csv')
year12 = pd.read_csv('solar_wind_data/2012_CELIAS_Proton_Monitor_5min.csv')
year13 = pd.read_csv('solar_wind_data/2013_CELIAS_Proton_Monitor_5min.csv')
year14 = pd.read_csv('solar_wind_data/2014_CELIAS_Proton_Monitor_5min.csv')
year15 = pd.read_csv('solar_wind_data/2015_CELIAS_Proton_Monitor_5min.csv')
year16 = pd.read_csv('solar_wind_data/2016_CELIAS_Proton_Monitor_5min.csv')
year17 = pd.read_csv('solar_wind_data/2017_CELIAS_Proton_Monitor_5min.csv')
year18 = pd.read_csv('solar_wind_data/2018_CELIAS_Proton_Monitor_5min.csv')
year19 = pd.read_csv('solar_wind_data/2019_CELIAS_Proton_Monitor_5min.csv')
year20 = pd.read_csv('solar_wind_data/2020_CELIAS_Proton_Monitor_5min.csv')
year21 = pd.read_csv('solar_wind_data/2021_CELIAS_Proton_Monitor_5min.csv')
year22 = pd.read_csv('solar_wind_data/2022_CELIAS_Proton_Monitor_5min.csv')
year23 = pd.read_csv('solar_wind_data/2023_CELIAS_Proton_Monitor_5min.csv')
dataset = pd.concat([year07, year08,year09,year10,year11,year12,year13,year14,year15,year16,year17,year18,year19,year20,year21,year22,year23], ignore_index=True)

def replace_SPEED(x):
    if x > 400 and x < 600:
        return 0
    elif x >= 400 and x <= 600:
        return 1
    else:
        return 2

dataset['SPEED'] = dataset['SPEED'].apply(replace_SPEED)

def replace_Np(x):
    if x != 1:
        return 0
    else:
        return 1

dataset['Np'] = dataset['Np'].apply(replace_Np)

def replace_Bz(x):
    if x <= -2:
        return 0
    else:
        return 1

dataset['N/S'] = dataset['N/S'].apply(replace_Bz)

dataset.drop(columns=['Vth','V_He','GSE_X','GSE_Y','GSE_Z','RANGE','CRN(E)'])

predict_dataset = pd.concat([year07, year08,year09,year10,year11,year12,year13,year14,year15,year16,year17,year18,year19,year20,year21,year22,year23], ignore_index=True)

predict_dataset['Np'] = predict_dataset['Np'].apply(replace_Np)
predict_dataset['N/S'] = predict_dataset['N/S'].apply(replace_Bz)
predict_dataset['SPEED'] = predict_dataset['SPEED'].apply(replace_SPEED)
predict_dataset.drop(columns=['YY','MON','DY','DOY:HH:MM:SS','Vth','V_He','GSE_X','GSE_Y','GSE_Z','RANGE','HGLAT','HGLONG','CRN(E)'])