import pandas


def Fakt_Girl_Check(df):
    fakt_girl = df[df['Fakt'] == 1]
    fakt_girl = len(fakt_girl[fakt_girl['Nem'] == 'l'])
    return fakt_girl


def Boys_check(df):
    man_uni = df[df['Nem'] == 'f'].index
    data_column = set()
    for i in man_uni:
        data = i.split(' ')[1]
        data_column.add(data)
    return len(data_column)

file = 'osztaly.csv'

df_room = pandas.read_csv(file, sep='#', engine='pyarrow', encoding='utf8')

df_room.sort_values(by='Név').reset_index(drop=True, inplace=True)
df_room.set_index('Név', inplace=True)
df_room['Átlag'] = df_room.apply(lambda x : (x['T1'] + x['T2'] + x['T3'] + x['T4'] + x['T5'])/5, axis=1)
print(df_room)


name_16 = df_room[df_room['Kor'] == 16]

print('\n'.join(name_16.index))
fakt_girls_number = Fakt_Girl_Check(df_room)
print(fakt_girls_number)

boys_number = Boys_check(df_room)
print()
print(f'{boys_number} db különböző férfi keresztnév van.')

new_room = pandas.DataFrame()
new_room['Male'] = pandas.Series
new_room['Female'] = pandas.Series

for i in range(16,19):
    kor_data = df_room[df_room['Kor'] == i]
    kor_f = kor_data[kor_data['Nem'] == 'f']
    kor_l = kor_data[kor_data['Nem'] == 'l']

    print(kor_data)
    new_row = {'Male' : kor_f['Átlag'].mean().round(decimals=2), 'Female' : kor_l['Átlag'].mean().round(decimals=2)}
    new_room.loc[i] = new_row

print(new_room)
