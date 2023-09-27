import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
pd.set_option('display.width',1000)

file = 'movie_metadata.csv'

df_imdb = pd.read_csv(file,sep=',', engine='pyarrow')


hun_movies = df_imdb[(df_imdb['country'] == 'Hungary') | (df_imdb['language'] == 'Hungarian')]

task_2 = pd.DataFrame(df_imdb.groupby('language')['imdb_score']
                          .mean().round(decimals=2)).sort_values(by='language')



'''
plot_task_2 = task_2.plot(kind='bar', title='IMDB Avg of Languages')
plt.show()
'''
actor_1_name_like = pd.DataFrame(df_imdb[['actor_1_name','actor_1_facebook_likes']])
actor_1_name_like.rename(columns={'actor_1_name':'name','actor_1_facebook_likes':'like'}, inplace=True)
actor_2_name_like = pd.DataFrame(df_imdb[['actor_2_name','actor_2_facebook_likes']])
actor_2_name_like.rename(columns={'actor_2_name':'name','actor_2_facebook_likes':'like'}, inplace=True)
actor_3_name_like = pd.DataFrame(df_imdb[['actor_3_name','actor_3_facebook_likes']])
actor_3_name_like.rename(columns={'actor_3_name':'name','actor_3_facebook_likes':'like'}, inplace=True)
#full_name_like = pd.merge(actor_1_name_like,actor_2_name_like, on='name',validate='many_to_many',how='outer')
#full_name_like = pd.merge(full_name_like,actor_3_name_like, on='name',validate='many_to_many',how='outer')
'''
print(actor_1_name_like.head().sort_values(by='name'))
print(actor_2_name_like.head().sort_values(by='name'))
print(actor_3_name_like.head().sort_values(by='name'))
'''

full_name_like = pd.concat([actor_1_name_like,actor_2_name_like,actor_3_name_like],
                                                ignore_index=True)
full_name_like.dropna(axis=0,inplace=True)

full_name_like = pd.DataFrame(full_name_like.groupby('name').agg({'like':'sum'}))

print(full_name_like.sort_values(ascending=False, by='like').head(10))

#cch = df_imdb[(df_imdb['actor_1_name'] == 'CCH Pounder') | (df_imdb['actor_2_name'] == 'CCH Pounder') | (df_imdb['actor_3_name'] == 'CCH Pounder')]
#print(cch)

df_matrix = df_imdb[ ["num_critic_for_reviews", "duration", "director_facebook_likes",
                      "cast_total_facebook_likes", "gross", "num_voted_users", "budget",
                      "title_year" , "imdb_score"]]

corr_matrix = df_matrix.corr(method='pearson')
#print(corr_matrix)
corr_triu = np.tril(np.ones(corr_matrix.shape)).astype(np.bool_)
print(corr_triu)
#print(corr_triu)
df_lt = corr_matrix.where(np.tril(np.ones(corr_matrix.shape)).astype(np.bool_))
print(df_lt)
fig, ax = plt.subplots(figsize=(7, 6))
hmap=sns.heatmap(df_lt,cmap="Spectral")
plt.xticks(rotation=35)
plt.show()
hmap.figure.savefig("Correlation_Heatmap_Lower_Triangle_with_Seaborn.png",
                    format='png',
                    dpi=150)