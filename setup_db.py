import sqlite3
import os

DB_PATH = 'games.db'

def setup_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS games (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            genre TEXT NOT NULL,
            year INTEGER,
            players INTEGER
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Database creato con successo!")

if __name__ == '__main__':
    setup_database()