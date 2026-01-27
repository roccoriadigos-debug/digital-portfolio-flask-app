## Imports
import json
import uuid
import os

from werkzeug.utils import secure_filename
from flask import Flask, render_template, abort, request, redirect, url_for


# =========================
# App Configuration
# =========================

UPLOAD_FOLDER = "static/uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# =========================
# Data Helpers
# =========================

def load_users():
    with open("data/users.json", "r") as f:
        return json.load(f)

USERS = load_users()


def get_user_by_id(user_id):
    user = USERS.get(user_id)
    if not user:
        abort(404)
    return user


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


# =========================
# Routes
# =========================

@app.route("/")
def home():
    return render_template("home.html", users=USERS)


@app.route("/<user_id>/<username>/Overview")
def overview(user_id, username):
    user = get_user_by_id(user_id)
    return render_template(
        "overview.html",
        user=user,
        user_id=user_id,
        username=username
    )


@app.route("/<user_id>/<username>/Projects")
def projects(user_id, username):
    user = get_user_by_id(user_id)
    return render_template(
        "projects.html",
        user=user,
        user_id=user_id,
        username=username
    )


@app.route("/<user_id>/<username>/Education")
def education(user_id, username):
    user = get_user_by_id(user_id)
    return render_template(
        "education.html",
        user=user,
        user_id=user_id,
        username=username
    )


@app.route("/<user_id>/<username>/Contact")
def contact(user_id, username):
    user = get_user_by_id(user_id)
    return render_template(
        "contact.html",
        user=user,
        user_id=user_id,
        username=username
    )


# =========================
# User Management
# =========================

@app.route("/Manage_User_Accounts")
def manage_user_accounts():
    return render_template("manageuseraccounts.html")


@app.route("/New_User", methods=["GET", "POST"])
def new_user():
    if request.method == "POST":
        user_id = uuid.uuid4().hex[:6]

        # ---- Handle profile image upload ----
        file = request.files.get("profile_image")
        image_filename = None

        if file and file.filename and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            image_filename = f"{user_id}_{filename}"
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], image_filename))

        # ---- Create user record ----
        new_user_data = {
            "profile_image": image_filename,
            "first_name": request.form["first_name"],
            "middle_initial": request.form.get("middle_initial", ""),
            "last_name": request.form["last_name"],
            "email": request.form["email"],
            "phone_number": request.form.get("phone_number", ""),
            "city": request.form.get("city", ""),
            "state": request.form.get("state", ""),
            "bio": request.form.get("bio", ""),
            "projects": [],
            "education": []
        }

        USERS[user_id] = new_user_data

        # ---- Persist to JSON ----
        with open("data/users.json", "w") as f:
            json.dump(USERS, f, indent=2)

        username = f"{new_user_data['first_name']}_{new_user_data['last_name']}"
        return redirect(url_for("overview", user_id=user_id, username=username))

    return render_template("newuser.html")


@app.route("/Modify_User")
def modify_user():
    return render_template("modifyuser.html")


@app.route("/Delete_User")
def delete_user():
    return render_template("deleteuser.html")


# =========================
# Run App
# =========================

if __name__ == "__main__":
    app.run(debug=True)
