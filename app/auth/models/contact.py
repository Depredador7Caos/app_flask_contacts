from app.auth.utils.db import db

#Clase Contact
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    fullname = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))

    def __init__(self, fullname, email, phone):
        self.fullname = fullname
        self.email = email
        self.phone = phone
