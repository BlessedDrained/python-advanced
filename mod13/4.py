import sqlite3


def ivan_sovin_the_most_effective(cursor, name):
    ivan_sovin_salary = cursor.execute("SELECT salary FROM table_effective_manager WHERE name = 'Иван Совин'").fetchone()[0]
    employee = cursor.execute("SELECT * FROM table_effective_manager WHERE name=?", (name,)).fetchone()
    if not employee:
        print(f"{name} is not found in DB")
    elif name == 'Иван Совин':
        print("Effective manager's salary cannot be changed")
    else:
        increased_salary = int(employee[2] * 1.1)
        if increased_salary > ivan_sovin_salary:
            cursor.execute("DELETE FROM table_effective_manager WHERE name=?", (name,))
            print(f"Employee {name} is fired because his salary is higher that Ivan Sovin's one")
        else:
            cursor.execute("UPDATE table_effective_manager SET salary = ? WHERE name = ?", (increased_salary, name))
            print(f"{name}'s salary has been increased")


def main():
    with sqlite3.connect("hw.db") as conn:
        cursor = conn.cursor()
        employee_name = input("Employee's name: ")
        ivan_sovin_the_most_effective(cursor, employee_name)


if __name__ == "__main__":
    main()
