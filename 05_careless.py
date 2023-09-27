import pandas
import numpy as np
import datetime

file = 'titkarno1.csv'
file_2 = 'titkarno2.csv'

df_care_1 = pandas.read_csv(file, sep=';',encoding='latin', engine='pyarrow')
# fill NaN and change type to date on file
df_care_1.replace('-', np.nan, inplace=True)
print(df_care_1)

df_care_1['születési dátum'] = pandas.to_datetime(df_care_1['születési dátum'], format='mixed')
df_care_1['állampolgárság'].replace(regex={'m.*': 'magyar'}, inplace=True)

df_care_1['nem'].replace(regex={'m.*': 'férfi','M.*': 'férfi','f.*': 'nő','F.*': 'nő'}, inplace=True)

df_care_1['születési dátum'] = pandas.to_datetime(df_care_1['születési dátum'], format='mixed')
#print(df_care_1)

## fill NaN and change type to date on file 2
df_care_2 = pandas.read_csv(file_2, sep='\t', encoding='latin', engine='pyarrow')

df_care_2['születési dátum'].replace(regex={' ': np.nan}, inplace=True)
df_care_2['születési dátum'] = pandas.to_datetime(df_care_2['születési dátum'], format='mixed')
df_care_2['állampolgárság'].replace(regex={'h.*': 'magyar',' ': np.nan,'H.*': 'magyar','': np.nan}, inplace=True)
df_care_2['nem'].replace(regex={'f.*': 'férfi',' ': np.nan,'': np.nan}, inplace=True)
df_care_2['TAJ-szám'].replace({' ': np.nan,'': np.nan,'  ': np.nan}, inplace=True)

print(df_care_2)

df_care_full = pandas.concat((df_care_1,df_care_2), ignore_index=True)

df_care_full['név'] = df_care_full['név'].apply(lambda x: np.nan if len(str(x)) < 4 else x)

print()

df_care_full.dropna(how='all',axis=0,inplace=True) #dropped only rows where every data missing
df_care_full.dropna(how='all',axis=1,inplace=True) #dropped only columns where every data missing
df_care_full.dropna(inplace=True,subset=['név']) # dropped only Nan rows where column of names = nan

taj_count = df_care_full.groupby('TAJ-szám')['TAJ-szám'].count()
taj_count = taj_count[taj_count.values > 1].index
df_care_full.set_index('TAJ-szám', inplace=True)
for i in taj_count:
    df_care_full.drop(i, inplace=True,axis=0)
df_care_full.reset_index(inplace=True)

print(f'\nÖsszes sorok száma a műveletek után{len(df_care_full)}\n')
print(df_care_full['születési dátum'].dtype)
df_care_full['Kor'] = (datetime.date.today().year - df_care_full['születési dátum'].dt.year)
df_care_full.sort_values(by='Kor',inplace=True)

youngest = df_care_full.loc[lambda x: x['Kor'] == min(df_care_full['Kor'])]
oldest = df_care_full.loc[lambda x: x['Kor'] == max(df_care_full['Kor'])]
df_care_full_without_nan_age = df_care_full.copy(deep=True)
df_care_full_without_nan_age.dropna(inplace=True,subset=['születési dátum'],axis=0)
print(youngest)
print(oldest)

df_care_full.sort_values(by='születési dátum',)
print(df_care_full_without_nan_age)
