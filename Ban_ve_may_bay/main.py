from flask import render_template
from Ban_ve_may_bay import app, unit

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

if __name__ == "__main__":
    app.run(debug=True, port=2800)
