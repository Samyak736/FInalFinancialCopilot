from pathlib import Path
import os

from flask import Flask, render_template_string

from config import BASE_DIR, SECRET_KEY
from models.db import init_db
from routes.auth import auth_bp
from routes.copilot import copilot_bp
from routes.dashboard import dashboard_bp, register_pages
from routes.upload import upload_bp


def create_app() -> Flask:
    app = Flask(
        __name__,
        template_folder=str(BASE_DIR / "templates"),
        static_folder=str(BASE_DIR / "static"),
    )
    app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024
    app.secret_key = SECRET_KEY

    try:
        # On Vercel, data dir might not be needed since DB is in /tmp
        if not os.environ.get("VERCEL"):
            Path(BASE_DIR / "data").mkdir(parents=True, exist_ok=True)
        init_db()
    except Exception as e:
        # Log error but don't crash the app
        print(f"Database initialization warning: {e}")

    app.register_blueprint(auth_bp)
    app.register_blueprint(upload_bp, url_prefix="/api")
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(copilot_bp)
    register_pages(app)
    return app


app = create_app()

# Only run if not on Vercel (serverless)
if __name__ == "__main__" and not os.environ.get("VERCEL"):
    app.run(host="0.0.0.0", port=5000, debug=True)

if __name__ == "__main__" and not os.environ.get("VERCEL"):
    app.run(host="0.0.0.0", port=5000, debug=True)
