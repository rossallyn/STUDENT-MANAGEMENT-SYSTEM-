from flask import Flask
from os import getenv
from flask_mysqldb import MySQL
from config import CLOUD_NAME, API_KEY, API_SECRET
import cloudinary

mysql = MySQL()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = getenv('SECRET_KEY')
    app.config['MYSQL_HOST'] = getenv('DB_HOST')
    app.config['MYSQL_USER'] = getenv('DB_USERNAME')
    app.config['MYSQL_PASSWORD'] = getenv('DB_PASSWORD')
    app.config['MYSQL_DB'] = getenv('DB_NAME')
    mysql.init_app(app)
    cloudinary.config(
        cloud_name=CLOUD_NAME,
        api_key=API_KEY,
        api_secret=API_SECRET,)



    if __name__ == '__main__':
        app.run(debug=True)


    from .webapp import home, program, student, college, course

    app.register_blueprint(home, url_prefix='/')
    app.register_blueprint(program, url_prefix='/')
    app.register_blueprint(student, url_prefix='/')
    app.register_blueprint(college, url_prefix='/')
    app.register_blueprint(course, url_prefix='/')

    return app