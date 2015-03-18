from flask import render_template, flash, redirect
from app import app
from forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Kut' }
    return render_template("index.html",
        title = "Home",
        user = user)



@app.route('/login', methods =  ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login=' + form.openid.data + ', remember_me=' + str(form.remember_me.data))
        if form.openid.data=='kut' or form.openid.data=='anna':
            return redirect('/index')
    return render_template('login.html',
        form = form)