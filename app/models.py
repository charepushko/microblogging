from app import db

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(50), index = True, unique = True)
    email = db.Column(db.String(100), index = True, unique = True)
    password = db.Column(db.String(35), index = True)
    last_been = db.Column(db.Date, index = True, unique = True)

    def __repr__(self):
        return '<User %r>' % (self.nickname)

class Tweets(db.Model):
    post_id = db.Column(db.Integer, primary_key = True)
    author_id = db.Column(db.Integer)
    text = db.Column(db.String(200), index = True)
