import os

token = os.environ['FLASK_TOKEN']


class Config():
	DEBUG=True
	SQLALCHEMY_TRACK_MODIFICATIONS=False
	SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://kuperae:{token}@localhost/app_db'
	SECRET_KEY='secret'
	WTF_CSRF_ENABLED = False

#### FLASK_MAIL ####
	MAIL_SERVER = os.environ.get('MAIL_SERVER')
	MAIL_PORT = os.environ.get('MAIL_PORT')
	MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS')
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

#### FLASK_SECURITY ####
	SECURITY_PASSWORD_SALT = 'salt'
	SECURITY_PASSWORD_HASH = 'sha512_crypt'