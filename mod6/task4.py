import json
import pandas as pd
from datetime import datetime

if __name__ == '__main__':
    pd.set_option("expand_frame_repr", False)
    with open('stderr.txt', 'r') as f:
        data = [json.loads(x) for x in f.readlines()]
    df_orig = pd.DataFrame.from_dict(data)

    # 1
    df = df_orig.copy()
    print(df.groupby('level').count())

    # 2
    df = df_orig.copy()
    df['time'] = df.apply(lambda row: datetime.strptime(row['time'], '%H:%M:%S').hour, axis=1)
    df['count'] = df.groupby('time')['time'].transform('count')
    print(df.drop_duplicates(subset=['time'])[['time', 'count']])

    # 3
    df = df_orig.copy()
    df['time'] = pd.to_datetime(df['time'])
    df = df.set_index('time').between_time('05:00:00', '05:20:00')
    print(len(df[df['level'] == 'CRITICAL']))

    # 4
    df = df_orig.copy()
    print(len(df[df['message'].str.contains('dog')]))

    # 5
    df = df_orig.copy()
    df = df[df['level'] == 'WARNING']
    print(len(set(df['message'].str.split().explode())))
