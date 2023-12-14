from flask import Blueprint, render_template, redirect, url_for

athentication = Blueprint("athentication", __name__, template_folder = "templates")

@athentication.route("/")
def index():
    return render_template("index.html")

@athentication.route("/about")
def about():
    return render_template("about.html")
