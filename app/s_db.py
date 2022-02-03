from app import mysql


def register(tuples):
    cur = mysql.connection.cursor() 
    cur.execute("INSERT INTO userlogin(name, email, username, password) VALUES (%s, %s, %s, %s)", tuples)
    mysql.connection.commit()

def login(username):
    cur = mysql.connection.cursor() 
    result = cur.execute("SELECT * FROM userlogin WHERE username = %s", [username])
    return cur.fetchall()

def collegelist(dashboard):
    cur = mysql.connection.cursor() 
    if dashboard == "coll":
        cur.execute("SELECT * FROM college")
    elif dashboard == "crs":
        cur.execute("SELECT * FROM course")
    else:
        cur.execute("SELECT * FROM students")
    return cur.fetchall()

#Student DB  
def read(dashboard):
    cur = mysql.connection.cursor() 
    if dashboard == "stud":
        cur.execute("SELECT * FROM students")
    elif dashboard == "crs":
        cur.execute("SELECT * FROM course")
    else:
        cur.execute("SELECT * FROM college")
    return cur.fetchall()

def delete(id):
    cur = mysql.connection.cursor() 
    cur.execute("DELETE FROM students WHERE id = %s", (id,))
    mysql.connection.commit()

def edit(tuples):
    cur = mysql.connection.cursor() 
    cur.execute("UPDATE students SET id=%s, idno=%s, firstname=%s, lastname=%s, gender=%s, year=%s, course=%s, photo=%s where id=%s",tuples)
    mysql.connection.commit()

def edits(tuples):
    cur = mysql.connection.cursor() 
    cur.execute("UPDATE students SET id=%s, idno=%s, firstname=%s, lastname=%s, gender=%s, year=%s, course=%s where id=%s",tuples)
    mysql.connection.commit()

def addStudent(tuples):
    cur = mysql.connection.cursor() 
    cur.execute("INSERT INTO students(idno, firstname, lastname, gender, year, course, photo) VALUES(%s, %s, %s, %s, %s, %s, %s)",tuples)
    mysql.connection.commit()

#College DB 
def readCollege(dashboard):
    cur = mysql.connection.cursor() 
    if dashboard == "coll":
        cur.execute("SELECT * FROM college")
    elif dashboard == "crs":
        cur.execute("SELECT * FROM course")
    else:
        cur.execute("SELECT * FROM students")
    return cur.fetchall()

def deleteCollege(college_code):
    cur = mysql.connection.cursor() 
    cur.execute("DELETE FROM college WHERE college_code = %s", [college_code])
    mysql.connection.commit()

def editCollege(tuples):
    cur = mysql.connection.cursor() 
    cur.execute("UPDATE college SET college_code=%s, college_name=%s where college_code=%s",tuples)
    mysql.connection.commit()

def addCollege(tuples):
    cur = mysql.connection.cursor() 
    cur.execute("INSERT INTO college(college_code, college_name) VALUES(%s, %s)",tuples)
    mysql.connection.commit()

#Courses DB
def readCourse(dashboard):
    cur = mysql.connection.cursor() 
    if dashboard == "coll":
        cur.execute("SELECT * FROM college")
    elif dashboard == "crs":
        cur.execute("SELECT * FROM course")
    else:
        cur.execute("SELECT * FROM students")
    return cur.fetchall()

def deleteCourse(course_code):
    cur = mysql.connection.cursor() 
    cur.execute("DELETE FROM course WHERE course_code = %s", [course_code])
    mysql.connection.commit()

def editCourse(tuples):
    cur = mysql.connection.cursor() 
    cur.execute("UPDATE course SET course_code=%s, course_name=%s, coll_code=%s where course_code=%s",tuples)
    mysql.connection.commit()

def addCourse(tuples):
    cur = mysql.connection.cursor() 
    cur.execute("INSERT INTO course(course_code,course_name,coll_code) VALUES(%s, %s, %s)",tuples)
    mysql.connection.commit()
