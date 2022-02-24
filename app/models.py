from datetime import datetime
from flask_login import current_user
from app import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from app import login
from hashlib import md5
from time import time
import jwt
from app import app



class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime,default=datetime.utcnow)


    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self,password):
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    def avatar(self,size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)

    def get_reset_password_token(self, expires_in=600):
        return jwt.encode(
            {'reset_password': self.id, 'exp': time() + expires_in},
            app.config['SECRET_KEY'], algorithm='HS256').decode('utf-8')

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, app.config['SECRET_KEY'],
                            algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))



class followers(db.Model):
    __tablename__ = 'followers'
    rec_id = db.Column(db.Integer,primary_key=True)
    followed_id = db.Column(db.Integer,index=True)
    follower_id = db.Column(db.Integer,index=True)

    def __repr__(self):
        return '<follow_relationship %s %s>' % (self.followed_id,self.follower_id)


    def is_following(self,user_id):
        return self.query.filter_by(followed_id=user_id,follower_id=current_user.id).count()


class Posts(db.Model):
    __tablename__ = 'Posts'
    rec_id = db.Column(db.Integer, primary_key=True)
    anther_id = db.Column(db.Integer, index=True)
    title = db.Column(db.String(50))
    body = db.Column(db.String(140))

    def followed_posts(self):
        a= db.session.query(followers).all()
        return a
    def my_posts(self):
        return db.session.query(Posts).filter(Posts.anther_id==current_user.id).all()
