import hashlib, os, binascii, sqlite3

db_name="prugym.db"

def createdb():
    db = sqlite3.connect(db_name)
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS treningi(id INTEGER, cwiczenie TEXT, czas INTEGER)''')
    db.commit()
    db.close()

def dodajcwiczenie(numerek, friend1, friend2):
    db = sqlite3.connect(db_name)
    cursor = db.cursor()
    cursor.execute('''INSERT INTO treningi(id, cwiczenie, czas) VALUES(?,?,?)''', (numerek,friend1,friend2))
    db.commit()
    db.close()

createdb()
dodajcwiczenie(1,"Orbiterek",5)
dodajcwiczenie(2, "Wahadło",3)
dodajcwiczenie(3,"Biegacz",3)
dodajcwiczenie(4,"Twister",2)
dodajcwiczenie(5,"Wioślarz",4)
dodajcwiczenie(6,"Wyciskacz",2)

dodajcwiczenie(7,"Orbiterek",7)
dodajcwiczenie(8, "Wahadło",4)
dodajcwiczenie(9,"Biegacz",4)
dodajcwiczenie(10,"Twister",4)
dodajcwiczenie(11,"Wioślarz",6)
dodajcwiczenie(12,"Wyciskacz",4)

dodajcwiczenie(13,"Orbiterek",8)
dodajcwiczenie(14, "Wahadło",6)
dodajcwiczenie(15,"Biegacz",5)
dodajcwiczenie(16,"Twister",5)
dodajcwiczenie(17,"Wioślarz",6)
dodajcwiczenie(18,"Wyciskacz",5)
