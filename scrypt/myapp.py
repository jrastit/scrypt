#!/usr/bin/3

from flask import Flask, send_from_directory
from flask_cors import CORS

from scrypt.config import settings

from scrypt.global_var import set_app
from scrypt.model.db import db, Base

from scrypt.api.test.api_test import test_api


def init_app():
    # Create the web app
    app = Flask(__name__)
    # Added for allow origin issue
    CORS(app)
    # configure the Postgres database
    # app.config['SQLALCHEMY_ECHO'] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = settings.db_dsn
    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
        "connect_args": {
            "connect_timeout": 5,
            "options": "-c lock_timeout=3000 -c statement_timeout=3000",
        }
    }
    db.init_app(app)
    app.app_context().push()

    # Register app services per section
    app.register_blueprint(test_api)
    # Support OpenApi V3
    # app.config["SWAGGER"]['openapi'] = '3.0.2'
    Base.metadata.create_all(db.engine)
    # db.create_all()
    set_app(app)

    @app.route("/api/swagger.json")
    def specs():
        return send_from_directory("../", "swagger.json")

    return app
