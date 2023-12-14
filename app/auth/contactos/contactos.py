from flask import  Blueprint, render_template, redirect, request, url_for, flash
from app.auth.models.contact import Contact
from app.auth.utils.db import db

contact = Blueprint("contacto", __name__, template_folder = "templates")

@contact.route('/add_contacto', methods=['POST'])
def add_contacto():
    fullname = request.form["fullname"]
    email = request.form["email"]
    phone = request.form["phone"]
    new_contact = Contact(fullname, email, phone)

    db.session.add(new_contact)
    db.session.commit()

    flash("Contact added successfully")

    return redirect(url_for('contacto.get_contactos'))


@contact.route('/_list_contactos')
def get_contactos():
    contacts = Contact.query.all()
    return render_template("contactos/_list_contactos.html", contacts = contacts)


@contact.route('/update/<id>', methods=['GET', 'POST'])
def update_contacto(id):
    contact = Contact.query.get(id)

    if request.method == 'POST':
        contact.fullname = request.form["fullname"]
        contact.emial = request.form["email"]
        contact.phone = request.form["phone"]

        db.session.commit()

        flash("Contact updated successfully")

        return redirect(url_for('contacto.get_contactos'))
    return render_template("contactos/_update_contact.html", contacto=contact)


@contact.route('/delete/<id>')
def delete_contacto(id):
    contact = Contact.query.get(id)

    db.session.delete(contact)
    db.session.commit()

    flash("Contact delete successfully")

    return redirect(url_for('contacto.get_contactos'))
