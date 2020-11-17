from sqlalchemy import Column, Integer, Float, ForeignKey, String, Boolean
from sqlalchemy.orm import relationship
from Ban_ve_may_bay import db
from datetime import datetime
from flask_login import UserMixin

class Chuyenbay(db.Model):
    __tablename__ = "chuyenbay"

    ma = Column(String(10), primary_key=True)
    depart = Column(String(255), nullable=False)
    arrive = Column(String(255), nullable=False)
    day_time = Column(datetime, nullable=False)
    time_flight = Column(datetime, nullable=False)
    ghe = relationship('Ghe', backref = 'ghe', lazy = True)
    transit_first = Column(String(255))
    time_delay_first = Column(datetime)
    transit_second = Column(String(255))
    time_delay_second = Column(datetime)

    def __str__(self):
        return self.ma

class Ghe(db.Model):
    __tablename__ = "ghe"

    chuyenbay_ma = Column(String(10), ForeignKey(Chuyenbay.ma), primary_key=True, nullable=False)
    hang = Column(Integer, primary_key=True)
    soluong = Column(Integer)
    price =  Column(Float, default=0)

    def __str__(self):
        return self.hang

class Khachhang(db.Model):
    __tablename__ = "khachhanh"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ten = Column(String(255), nullable=False)
    cmnd = Column(String(9))
    sdt = Column(Integer(10), nullable=False)
    chuyenbay_ma = Column(String(10), ForeignKey(Chuyenbay.ma), nullable=False)
    ghehang = Column(Integer, ForeignKey(Ghe.hang), nullable=False)


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

if __name__ == '__main__':
    db.create_all()





