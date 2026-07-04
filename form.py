from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField

from wtforms.validators import DataRequired, DataRequired,Length,Email


class reg(FlaskForm):
    name=StringField('username',validators=[DataRequired(),Length(min=3,max=25)])
    password=PasswordField('password',validators=[DataRequired(),Length(min=3)])
    email=StringField('email',validators=[DataRequired(),Email()])
    submit=SubmitField('submit')


