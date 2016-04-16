#!user/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect
import re
import os
import pickle


class NotValidEmail(Exception):
    pass

app = Flask(__name__)

todoList = []


@app.route('/')
def hello_world():

    return render_template('index.html', todoList = todoList)

@app.route('/submit', methods = ['POST'])
def submit():
    task = request.form['todo']
    email = request.form['email']
    priority = request.form['priority']


    if not re.search('(@)', email):
        return render_template('error.html', methods = ['POST'])

    if os.path.exists('todolist.pkl'):
        filehandler = open('todolist.pkl', 'rb')
        todoList = pickle.load(filehandler)
        filehandler.close()

    todoList.append((task, email, priority))
    filehandler = open('todolist.pkl', 'wb')
    pickle.dump(todoList, filehandler)
    global todoList

    for item in todoList:
        print 'Entered: {}, for Email: {},  with a priority of {} '.format(item[0], item[1], item[2])
    filehandler.close()

    return redirect('/')

"""
@app.errorhandler('/error', methods = ['POST'])
def errorhandler():

    return render_template('error.html', ) """





if __name__ == "__main__":
    app.run()