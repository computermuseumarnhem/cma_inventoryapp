from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, IntegerField
#from wtforms.validators import ValidationError, DataRequired

def render_kw(field):
    if field.render_kw is None:
        field.render_kw = {}
    return field.render_kw        

class EditItemForm(FlaskForm):
    id = IntegerField('ID', render_kw={'readonly': True})
    name = StringField('Name')
    label = StringField('Label')
    manufacturer = StringField('Manufacturer')
    model = StringField('Model')
    serial = StringField('Serial no')
    wikilink = StringField('Hack42 wiki')
    description = TextAreaField('Description')
    submit = SubmitField('Save')

    def __init__(self, readonly=False, *args, **kwargs):
        super(EditItemForm, self).__init__(*args, **kwargs)
        render_kw(self.name)['readonly'] = readonly
        render_kw(self.label)['readonly'] = readonly
        render_kw(self.manufacturer)['readonly'] = readonly
        render_kw(self.model)['readonly'] = readonly
        render_kw(self.serial)['readonly'] = readonly
        render_kw(self.wikilink)['readonly'] = readonly
        render_kw(self.description)['readonly'] = readonly
        if readonly:
            self.submit.label.text = 'Edit'
