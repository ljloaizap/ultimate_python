import sqlite3

with sqlite3.connect('sqlite_8/app.db') as conn:
    sql = "SELECT * FROM users;"
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for r in result:
        print(r)
