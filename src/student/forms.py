from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length
'''
flask_wtf - Пакет представляет класс FlaskForm
wtforms - Пакет предоставляющий поля StringField, PasswordField, SelectField и др.
'''




class StudentForm(FlaskForm):
	name = StringField('Имя: ', validators=[DataRequired("Введите имя")])
	email = StringField('E-Mail', validators=[Email()])
	phone = StringField('Телефон', validators=[DataRequired()])
	submit = SubmitField('Добавить')


#name = StringField('Name', validators=[DataRequired(), Length(min=-1, max=80, message='You cannot have more than 80 characters')])
#surname = StringField('Surname', validators=[Length(min=-1, max=100, message='You cannot have more than 100 characters')])
#email = StringField('E-Mail', validators=[Email(), Length(min=-1, max=200, message='You cannot have more than 200 characters')])
#phone = StringField('Phone', validators=[Length(min=-1, max=20, message='You cannot have more than 20 characters')])