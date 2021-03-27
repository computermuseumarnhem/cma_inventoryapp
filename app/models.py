import os
from datetime import datetime

from flask import url_for

from app import db


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(50), nullable=True)
    label = db.Column(db.String(20), index=True, unique=True, nullable=True)
    manufacturer = db.Column(db.String(50), nullable=True)
    model = db.Column(db.String(50), nullable=True)
    serial = db.Column(db.String(50), nullable=True)
    description = db.Column(db.Text(), nullable=True)

    wikilink = db.Column(db.String(250), nullable=True)
    thumbnail = db.Column(db.Integer, db.ForeignKey('picture.id'), nullable=True)

    def get_thumbnail(self):
        return Picture.query.get(self.thumbnail)


class Picture(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    file = db.Column(db.String(128), unique=True)

    def link(self, size=None):
        if size:
            filename = os.path.join(size, self.file)
        else:
            filename = self.file
        return url_for('static', filename=filename)
