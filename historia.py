import sqlite3

def addactivitysql(username):
    zm = "INSERT INTO "+username+"(activity, time, calories, type, distance, pace) VALUES(?,?,?,?,?,?)"
    return zm

def addtrainingsql(username):
    zm = "INSERT INTO "+username+"(activity, calories, type) VALUES(?,?,?)"
    return zm

def insertactivity(username, time, distance, type):
    if(type=="swim"):
        calories=distance*0.2
        pace=time*100/distance
    else:
        calories=distance*0.1
        pace=time*1000/distance
    sql=addactivitysql(username)
    db = sqlite3.connect("prugym.db")
    cursor = db.cursor()
    cursor.execute(sql,(type,time,calories,type,distance,pace))
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

insertactivity("Adam", 35, 10000, "swim")
insertactivity("Adam", 35, 10000, "run")
inserttraining("Adam","begginer")

def selectbestpacesql(username,type):
    zm = "SELECT MIN(pace) FROM "+username+" WHERE type='"+type+"'"
    return zm

def selectbestdistancesql(username,type):
    zm = "SELECT MAX(distance) FROM "+username+" WHERE type='"+type+"'"
    return zm

def selectbesttimeesql(username,type):
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
