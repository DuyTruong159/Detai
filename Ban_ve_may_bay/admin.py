from flask_admin.contrib.sqla import ModelView
from Ban_ve_may_bay.model import *
from Ban_ve_may_bay import db, admin
from flask_admin import BaseView, expose
from flask_login import logout_user, current_user
from flask import redirect

class ContactView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/contact.html')

class LogoutView(BaseView):
    @expose('/')
    def index(self):
        logout_user()
        return redirect('/admin')

    def is_accessible(self):
        return current_user.is_authenticated

admin.add_view(ModelView(Chuyenbay, db.session))
admin.add_view(ModelView(Transit, db.session))
admin.add_view(ModelView(Ghe, db.session))
admin.add_view(ModelView(Khachhang, db.session))
admin.add_view(ContactView(name="Liên hệ"))
admin.add_view(LogoutView(name="Logout"))
