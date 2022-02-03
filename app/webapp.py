from flask import Flask, render_template, flash, redirect, url_for, session, request, Blueprint
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, SelectField
from passlib.hash import sha256_crypt
from functools import wraps
import app.s_db as s_db
import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url

home = Blueprint('home', __name__)
program = Blueprint('program', __name__)
student = Blueprint('student', __name__)
college = Blueprint('college', __name__)
course = Blueprint('course', __name__)

@home.route('/')  
def index():
    return render_template('home.html')

# About
@home.route('/about')
def about():
    return render_template('about.html')

# Programs Offered
@program.route('/programs')
def programs():
    return render_template('programs.html')

# College/Course Page
@program.route('/collegelist')
def collegelist():
    return render_template('collegelist.html', college=s_db.collegelist("coll"),course=s_db.collegelist("crs"))

# Register Form Class
class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=7, max=50)])
    username = StringField('Username', [validators.Length(min=7, max=25)])
    email = StringField('Email', [validators.Length(min=7, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')

# User Register
@home.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))
        tuples=(name,email,username,password) 
        s_db.register(tuples)
        flash('You are now registered and can log in', 'success')

        return redirect(url_for('home.index'))
    return render_template('register.html', form=form)

# User login
@home.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get Form Fields
        username = request.form['username']
        password_candidate = request.form['password']
        result = s_db.login(username)
        if len(result) > 0:
            # Get stored hash
            password=result[0][4]
            # Compare Passwords
            if sha256_crypt.verify(password_candidate, password):
                # Passed
                session['logged_in'] = True
                session['username'] = username

                flash('You are now logged in', 'success')
                return redirect(url_for('student.dashboard'))
            else:
                error = 'Invalid login'
                return render_template('login.html', error=error)
        else:
            error = 'Username not found'
            return render_template('login.html', error=error)
    return render_template('login.html')

# Check if user logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('home.login'))
    return wrap

# Logout
@home.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('home.login'))

# Dashboard/Search
@student.route ('/dashboard')
@student.route ('/search_student', methods = ['POST', 'GET'])
def dashboard():
    data=s_db.read("stud")
    if request.method == 'POST':
        newdata = []
        for y in data:
            for z in y:
                if z == request.form['searchbar']:
                    newdata.append (y)
                    break
        data = newdata
    return render_template('dashboard.html', students=data,college=s_db.read("asasdsda"),
                            course=s_db.read("crs"),
                            cloudinary_url=cloudinary_url)


# Edit Student
@student.route('/edit_student', methods = ['POST','GET'])
def edit_student():
    Id = request.form['Id']
    idno = request.form['idno']
    firstname = request.form['firstname']
    gender = request.form['gender']
    lastname = request.form['lastname']
    year = request.form['year']
    course = request.form.get('courses')
    image = request.files.get("photo")
    if request.method == 'POST':
        if image:
            flash("Data Updated Successfully")
            result = cloudinary.uploader.upload(image)
            photo = result.get("public_id")
            tuples=(Id,idno,firstname,lastname,gender,year,course,photo,Id)
            s_db.edit(tuples)
        else:
            tuples=(Id,idno,firstname,lastname,gender,year,course,Id)
            s_db.edits(tuples)
    return redirect(url_for('student.dashboard'))

# Delete Student
@student.route('/delete_student/<string:id>', methods=['POST','GET'])
def delete_student(id):
   s_db.delete(id)
   flash('Student Deleted', 'success')
   return redirect(url_for('student.dashboard'))

# Add Student
@student.route('/add_student', methods=['POST','GET'])
def add_student():
   if request.method == 'POST':
       flash('Student Data Created', 'success')
       idno = request.form['idno']
       photo = request.files.get('photo')
       firstname = request.form['firstname']
       lastname = request.form['lastname']
       gender = request.form['gender']
       year = request.form['year']
       course = request.form['courses']
       result = cloudinary.uploader.upload(photo)
       image = result.get("public_id")
       print(photo)
       tuples=(idno,firstname,lastname,gender,year,course,image)
       print(tuples)
       s_db.addStudent(tuples)
   return redirect(url_for('student.dashboard'))

# Colleges/Search
@college.route('/colleges')
@college.route ('/search_college', methods = ['POST', 'GET'])
def colleges():
   data=s_db.readCollege("coll")
   if request.method == 'POST':
       newdata = []
       for y in data:
           for z in y:
               if z == request.form['searchbar']:
                   newdata.append (y)
                   break
       data = newdata
   return render_template('colleges.html', college=data,student=s_db.read("asasdsda"),course=s_db.read("crs"))

# Delete College
@college.route('/delete_college/<string:college_code>', methods=['POST','GET'])
def delete_college(college_code):
   s_db.deleteCollege(college_code)
   flash('College Deleted', 'success')
   return redirect(url_for('college.colleges'))

# Edit College
@college.route('/edit_college', methods = ['POST','GET'])
def edit_college():
   if request.method == 'POST':
       flash("Data Updated Successfully")
       college_code_old = request.form['college_code_old']
       college_code = request.form['college_code']
       college_name = request.form['college_name']
       tuples=(college_code,college_name,college_code_old)
       s_db.editCollege(tuples)
   return redirect(url_for('college.colleges'))

# Add College
@college.route('/add_college', methods=['POST','GET'])
def add_college():
   if request.method == 'POST':
       flash('College Data Created', 'success')
       college_code = request.form['college_code']
       college_name = request.form['college_name']
       tuples=(college_code,college_name)
       s_db.addCollege(tuples)
   return redirect(url_for('college.colleges'))

# Departments/Search
# Delete Departments

# Courses/Search
@course.route('/courses')
@course.route('/search_courses', methods = ['POST', 'GET'])
def courses():
   data=s_db.readCourse("crs")
   if request.method == 'POST':
       newdata = []
       for y in data:
           for z in y:
               if z == request.form['searchbar']:
                   newdata.append (y)
                   break
       data = newdata
   return render_template('courses.html', course=data,student=s_db.read("asasdsda"),college=s_db.read("coll"))

# Delete Courses
@course.route('/delete_courses/<string:course_code>', methods=['POST','GET'])
def delete_courses(course_code):
   s_db.deleteCourse(course_code)
   flash('Course Deleted', 'success')
   return redirect(url_for('course.courses'))

# Edit Courses
@course.route('/edit_courses', methods = ['POST','GET'])
def edit_courses():
   if request.method == 'POST':
       flash("Data Updated Successfully")
       course_code_old = request.form['course_code_old']
       course_code = request.form['course_code']
       course_name = request.form['course_name']
       college_code = request.form.get('college')
       tuples=(course_code,course_name,college_code,course_code_old)
       s_db.editCourse(tuples)
   return redirect(url_for('course.courses'))

# Add Departments
@course.route('/add_courses', methods=['POST','GET'])
def add_courses():
   if request.method == 'POST':
       flash('Course Data Created', 'success')
       course_code = request.form['course_code']
       course_name = request.form['course_name']
       college_code = request.form.get('college')
       tuples=(course_code,course_name,college_code)
       s_db.addCourse(tuples)
   return redirect(url_for('course.courses'))

