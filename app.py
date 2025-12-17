from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/Overview")
def overview():
    return render_template("overview.html")

@app.route("/Projects")
def projects():
    return render_template("projects.html")

@app.route("/Education")
def education():
    return render_template("education.html")

@app.route("/Contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)