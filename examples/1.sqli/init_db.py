import sqlite3

con = sqlite3.connect("db.sqlite3")
cur = con.cursor()
cur.execute("CREATE TABLE users (name, pwd)")
cur.execute("INSERT INTO users VALUES (?, ?), (?, ?), (?, ?)", ('admin', 'pwd', 'user1', 'pwd1', 'user2', 'pwd2'))

cur.execute("CREATE TABLE secret (msg)")
con.execute('INSERT INTO secret VALUES (?)', ('This should not be found', ))