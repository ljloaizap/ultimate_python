import sqlite3

with sqlite3.connect('sqlite_8/app.db') as conn:
    users = [
        (2, 'Chanchito'),
        (3, 'Jaun'),
        (4, 'Mery'),
    ]
    cursor = conn.cursor()
    cursor.executemany(
        "INSERT INTO users VALUES(?, ?);",
        users
    )
