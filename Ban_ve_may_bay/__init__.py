from flask import Flask
from flask_admin import Admin

app = Flask(__name__)

admin = Admin(app=app, name="Thống kê bán vé", template_mode = "bootstrap4")