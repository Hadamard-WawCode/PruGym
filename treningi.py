import hashlib, os, binascii, sqlite3

db_name="prugym.db"

def createdb():
    db = sqlite3.connect(db_name)
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS treningi(id INTEGER, cwiczenie TEXT, czas INTEGER, link TEXT)''')
    db.commit()
    db.close()

def dodajcwiczenie(numerek, friend1, friend2, link):
    db = sqlite3.connect(db_name)
    cursor = db.cursor()
    cursor.execute('''INSERT INTO treningi(id, cwiczenie, czas, link) VALUES(?,?,?, ?)''', (numerek,friend1,friend2, link))
    db.commit()
    db.close()

createdb()
dodajcwiczenie(1,"Orbiterek",5, "http://prudens.vot.pl/orbiterek.jpg")
dodajcwiczenie(2, "Wahadło",3, "http://prudens.vot.pl/wahadlo.jpg")
dodajcwiczenie(3,"Biegacz",3, "http://prudens.vot.pl/biegacz.jpg")
dodajcwiczenie(4,"Twister",2, "http://prudens.vot.pl/twister.jpg")
dodajcwiczenie(5,"Wioślarz",4, "http://prudens.vot.pl/wioslarz.jpg")
dodajcwiczenie(6,"Wyciskacz",2, "http://prudens.vot.pl/wyciskacz.jpg")

dodajcwiczenie(7,"Orbiterek",7, "http://prudens.vot.pl/orbiterek.jpg")
dodajcwiczenie(8, "Wahadło",4, "http://prudens.vot.pl/wahadlo.jpg")
dodajcwiczenie(9,"Biegacz",4, "http://prudens.vot.pl/biegacz.jpg")
dodajcwiczenie(10,"Twister",4, "http://prudens.vot.pl/twister.jpg")
dodajcwiczenie(11,"Wioślarz",6, "http://prudens.vot.pl/wyciskacz.jpg")
dodajcwiczenie(12,"Wyciskacz",4)

dodajcwiczenie(13,"Orbiterek",8, "http://prudens.vot.pl/orbiterek.jpg")
dodajcwiczenie(14, "Wahadło",6, "http://prudens.vot.pl/wahadlo.jpg")
dodajcwiczenie(15,"Biegacz",5, "http://prudens.vot.pl/biegacz.jpg")
dodajcwiczenie(16,"Twister",5, "http://prudens.vot.pl/twister.jpg")
dodajcwiczenie(17,"Wioślarz",6, "http://prudens.vot.pl/wioslarz.jpg")
dodajcwiczenie(18,"Wyciskacz",5, "http://prudens.vot.pl/wyciskacz.jpg")
