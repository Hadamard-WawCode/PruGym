from flask import Flask, flash, render_template, redirect, request, url_for, jsonify, session
from login import signup_f, login_f
from objects import get_all_objects

app = Flask(__name__)
app.secret_key = '9je0jaj09jk9dkakdwjnjq'

@app.route('/')
def main():
    if 'username' in session:
        return redirect(url_for('index'))
    else:
        return redirect(url_for('signup'))

@app.route('/index')
def index():
    return render_template('index.html', obiekty = get_all_objects())


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('index'))
    if request.method == 'POST':
        username = request.form['user']
        password = request.form['password']
        if login_f(username, password):
            session['username'] = username
            session['password'] = password
            return redirect(url_for('main'))
        else:
        	#zły login lub hasło
            return render_template('login.html', info="Zły login lub hasło!")

    return render_template('login.html', info = "")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if 'username' in session:
        return redirect(url_for('index'))
    if request.method == 'POST':
        username = request.form['user']
        password = request.form['password']
        if signup_f(username, password):
            return redirect(url_for('main'))
        else:
        	#zły login lub hasło
            return render_template('signup.html')

    return render_template('signup.html')


if __name__=='__main__':
    app.run(debug=True)