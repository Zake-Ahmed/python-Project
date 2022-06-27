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

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = PostForm()
    form.user.choices=[(users.id,users.userName) for users in Users.query.all()]
    if request.method == 'POST':
        if form.validate_on_submit():
            taskData = Posts(
                message = form.message.data,
                userID = form.user.data
                
            )
            
            db.session.add(taskData)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('addTask.html', form=form)