from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_continuum import Continuum
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
continuum = Continuum(app, db, migrate)

bootstrap = Bootstrap(app)

login = LoginManager(app)
login.login_view = 'login'

mail = Mail(app)

from app import routes, models          # noqa: E402
