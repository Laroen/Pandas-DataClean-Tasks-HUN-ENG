import pandas
import matplotlib.pyplot as plt
import numpy as np

pandas.set_option('display.max_columns', None)
pandas.set_option('display.max_rows', None)
pandas.set_option('display.width', 1000)


def Histogram_Intersection(a, b):
    v = np.minimum(a, b).sum().round(decimals=1)
    return v


file = 'T_adat.csv'
file_2 = 'co2_adat.txt'

df_t_data = pandas.read_csv(file, sep=',', skiprows=1)
df_t_data.set_index('Year', inplace=True)
df_t_data.replace('***',0, inplace=True)
df_t_data.drop(columns=['J-D' , 'D-N' , 'DJF' , 'MAM' , 'JJA'  ,'SON'], inplace=True)

#task 02
columns = df_t_data.columns
for i in columns:
    df_t_data[i] = df_t_data[i].astype(float)
#print(df_t_data.dtypes)
#print(df_t_data.head())
df_t_data['Avg_temp'] = df_t_data.apply(lambda x: x.mean().round(decimals=2), axis=1)
print(df_t_data.head())

df_co2 = pandas.read_csv(file_2, skiprows=72,header=None, sep='\s+')
df_co2.rename(columns={0:'Year',1:'Month', 2:'decimal',3:'Avg_CO2',4:'interpolated',5:'season corr',6:'days'}, inplace=True)
df_co2.replace(-99.99, df_co2.mean().round(decimals=2), inplace=True)
df_co2.replace(-1, df_co2.median().round(decimals=2), inplace=True)

co2_year_avg = pandas.DataFrame(df_co2.groupby('Year')['Avg_CO2'].mean().round(decimals=2))

print(df_co2.head())
print(co2_year_avg.head())

# task 03
full= pandas.merge(df_t_data,df_co2, on='Year', validate='one_to_many', how='right')
full.set_index('Year', inplace=True)
print(full.head())

correlation = pandas.DataFrame(full.groupby('Year')[['Avg_temp','Avg_CO2']].mean().round(decimals=2))
print(correlation.head())

corr_df = correlation.corr(method=Histogram_Intersection)
print(corr_df)