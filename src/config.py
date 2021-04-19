import os

token = os.environ['FLASK_TOKEN']


class Config():
	DEBUG=True
	SQLALCHEMY_TRACK_MODIFICATIONS=False
	SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://kuperae:{token}@localhost/users'
	SECRET_KEY='secret'
	WTF_CSRF_ENABLED = False


#### FLASK_SECURITY ####
	SECURITY_PASSWORD_SALT = 'salt'
	SECURITY_PASSWORD_HASH = 'sha512_crypt'