import sqlite3
from datetime import datetime, date, time


db = sqlite3.connect("my.db")

sql = db.cursor()

def addUser(name):
    sql.execute(f"SELECT name FROM users WHERE name = '{name}'")
    if(sql.fetchone() is None):
        print("User is registered")
        sql.execute("INSERT INTO users (name) VALUES (?)", [name])
        db.commit()
        return True
    else:
        print("User is already registered")
        return False

def getUser(name):
    sql.execute(f"SELECT name FROM users WHERE name = '{name}'")
    if(sql.fetchone() is None):
        return False
    else:
        return True

def addStyle(name, word):
    word = word.lower()
    sql.execute(f"SELECT word FROM style INNER JOIN users ON style.user_id=users.id WHERE users.name = '{name}' AND word = '{word}'")
    if(sql.fetchone() is None):
        sql.execute(f"SELECT id FROM users WHERE name = '{name}'")
        myId = sql.fetchone()
        sql.execute(f"INSERT INTO style (word, user_id) VALUES ('{word}', '{myId[0]}')")
        db.commit()
        return True

    else:
        return False
def delStyle(name, word):
    word = word.lower()
    sql.execute(f"SELECT word FROM style INNER JOIN users ON style.user_id=users.id WHERE users.name = '{name}' AND word = '{word}'")
    if(sql.fetchone() is None):
        return False
    else:
        sql.execute(f"SELECT id FROM users WHERE name = '{name}'")
        myId = sql.fetchone()
        sql.execute(f"DELETE FROM style WHERE word='{word}' AND  user_id ='{myId[0]}'")
        db.commit()
        return True

def getStyle(name):
    sql.execute(f"SELECT word FROM style INNER JOIN users ON style.user_id=users.id WHERE users.name = '{name}'")

    return sql.fetchall()

def addFileName(filename):
    sql.execute(f"INSERT INTO files (name) VALUES ('{filename}') ")
    db.commit()

def endTime(filename, startDateTime):
    sql.execute(f"SELECT id FROM files WHERE name = '{filename}'")
    idFile = sql.fetchone()
    currentTime = datetime.now()
    sql.execute(f"INSERT INTO history  (file_id ,start_date,end_date) VALUES ('{idFile[0]}', '{startDateTime}', '{currentTime}') ")
    db.commit()
    return currentTime

def addStats(filename, grade, tov , prod):
    sql.execute(f"SELECT id FROM files WHERE name ='{filename}' ORDER BY id DESC LIMIT 1")
    newestId = sql.fetchone()
    sql.execute(f"UPDATE files SET grade = '{grade}', tov = '{tov}', prod = '{prod}' WHERE id = '{newestId[0]}'")
    db.commit()

def getGrade(filename):
    sql.execute(f"SELECT grade FROM files WHERE name = '{filename}'")
    return sql.fetchall()

def getTov(filename):
    sql.execute(f"SELECT tov FROM files WHERE name = '{filename}'")
    return sql.fetchall()

def getProd(filename):
    sql.execute(f"SELECT prod FROM files WHERE name = '{filename}'")
    return sql.fetchall()

#addStats("D:/DimonCource/MytestFile.txt", 1, 10, 5)