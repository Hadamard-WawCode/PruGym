from flask import Flask, flash, render_template, redirect, request, url_for, jsonify, session
from login import signin, login

app = Flask(__name__)

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('index'))
    else:
        return redirect(url_for('signin'))

@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login')
def index():
    if 'username' in session:
        return redirect(url_for('index'))
    if request.method == 'POST':
        username = request.form['user']
        password = request.form['password']
        if login(username, password):
            session['username'] = username
            session['password'] = password
            return redirect(url_for('index'))
        else:
        	#zły login lub hasło
            return render_template('login.html',)

    return render_template('login.html')


@app.route('/signin')
def index():
    if 'username' in session:
        return redirect(url_for('index'))
    if request.method == 'POST':
        username = request.form['user']
        password = request.form['password']
        if signin(username, password):
            return redirect(url_for('login'))
        else:
        	#zły login lub hasło
            return render_template('signin.html')

    return render_template('signin.html')