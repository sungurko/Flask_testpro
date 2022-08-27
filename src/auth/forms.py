from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email, ValidationError
from src.model.users import User


class LoginForm(FlaskForm):
	username = StringField('Пользователь', validators=[DataRequired()], render_kw={'placeholder': 'Имя пользователя'})
	password = PasswordField('Пароль', validators=[DataRequired()], render_kw={'placeholder': 'Пароль'})
	remember = BooleanField('Запомнить', default=False)
	submit = SubmitField('Войти')

class RegisterForm(FlaskForm):
	username = StringField('Пользователь', validators=[DataRequired()], render_kw={'placeholder': 'Имя пользователя'})
	email = StringField('Email', validators=[DataRequired()], render_kw={'placeholder': 'Email'})
	password = PasswordField('Пароль', validators=[DataRequired()], render_kw={'placeholder': 'Пароль'})
	confirm_pass = PasswordField('Повтор пароля', validators=[DataRequired(), EqualTo('password', 'Пароли несовместимы')], render_kw={'placeholder': u'Подтвердите пароль'})
	submit = SubmitField('Зарегистрироваться')

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user is not None:
			raise ValidationError('Пользователь существует')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user is not None:
			raise ValidationError('Email занят')

class ResetForm(FlaskForm):
	email = StringField(label = 'Введите ваш Email', validators=[DataRequired()], render_kw={'placeholder': 'Email'})
	submit = SubmitField(label = 'Сброс пароля', validators=[DataRequired()])


