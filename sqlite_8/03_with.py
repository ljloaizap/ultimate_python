import sqlite3

with sqlite3.connect('sqlite_8/app.db') as conn:
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER primary key,
            name VARCHAR(50)
        );
        """
    )
