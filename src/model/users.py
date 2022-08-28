from flask import current_app
from . import db
from src.config import Config
from src.auth import login_manager
from flask_security import UserMixin, RoleMixin # добавляется несколько методов
from itsdangerous import JSONWebSignatureSerializer as Serializer
from time import time
import jwt
import os



@login_manager.user_loader
def load_user(user_id):
		return User.query.get(int(user_id))



roles_users = db.Table('roles_users',
	db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
	db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
	)


class User(db.Model, UserMixin):
	id=db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(30), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(255), nullable=False)
	is_active = db.Column(db.Boolean, unique=False, default=True)
	roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))

	def __repr__(self):
		return '<User {}, Email {} >'.format(self.username, self.email)
		#return f"User('{self.username}', '{self.email}')"

	#def get_token(self, expires = 300):
		#return jwt.encode({'reset_password': self.username}, algorithm='HS256)
	def generate_token(self):
		return jwt.encode({'id': self.id}, current_app.config['SECRET_KEY'], algorithm='HS256')

	@staticmethod
	def verify_token(token):
		try:
			data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithm='HS256')
			return User.query.filter_by(id=data['id']).first()
		except:
			return
		return User.query.filter_by(username=username).first()



class Role(db.Model, RoleMixin):
	id=db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(30), unique=True)
	description = db.Column(db.String(255))

	def __repr__(self):
		return '<Role {}>'.format(self.name)