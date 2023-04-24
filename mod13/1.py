import sqlite3
import pandas as pd


def check_if_vaccine_has_spoiled(truck_number):
    with sqlite3.connect("hw.db") as con:
        result = pd.read_sql(
            "SELECT COUNT(*) as c FROM (SELECT * FROM table_truck_with_vaccine WHERE truck_number = ? AND temperature_in_celsius NOT BETWEEN -20 AND -16)",
            con, params={truck_number})
    return int(result["c"][0]) > 2


def main():
    truck_number = input()
    result = check_if_vaccine_has_spoiled(truck_number)
    print(result)


if __name__ == '__main__':
    main()
