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


def get_stats(user):
    db = sqlite3.connect("prugym.db")
    cursor = db.cursor()
    query = f"SELECT * FROM {user};"
    print(query)
    res = cursor.execute(query).fetchone()
    db.close()
    return res
