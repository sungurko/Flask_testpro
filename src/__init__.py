from flask import Flask
from src.config import Config
from src.admin.admin import admin
from src.auth import login_manager, mail
import src.model.users


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config())

    # инициализация расширений

    model.db.init_app(app)
    admin.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    
    # blueprints

    from src.auth.view import auth
    from src.home.view import home
    from src.student.view import student
    from src.errors.handlers import errors

    # регистрация модулей в приложении

    app.register_blueprint(auth) 
    app.register_blueprint(home)
    app.register_blueprint(student)
    app.register_blueprint(errors)   
        
    
    with app.app_context():
        model.db.create_all()

    return app

app = create_app()


    



