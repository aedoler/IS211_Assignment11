#!user/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect
app = Flask(__name__)
todoList = []

@app.route('/')
def hello_world():

    return render_template('index.html')

@app.route('/todolist', methods = ['POST'])
def signup():
    email = request.form['todo']
    todoList.append(email)
    for email1 in todoList:
        print 'Entered:{} '.format(email1)
    return redirect('/')





if __name__ == "__main__":
    app.run()