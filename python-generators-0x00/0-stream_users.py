import sqlite3

def stream_users():
    conn = sqlite3.connect('your_database.db')  # Change to your DB file
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user_data")
    for row in cursor:
        yield row
    conn.close()
