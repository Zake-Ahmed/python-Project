from application import app, db
from application.models import ToDo,Users,Posts
from application.forms import TaskForm ,PostForm,UserForm
from flask import Flask, redirect, url_for, render_template, request