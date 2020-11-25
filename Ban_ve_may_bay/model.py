from sqlalchemy import Column, Integer, Float, ForeignKey, String, Boolean
from sqlalchemy.orm import relationship, backref
from Ban_ve_may_bay import db, admin
from flask_login import UserMixin, logout_user, current_user
from flask_admin import BaseView, expose
from flask import redirect
from flask_admin.contrib.sqla import ModelView

class Chuyenbay(db.Model):
    __tablename__ = "chuyenbay"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ma = Column(String(10), nullable=False)
    depart = Column(String(255), nullable=False)
    arrive = Column(String(255), nullable=False)
    day_time = Column(String(100), nullable=False)
    time_flight = Column(String(100), nullable=False)
    ghe = relationship('Ghe', backref='chuyenbay', lazy=True)
    trasit = relationship('Transit', backref='chuyenbay', lazy = True)
    khachhang = relationship('Khachhang', backref='chuyenbay', lazy=True)

    def __str__(self):
        return self.ma

class Transit(db.Model):
    __tablename__ = "transit"

    chuyenbay_id = Column(Integer, ForeignKey(Chuyenbay.id), primary_key=True)
    stt = Column(Integer, primary_key=True, autoincrement=True)
    transit = Column(String(255))
    time_delay = Column(String(100))

    def __str__(self):
        return self.id

class Ghe(db.Model):
    __tablename__ = "ghe"

    id = Column(Integer, primary_key=True, autoincrement=True)
    chuyenbay_id = Column(Integer, ForeignKey(Chuyenbay.id))
    hang = Column(Integer, primary_key=True)
    soluong = Column(Integer, nullable=False)
    price =  Column(Float, default=0)
    khachhang_ghe = relationship('Khachhang', backref='ghe', lazy=True)

    def __str__(self):
        return self.hang

class Khachhang(db.Model):
    __tablename__ = "khachhang"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ten = Column(String(255), nullable=False)
    cmnd = Column(Integer)
    sdt = Column(Integer, nullable=False)
    chuyenbay_id = Column(String(10), ForeignKey(Chuyenbay.id), primary_key=True)
    hangghe = Column(Integer, ForeignKey(Ghe.hang))

    def __str__(self):
        return self.ten

class User(db.Model, UserMixin):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    active = Column(Boolean, default=True)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)

    def __str__(self):
        return self.name

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

class ChuyenbayModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

class TransitModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

class GheModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

class KhachhangModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

admin.add_view(ChuyenbayModelView(Chuyenbay, db.session))
admin.add_view(TransitModelView(Transit, db.session))
admin.add_view(GheModelView(Ghe, db.session))
admin.add_view(KhachhangModelView(Khachhang, db.session))
admin.add_view(ContactView(name="Liên hệ"))
admin.add_view(LogoutView(name="Logout"))

if __name__ == '__main__':
    db.create_all()





