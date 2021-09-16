import sqlite3
from nltk.sentiment.vader import SentimentIntensityAnalyzer

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

def getCourses():
    conn = getConnection()
    courses = conn.execute("select * from course").fetchall()
    conn.close()
    return courses

    
def addFeedback(feedback,course_id):
    conn = getConnection()
    sentiment = SentimentIntensityAnalyzer()
    try:
        predicted_sentiment = "Positive" if sentiment.polarity_scores(feedback)['compound'] > 0 else "Negative"
        conn.execute("insert into feedback(id,content,course_id,sentiment) values(?,?,?,?)",(None, feedback, course_id, predicted_sentiment))
        conn.commit()
        return f"success! predicted sentiment is {predicted_sentiment}"
    except Exception as e:
        print(e)
        return "failure"
    finally:
        conn.close()

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
