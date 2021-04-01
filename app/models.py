import os
from time import time
from datetime import datetime
import jwt

from flask import url_for
from flask_login import UserMixin
from flask_continuum import VersioningMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import app, db, login


class Item(db.Model, VersioningMixin):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(50), index=True, nullable=True)
    label = db.Column(db.String(50), index=True, unique=True, nullable=True)
    manufacturer = db.Column(db.String(50), nullable=True)
    model = db.Column(db.String(50), nullable=True)
    serial = db.Column(db.String(50), nullable=True)
    description = db.Column(db.Text(), nullable=True)
    category = db.Column(db.String(50), nullable=True)
    tags = db.relationship('Tag', backref='item', lazy='dynamic', foreign_keys='Tag.item_id')
    thumbnail_id = db.Column(db.Integer(), db.ForeignKey('picture.id'), nullable=True)
    pictures = db.relationship('Picture', backref='item', lazy='dynamic', foreign_keys='Picture.item_id')
    created_at = db.Column(db.DateTime(), default=datetime.now, nullable=False)
    updated_at = db.Column(db.DateTime(), default=datetime.now, onupdate=datetime.now, nullable=False)
    updated_by = db.Column(db.String(50), nullable=False)

    def get_name(self):
        """supply a default name if name is not given"""
        if self.name:
            return self.name
        return ((self.manufacturer or '') + ' ' + (self.model or '')).strip()


class Picture(db.Model, VersioningMixin):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(128), unique=True)
    item_id = db.Column(db.Integer(), db.ForeignKey('item.id'), nullable=True)
    created_at = db.Column(db.DateTime(), default=datetime.now, nullable=False)
    updated_at = db.Column(db.DateTime(), default=datetime.now, onupdate=datetime.now, nullable=False)
    updated_by = db.Column(db.String(50), nullable=False)
    thumbnail_item = db.relationship('Item', backref='thumbnail', lazy='dynamic', foreign_keys='Item.thumbnail_id')

    def link(self, size=None):
        if size:
            filename = os.path.join(size, self.name)
        else:
            filename = self.name
        return url_for('static', filename=filename)

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True, nullable=False)
    value = db.Column(db.String(50), index=True, nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=True)


class User(UserMixin, db.Model, VersioningMixin):
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(64), index=True, unique=True)
    fullname = db.Column(db.String(250))
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(128), index=True)
    telegram = db.Column(db.String(64))
    created_at = db.Column(db.DateTime(), default=datetime.now, nullable=False)
    updated_at = db.Column(db.DateTime(), default=datetime.now, onupdate=datetime.now, nullable=False)
    updated_by = db.Column(db.String(50), nullable=False)

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
