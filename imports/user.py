"""
CREATE TABLE user (
	id INTEGER NOT NULL, 
	username VARCHAR(64), 
	password_hash VARCHAR(128), 
	email VARCHAR(128), 
	telegram_name VARCHAR(64), fullname VARCHAR(250), 
	PRIMARY KEY (id)
);
INSERT INTO user VALUES(1,'denz','pbkdf2:sha256:150000$WsAQBF6k$f8cd4384549383235965038dafd13d6e10c4b91eeaa783b9306f265b6f00650e','alex.van.denzel@gmail.com',NULL,NULL);
INSERT INTO user VALUES(2,'gmc','pbkdf2:sha256:150000$InSc3EEy$5e83d9b0304753dc932183114e1800cc55870b86f6646d48b476e97aa0fa59a7','in+cma@metro.cx',NULL,NULL);
INSERT INTO user VALUES(3,'Stoneshop','pbkdf2:sha256:150000$LpE8GVao$a2713686a0d5db9e7de39793fae1daaa8c9a0f9a41d13832413fd16946884c94','rik.cma@steenwinkel.net',NULL,NULL);
"""

from app import db
from app.models import User

users = [
    (1,'denz','pbkdf2:sha256:150000$WsAQBF6k$f8cd4384549383235965038dafd13d6e10c4b91eeaa783b9306f265b6f00650e','alex.van.denzel@gmail.com',None,None),
    (2,'gmc','pbkdf2:sha256:150000$InSc3EEy$5e83d9b0304753dc932183114e1800cc55870b86f6646d48b476e97aa0fa59a7','in+cma@metro.cx',None,None),
    (3,'Stoneshop','pbkdf2:sha256:150000$LpE8GVao$a2713686a0d5db9e7de39793fae1daaa8c9a0f9a41d13832413fd16946884c94','rik.cma@steenwinkel.net',None,None),
]

from datetime import datetime

def do_import():
    for u in users:
        user = User()
        user.id = u[0]
        user.username = u[1]
        user.password_hash = u[2]
        user.email = u[3]
        user.updated_by = 'denz'
        user.updated_at = datetime.utcnow()

        db.session.add(user)
        db.session.commit()

do_import()