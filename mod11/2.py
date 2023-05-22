import requests
import sqlite3
import time
import threading

insert_sql = """INSERT INTO 'starwars' (name, age, gender) VALUES (?, ?, ?);"""

make_table_sql = """CREATE TABLE IF NOT EXISTS starwars (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age TEXT, gender TEXT)"""


def get_data(url, result):
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        return

    result.append((data["name"], data["birth_year"], data["gender"]))


def load_single_thread():
    url = "https://swapi.dev/api/people/"
    with sqlite3.connect("homework.db") as c:
        cur = c.cursor()

    result = []
    for i in range(1, 21):
        get_data(url + str(i), result)

    cur.executemany(insert_sql, result)
    c.commit()


def load_multiple_threads():
    url = "https://swapi.dev/api/people/"
    with sqlite3.connect("homework.db") as c:
        cur = c.cursor()

    result = []
    threads = []
    for i in range(1, 21):
        thread = threading.Thread(target=get_data, args=(url + str(i), result))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    cur.executemany(insert_sql, result)
    c.commit()


def main():
    with sqlite3.connect("homework.db") as conn:
        cur = conn.cursor()
    cur.execute(make_table_sql)
    conn.close()

    start = time.time()
    load_single_thread()
    end = time.time()
    print(f"Single thread time is: {end - start}")

    start = time.time()
    load_multiple_threads()
    end = time.time()
    print(f"Multithread time is: {end - start}")


if __name__ == "__main__":
    main()
