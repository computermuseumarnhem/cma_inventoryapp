from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, IntegerField, PasswordField, BooleanField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

from app.models import User, Item


class EditItemForm(FlaskForm):
    # id = IntegerField('ID', render_kw={'readonly': True})
    name = StringField('Name')
    label = StringField('Label')
    category = StringField('Category')
    manufacturer = StringField('Manufacturer')
    model = StringField('Model')
    serial = StringField('Serial no')
    description = TextAreaField('Description')
    submit = SubmitField('Save')
    cancel = SubmitField('Cancel', render_kw={'formnovalidate': True})

    def __init__(self, original_label, *args, **kwargs):
        super(EditItemForm, self).__init__(*args, **kwargs)
        self.original_label = original_label

    def validate_label(self, label):
        if label.data != self.original_label:
            item = Item.query.filter_by(label=label.data).first()
            if item is not None:
                raise ValidationError('Label is not unique. Please use another.')


class ShowItemForm(FlaskForm):
    # id = IntegerField('ID', render_kw={'readonly': True})
    name = StringField('Name', render_kw={'readonly': True})
    label = StringField('Label', render_kw={'readonly': True})
    category = StringField('Category', render_kw={'readonly': True})
    manufacturer = StringField('Manufacturer', render_kw={'readonly': True})
    model = StringField('Model', render_kw={'readonly': True})
    serial = StringField('Serial no', render_kw={'readonly': True})
    wikilink = StringField('Hack42 wiki', render_kw={'readonly': True})
    description = TextAreaField('Description', render_kw={'readonly': True})
    submit = SubmitField('Edit')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Log in')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request password reset')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Request Password Reset')
