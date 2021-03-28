import os
from time import time
from datetime import datetime
import jwt

from flask import url_for
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import app, db, login


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(50), nullable=True)
    label = db.Column(db.String(20), index=True, unique=True, nullable=True)
    manufacturer = db.Column(db.String(50), nullable=True)
    model = db.Column(db.String(50), nullable=True)
    serial = db.Column(db.String(50), nullable=True)
    description = db.Column(db.Text(), nullable=True)
    category = db.Column(db.String(50), nullable=True)

    wikilink = db.Column(db.String(250), nullable=True)
    thumbnail = db.Column(db.Integer, db.ForeignKey('picture.id'), nullable=True)

    def get_thumbnail(self):
        return Picture.query.get(self.thumbnail)

    def get_name(self):
        if self.name:
            name = [self.name]
        else:
            name = []
            if self.manufacturer:
                name.append(self.manufacturer)
            if self.model:
                name.append(self.model)
        return ' '.join(name)


class Picture(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    file = db.Column(db.String(128), unique=True)

    def link(self, size=None):
        if size:
            filename = os.path.join(size, self.file)
        else:
            filename = self.file
        return url_for('static', filename=filename)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    fullname = db.Column(db.String(250))
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(128), index=True)
    telegram_name = db.Column(db.String(64))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_reset_password_token(self, expires_in=600):
        return jwt.encode(
            {
                'reset_password': self.id,
                'exp': time()+expires_in
            },
            app.config['SECRET_KEY'],
            algorithm='HS256'
        )

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
