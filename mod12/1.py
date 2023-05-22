import multiprocessing
import time
import sqlite3
from multiprocessing.pool import ThreadPool, Pool
import requests

URL = "https://swapi.dev/api/people/"
insert_sql = """INSERT INTO 'starwars' (name, age, gender) VALUES (?, ?, ?);"""
clear_table_sql = """DELETE FROM starwars"""
make_table_sql = """CREATE TABLE IF NOT EXISTS starwars (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age TEXT, gender TEXT)"""
characters = []


def get_character(url, i):
    global characters
    response = requests.get(url + str(i))
    if response.status_code == 200:
        character_dict = dict(response.json())
        if character_dict is not None:
            characters.append((character_dict["name"], character_dict["birth_year"], character_dict["gender"]))


def load_process_pool():
    with Pool(processes=multiprocessing.cpu_count()) as pool:
        start = time.time()
        args = []
        for i in range(1, 22):
            args.append((URL, i))
        pool.starmap(get_character, args)

        cur.executemany(insert_sql, characters)
        end = time.time()
        print(f"Job done. Finished in {end - start} with process pool")


def load_thread_pool():
    with ThreadPool(processes=multiprocessing.cpu_count() * 6) as pool:
        start = time.time()
        args = []
        for i in range(1, 22):
            args.append((URL, i))
        pool.starmap(get_character, args)
        cur.executemany(insert_sql, characters)
        end = time.time()
        print(f"Job done. Finished in {end - start} with thread pool")


if __name__ == "__main__":
    with sqlite3.connect('hw.db') as conn:
        cur = conn.cursor()
        cur.execute(make_table_sql)
        load_thread_pool()
        cur.execute(clear_table_sql)
        load_process_pool()
