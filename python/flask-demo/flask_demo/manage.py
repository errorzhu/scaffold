import os
from ddc_edge import create_app, db
from flask_migrate import Migrate

profile = os.getenv("PROFILE") or "development"

app = create_app(profile)

migrate = Migrate(app, db)
