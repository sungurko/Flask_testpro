from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView # 


from src.admin import admin
from src.model import db
from src.model.student import Student
from src.model.users import User, Role


admin.add_view(ModelView(Student, db.session))
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Role, db.session))