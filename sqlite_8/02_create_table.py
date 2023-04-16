import sqlite3

conn = sqlite3.connect('sqlite_8/app.db')
cursor = conn.cursor()
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER primary key,
        name VARCHAR(50)
    );
    """
)
conn.commit()
conn.close()
