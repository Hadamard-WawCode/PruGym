from flask import Flask, flash, render_template, redirect, request, url_for, jsonify, session
from login import signup_f, login_f
from objects import get_all_objects, get_object, addevent, wszystkieob, infowyd
from historia import *

app = Flask(__name__)
app.secret_key = '9je0jaj09jk9dkakdwjnjq'

@app.route('/')
def main():
    if 'username' in session:
        return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))

@app.route('/index')
def index():
    if 'username' in session:
        return render_template('index.html', obiekty = get_all_objects(), username = session.get('username'))
    else:
        return redirect(url_for('login'))

@app.route('/gym', methods=['GET', 'POST'])
def gym():
    if 'username' in session:
        obj_id = request.args.get('id')
        if request.method == 'POST':
            eventName = request.form['nazwa']
            eventDesc = request.form['opis']
            eventDate = request.form['data']
            print(eventName, eventDesc, eventDate, obj_id)
            addevent(eventName,eventDesc,session['username'],obj_id, eventDate)
            return redirect('/gym?id='+obj_id)

        event_id_list = wszystkieob(obj_id)
        events = []
        for event_id in event_id_list:
            events.append(infowyd(event_id))

        return render_template('gym.html', obiekty = get_object(obj_id), eventy=events, username = session.get('username'))
    else:
        return redirect(url_for('main'))


@app.route('/myActivity')
def myActivity():
    if 'username' in session:
        return render_template('myActivity.html', username = session.get('username'))
    else:
        return redirect(url_for('main'))


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

@app.route('/addPic')
def addPic():
    if 'username' in session:
        return render_template('addPic.html', username = session.get('username'))
    else:
        return redirect(url_for('main'))

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

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    del session['username']
    del session['password']
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)
