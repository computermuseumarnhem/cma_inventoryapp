from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

from app import app, db
from app.models import Item, User
from app.forms import EditItemForm, ShowItemForm, LoginForm, RegistrationForm, ResetPasswordForm, ResetPasswordRequestForm
from app.email import send_password_reset_email


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/item')
def show_items():
    items = Item.query.order_by(Item.name).all()

    return render_template('items.html', title='Items', items=items)


@app.route('/item/<id>', methods=['GET', 'POST'])
def show_item(id):
    item = Item.query.get_or_404(id)
    form = ShowItemForm()
    if form.validate_on_submit():
        return redirect(url_for('edit_item', id=item.id))

    # form.id.data = item.id
    form.name.data = item.name
    form.label.data = item.label
    form.category.data = item.category
    form.manufacturer.data = item.manufacturer
    form.model.data = item.model
    form.serial.data = item.serial
    form.wikilink.data = item.wikilink
    form.description.data = item.description
    return render_template('edititem.html', title=item.get_name(), item=item, form=form)


@app.route('/item/<id>/edit', methods=['GET', 'POST'])
@login_required
def edit_item(id):
    item = Item.query.get_or_404(id)
    form = EditItemForm()
    if form.cancel.data:
        return redirect(url_for('show_item', id=item.id))
    if form.validate_on_submit():
        item.name = form.name.data
        item.label = form.label.data if form.label.data else None
        item.category = form.category.data
        item.manufacturer = form.manufacturer.data
        item.model = form.model.data
        item.serial = form.serial.data
        item.wikilink = form.wikilink.data
        item.description = form.description.data
        db.session.commit()
        flash("Changes are saved")
        return redirect(url_for('show_item', id=item.id))
    elif request.method == 'GET':
        # form.id.data = item.id
        form.name.data = item.name
        form.label.data = item.label
        form.category.data = item.category
        form.manufacturer.data = item.manufacturer
        form.model.data = item.model
        form.serial.data = item.serial
        form.wikilink.data = item.wikilink
        form.description.data = item.description
    return render_template('edititem.html', title=item.get_name(), item=item, form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash('Check your email for the instructions to reset your password')
        return redirect(url_for('login'))
    return render_template('reset_password_request.html', title='Reset Password', form=form)

@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Your password has been reset.')
        return redirect(url_for('login'))
    return render_template('reset_password.html', form=form)