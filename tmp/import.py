from tmp import sheet

for i in Item.query.all():  
    db.session.delete(i)


for p in Picture.query.all():
    db.session.delete(p)


db.session.commit()

for r in sheet.row():
    picture_id = None 
    if r['picture']:
        picture = Picture(file=r['picture'])
        db.session.add(picture)
        db.session.commit()
        picture_id = picture.id
    item = Item(id=r['id'], label=r['label'], name=r['name'], manufacturer=r['manufacturer'], model=r['model'], serial=r['serial'], thumbnail=picture_id)
    db.session.add(item)
    db.session.commit()
    print(item.id)
