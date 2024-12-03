import sqlite3


def get_db_connection():
    connection = sqlite3.connect("tasks.db")
    connection.row_factory = sqlite3.Row
    return connection

def set_up_database():
     with get_db_connection() as connection:
         connection.execute("""
         CREATE TABLE IF NOT EXISTS tasks(
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         title VARCHAR(64) NOT NULL,
         description VARCHAR(256) NOT NULL,
         deadline DATE NOT NULL,
         completed BOOLEAN NOT NULL DEFAULT FALSE        
         );
         """)
