import pandas as pd
import sqlite3

if __name__ == '__main__':
    pd.set_option('expand_frame_repr', False)
    df = pd.read_csv('data2.csv')
    df.columns = ['phone_id', 'phone_color']
    con = sqlite3.connect('phone_data.db')
    df.to_sql('table_phones', con, if_exists='replace', index=False)

    df = pd.read_csv('data22.csv')
    df.columns = ['phone_color', 'sold_count']
    df.to_sql('table_checkout', con, if_exists='replace', index=False)



