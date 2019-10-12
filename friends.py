import hashlib, os, binascii, sqlite3

db_name="prugym.db"

def createdb():
    db = sqlite3.connect(db_name)
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS friends(first TEXT,second TEXT)''')
    db.commit()
    db.close()

def makefriends(friend1, friend2):
    db = sqlite3.connect(db_name)
    cursor = db.cursor()
    cursor.execute('''INSERT INTO friends(first, second) VALUES(?,?)''', (friend1,friend2))
    cursor.execute('''INSERT INTO friends(first, second) VALUES(?,?)''', (friend2,friend1))
    db.commit()
    db.close()

def checkfriends(user):
    db = sqlite3.connect(db_name)
    cursor = db.cursor()
    cursor.execute('''SELECT second FROM friends WHERE first=?''', (user,))
    users = cursor.fetchall()
    for friends in users:
        print(friends)
    db.commit()
    db.close()
