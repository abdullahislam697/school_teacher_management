import flask
from flask import Flask, render_template, request, session, flash
from flask_login import login_user
from sqlalchemy.sql.functions import user

print(__file__)

import os
project_dir = os.path.dirname(os.path.abspath(__file__))
myApp =  Flask(__name__)

print(project_dir)

from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "bookdatabase.db"))

myApp.config["SQLALCHEMY_DATABASE_URI"] = database_file
myApp.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False



db = SQLAlchemy(myApp)

# db.create_all()

class User(db.Model):
    name = db.Column(db.String(40),unique=True, nullable=False, primary_key = True)
    password = db.Column(db.String(40),unique=False, nullable=False)
    city = db.Column(db.String(40),unique=False, nullable=False)

class Student(db.Model):
    name = db.Column(db.String(40), unique=True, nullable=False, primary_key=True)
    password = db.Column(db.String(40), unique=False, nullable=False)
    city = db.Column(db.String(40), unique=False, nullable=False)

class Teacher(db.Model):
    name = db.Column(db.String(40), unique=True, nullable=False, primary_key=True)
    password = db.Column(db.String(40),unique=False, nullable=False)
    city = db.Column(db.String(40),unique=False, nullable=False)
# # db.create_all()

@myApp.route('/signup')
def signup():
    return render_template('signup.html')

@myApp.route('/users')
def users_users1():
    myUsers = Teacher.query.all()
   # myUsers = Student.query.all()
    return render_template('users.html', users=myUsers)
def users1():
    myUsers1 = Student.query.all()
   # myUsers = Student.query.all()
    return render_template('users.html', users=myUsers1)



@myApp.route('/delete', methods=["POST"])
def delete_user():
    user_name = request.form['target_user']

    user_found = Teacher.filter_by(name=user_name).first()

    db.session.delete(user_found)
    db.session.commit()

    myUsers = Teacher.query.all()


    return render_template('users.html', users=myUsers)

def delete_user1():
    user1_name = request.form['target_user1']

    user1_found = Student.filter_by(name=user1_name).first()

    db.session.delete(user1_found)
    db.session.commit()

    myUsers1 = Student.query.all()


    return render_template('users.html', users=myUsers1)
@myApp.route('/')
def index():
    return render_template('index.html')





@myApp.route('/login',methods=['POST','GET'])
def login():

      return render_template('login.html')
    #return "<h1>Hello login!</h1><h1>Hello login!</h1><h1>Hello login!</h1>"

@myApp.route('/test1', methods=["POST", "GET"])
def mySignup():
    # print(request.form['username'])

    if request.method == "POST":
        user1 = Teacher()
        user1.name = request.form['username']
        user1.password = request.form['pass']
        user1.city = request.form['city']

        # user2 = Student()
        # user2.name = request.form['username']
        # user2.password = request.form['pass']
        # user2.city = request.form['city']

        db.session.add(user1)
        db.session.commit()



    return render_template('signup.html')


# print(__name__)

# if __name__ == "__main__":
myApp.run(debug=True)


