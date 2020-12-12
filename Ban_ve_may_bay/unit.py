import json
from Ban_ve_may_bay.model import *
from Ban_ve_may_bay import db

def read_data(path= 'data/chuyen_bay.json'):
    with open(path, encoding='utf-8') as f:
        return json.load(f)

def get_chuyenbay_by_stt(stt):
    product = read_data()
    for p in product:
        if p['stt'] == stt:
            return p

def datve(id):
    return Chuyenbay.query.get(id)

def gia(id):
    return Ghe.query.filter(Ghe.chuyenbay_id == id )

def add_ve(chuyenbay = None, hanhkhach = None, cmnd = None, sdt = None, hangve = None, giatien = None):
    hk = Khachhang(ten=hanhkhach,
                   cmnd=cmnd,
                   sdt=sdt)

    db.session.add(hk)
    db.session.commit()

    ve = Vechuyenbay(chuyenbay_id=chuyenbay,
                     Khachhang_id=hk.id,
                     hangghe=hangve,
                     gia=giatien)
    db.session.add(ve)
    db.session.commit()

def hj():
    cursor.execute('')


