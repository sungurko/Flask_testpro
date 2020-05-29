from . import db
from datetime import datetime


class Student(db.Model):
	__tablename__ = 'student'


	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(length=100), nullable=False)
	email = db.Column(db.String(length=256), unique=True, nullable=False)
	phone = db.Column(db.String(length=100), nullable=False)
	year = db.Column(db.DateTime, default=datetime.now())

	def __init__(self, name, email, phone):
		self.name=name
		self.email=email
		self.phone=phone


	def __repr__(self):
		return '<id {}, student name {} >'.format(self.id, self.name)