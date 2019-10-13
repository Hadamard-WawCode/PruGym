import os, os.path, random, hashlib, sys, json
from flask import Flask, flash, render_template, redirect, request, url_for, jsonify, session, Response
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

        return render_template('gym.html', obiekty = get_object(obj_id), eventy=events, username = session.get('username'), num = obj_id)
    else:
        return redirect(url_for('main'))

@app.route('/event', methods=['GET', 'POST'])
def event():
    if 'username' in session:
        obj_id = request.args.get('id')
        if request.method == 'POST':
            return redirect('/')
        return render_template('event.html', username = session.get('username'))
    else:
        return redirect(url_for('main'))


@app.route('/myActivity', methods=['GET', 'POST'])
def myActivity():
    if 'username' in session:
        if request.method == 'POST':
            sport = request.form['sport']
            if sport == "gym":
                gymname = request.form['trainplan']
                inserttraining(session['username'], gymname)
            else:
                dist = request.form['dist']
                hours = request.form['hours']
                minutes = request.form['minutes']
                try:
                    time = int(hours) * 60 + int(minutes)
                except:
                    return Response("", status=500, mimetype='application/json')
                insertactivity(session['username'], time, dist, sport)
                return redirect(url_for('myActivity'))
        return render_template('myActivity.html', username = session.get('username'), selectbest=sb)
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

@app.route('/addPic', methods=['POST'])
def addPic():
    if 'username' in session:
        names = []
        for fkey in request.files:
            file = request.files[fkey]
            if file.filename == '':
                continue
            file.save('current')
            data = open('current', 'rb').read()
            digest = hashlib.md5()
            digest.update(data)
            names.append('static/paste/' + digest.hexdigest() + os.path.splitext(file.filename)[1])
            os.rename('current', names[-1])
        add_pictures(request.form.get('num'), names)
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
