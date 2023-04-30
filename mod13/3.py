from datetime import datetime
import sqlite3

create_table_sql = """
CREATE TABLE IF NOT EXISTS table_with_birds(
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       bird_name TEXT NOT NULL,
       date_when_added TEXT NOT NULL);
"""

add_bird_sql = 'INSERT INTO table_with_birds (bird_name, date_when_added) VALUES (?, ?);'

check_bird_existence_sql = 'SELECT EXISTS(SELECT 1 FROM table_with_birds WHERE bird_name = ? LIMIT 1)'


def log_bird(cursor, bird_name, date_time):
    cursor.execute(add_bird_sql, (bird_name, date_time))


def check_if_such_bird_already_seen(cur, bird_name):
    result = cur.execute(check_bird_existence_sql, (bird_name,)).fetchone()[0]
    return bool(result)


def main():
    name = input("Название вида птицы: ")
    with sqlite3.connect("hw.db") as con:
        cur = con.cursor()
        cur.execute(create_table_sql)
        if not check_if_such_bird_already_seen(cur, name):
            log_bird(cur, name, datetime.utcnow().isoformat())
            print("Записано")
        else:
            print("Данный вид уже зафиксирован")


if __name__ == "__main__":
    main()
