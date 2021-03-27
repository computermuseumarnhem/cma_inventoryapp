from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.models import Item
from app.forms import EditItemForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/item')
def show_items():
    items = Item.query.order_by(Item.name).all()

    return render_template('items.html', title='Items', items = items)

@app.route('/item/<id>', methods=['GET', 'POST'])
def show_item(id):
    item = Item.query.get_or_404(id)
    form = EditItemForm(readonly=True)
    if form.validate_on_submit():
        return redirect(url_for('edit_item', id=item.id))

    form.id.data = item.id
    form.name.data = item.name
    form.label.data = item.label
    form.manufacturer.data = item.manufacturer
    form.model.data = item.model
    form.serial.data = item.serial
    form.wikilink.data = item.wikilink
    form.description.data = item.description
    return render_template('edititem.html', title=item.name, item = item, form=form)

@app.route('/item/<id>/edit', methods=['GET', 'POST'])
def edit_item(id):
    item = Item.query.get_or_404(id)
    form = EditItemForm()
    if form.validate_on_submit():
        item.name = form.name.data
        item.label = form.label.data
        item.manufacturer = form.manufacturer.data
        item.model = form.model.data
        item.serial = form.serial.data
        item.wikilink = form.wikilink.data
        item.description = form.description.data
        db.session.commit()
        flash("Changes are saved")
        return redirect(url_for('show_item', id=item.id))
    elif request.method == 'GET':
        form.id.data = item.id
        form.name.data = item.name
        form.label.data = item.label
        form.manufacturer.data = item.manufacturer
        form.model.data = item.model
        form.serial.data = item.serial
        form.wikilink.data = item.wikilink
        form.description.data = item.description
    return render_template('edititem.html', title=item.name, item=item, form=form)