from flask import Flask, Blueprint, render_template,request,redirect, url_for, flash
from app import db
from app.models.contact import Contact

bp = Blueprint("contact_bp", __name__)


@bp.route("/")
def index():
    contacts=Contact.query.all()
    return render_template("index.html", contacts=contacts)

@bp.route("/save", methods=["POST"])
def save():
    if request.method == 'POST':

        fullname=request.form['fullname']
        email=request.form['email']
        phone=request.form['phone']

        new_contact=Contact(fullname,email,phone)

        db.session.add(new_contact)
        db.session.commit()
        flash('Contact added successfully!')
        return redirect(url_for('contact_bp.index'))


@bp.route('/update/<string:id>', methods=["POST","GET"])
def update(id):
    contact=Contact.query.get(id)

    if request.method=='POST':
        # contact=Contact.query.get(id)
        contact.fullname=request.form["fullname"]
        contact.email=request.form['email']
        contact.phone=request.form['phone']

        db.session.commit()
        return redirect(url_for("contact_bp.index"))

    flash('Contact updated successfully!')
    return render_template("update.html",contact=contact)

@bp.route('/delete/<id>',methods=["GET"])
def delete(id):
    contact=Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()
    flash('Contact deleted successfully!')
    return redirect(url_for('contact_bp.index'))