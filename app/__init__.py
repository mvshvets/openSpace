from flask import Flask
from config import Config
from flask_cors import CORS


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    CORS(app, supports_credentials=True)

    from app.map import bp as map_bp
    app.register_blueprint(map_bp)

    return app
