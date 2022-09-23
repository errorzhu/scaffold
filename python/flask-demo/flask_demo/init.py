import os
import sys

sys.path.append("../")
from flask_demo import create_app, db

profile = os.getenv("PROFILE") or "development"
app = create_app(profile)

if __name__ == "__main__":
    with app.app_context():
        db.drop_all()
        db.create_all()

