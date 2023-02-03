"""
"""

import os
import logging
from flask import Flask, jsonify
from flask_sqlalchemy.extension import current_app
from flask_sqlalchemy.record_queries import get_recorded_queries
from config import config
from database import db
from utils.db import get_connection_url
from flask_cors import CORS
from route.categoria_route import categoria_route
from route.auth_route import auth_route




def create_app(config_name) -> Flask:
    """
    
    """
    application = Flask(__name__)

    application.config.from_object(config[config_name])
    
    application.register_blueprint(categoria_route)
    application.register_blueprint(auth_route)
    
    application.config["SQLALCHEMY_DATABASE_URI"] = get_connection_url()
    application.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    application.config["SQLALCHEMY_RECORD_QUERIES"] = True
    application.config["SLOW_DB_QUERY_TIME"] = 0.5

    db.init_app(application)
    CORS(application)
    
    return application

flask_env = os.getenv("FLASK_ENV") or "local"
app = create_app(flask_env)
