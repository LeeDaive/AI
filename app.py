from flask import Flask
from api.auth import bp
from api.chat import chat_bp
from config.config import Config
from extension import ext_database, ext_migrate
from extension.ext_database import db
from models import *

def initialize_extensions(app):
    ext_database.init_db(app)
    ext_migrate.init(app, db)

def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(chat_bp, url_prefix="/chat")
    app.register_blueprint(bp, url_prefix="/auth")
    app.config.from_object(Config())
    initialize_extensions(app)
    return app

app = create_app()

if __name__ == '__main__':
    app.run()