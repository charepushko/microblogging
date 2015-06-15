from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm, models
from forms import LoginForm, SignUpForm, Tweet, SettingsForm
from models import User, Post
import random, datetime
from hashlib import md5


@app.before_request
def before_request():
    g.user = current_user


@app.route('/', methods =  ['GET', 'POST'])
@app.route('/index', methods =  ['GET', 'POST'])
@app.route('/feed', methods =  ['GET', 'POST'])
def index():
    user = g.user
    if g.user is None:
        return redirect(url_for('login'))
    if not user.is_following(user):
        db.session.add(user.follow(user))
        db.session.commit()
        return redirect(url_for('index'))
    posts = g.user.followed_posts().all()
    form_tw = Tweet()
    if form_tw.validate_on_submit() and (form_tw.text.data is not None) and (len(form_tw.text.data) < 201):
        p = Post(user_id=user.id, text=form_tw.text.data, post_date=datetime.datetime.utcnow(), author=user, design=random.randint(1,4))
        db.session.add(p)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('feed.html', 
        user = user,
        posts = posts,
        form_tw=form_tw)




@lm.user_loader
def load_user(id):
    return models.User.query.filter_by(id=id).first()





@app.route('/login', methods =  ['GET', 'POST'])
def login():

    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form_l = LoginForm()
    form_s = SignUpForm()

    if form_l.validate_on_submit() and (len(form_l.openid.data) < 100) and (len(form_l.password.data) < 100):
        session['remember_me'] = form_l.remember_me.data
        user = db.session.query(User).filter(User.email == form_l.openid.data).filter(User.password == md5(form_l.password.data).hexdigest()).first()
        if user is not None:
            login_user(user, remember = form_l.remember_me.data)
            return redirect(url_for('index')) 
        else: 
            print("NOT FOUND")
        
    if form_s.validate_on_submit() and (len(form_s.email.data) < 100) and (len(form_s.login.data) < 50) and (len(form_s.password.data) < 100):
        k = False
        user = db.session.query(User).filter(User.email == form_s.email.data  or  User.nickname == form_s.login.data).first()
        if user is None:
            u = User(nickname=form_s.login.data, email=form_s.email.data, password=md5(form_s.password.data).hexdigest())
            db.session.add(u)
            db.session.commit()
            db.session.add(u.follow(u))
            db.session.commit()
            login_user(u)
            return redirect(url_for('index')) 
        else:
            print("EXISTS")
             
    return render_template('login1.html',
        form_l = form_l,
        form_s = form_s)




@app.route('/settings', methods = ['GET', 'POST'])
def settings():
    if g.user is None or not g.user.is_authenticated():
        return redirect(url_for('index'))
    form = SettingsForm()
    if form.validate_on_submit():
        if (md5(form.oldpass.data).hexdigest() == md5(g.user.password).hexdigest()) and (form.newpass.data == form.passagain.data != None):
            g.user.password = md5(form.newpass.data).hexdigest()
        if ((form.newlogin.data != "") and (db.session.query(User).filter(User.nickname == form.newlogin.data).first() == None) and (md5(form.logpass.data).hexdigest() == md5(g.user.password).hexdigest())):
            g.user.nickname = form.newlogin.data
        if (form.title.data != ""):
            g.user.title = form.title.data
        if (form.description.data != ""):
            g.user.about = form.description.data
        if (form.userpic.data != ""):
            g.user.style = form.userpic.data
        if (form.backgr.data != ""):
            g.user.background = form.backgr.data
        db.session.add(g.user)
        db.session.commit()
        return redirect(url_for('settings'))
 
    return render_template('settings.html',
        form = form,
        user = g.user)
    



@app.route('/user/<login>', methods =  ['GET', 'POST'])
@login_required
def user(login):
    user = User.query.filter_by(nickname=login).first()
    if g.user == None:
        redirect(url_for('login'))
    if user == None:
        flash('User not found')
        return redirect(url_for('index'))
    posts = user.posts.all()
    return render_template("index.html",
        user = user,
        posts = posts)




@app.route('/logout')
def logout():
    logout_user()
    print ("successfully logged out")
    return redirect(url_for('login'))




@app.route('/followers')
def followers():
    users = g.user.follows_you().all()
    return render_template("followers.html",
        users = users,
        user = g.user)






@app.route('/follow/<nickname>')
@login_required
def follow(nickname):
    user = User.query.filter_by(nickname=nickname).first()
    u = g.user.follow(user)
    if u is None:
        return redirect(url_for('user', login=nickname))
    db.session.add(u)
    db.session.commit()
    return redirect(url_for('user', login=nickname))




@app.route('/unfollow/<nickname>')
@login_required
def unfollow(nickname):
    user = User.query.filter_by(nickname=nickname).first()
    u = g.user.unfollow(user)
    if u is None:
        return redirect(url_for('user', login = nickname))
    db.session.add(u)
    db.session.commit()
    return redirect(url_for('user', login = nickname))
 
