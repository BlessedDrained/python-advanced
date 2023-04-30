import sqlite3


def main():
    with open('create_schema.sql', 'r') as sql_file:
        sql_script = sql_file.read()

    with sqlite3.connect('database.db') as con:
        cur = con.cursor()
        cur.execute('PRAGMA foreign_keys = ON;')
        cur.executescript(sql_script)
        con.commit()


if __name__ == '__main__':
    main()
