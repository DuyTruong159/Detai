from flask_admin.contrib.sqla import ModelView
from Ban_ve_may_bay.model import Khachhang, Ghe, Transit, Chuyenbay
from Ban_ve_may_bay import db, admin
from flask_admin import BaseView, expose

class ContactView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/contact.html')

admin.add_view(ModelView(Chuyenbay, db.session))
admin.add_view(ModelView(Ghe, db.session))
admin.add_view(ModelView(Transit, db.session))
admin.add_view(ModelView(Khachhang, db.session))
admin.add_view(ContactView(name="Liên hệ"))
