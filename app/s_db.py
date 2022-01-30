import mysql.connector 

mysql=mysql.connector.connect(host="localhost",user="root",password="root",db ="student_db")
cur=mysql.cursor()


def register(tuples):
    cur.execute("INSERT INTO userlogin(name, email, username, password) VALUES (%s, %s, %s, %s)", tuples)
    mysql.commit()


def login(username):
    result = cur.execute("SELECT * FROM userlogin WHERE username = %s", [username])
    return cur.fetchall()

def collegelist(dashboard):
    if dashboard == "coll":
        cur.execute("SELECT * FROM college")
    elif dashboard == "crs":
        cur.execute("SELECT * FROM course")
    else:
        cur.execute("SELECT * FROM students")
    return cur.fetchall()

#Student DB  
def read(dashboard):
    if dashboard == "stud":
        cur.execute("SELECT * FROM students")
    elif dashboard == "crs":
        cur.execute("SELECT * FROM course")
    else:
        cur.execute("SELECT * FROM college")
    return cur.fetchall()

def delete(id):
    cur.execute("DELETE FROM students WHERE id = %s", (id,))
    mysql.commit()

def edit(tuples):
    cur.execute("UPDATE students SET id=%s, idno=%s, firstname=%s, lastname=%s, gender=%s, year=%s, course=%s, photo=%s where id=%s",tuples)
    mysql.commit()

def edits(tuples):
    cur.execute("UPDATE students SET id=%s, idno=%s, firstname=%s, lastname=%s, gender=%s, year=%s, course=%s where id=%s",tuples)
    mysql.commit()

def addStudent(tuples):
    cur.execute("INSERT INTO students(idno, firstname, lastname, gender, year, course, photo) VALUES(%s, %s, %s, %s, %s, %s, %s)",tuples)
    mysql.commit()

#College DB 
def readCollege(dashboard):
    if dashboard == "coll":
        cur.execute("SELECT * FROM college")
    elif dashboard == "crs":
        cur.execute("SELECT * FROM course")
    else:
        cur.execute("SELECT * FROM students")
    return cur.fetchall()

def deleteCollege(college_code):
    cur.execute("DELETE FROM college WHERE college_code = %s", [college_code])
    mysql.commit()

def editCollege(tuples):
    cur.execute("UPDATE college SET college_code=%s, college_name=%s where college_code=%s",tuples)
    mysql.commit()

def addCollege(tuples):
    cur.execute("INSERT INTO college(college_code, college_name) VALUES(%s, %s)",tuples)
    mysql.commit()

#Department DB

#Courses DB
def readCourse(dashboard):
    if dashboard == "coll":
        cur.execute("SELECT * FROM college")
    elif dashboard == "crs":
        cur.execute("SELECT * FROM course")
    else:
        cur.execute("SELECT * FROM students")
    return cur.fetchall()

def deleteCourse(course_code):
    cur.execute("DELETE FROM course WHERE course_code = %s", [course_code])
    mysql.commit()

def editCourse(tuples):
    cur.execute("UPDATE course SET course_code=%s, course_name=%s, coll_code=%s where course_code=%s",tuples)
    mysql.commit()

def addCourse(tuples):
    cur.execute("INSERT INTO course(course_code,course_name,coll_code) VALUES(%s, %s, %s)",tuples)
    mysql.commit()
