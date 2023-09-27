import gzip
import pandas as pd
import json


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows',None)
pd.set_option('display.width',1000)

data_json = [json.loads(str(s).strip("\r\n")) for s in gzip.
                                        open("twitter_sample.gz",mode="rt").readlines()]

df_j = pd.DataFrame(data_json)

print(df_j.head(10).sort_values(by='retweet_count',ascending=False))
#print(df_j.dtypes)

df_j['created_at'] = pd.to_datetime(df_j['created_at'], format='mixed')
df_creat = df_j[['created_at','text']].dropna(axis=0)
df_creat = df_creat.groupby('created_at').agg({'text': 'count'}).sort_values(by='created_at')
print(df_creat.head(10))


