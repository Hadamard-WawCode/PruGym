import sqlite3

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
    return res

def add_object(typ, nazwa, adres, dzielnica, lat, lon, opis, url_zdjecia):
    try:
        db = sqlite3.connect("prugym.db")
        cursor = db.cursor()
        q = f"""INSERT INTO Obiekty (Typ, Nazwa, Adres, Dzielnica, lat, lon, Opis, Zdjecie) 
            values ('{typ}', '{nazwa}', '{adres}', '{dzielnica}', '{lat}', '{lon}', '{opis}', '{url_zdjecia}')"""
        cursor.execute(q)
        db.commit()
        db.close()
    except:
        return False
    return True

def add_workout():
    pass