from flask import Blueprint
from flask_login import LoginManager


auth = Blueprint('auth', __name__, template_folder='templates')
login_manager = LoginManager()
login_manager.login_view = 'login'

