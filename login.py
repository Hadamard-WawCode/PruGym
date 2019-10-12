import hashlib, os, binascii, sqlite3

def hash(password):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')

def verify(stored_password, provided_password):
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', provided_password.encode('utf-8'),salt.encode('ascii'),100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password

def createdb():
    db = sqlite3.connect("prugym.db")
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users(name TEXT,password TEXT)''')
    db.commit()
    db.close()

def insertuser(username, hash):
    db = sqlite3.connect("prugym.db")
    cursor = db.cursor()
    cursor.execute('''INSERT INTO users(name,password) VALUES(?,?)''', (username,hash))
    db.commit()
    db.close()

def createsql(username):
    zm = "CREATE TABLE IF NOT EXISTS "+username+"(activity TEXT,time INTEGER, startlat TEXT, startlon TEXT, calories INTEGER, type TEXT, distance REAL, pace REAL)"
    return zm

def createuserdb(username):
    db = sqlite3.connect("prugym.db")
    cursor = db.cursor()
    sql=createsql(username)
    cursor.execute(sql)
    db.commit()
    db.close()

def signup_f(user, passwd):
    try:
        passwdhash=hash(passwd)
        insertuser(user,passwdhash)
        createuserdb(user)
    except:
        return False
    return True

def login_f(user, passwd):
    db = sqlite3.connect("prugym.db")
    cursor = db.cursor()
    cursor.execute('''SELECT password FROM users WHERE name=?''', (user,))
    users = cursor.fetchone()
    if users == None:
        return False
    user1=users[0]
    db.commit()
    db.close()
    return verify(user1, passwd)
