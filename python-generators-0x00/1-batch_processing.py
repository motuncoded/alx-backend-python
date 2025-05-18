import sqlite3

def stream_users_in_batches(batch_size):
    """Yields batches of user rows from the user_data table."""
    conn = sqlite3.connect('your_database.db')  # Replace with your DB file
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user_data")
    while True:
        batch = cursor.fetchmany(batch_size)
        if not batch:
            break
        yield batch
    conn.close()

def batch_processing(batch_size):
    """Processes each batch and prints users over the age of 25."""
    for batch in stream_users_in_batches(batch_size):
        # Filter users over the age of 25; assuming age is in the third column (index 2)
        users_over_25 = [user for user in batch if user[2] > 25]
        for user in users_over_25:
            print(user)

# Example usage:
if __name__ == "__main__":
    batch_processing(5)