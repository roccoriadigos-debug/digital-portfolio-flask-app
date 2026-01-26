## Imports 
import json
from flask import Flask, render_template, abort




## Flask App Setup 
app = Flask(__name__)


## Load the User Data for all active user accounts
def load_users():
    with open("data/users.json", "r") as f:
        return json.load(f)

USERS = load_users()


## Obtain User's Data when selected
def get_user(username):
    for key in USERS:
        if key.lower() == username.lower():
            return USERS[key]
    abort(404)





## Flask Routes
@app.route("/")
def home():
    return render_template("home.html", users=USERS)



@app.route("/<username>/Overview")
def overview(username):
    user = get_user(username)
    return render_template(
        "overview.html",
        user=user,
        username=user["first_name"]
    )



@app.route("/<username>/Projects")
def projects(username):
    user = get_user(username)
    return render_template(
        "projects.html",
        user=user,
        username=user["first_name"]
    )



@app.route("/<username>/Education")
def education(username):
    user = get_user(username)
    return render_template(
        "education.html",
        user=user,
        username=user["first_name"]
    )



@app.route("/<username>/Contact")
def contact(username):
    user = get_user(username)
    return render_template(
        "contact.html",
        user=user,
        username=user["first_name"]
    )




## Managing User Accounts

@app.route("/Manage_User_Accounts")
def manage_user_accounts():
    return render_template("manageuseraccounts.html")

@app.route("/New_User")
def new_user():
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