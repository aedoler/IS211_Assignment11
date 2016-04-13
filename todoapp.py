#!user/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect
app = Flask(__name__)
todoList = []

@app.route('/')
def hello_world():

    return render_template('index.html', todoList = todoList)

@app.route('/todolist', methods = ['POST'])
def signup():
    task = request.form['todo']
    email = request.form['email']
    priority = request.form['priority']

    todoList.append((task, email, priority))
    for item in todoList:
        print 'Entered: {}, for Email: {},  with a priority of {} '.format(item[0], item[1], item[2])
    return redirect('/')




if __name__ == "__main__":
    app.run()