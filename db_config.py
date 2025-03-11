# db_config.py
import sqlite3
from datetime import datetime

def create_connection():
    conn = sqlite3.connect("chat_data.db")
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chat_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_text TEXT NOT NULL,
            bot_response TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def insert_chat_data(user_text, bot_response):
    conn = create_connection()
    cursor = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("""
        INSERT INTO chat_history (user_text, bot_response, timestamp)
        VALUES (?, ?, ?)
    """, (user_text, bot_response, timestamp))
    conn.commit()
    conn.close()

# Call this once at the start
create_table()