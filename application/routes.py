from application import app, db
from application.models import ToDo,Users,Posts
from application.forms import TaskForm ,PostForm,UserForm
from flask import Flask, redirect, url_for, render_template, request

@app.route('/index')
def index():
    posts = Posts.query.all()

    return render_template("task.html", Posts=posts)

@app.route('/indexU')
def indexU():
    posts = Users.query.all()

    return render_template("userList.html", Posts=posts)

@app.route('/about')
def about():
    return render_template("about.html")