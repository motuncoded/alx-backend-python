## Objective

Create a Python generator that streams rows from an SQL database one by one.

## Instructions

Write a Python script named `seed.py` that performs the following tasks:

1. **Set up the MySQL database**:  
   - Create a database named `ALX_prodev`.
   - Create a table `user_data` with the following fields:
     - `user_id` (Primary Key, UUID, Indexed)
     - `name` (VARCHAR, NOT NULL)
     - `email` (VARCHAR, NOT NULL)
     - `age` (DECIMAL, NOT NULL)

2. **Populate the database**:  
   - Insert sample data from `user_data.csv` into the `user_data` table.

## Function Prototypes

- `def connect_db()`: Connects to the MySQL database server.
- `def create_database(connection)`: Creates the `ALX_prodev` database if it does not exist.
- `def connect_to_prodev()`: Connects to the `ALX_prodev` database in MySQL.
- `def create_table(connection)`: Creates the `user_data` table if it does not exist with the required fields.
- `def insert_data(connection, data)`: Inserts data into the database if it does not exist.