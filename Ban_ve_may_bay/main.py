from flask import render_template, request, redirect
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

@app.route("/datve/<int:stt>")
def vechuyenbay(stt):
    chuyen_bay = unit.get_chuyenbay_by_stt(stt = stt)
    return render_template('vechuyenbay.html', chuyen_bay = chuyen_bay)

@app.route("/datvetruoc/<int:stt>")
def datvetruoc(stt):
    chuyen_bay = unit.get_chuyenbay_by_stt(stt = stt)
    return render_template('datvetruoc.html', chuyen_bay = chuyen_bay)

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
        user = User.query.fillter(User.username == username.strip(),
                           User.password == password).first()

        if user:
            login_user(user = user)

    return redirect("/admin")

if __name__ == "__main__":
    app.run(debug=True, port=2800)
