import json, pymysql
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

def count_1():
    pymysql.install_as_MySQLdb()

    db = pymysql.connect("localhost", "root", "phamduytruong", "detai")
    cursor = db.cursor()

    dem = cursor.execute("SELECT * FROM Vechuyenbay WHERE chuyenbay_id = 1")

    return dem

def count_2():
    pymysql.install_as_MySQLdb()

    db = pymysql.connect("localhost", "root", "phamduytruong", "detai")
    cursor = db.cursor()

    dem = cursor.execute("SELECT * FROM Vechuyenbay WHERE chuyenbay_id = 2")

    return dem

def count_3():
    pymysql.install_as_MySQLdb()

    db = pymysql.connect("localhost", "root", "phamduytruong", "detai")
    cursor = db.cursor()

    dem = cursor.execute("SELECT * FROM Vechuyenbay WHERE chuyenbay_id = 3")

    return dem

def count_4():
    pymysql.install_as_MySQLdb()

    db = pymysql.connect("localhost", "root", "phamduytruong", "detai")
    cursor = db.cursor()

    dem = cursor.execute("SELECT * FROM Vechuyenbay WHERE chuyenbay_id = 4")

    return dem

def count_5():
    pymysql.install_as_MySQLdb()

    db = pymysql.connect("localhost", "root", "phamduytruong", "detai")
    cursor = db.cursor()

    dem = cursor.execute("SELECT * FROM Vechuyenbay WHERE chuyenbay_id = 5")

    return dem

def empty():
    data = read_data()

    if data[0]['second_chair'] + count_1() != 40:
        data[0]['second_chair'] = data[0]['second_chair'] - 1
        o = open('data/chuyen_bay.json', 'w', encoding='utf-8')
        json.dump(data[0], o)

    elif data[1]['second_chair'] + count_2() != 40:
        data[1]['second_chair'] = data[1]['second_chair'] - 1
        o = open('data/chuyen_bay.json', 'w', encoding='utf-8')
        json.dump(data[1], o)


    elif data[2]['second_chair'] + count_3() != 40:
        data[2]['second_chair'] = data[2]['second_chair'] - 1
        o = open('data/chuyen_bay.json', 'w', encoding='utf-8')
        json.dump(data[2], o)


    elif data[3]['second_chair'] + count_4() != 40:
        data[3]['second_chair'] = data[3]['second_chair'] - 1
        o = open('data/chuyen_bay.json', 'w', encoding='utf-8')
        json.dump(data[3], o)

    elif data[4]['second_chair'] + count_5() != 40:
        data[4]['second_chair'] = data[4]['second_chair'] - 1
        o = open('data/chuyen_bay.json', 'w', encoding='utf-8')
        json.dump(data[4], o)()

def dt_1():
    vcb = sum(Vechuyenbay.query.join(Chuyenbay, Vechuyenbay.chuyenbay_id == 1).filter(Vechuyenbay.gia))
    return vcb

def dt_2():
    vcb = sum(Vechuyenbay.query.join(Chuyenbay, Vechuyenbay.chuyenbay_id == 2).filter(Vechuyenbay.gia))
    return vcb

def dt_3():
    vcb = sum(Vechuyenbay.query.join(Chuyenbay, Vechuyenbay.chuyenbay_id == 3).filter(Vechuyenbay.gia))
    return vcb

def dt_4():
    vcb = sum(Vechuyenbay.query.join(Chuyenbay, Vechuyenbay.chuyenbay_id == 4).filter(Vechuyenbay.gia))
    return vcb

def dt_5():
    vcb = sum(Vechuyenbay.query.join(Chuyenbay, Vechuyenbay.chuyenbay_id == 5).filter(Vechuyenbay.gia))
    return vcb