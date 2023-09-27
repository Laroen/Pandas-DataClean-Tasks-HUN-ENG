import pandas
import matplotlib.pyplot as plt


pandas.set_option('display.max_columns', None)
#pandas.set_option('display.max_rows', None)
pandas.set_option('display.width', 1000)

file = 'cities.csv'
df_cities = pandas.read_csv(file,sep='#', engine='pyarrow')
#print(df_cities.dtypes)

europe = df_cities[(df_cities['population'] > 2000000) & (df_cities['lon'] > -20.2) &
                   (df_cities['lon'] < 42.7) & (df_cities['lat'] < 72.4) & (df_cities['lat'] > 34.5)
                    ].sort_values(by='population', ascending=False)

print(df_cities.head())
print(europe)
