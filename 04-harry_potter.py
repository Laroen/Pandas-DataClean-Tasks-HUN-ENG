import pandas

file = 'hpattributes.txt'
file_2 = 'hpnames.txt'
# Info : Gender: 1 - male, 2 - female;  Houses: 1 - Gryffindor , 2 - Hufflepuff , 3 - Ravenclaw , 4 - Slytherin
df_hp = pandas.read_csv(file, engine='pyarrow', sep='\t')
df_hp_names = pandas.read_csv(file_2, engine='pyarrow', sep='\t')

print(df_hp.head())
print(df_hp_names.head())

df_hp_full = pandas.merge(df_hp_names,df_hp, on='id', validate='one_to_one', how='right').set_index('id')
ravenclaw_df = df_hp_full[df_hp_full['house'] == 3].sort_values(by='schoolyear', ascending=False)
print(df_hp_full.head())
print(ravenclaw_df.head())

count_year = 2017
gryffindor_olds = pandas.DataFrame(df_hp_full[df_hp_full['house'] == 1])
gryffindor_olds['Age'] = gryffindor_olds.apply(lambda x : count_year - x['schoolyear'] + 11, axis=1)
print(gryffindor_olds)
schoolyear_count= pandas.DataFrame(df_hp_full.groupby('schoolyear')['schoolyear'].value_counts()
                                   .sort_values(ascending=False))
print(schoolyear_count.head())
