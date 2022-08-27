from flask import Blueprint
from flask_login import LoginManager
from flask_mail import Mail


auth = Blueprint('auth', __name__, template_folder='templates')

login_manager = LoginManager()
mail = Mail()
login_manager.login_view = 'auth.login'
login_manager.login_message_category = "info"

