from Ban_ve_may_bay import admin
from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose

class ContactView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/contact.html')

