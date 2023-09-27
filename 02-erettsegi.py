import pandas
import matplotlib.pyplot as plt
import numpy as np


def func(pct, allvalues):
    data = int(pct / 100.*np.sum(allvalues))
    return f"{data} fő"


pandas.set_option('display.max_columns', None)
pandas.set_option('display.width', 1000)

file = 'erettsegi.csv.gz'

df_erettsegi = pandas.read_csv(file, sep=';')
df_erettsegi.drop(columns=df_erettsegi.columns[0],inplace=True)
df_erettsegi['vizsgázó neme'].replace('nõ','nő', inplace=True)

top_vizsga = df_erettsegi[(df_erettsegi['vizsga szintje'] == 'emelt') & (df_erettsegi['év'] == 2015)]\
    .sort_values(by='össz százalék',ascending=False)

print(top_vizsga.head(3))
print(top_vizsga.tail(5))
print()
task_2 = df_erettsegi[df_erettsegi['vizsga szintje'] == 'emelt']
task_2 = pandas.DataFrame(task_2.groupby(['vizsgázó neme','év']).aggregate({'szóbeli pontszám': 'mean'})).unstack()
print(task_2)

plot = task_2.plot(kind='bar', stacked=False).legend(loc='upper center')

print()
task_3 = df_erettsegi.groupby(['vizsga szintje','vizsgázó neme'])['vizsgázó neme'].value_counts().unstack()
task_3_new = pandas.DataFrame.transpose(task_3)
print(task_3_new)


fig, ax_1 = plt.subplots(1,2)
ax_1[0].pie(task_3_new['emelt'], startangle=90, labels=task_3_new.index, autopct=lambda pct: func(pct, task_3_new['emelt']))
ax_1[0].set_title('Emelt')
ax_1[1].pie(task_3_new['közép'], startangle=90, labels=task_3_new.index, autopct=lambda pct: func(pct, task_3_new['közép']))
ax_1[1].set_title('Közép')


task_4 = df_erettsegi[(df_erettsegi['év'] == 2014) & (df_erettsegi['vizsga szintje']== 'közép')]
task_4 = pandas.DataFrame(task_4.groupby(['érdemjegy'])['érdemjegy'].count())
print(task_4)

plot = task_4.plot(kind='bar', stacked=False).legend(loc='upper center')


task_6 = df_erettsegi[(df_erettsegi['év'] <= 2015) & (df_erettsegi['év'] >= 2011) & (df_erettsegi['vizsga szintje']== 'emelt')]
print(task_6.head(2))
task_6 = task_6.groupby(['vizsgázó képzési típusa','év']).aggregate({'össz pontszám' : 'mean'}).unstack()
task_6.rename( index={'-': 'ismeretlen'}, columns={'össz pontszám' : 'Átlag'}, inplace=True)

print(task_6)
plot = task_6.plot(kind = 'bar', stacked=False, subplots=True, rot='horizontal', position=1, grid = True ,layout=(2,3),
                   title='Átlag pontszámok évenkénti kimutatása', fontsize=10, xlabel='',sharex=False)


task_7 = df_erettsegi[df_erettsegi['vizsga szintje'] == 'emelt']
task_7 = pandas.DataFrame(task_7.groupby(['vizsgázó neme','év']).aggregate({'szóbeli pontszám': 'mean'})).unstack()
task_7 = task_7.unstack()
task_7 = task_7.unstack()
task_7['különbség'] = pandas.Series()
task_7['különbség'] = task_7.apply(lambda x: x['férfi'] - x['nő'], axis=1)
kulonbseg = task_7['különbség']
plot = task_7.plot(kind = 'bar', stacked=False,rot='horizontal')

plot = kulonbseg.plot(kind = 'bar', stacked=False,rot='horizontal',xlabel='',
                      title='Évenkénti érettségi eredmény különbség (férfi/nő)')

print(task_7)
plt.show()
