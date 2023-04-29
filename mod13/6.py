import sqlite3
import datetime

sport_types = ['футбол', 'хоккей', 'шахматы', 'SUP-сёрфинг', 'бокс', 'Dota2', 'шахбокс']

delete_sql = 'DELETE FROM table_friendship_schedule'
insert_sql = '''INSERT INTO table_friendship_schedule SELECT table_friendship_employees.id, ( ? ) 
                                                            FROM table_friendship_employees
                                                            WHERE preferable_sport = ( ? )'''


def set_schedule(cur):
    cur.execute(delete_sql)
    end_date = datetime.date(2020, 12, 31)
    for day_number in range(7):
        start_date = datetime.date(2020, 1, 1)
        day_delta = datetime.timedelta(days=1)
        while start_date <= end_date:
            if start_date.weekday() == day_number:
                cur.execute(insert_sql, (start_date, sport_types[day_number]))
            start_date += day_delta


def main():
    with sqlite3.connect('hw.db') as con:
        cursor = con.cursor()
        set_schedule(cursor)


if __name__ == '__main__':
    main()
