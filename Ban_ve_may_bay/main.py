from flask import render_template, request, redirect, jsonify, session
from Ban_ve_may_bay import app, unit, login, decorator
from Ban_ve_may_bay.model import *
from flask_login import login_user, login_required
import hashlib

@app.route("/")
def index():
    dem_1 = unit.count_1()
    dem_2 = unit.count_2()
    dem_3 = unit.count_3()
    dem_4 = unit.count_4()
    dem_5 = unit.count_5()
    chuyen_bay = unit.read_data()
    return render_template('index.html', chuyen_bay = chuyen_bay, dem_1=dem_1,
                           dem_2=dem_2, dem_3=dem_3, dem_4=dem_4, dem_5=dem_5)

@app.route("/lich/<int:stt>")
def lichchuyenbay(stt):
    chuyen_bay = unit.get_chuyenbay_by_stt(stt = stt)
    return render_template('Lichchuyenbay.html', chuyen_bay = chuyen_bay)

@app.route("/datve/<int:id>", methods=['get', 'post'])
@decorator.login_required
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
    dem_1 = unit.count_1()
    dem_2 = unit.count_2()
    dem_3 = unit.count_3()
    dem_4 = unit.count_4()
    dem_5 = unit.count_5()
    dt_1 = unit.dt_1()
    dt_2 = unit.dt_2()
    dt_3 = unit.dt_3()
    dt_4 = unit.dt_4()
    dt_5 = unit.dt_5()
    return render_template('baocaothang.html', chuyen_bay = chuyen_bay, dem_1=dem_1, dem_2=dem_2, dem_3=dem_3,
                           dem_4=dem_4, dem_5=dem_5, dt_1=dt_1, dt_2=dt_2, dt_3=dt_3, dt_4=dt_4, dt_5=dt_5  )

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
        admin = Admin.query.filter(Admin.username == username.strip(),
                                   Admin.password == password).first()

        if admin:
            login_user(user=admin)

        return redirect("/admin")

@app.route("/login", methods=['post', 'get'])
def login():
    if request.method == 'POST':
        username = request.form.get("usr")
        password = request.form.get("pw", "")
        password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
        user = User.query.filter(User.username == username.strip(),
                                 User.password == password).first()

        if user:
            login_user(user=user)

        return redirect("/")

    return render_template('login.html')

@app.route("/register", methods=['post', 'get'])
def register():
    err_msg = ""
    if request.method == 'POST':
        name = request.form.get("ten")
        username = request.form.get("usr")
        password = request.form.get("pw","")
        password_confirm = request.form.get("pw_confirm","")

        if User.query.filter(User.username == str(username)).first():
            err_msg = "Có người sử dụng"
        elif password != password_confirm:
            err_msg = "Mật khẩu nhập không trùng"
        elif password == password_confirm:
            unit.add_user(ten=name, username=username, password=password)
            password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
            user = User.query.filter(User.username == username.strip(),
                                     User.password == password).first()
            if user:
                login_user(user=user)

            return redirect("/")

    return render_template('register.html', err_msg=err_msg)

@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, port=3938)