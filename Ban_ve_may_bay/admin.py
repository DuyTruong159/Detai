from flask_admin.contrib.sqla import ModelView
from Ban_ve_may_bay.model import Khachhang, Ghe, Chuyenbay, User
from Ban_ve_may_bay import db, admin, login, app
from flask_admin import BaseView, expose
from  flask_login import login_user, logout_user, current_user
from flask import request, redirect
import hashlib

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

@app.route("/login-admin", methods = ['post'])
def login_admin():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password","")
        password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
        user = User.query.fillter(User.username == username.strip(),
                           User.password == password).first()

        if user:
            login_user(user = user)

    return redirect("/admin")

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)


admin.add_view(ModelView(Chuyenbay, db.session))
admin.add_view(ModelView(Ghe, db.session))
admin.add_view(ModelView(Khachhang, db.session))
admin.add_view(ContactView(name="Liên hệ"))
admin.add_view(LogoutView(name="Logout"))
