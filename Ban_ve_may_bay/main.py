from flask import render_template, request, redirect, jsonify, session
from Ban_ve_may_bay import app, unit, login
from Ban_ve_may_bay.model import *
from flask_login import login_user
import hashlib

@app.route("/")
def index():
    chuyen_bay = unit.read_data()
    return render_template('index.html', chuyen_bay = chuyen_bay)

@app.route("/lich/<int:stt>")
def lichchuyenbay(stt):
    chuyen_bay = unit.get_chuyenbay_by_stt(stt = stt)
    return render_template('Lichchuyenbay.html', chuyen_bay = chuyen_bay)

@app.route("/datve/<int:id>", methods=['get', 'post'])
def vechuyenbay(id):
    chuyen_bay = unit.datve(id = id)
    price = unit.gia(id = id)
    err_msg = ""
    if request.method == 'POST':
        chuyenbay = Chuyenbay.query.get(id).id
        hanhkhach = request.form.get('hanhkhach')
        cmnd = request.form.get('cmnd')
        sdt = request.form.get('dt')
        hangve = request.form.get('hang')
        giatien = request.form.get('price')
        kh = Khachhang.query.filter(Khachhang.ten == hanhkhach).first()

        if kh:
            err_msg = "Đã đặt vé"
        elif hanhkhach == "" or cmnd == "" or sdt == "":
            err_msg = "Thiếu thông tin"
        else:
            unit.add_ve(chuyenbay=chuyenbay, hanhkhach=hanhkhach, cmnd=cmnd,sdt=sdt, hangve=hangve, giatien=giatien)
            err_msg = "Đặt vé thành công"

    return render_template('vechuyenbay.html', chuyen_bay = chuyen_bay, price=price, err_msg=err_msg)

@app.route("/baocaothang")
def baocaothang():
    chuyen_bay = unit.read_data()
    return render_template('baocaothang.html', chuyen_bay = chuyen_bay)

@app.route("/baocaonam")
def baocaonam():
    chuyen_bay = unit.read_data()
    return render_template('baocaonam.html', chuyen_bay = chuyen_bay)

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route("/login-admin", methods = ['post'])
def login_admin():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password","")
        password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
        user = User.query.filter(User.username == username.strip(),
                                 User.password == password).first()

        if user:
            login_user(user = user)

    return redirect("/")

@app.route("/login")
def login():
    return redirect("/admin")

@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, port=7430)
