import pandas as pd
import sqlite3

if __name__ == '__main__':
    pd.set_option('expand_frame_repr', False)
    df = pd.read_csv('data1.csv')
    df.columns = ['id', 'number', 'car_name', 'description', 'owner']

    con = sqlite3.connect('table_car.db')
    df.to_sql('table_car', con, if_exists='replace', index=False, )
