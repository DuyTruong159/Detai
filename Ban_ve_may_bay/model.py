from sqlalchemy import Column, Integer, Float, ForeignKey, String
from sqlalchemy.orm import relationship
from Ban_ve_may_bay import db
from datetime import datetime

class Chuyenbay(db.Model):
    __tablename__ = "chuyenbay"

    ma = Column(String(3), primary_key=True)
    depart = Column(String(255), nullable=False)
    arrive = Column(String(255), nullable=False)
    day_time = Column(datetime, nullable=False)
    time_flight = Column(datetime, nullable=False)
    ghe = relationship('Ghe', backref ='ghe', lazy =True)
    transit = relationship('Transit', backref ='transit', lazy = True )


    def __str__(self):
        return self.Ma

class Ghe(db.Model):
    __tablename__ = "ghe"

    hang = Column(Integer, primary_key=True, nullable=False)
    soluong = Column(Integer)
    price =  Column(Float, default=0)
    chuyenbay_ma = Column(String(3), ForeignKey(Chuyenbay.ma), nullable=False)

    def __str__(self):
        return self.Hang

class Khachhang(db.Model):
    __tablename__ = "khachhanh"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ten = Column(String(255), nullable=False)
    cmnd = Column(String(9))
    sdt = Column(Integer(10), nullable=False)
    chuyenbay_ma = Column(String(3), ForeignKey(Chuyenbay.ma), nullable=False)
    hang = Column(Integer, ForeignKey(Ghe.hang), nullable=False)


    def __str__(self):
        return self.Ten

class Transit(db.Model):
    __tablename__ = "transit"

    id = Column(Integer, primary_key=True, autoincrement=True)
    transit = Column(String(255))
    time_delay = Column(datetime)
    chuyenbay_ma = Column(String(3), ForeignKey(Chuyenbay.ma), nullable=False)

    def __str__(self):
        return self.ID

if __name__ == '__main__':
    db.create_all()





