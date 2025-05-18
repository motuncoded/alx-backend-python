import sqlite3

def paginate_users(page_size, offset):
    """Fetches a single page of users from the user_data table starting from the given offset."""
    conn = sqlite3.connect('your_database.db')  # Replace with your actual database file
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user_data LIMIT ? OFFSET ?", (page_size, offset))
    rows = cursor.fetchall()
    conn.close()
    return rows

def lazy_paginate(page_size):
    """Generator that yields each page of users lazily, fetching only when needed."""
    offset = 0
    while True:
        page = paginate_users(page_size, offset)
        if not page:
            break
        yield page
        offset += page_size