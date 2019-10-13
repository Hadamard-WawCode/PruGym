import sqlite3, json

def get_all_objects():
    db = sqlite3.connect("prugym.db")
    cursor = db.cursor()
    res = cursor.execute("SELECT id, Typ, lat, lon FROM Obiekty").fetchall()
    db.close()
    return res

def get_object(id):
    db = sqlite3.connect("prugym.db")
    cursor = db.cursor()
    res = cursor.execute(f"SELECT * FROM Obiekty WHERE id = {id}").fetchone()
    db.close()
    if res[3] != '':
        res = list(res)
        res[3] = '(' + res[3] + ')'
        res = tuple(res)
    return res

def add_photos(id, url_list_zdjec):
    try:
        url_list_zdjec = json.dumps(url_list_zdjec)
        db = sqlite3.connect("prugym.db")
        cursor = db.cursor()
        q = f"""INSERT INTO Obiekty (Zdjecie) WHERE id={id}
            values ('{url_list_zdjec}')"""
        cursor.execute(q)
        db.commit()
        db.close()
    except:
        return False
    return True

def addevent(nazwa,opis,user,location):
    db = sqlite3.connect("prugym.db")
    cursor = db.cursor()
    sql="CREATE TABLE IF NOT EXISTS wydarzenia('id' INTEGER PRIMARY KEY AUTOINCREMENT,'nazwa' TEXT,'opis' TEXT,'user' TEXT,'location' TEXT, 'ilosc' INTEGER);"
    cursor.execute(sql)
    sql1="INSERT INTO wydarzenia(nazwa,opis,user,location) VALUES(?,?,?,?)"
    cursor.execute(sql1, (nazwa,opis,user,location))
    cursor.execute("SELECT MAX(id) FROM wydarzenia")
    sel=cursor.fetchone()
    id=sel[0]
    sql2="INSERT INTO "+user+"_events(id) VALUES(?)"
    cursor.execute(sql2,(id,))
    cursor.execute("INSERT INTO "+location+"(id) VALUES(?)", (id,))
    db.commit()
    db.close()
    return id

def infowyd(numer):
    db = sqlite3.connect("prugym.db")
    cursor = db.cursor()
    cursor.execute("SELECT name FROM wydarzenia WHERE id=(?)", (numer,))
    name=cursor.fetchone()[0]
    cursor.execute("SELECT opis FROM wydarzenia WHERE id=(?)", (numer,))
    opis=cursor.fetchone()[0]
    cursor.execute("SELECT user FROM wydarzenia WHERE id=(?)", (numer,))
    user=cursor.fetchone()[0]
    cursor.execute("SELECT location FROM wydarzenia WHERE id=(?)", (numer,))
    location=cursor.fetchone()[0]
    cursor.execute("SELECT ilosc FROM wydarzenia WHERE id=(?)", (numer,))
    ilosc=cursor.fetchone()[0]
    db.commit()
    db.close()
    return name,opis,user,location,ilosc

def wszystkieuzyt(user):
    arr=[]
    db = sqlite3.connect("prugym.db")
    cursor = db.cursor()
    cursor.execute("SELECT id FROM "+user+"_events")
    tab=cursor.fetchall()
    for i in tab:
        arr.append(i[0])
    db.commit()
    db.close()
    return arr

def wszystkieob(obiekt):
    arr=[]
    db = sqlite3.connect("prugym.db")
    cursor = db.cursor()
    cursor.execute("SELECT id FROM "+obiekt)
    tab=cursor.fetchall()
    for i in tab:
        arr.append(i[0])
    db.commit()
    db.close()
    return arr
