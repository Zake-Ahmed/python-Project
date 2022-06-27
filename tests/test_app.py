# Import the necessary modules
from flask import url_for
from flask_testing import TestCase

# import the app's classes and objects
from application import app, db
from application.models import Users,Posts
from application.forms import UserForm,PostForm
from flask import redirect, url_for, render_template, request

# Create the base class
class TestBase(TestCase):
    def create_app(self):

        # Pass in testing configurations for the app. 
        # Here we use sqlite without a persistent database for our tests.
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///data.db",
                SECRET_KEY="TEST_SECRET_KEY",
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    # Will be called before every test
    def setUp(self):
        # Create table
        db.create_all()
        rootUser = Users(userName="Root",firstName="root",lastName="root")
        db.session.add(rootUser)
        db.session.commit()

        rootUser = Users(userName="Admin",firstName="admin",lastName="admin")
        db.session.add(rootUser)
        db.session.commit()

        rootPost= Posts(message="root" ,userID=1)
        db.session.add(rootPost)
        db.session.commit()

        rootPost= Posts(message="admin" ,userID=2)
        db.session.add(rootPost)
        db.session.commit()

    # Will be called after every test
    def tearDown(self):
        # Close the database session and remove all contents of the database
        db.session.remove()
        db.drop_all()

# Write a test class to test Read functionality
class TestViews(TestBase):
    def test_index_get(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'root', response.data)

    def test_about_get(self):
        response = self.client.get(url_for('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'This is the About Page', response.data)

class TestDislike(TestBase):
    def test_dislike(self):
        response = self.client.post(
            url_for('dislike',id=2),
            data = dict(message="admin" ,userID=2)
        )
        assert Posts.query.get(2).likes == -1

class TestLike(TestBase):
    def test_like(self):
        response = self.client.post(
            url_for('like',id=1),
            data = dict(message="root" ,userID=1,like=0)
        )
        assert Posts.query.get(1).likes == 1
"""
class TestDislike(TestBase):
    def test_dislike(self):
        response = self.client.post(
            url_for('dislike',id=1),
            data = dict(message="root" ,userID=1)
        )
        assert Posts.query.get(1).likes == -1
"""