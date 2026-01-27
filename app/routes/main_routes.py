# =========================
# Imports
# =========================
from flask import Blueprint, render_template, abort
from app.models import User


main_bp = Blueprint('main_bp', __name__)


@main_bp.route("/")
def home():
    users = User.query.all()
    return render_template("home.html", users=users)

@main_bp.route("/<user_id>/<username>/Overview")
def overview(user_id, username):
    user = User.query.get(user_id)
    if not user:
        abort(404)
    return render_template("overview.html", user=user, user_id=user_id, username=username)

@main_bp.route("/<user_id>/<username>/Projects")
def projects(user_id, username):
    user = User.query.get(user_id)
    if not user:
        abort(404)
    return render_template("projects.html", user=user, user_id=user_id, username=username)

@main_bp.route("/<user_id>/<username>/Education")
def education(user_id, username):
    user = User.query.get(user_id)
    if not user:
        abort(404)
    return render_template("education.html", user=user, user_id=user_id, username=username)

@main_bp.route("/<user_id>/<username>/Contact")
def contact(user_id, username):
    user = User.query.get(user_id)
    if not user:
        abort(404)
    return render_template("contact.html", user=user, user_id=user_id, username=username)