import sqlite3
import pandas as pd


def delete_wrong_fees(cur, filename):
    df = pd.read_csv(filename, encoding='cp1251')
    for index, row in df.iterrows():
        cur.execute("DELETE FROM table_fees WHERE truck_number = ? AND timestamp = ?", (row["car_number"], row["timestamp"]))


def main():
    filename = input()
    with sqlite3.connect("hw.db") as con:
        cur = con.cursor()
        delete_wrong_fees(cur, filename)


if __name__ == '__main__':
    main()
