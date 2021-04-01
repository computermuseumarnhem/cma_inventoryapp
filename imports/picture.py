from app.models import Picture
from app import db

pictures = [
    'apple-iic.jpg',
    'apple-imac.jpg',
    'asi286.jpg',
    'at_t-unix-pc.jpg',
    'digital-decwriter-iii-la120.jpg',
    'digital-la50.jpg',
    'digital-pdp8f.jpg',
    'digital-qbus-unibus-card.jpg',
    'digital-vt55.jpg',
    'holborn-9120.jpg',
    'ibm-029.jpg',
    'ibm-pc-xt.jpg',
    'lexitron-videotype-94.jpg',
    'sgi-o2.jpg',
    'tektronix-4002a.jpg',
    'tektronix-4951-joystick.jpg',
    'toshiba-satellite-100cs.jpg',
    'trs-80-mc-10.jpg',
    'vosim-99s.jpg',
]

def do_import():
    for p in pictures:
        picture = Picture()
        
        picture.name = p
        
        picture.updated_by = 'denz'
        
        db.session.add(picture)
        db.session.commit()

do_import()