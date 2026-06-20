import sqlite3

password = "admin123"

def get_user(username):
    conn = sqlite3.connect("users.db")
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    result = conn.execute(query).fetchall()
    return result

def calc(x):
    return eval(x)

print("Hello World")