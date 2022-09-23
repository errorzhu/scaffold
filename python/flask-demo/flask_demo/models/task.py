from flask_demo import db


class Task(db.Model):
    __tablename__ = "task"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15))
    user_id = db.Column(db.Integer, name="password")

