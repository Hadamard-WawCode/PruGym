import sqlite3, json

def addactivitysql(username):
    zm = "INSERT INTO "+username+"(activity, time, calories, type, distance, pace) VALUES(?,?,?,?,?,?)"
    return zm

def addtrainingsql(username):
    zm = "INSERT INTO "+username+"(activity, calories, type) VALUES(?,?,?)"
    return zm

def insertactivity(username, time, distance, type):
    distance = float(distance) * 1000
    if(type=="swim"):
        calories=distance*0.2
        pace=time*100/distance
    else:
        calories=distance*0.1
        pace=time*1000/distance
    sql=addactivitysql(username)
    db = sqlite3.connect("prugym.db")
    cursor = db.cursor()
    cursor.execute(sql,(type,time,calories,type,float(distance),pace))
    db.commit()
    db.close()

def inserttraining(username,type):
    if(type=="begginer"):
        calories=200
    if(type=="semi"):
        calories=350
    if(type=="pro"):
        calories=600
    sql=addtrainingsql(username)
    db = sqlite3.connect("prugym.db")
    cursor = db.cursor()
    cursor.execute(sql,(type,calories,type))
    db.commit()
    db.close()

def selectbestpacesql(username,type):
    zm = "SELECT MIN(pace) FROM "+username+" WHERE type='"+type+"'"
    return zm

def selectbestdistancesql(username,type):
    zm = "SELECT MAX(distance) FROM "+username+" WHERE type='"+type+"'"
    return zm

def selectbesttimesql(username,type):
    zm = "SELECT MAX(time) FROM "+username+" WHERE type='"+type+"'"
    return zm

def selectbest(username, type, which):
    db = sqlite3.connect("prugym.db")
    cursor = db.cursor()
    if(which=="time"):
        sql=selectbesttimesql(username,type)
    if(which=="distance"):
        sql=selectbestdistancesql(username,type)
    if(which=="pace"):
        sql=selectbestpacesql(username,type)
    cursor.execute(sql)
    ret=cursor.fetchone()
    if(ret==None):
        return "No activities"
    ret0=ret[0]
    db.commit()
    db.close()
    return ret0

def counttra(username, type):
    db = sqlite3.connect("prugym.db")
    cursor = db.cursor()
    if(type == "beginner"):
        sql = "SELECT COUNT(type) FROM "+username+" WHERE type='beginner'"
    if(type == "semi"):
        sql = "SELECT COUNT(type) FROM "+username+"  WHERE type='semi'"
    if(type == "pro"):
        sql = "SELECT SUM(type) FROM "+username+"  WHERE type='pro'"
    cursor.execute(sql)
    ret=cursor.fetchone()
    if(ret == None):
        return "No activities"
    ret0 = ret[0]
    db.commit()
    db.close()
    return ret0

def get_stats(user):
    db = sqlite3.connect("prugym.db")
    cursor = db.cursor()
    query = f"SELECT * FROM {user};"
    res = cursor.execute(query).fetchone()
    db.close()
    return res

def add_pictures(id, names):
    db = sqlite3.connect("prugym.db")
    cursor = db.cursor()
    query = f"SELECT Zdjecie FROM Obiekty WHERE id = {id};"
    print(query)
    res = cursor.execute(query).fetchone()
    newval = json.dumps((json.loads(res[0]) if res[0] else []) + names) #TODO: add insead of replacing
    newval = newval.replace('\"', '\'')
    query2 = f"UPDATE Obiekty SET Zdjecie = \"{newval}\" WHERE id = {id};"
    cursor.execute(query2)
    db.commit()
    db.close()
    return res
