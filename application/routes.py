from application import app, db
from application.models import Users,Posts
from application.forms import PostForm,UserForm
from flask import Flask, redirect, url_for, render_template, request

@app.route('/index')
def index():
    posts = Posts.query.all()

    return render_template("post.html", Post=posts)

@app.route('/indexU')
def indexU():
    posts = Users.query.all()

    return render_template("userList.html", Post=posts)

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
            postData = Posts(
                message = form.message.data,
                userID = form.user.data
                
            )
            
            db.session.add(postData)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('addPost.html', form=form)

@app.route('/update/<id>', methods=['GET', 'POST'])
def update(id):
    form = PostForm()
    post = Posts.query.get(id)

    if form.validate_on_submit():
        post.message = form.message.data
            
        db.session.commit()
        return redirect(url_for('index'))
    elif request.method == 'GET':
        form.message.data = post.message
        return render_template('update.html', post=post,form=form)
    elif request.method == 'POST':
        post.message = form.message.data
            
        db.session.commit()
        return redirect(url_for('index'))


@app.route('/delete/<id>')
def delete(id):
    post_del =Posts.query.get(id)
    db.session.delete(post_del)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/like/<id>')
def like(id):
    post = Posts.query.get(id)
    post.likes +=1
    db.session.commit()
    return redirect(url_for('index'))
@app.route('/dislike/<id>')
def dislike(id):
    post = Posts.query.get(id)
    post.likes -=1
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/addUser', methods=['GET', 'POST'])
def addUser():
    form = UserForm()
    User=Users.query.all()

    if request.method == 'POST':
        if form.validate_on_submit():
            userData = Users(
                userName = form.userName.data,
                firstName = form.firstName.data,
                lastName = form.lastName.data
                
            )
            
            for users in User:
                if users.userName==form.userName.data:
                    form1 = UserForm()
                    return render_template('addUser.html', form=form1 , error="User name already taken pick another one :)")

            
            db.session.add(userData)
            db.session.commit()
            return redirect(url_for('indexU'))
    return render_template('addUser.html', form=form,error="")

@app.route('/user/<id>')
def user(id):
    posts = Posts.query.filter_by(userID=id)
    userName=Users.query.filter_by(id=id).first()

    return render_template("user.html", Post=posts,username=userName.userName,id=id)

@app.route('/deleteU/<id>')
def deleteU(id):
    user_del =Users.query.get(id)
    posts= Posts.query.filter_by(userID=id)
    for post in posts:
        db.session.delete(post)
        db.session.commit()

    db.session.delete(user_del)
    db.session.commit()
    return redirect(url_for('indexU'))



@app.route('/updateU/<id>', methods=['GET', 'POST'])
def updateU(id):
    form = UserForm()
    user = Users.query.get(id)
    User=Users.query.all()

    if form.validate_on_submit():
        user.firstName = form.firstName.data
        user.lastName = form.lastName.data

            
        db.session.commit()
        return redirect(url_for('indexU'))
    elif request.method == 'GET':
        form.firstName.data = user.firstName 
        form.lastName.data = user.lastName 
            
        return render_template('updateU.html', user=user,form=form)
    elif request.method == 'POST':
        user.firstName = form.firstName.data
        user.lastName = form.lastName.data
            
        db.session.commit()
        return redirect(url_for('indexU'))