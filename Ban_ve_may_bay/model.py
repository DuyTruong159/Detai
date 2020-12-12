from sqlalchemy import Column, Integer, Float, ForeignKey, String, Boolean, Date, DateTime
from sqlalchemy.orm import relationship
from Ban_ve_may_bay import db, admin
from flask_login import UserMixin, logout_user, current_user
from flask_admin import BaseView, expose
from flask import redirect
from flask_admin.contrib.sqla import ModelView
from datetime import datetime


class Chuyenbay(db.Model):
    __tablename__ = "chuyenbay"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ma = Column(String(10), nullable=False)
    depart = Column(String(255), nullable=False)
    arrive = Column(String(255), nullable=False)
    day_time = Column(String(100), nullable=False)
    time_flight = Column(String(100), nullable=False)
    transit = relationship('Transit', backref='transit_chuyenbay', lazy=True)
    vechuyenbay = relationship('Vechuyenbay', backref='vechuyenbay_chuyenbay', lazy=True)
    ghe = relationship('Ghe', backref='ghe_chuyenbay', lazy=True)

    def __str__(self):
        return self.ma


class Transit(db.Model):
    __tablename__ = "transit"

    id = Column(Integer, primary_key=True, autoincrement=True)
    stt = Column(Integer, nullable=False)
    airport = Column(String(255), nullable=False)
    time_delay = Column(String(100), nullable=False)
    chuyenbay_id = Column(Integer, ForeignKey(Chuyenbay.id), nullable=False)

    def __str__(self):
        return self.stt


class Ghe(db.Model):
    __tablename__ = "ghe"

    id = Column(Integer, primary_key=True, autoincrement=True)
    hang = Column(String(1), nullable=False)
    soluong = Column(Integer)
    price = Column(Float)
    chuyenbay_id = Column(Integer, ForeignKey(Chuyenbay.id), nullable=False)

    def __str__(self):
        return self.hang


class Khachhang(db.Model):
    __tablename__ = "khachhang"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ten = Column(String(255), nullable=False)
    cmnd = Column(Integer)
    sdt = Column(Integer)
    vechuyenbay = relationship('Vechuyenbay', backref='khachhang_chuyenbay', lazy=True)

    def __str__(self):
        return self.ten


class Vechuyenbay(db.Model):
    __tablename__ = "vechuyenbay"

    id = Column(Integer, primary_key=True, autoincrement=True)
    chuyenbay_id = Column(Integer, ForeignKey(Chuyenbay.id), nullable=False)
    Khachhang_id = Column(Integer, ForeignKey(Khachhang.id), nullable=False)
    hangghe = Column(String(100))
    gia = Column(Float)
    NgayDk = Column(Date, default=datetime.now())


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


class VechuyenbayModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated


admin.add_view(ChuyenbayModelView(Chuyenbay, db.session))
admin.add_view(TransitModelView(Transit, db.session))
admin.add_view(GheModelView(Ghe, db.session))
admin.add_view(KhachhangModelView(Khachhang, db.session))
admin.add_view(VechuyenbayModelView(Vechuyenbay, db.session))
admin.add_view(ContactView(name="Liên hệ"))
admin.add_view(LogoutView(name="Logout"))

if __name__ == '__main__':
    db.create_all()
