#!user/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect
import re
import os
import pickle


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

    if not re.search('([^@|\s]+@[^@]+\.[^@|\s]+)', email): #Checks for correct email
        errorvalue = 'email address!'
        return render_template('error.html', methods = ['GET', 'POST'], errorvalue = errorvalue )
    elif not re.search('(high|medium|low)', priority): #Added value "none" in html to test this
        errorvalue = 'priority!'
        return render_template('error.html', methods = ['GET', 'POST'], errorvalue = errorvalue )


    if os.path.exists('todolist.pkl'): #Checks if file exists so as to not overwrite it
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


@app.route('/clear', methods = ['GET', 'POST']) #So far, this functions DOES delete the list, however I it does not refresh the list
def clear():                             #on the screen until you restart the app, which start with a cleared list.

    todoList = [] # Deletes content in list
    filehandler = open('todolist.pkl', 'wb')
    pickle.dump(todoList, filehandler)
    filehandler.close()
    return render_template('index.html', todoList=todoList)


if __name__ == "__main__":
    app.run()