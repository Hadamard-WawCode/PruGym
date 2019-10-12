import sqlite3

def addactivitysql(username,time,distance,type):
    if(type="swim"):
        calories=distance*0.2
        pace=(time/distance)*100
    else:
        calories=distance*0.1
        pace=(time/distance)*1000
    zm = "INSERT INTO "+username+"(activity, time, calories, type, distance, pace) VALUES("+type+","+time+","+calories+","+type+","+distance+","+pace+")"
    return zm

def addtrainingsql(username, type):
    if(type="begginer"):
        calories=200
    if(type="semi"):
        calories=350
    if(type="pro"):
        calories=600
    zm = "INSERT INTO "+username+"(activity, time, calories, type, pace) VALUES("+type+","+time+","+calories+","+type+","+pace+")"
    return zm

def insertactivity(username, time, distance, type):
    sql=addactivitysql(username,time,distance,type)
    db = sqlite3.connect("prugym.db")
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    db.close()

def inserttraining(username,type):
    sql=addtrainingsql(username,time,distance,type)
    db = sqlite3.connect("prugym.db")
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    db.close()

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
    if(which="time"):
        sql=selectbesttimesql(username,type)
    if(which="distance"):
        sql=selectbestdistancesql(username,type)
    if(which="pace"):
        sql=selectbestpacesql(username,type)
    cursor.execute(sql)
    ret=cursor.fetchone()
    if(ret=None)
        return "No activities"
    ret0=ret[0]
    db.commit()
    db.close()
    return ret0
