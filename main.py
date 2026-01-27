## Imports 
import json
import uuid
from flask import Flask, render_template, abort, request, redirect, url_for




## Flask App Setup 
app = Flask(__name__)


## Load the User Data for all active user accounts
def load_users():
    with open("data/users.json", "r") as f:
        return json.load(f)

USERS = load_users()


## Obtain a User's Data by ID
def get_user_by_id(user_id):
    user = USERS.get(user_id)
    if not user:
        abort(404)
    return user






## Flask Routes
@app.route("/")
def home():
    return render_template("home.html", users=USERS)



@app.route("/<user_id>/<username>/Overview")
def overview(user_id, username):
    user = get_user_by_id(user_id)
    return render_template("overview.html", user=user, user_id=user_id, username=username)



@app.route("/<user_id>/<username>/Projects")
def projects(user_id, username):
    user = get_user_by_id(user_id)
    return render_template("projects.html", user=user, user_id=user_id, username=username)



@app.route("/<user_id>/<username>/Education")
def education(user_id, username):
    user = get_user_by_id(user_id)
    return render_template("education.html", user=user, user_id=user_id, username=username)



@app.route("/<user_id>/<username>/Contact")
def contact(user_id, username):
    user = get_user_by_id(user_id)
    return render_template("contact.html", user=user, user_id=user_id, username=username)




## Managing User Accounts

@app.route("/Manage_User_Accounts")
def manage_user_accounts():
    return render_template("manageuseraccounts.html")

@app.route("/New_User", methods=["GET", "POST"])
def new_user():
    if request.method == "POST":
        user_id = str(uuid.uuid4().hex[:6]) # Create a 6-bit unique ID

        # Create user data
        new_user_data = {
            "first_name": request.form["first_name"],
            "middle_initial": request.form["middle_initial"],
            "last_name": request.form["last_name"],
            "email": request.form["email"],
            "phone_number": request.form["phone_number"],
            "city": request.form["city"],
            "state": request.form["state"],
            "bio": request.form["bio"],
            "projects": [],
            "education": []
        }

        # Add to USERS dict
        USERS[user_id] = new_user_data

        # Save to JSON
        with open("data/users.json", "w") as f:
            json.dump(USERS, f, indent=2)


        # Open their Overview Page
        username = f"{new_user_data['first_name']}_{new_user_data['last_name']}"
        return redirect(url_for("overview", user_id=user_id, username=username))

    return render_template("newuser.html")

@app.route("/Modify_User")
def modify_user():
    return render_template("modifyuser.html")

@app.route("/Delete_User")
def delete_user():
    return render_template("deleteuser.html")








## Run Flask App 
if __name__ == "__main__":
    app.run(debug=True)