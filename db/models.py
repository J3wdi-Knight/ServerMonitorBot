from datetime import datetime
import sqlite3

def init_db():
    with sqlite3.connect('myDB.db') as conn:
        cursor = conn.cursor()

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            alerts_enable BOOLEAN DEFAULT 0
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS alert_settings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            cpu_threshold INTEGER,
            ram_threshold INTEGER
        )
        ''')
    print("DB is initialized")

def add_user(username, isenable=False):
    with sqlite3.connect('myDB.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (username, alerts_enable) VALUES (?, ?)', (username, isenable))
        conn.commit()

        cursor.execute('SELECT * FROM users')
        print('Users:', cursor.fetchall())
