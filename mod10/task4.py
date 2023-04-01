import sqlite3
import pandas as pd

if __name__ == '__main__':
    with sqlite3.connect('hw_4_database.db') as con:
        df = pd.read_csv('data41.csv')
        df.to_sql('salaries', con, if_exists='replace', index=False)

        query = 'SELECT COUNT(*) AS c FROM salaries WHERE salary < 5000'
        result = pd.read_sql(query, con)
        print(f'{result["c"][0]} people have salary less than 5000')

        print('-' * 40)

        query = 'SELECT AVG(salary) AS s FROM salaries'
        result = pd.read_sql(query, con)
        print(f'Average salary is {result["s"][0]}')

        print('-' * 40)

        query = 'SELECT salary as m FROM salaries ORDER BY salary LIMIT 1 OFFSET (SELECT COUNT(*) FROM salaries) / 2'
        result = pd.read_sql(query, con)
        print(f'Median salary is {result["m"][0]}')

        print('-' * 40)

        query_citizens_count = 'SELECT COUNT(*) AS c FROM salaries'
        citizens_count = int(pd.read_sql(query_citizens_count, con)['c'][0])
        query_t = f'SELECT SUM(salary) as t FROM (SELECT * FROM salaries ORDER BY salary DESC LIMIT 0.1 * {citizens_count})'
        t = int(pd.read_sql(query_t, con)['t'][0])
        query_k = f'SELECT SUM(salary) - {t} as k FROM salaries'
        k = int(pd.read_sql(query_k, con)['k'][0])
        # query_result = f'SELECT ROUND({t} / {k}, 2) * 100 as r FROM salaries'
        # result = pd.read_sql(query_result, con)['r'][0]

        result = round(t / k, 2)
        print(f'F value is {result}%')
