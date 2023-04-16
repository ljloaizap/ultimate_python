import sqlite3

with sqlite3.connect('sqlite_8/app.db') as conn:
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users VALUES(?, ?);",
        (1, 'Brian')
    )
