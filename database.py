import sqlite3

def getConnection(dbfile="data.db"):
    try:
        conn = sqlite3.connect(dbfile)
        return conn
    except Exception as e:
        return None

def createTables():
    #create course table
    conn = getConnection()
    if conn:
        conn.execute("create table course(id integer primary key autoincrement, name varchar(50) not null, fees int not null)")
        conn.commit()
        conn.execute('''create table feedback(id integer primary key autoincrement, 
                        content text not null,
                        sentiment varchar(20),
                        course_id integer not null,
                        foreign key(course_id) references course(id))
                    ''')
        conn.commit()
        conn.close()
        print("created tables successfully")
    else:
        print("Could not connect to db")

def addCourse(name, fees):
    conn = getConnection()
    try:
        conn.execute("insert into course(id,name,fees) values(?,?,?)",(None, name,fees))
        conn.commit()
        return "success"
    except Exception as e:
        print(e)
        return "failure"
    finally:
        conn.close()

if __name__ == "__main__":
    # createTables()
    print(addCourse('python',5000))
