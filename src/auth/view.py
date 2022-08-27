from flask import render_template, url_for, redirect, request, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message



from src.model import db
from src.auth import auth, mail
from src.model.users import User, Role
from src.auth.forms import LoginForm, RegisterForm, ResetForm



@auth.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('home.index'))
	form = RegisterForm()
	if form.validate_on_submit():
		hash_pass = generate_password_hash(form.password.data)
		user = User(username=form.username.data, email=form.email.data, password=hash_pass)
		db.session.add(user)
		db.session.commit()
		flash(f'Вы зарегистрировались как {form.username.data}!', category='success')
		return redirect(url_for('auth.login'))
	return render_template('auth/register.html', form=form)



@auth.route("/login", methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home.index'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user and check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			#######
			next_page = request.args.get('next')
			return redirect(next_page) if next_page else redirect(url_for('home.index'))
		else:
			flash('Войти не удалось. Please check email and password', 'danger')
	return render_template('auth/login.html', title='Login', form=form)


@auth.route("/account")
@login_required
def account():
    return render_template('auth/account.html', title='Account')


def send_email():
    msg = Message('Flask app test send message',
    	sender='flaskappsmail@gmail.com',
    	recipients=['sungurko@mail.ru'])
    msg.html = '<h1>Это письмо тест отправки</h1>'
    mail.send(msg)
    return 'Письмо отправлено....'


@auth.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('auth.login'))

@auth.route('/reset', methods=['GET', 'POST'])
def reset_pass():
	form = ResetForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user:
			send_email()
			flash('Запрос на сброс пароля отправлен, проверьте почту')
			return redirect(url_for('auth.login'))

	return render_template('auth/reset.html', title = 'Reset', form=form)









	