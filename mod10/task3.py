import pandas as pd
import sqlite3

if __name__ == '__main__':
    pd.set_option('expand_frame_repr', False)
    with sqlite3.connect('hw_3_database.db') as con:
        for i in range(3):
            df = pd.read_csv(f'data3{i + 1}.csv')
            df.to_sql(f'table_{i + 1}', con, if_exists='replace', index=False)

        for i in range(3):
            table_name = f'table_{i + 1}'
            query = f'SELECT COUNT(*) AS c FROM {table_name}'
            result = pd.read_sql(query, con)
            print(f'{table_name} elements count: {result["c"][0]}')

        print('-' * 40)

        query = 'SELECT COUNT(DISTINCT value) AS c FROM table_1'
        result = pd.read_sql(query, con)
        print(f'Table_2 has {result["c"][0]} rows')

        print('-' * 40)

        query = 'SELECT COUNT(*) AS c FROM table_1 JOIN table_2 ON table_1.value = table_2.value'
        result = pd.read_sql(query, con)
        print(f'Table_1 has {result["c"][0]} rows which are in table_2')

        print('-' * 40)

        query = 'SELECT COUNT(*) as c FROM (SELECT value FROM table_1 INTERSECT SELECT value FROM table_2 INTERSECT SELECT value FROM table_3);'
        result = pd.read_sql(query, con)
        print(f'Table_1 has {result["c"][0]} rows which are in table_2 and table_3')
