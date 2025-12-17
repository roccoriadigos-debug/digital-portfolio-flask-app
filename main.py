## Imports 

import json
from flask import Flask, render_template, abort




## Setup 

app = Flask(__name__)

def load_users():
    with open("data/users.json", "r") as f:
        return json.load(f)

USERS = load_users()



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
        username=user["name"]
    )



@app.route("/<username>/Projects")
def projects(username):
    user = get_user(username)
    return render_template(
        "projects.html",
        user=user,
        username=user["name"]
    )



@app.route("/<username>/Education")
def education(username):
    user = get_user(username)
    return render_template(
        "education.html",
        user=user,
        username=user["name"]
    )



@app.route("/<username>/Contact")
def contact(username):
    user = get_user(username)
    return render_template(
        "contact.html",
        user=user,
        username=user["name"]
    )






if __name__ == "__main__":
    app.run(debug=True)