from flask import Flask
from .routes import main
from .extentions import db
def create_app():
    app = Flask(__name__)
    app.config.from_prefixed_env()
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.register_blueprint(main)
    return app