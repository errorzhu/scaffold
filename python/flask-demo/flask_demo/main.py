import logging.config
import os
from flask_demo import create_app

current_dir = os.path.dirname(__file__)
project_dir = os.path.abspath(os.path.join(current_dir, "../../"))
profile = os.getenv("PROFILE") or "development"
app = create_app(profile)

if __name__ == "__main__":
    app.logger.info("starting up  ........")
    app.run(host="0.0.0.0")

if __name__ != "__main__":
    gunicorn_logger = logging.getLogger("gunicorn.error")
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
    app.logger.info("gunicorn starting up  ........")
