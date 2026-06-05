import sqlite3

# Connect DB
conn = sqlite3.connect("chat_history/chats.db")

cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS chats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_message TEXT,
    bot_response TEXT
)
""")
conn.commit()

# Save chat
def save_chat(user_message, bot_response):
    cursor.execute("""
    INSERT INTO chats (
        user_message,
        bot_response
    )
    VALUES (?, ?)
    """, (user_message, bot_response))
    conn.commit()