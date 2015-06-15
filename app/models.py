from app import db

followers = db.Table('followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nickname = db.Column(db.String(50), index=True, unique=True)
    email = db.Column(db.String(100), index=True, unique=True)
    password = db.Column(db.String(100), index=True)
    last_been = db.Column(db.Date, index=True, unique=True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    about = db.Column(db.String(250), index=True)
    title = db.Column(db.String(50), index=True)
    background = db.Column(db.String(200), index=True)
    style = db.Column(db.String(200), index=True)

    followed = db.relationship('User',
        secondary = followers,
        primaryjoin = (followers.c.follower_id == id),
        secondaryjoin = (followers.c.followed_id == id),
        backref = db.backref('followers', lazy='dynamic'),
        lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % (self.nickname)

    def is_active(self):
        return True;

    def is_authenticated(self):
        return True;

    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)
            return self

    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)
            return self

    def is_following(self, user):
        return self.followed.filter(followers.c.followed_id == user.id).count() > 0

    def get_id(self):
        return str(self.id).encode('utf-8')

    def followed_posts(self):
        return Post.query.join(followers, (followers.c.followed_id == Post.user_id)).filter(followers.c.follower_id == self.id).order_by(Post.post_date.asc())

    def follows_you(self):
         return User.query.join(followers, (followers.c.followed_id is User.id).filter(followers.c.follower_id == self.id)



class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    text = db.Column(db.String(200), index=True)
    post_date = db.Column(db.DateTime)
    design = db.Column(db.Integer, index=True)

    def __repr__(self):
        return '<Post %r>' % (self.text)

