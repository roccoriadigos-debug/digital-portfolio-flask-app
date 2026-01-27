# Imports 
from app import db

class User(db.Model):
    user_id = db.Column(db.String(6), primary_key=True, unique=True, nullable=False)
    first_name = db.Column(db.String(120), nullable=False)
    middle_initial = db.Column(db.String(1))
    last_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String(20))
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    bio = db.Column(db.Text)
    profile_image = db.Column(db.String(255))

    def __repr__(self):
        return f"<User {self.first_name} {self.last_name}>"
