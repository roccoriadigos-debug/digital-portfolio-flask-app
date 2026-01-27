# =========================
# Imports
# =========================
import os
import uuid
from flask import Blueprint, render_template, request, redirect, url_for, current_app, send_from_directory, abort
from werkzeug.utils import secure_filename
from app import db
from app.models import User

user_bp = Blueprint('user_bp', __name__)

# Allowed image extensions
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}

# ----------------------------
# Helper functions
# ----------------------------

def allowed_file(filename):
    """Check if the uploaded file has an allowed extension."""
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def get_upload_folder():
    """Return the instance uploads folder path and ensure it exists."""
    upload_folder = os.path.join(current_app.instance_path, "uploads")
    os.makedirs(upload_folder, exist_ok=True)
    return upload_folder

# ----------------------------
# Serve uploaded images
# ----------------------------

@user_bp.route("/uploads/<filename>")
def uploaded_file(filename):
    """Serve uploaded files from instance/uploads"""
    upload_folder = get_upload_folder()
    return send_from_directory(upload_folder, filename)

# ----------------------------
# User Management Routes
# ----------------------------

@user_bp.route("/Manage_User_Accounts")
def manage_user_accounts():
    return render_template("manageuseraccounts.html")


@user_bp.route("/New_User", methods=["GET", "POST"])
def new_user():
    if request.method == "POST":
        user_id = str(uuid.uuid4().hex[:6])

        # Handle profile image
        file = request.files.get("profile_image")
        image_filename = None

        if file and file.filename != "" and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            image_filename = f"{user_id}_{filename}"
            file.save(os.path.join(get_upload_folder(), image_filename))

        # Create and save user
        new_user = User(
            user_id=user_id,
            profile_image=image_filename,
            first_name=request.form["first_name"],
            middle_initial=request.form["middle_initial"],
            last_name=request.form["last_name"],
            email=request.form["email"],
            phone_number=request.form["phone_number"],
            city=request.form["city"],
            state=request.form["state"],
            bio=request.form["bio"],
        )

        db.session.add(new_user)
        db.session.commit()

        username = f"{new_user.first_name}_{new_user.last_name}"
        return redirect(url_for("main_bp.overview", user_id=user_id, username=username))

    return render_template("newuser.html")


@user_bp.route("/Modify_User")
def modify_user():
    return render_template("modifyuser.html")


@user_bp.route("/Delete_User")
def delete_user():
    return render_template("deleteuser.html")
