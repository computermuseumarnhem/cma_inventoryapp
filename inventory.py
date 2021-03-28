from app import app, db
from app.models import Item, Picture, User

@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'Item': Item,
        'Picture': Picture,
        'User': User,
    }
